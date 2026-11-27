"""Trusted build-time consumer fixture; no site or snapshot-code execution."""
import argparse
from contextlib import contextmanager
import hashlib
import io
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tarfile
import tempfile

from curriculum_manifest import ROOT, load_manifest, read_json
from curriculum_relationships import validate_relationships

VERSIONS = {"manifest": "1.0.0", "quizzes": "1.0.0", "exercises": "1.0.0",
            "interviews": "0.1.0", "mocks": "0.1.0"}
SCHEMAS = tuple(f"schemas/{name}.schema.json" for name in (
    "curriculum-manifest", "quiz-index", "quiz", "exercise-index", "exercise",
))
DEFAULT_LOCK = ROOT / "tests/fixtures/learning-hub/consumer-lock.json"
SHA = re.compile(r"[0-9a-f]{40}")


def load_lock(path):
    """Read the external, explicitly approved exact-version lock."""
    data = read_json(Path(path))
    if (not isinstance(data, dict) or set(data) != {"lock_version", "revision", "versions"}
            or data["lock_version"] != "1.0.0" or data["versions"] != VERSIONS
            or not isinstance(data["revision"], str)
            or SHA.fullmatch(data["revision"]) is None):
        raise ValueError("unsupported consumer lock or revision; full exact SHA required")
    return data


def git_bytes(repository, *args):
    try:
        return subprocess.run(
            ["git", "--no-replace-objects", "-C", str(repository), *args],
            check=True, capture_output=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError(f"trusted Git object lookup failed: {args[0]}") from exc


def canonical_path(value):
    path = PurePosixPath(value)
    if (not value or path.is_absolute() or path.as_posix() != value
            or any(part in {".", ".."} or part.casefold() == ".git" for part in path.parts)
            or any(c in value for c in ("\\", ":", "%"))
            or any(ord(c) < 32 or ord(c) == 127 for c in value)):
        raise ValueError(f"unsafe snapshot path: {value!r}")
    return path


def commit_tree(repository, revision):
    """Read the exact SHA-1 Git commit's regular blob paths, not the worktree."""
    if SHA.fullmatch(revision) is None:
        raise ValueError("full revision required")
    if git_bytes(repository, "cat-file", "-t", revision).strip() != b"commit":
        raise ValueError("pinned revision is not a commit")
    actual = git_bytes(repository, "rev-parse", "--verify", revision + "^{commit}").strip()
    if actual != revision.encode("ascii"):
        raise ValueError("revision identity mismatch")
    entries = git_bytes(repository, "ls-tree", "-r", "-z", "--full-tree", revision)
    tree = {}
    folded = {}
    for entry in entries.split(b"\0"):
        if not entry:
            continue
        meta, raw = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split(" ")
        path = canonical_path(raw.decode("utf-8"))
        name = path.as_posix()
        if mode not in {"100644", "100755"} or kind != "blob" or not SHA.fullmatch(oid):
            raise ValueError(f"nonregular Git tree entry: {name}")
        if name in tree:
            raise ValueError(f"duplicate Git tree entry: {name}")
        for component in (path, *path.parents):
            spelling = component.as_posix()
            if folded.setdefault(spelling.casefold(), spelling) != spelling:
                raise ValueError(f"case-colliding snapshot path: {name}")
        tree[name] = oid
    if not tree:
        raise ValueError("empty pinned tree")
    return tree


def blob_hash(data):
    # Git SHA-1 object identity, not an independent signature or trust anchor.
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data,
                        usedforsecurity=False).hexdigest()


def expected_dirs(tree):
    return {p.as_posix() for name in tree for p in PurePosixPath(name).parents
            if p != PurePosixPath(".")}


def external_boundary(repository, lock_path, snapshot):
    resolved = snapshot.resolve()
    if (Path(lock_path).resolve().is_relative_to(resolved)
            or ROOT.resolve().is_relative_to(resolved)
            or resolved.is_relative_to(ROOT.resolve())
            or Path(repository).resolve().is_relative_to(resolved)):
        raise ValueError("lock, trusted validators and repository must be outside snapshot")


def verify_tree(snapshot, tree):
    if not stat.S_ISDIR(snapshot.lstat().st_mode):
        raise ValueError("snapshot root must be a regular directory")
    actual = {}
    directories = set()
    for folder, dirs, files in os.walk(snapshot, followlinks=False):
        for name in dirs:
            path = Path(folder) / name
            if not stat.S_ISDIR(path.lstat().st_mode):
                raise ValueError("snapshot requires regular directories")
            directories.add(canonical_path(path.relative_to(snapshot).as_posix()).as_posix())
        for name in files:
            path = Path(folder) / name
            if not stat.S_ISREG(path.lstat().st_mode):
                raise ValueError("snapshot requires regular files")
            relative = canonical_path(path.relative_to(snapshot).as_posix()).as_posix()
            actual[relative] = path
    if set(actual) != set(tree) or directories != expected_dirs(tree):
        raise ValueError("snapshot tree coverage mismatch")
    for name, path in actual.items():
        if blob_hash(path.read_bytes()) != tree[name]:
            raise ValueError(f"snapshot blob mismatch: {name}")


def verify_snapshot(repository, lock_path, snapshot):
    """Reject mixed revisions, extra/missing files, and nonregular entries."""
    snapshot = Path(snapshot)
    external_boundary(repository, lock_path, snapshot)
    lock = load_lock(lock_path)
    tree = commit_tree(repository, lock["revision"])
    verify_tree(snapshot, tree)
    return tree


@contextmanager
def export_snapshot(repository, lock_path):
    """Materialize only verified regular blobs into isolated temporary staging."""
    lock = load_lock(lock_path)
    tree = commit_tree(repository, lock["revision"])
    archive = git_bytes(repository, "archive", "--format=tar", lock["revision"])
    dirs = expected_dirs(tree)
    with tempfile.TemporaryDirectory(prefix="curriculum-consumer-") as directory:
        root = Path(directory)
        external_boundary(repository, lock_path, root)
        seen = set()
        with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as tar:
            for member in tar:
                name = canonical_path(member.name.rstrip("/") if member.isdir()
                                      else member.name).as_posix()
                if name in seen:
                    raise ValueError(f"duplicate archive entry: {name}")
                seen.add(name)
                path = root / name
                if member.isdir() and name in dirs:
                    path.mkdir(parents=True, exist_ok=True)
                elif member.isfile() and name in tree:
                    source = tar.extractfile(member)
                    if source is None:
                        raise ValueError("missing archive blob")
                    with source:
                        data = source.read()
                    if blob_hash(data) != tree[name]:
                        raise ValueError(f"archive blob mismatch: {name}")
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with path.open("xb") as target:
                        target.write(data)
                else:
                    raise ValueError(f"unexpected or nonregular archive entry: {name}")
        verify_tree(root, tree)
        yield root


def validate_navigation(data):
    """Independent manifest navigation check, without authoring sources."""
    modules = data["modules"]
    chapters = [chapter for module in modules for chapter in module["chapters"]]
    ids = [c["id"] for c in chapters]
    localized = [p for m in modules for p in m["index"].values()]
    localized.extend(p for c in chapters for p in c["content"].values())
    if (len(modules) != 14 or len(chapters) != 115
            or len({m["id"] for m in modules}) != len(modules)
            or len({m["slug"] for m in modules}) != len(modules)
            or len(set(ids)) != len(ids) or len(set(localized)) != len(localized)):
        raise ValueError("invalid consumer curriculum coverage or duplicate identity")
    for order, module in enumerate(modules):
        entries = module["chapters"]
        if (module["order"] != order or not entries
                or len({c["slug"] for c in entries}) != len(entries)
                or [c["order"] for c in entries] != list(range(len(entries)))):
            raise ValueError("invalid consumer curriculum order")
    for i, chapter in enumerate(chapters):
        previous = ids[i - 1] if i else None
        following = ids[i + 1] if i + 1 < len(ids) else None
        if chapter["previous_id"] != previous or chapter["next_id"] != following:
            raise ValueError("invalid consumer navigation")


def validate_snapshot(repository, lock_path, snapshot):
    """Accept only the pinned tree and exact trusted schema/record contract."""
    snapshot = Path(snapshot)
    tree = verify_snapshot(repository, lock_path, snapshot)
    for path in SCHEMAS:
        if path not in tree or (snapshot / path).read_bytes() != (ROOT / path).read_bytes():
            raise ValueError(f"snapshot differs from trusted schema: {path}")
    data = load_manifest(snapshot)
    actual = {"manifest": data["schema_version"],
              **{key: item["schema_version"] for key, item in data["banks"].items()}}
    if actual != load_lock(lock_path)["versions"]:
        raise ValueError("unsupported snapshot versions")
    validate_navigation(data)
    return validate_relationships(data, snapshot, set(tree))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=ROOT)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    args = parser.parse_args()
    try:
        with export_snapshot(args.repository, args.lock) as snapshot:
            data = validate_snapshot(args.repository, args.lock, snapshot)
        print(f"Validated pinned consumer fixture {load_lock(args.lock)['revision']}: "
              f"{len(data['modules'])} modules, complete relationships.")
    except (ValueError, OSError, tarfile.TarError) as exc:
        print(f"Consumer validation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

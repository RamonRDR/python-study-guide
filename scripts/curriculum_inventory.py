"""Authoring inventory checks for Sprint 08B; not a consumer import API."""
from pathlib import Path, PurePosixPath
import re
import subprocess

from assessment_records import load_matrix
from check_chapter_navigation import CHAPTER_PATH, learning_order
from curriculum_manifest import LOCALES, ROOT, load_manifest, manifest_file, validate_manifest

HEADING = re.compile(
    r"## (?:(?:Curriculum order|Ordem curricular|Orden curricular) 00"
    r"|(?:Phase|Fase) (\d+)|Complementary module|Módulo complementar"
    r"|Módulo complementario)\s*[·:]\s*(.*?)\s*(?:✅)?"
)
ENTRY = re.compile(
    r"\d+\.\s+(?:✅\s+)?\[(.+)\]\(\.\./("
    + CHAPTER_PATH.pattern + r")\)"
)
IMAGE_EXTENSIONS = {".png", ".svg", ".jpg", ".jpeg", ".webp", ".gif"}
ASSOCIATIONS = ("quiz_ids", "exercise_ids", "interview_ids", "mock_ids")
LOCAL_REASON = {
    "en": "Requires local Python for platform-specific filesystem operations.",
    "pt-BR": "Requer Python local para operações de sistema de arquivos específicas da plataforma.",
    "es": "Requiere Python local para operaciones del sistema de archivos específicas de la plataforma.",
}


def tracked_paths(root):
    """Read authoring checkout inventory, excluding untracked generated files."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("authoring inventory requires a Git checkout") from exc
    return set(result.stdout.decode("utf-8").split("\0")) - {""}


def is_image(path):
    return PurePosixPath(path).suffix.lower() in IMAGE_EXTENSIONS


def read_learning_path(root, locale):
    path = f"docs/learning-path.{locale}.md"
    text = manifest_file(root, path).read_text(encoding="utf-8")
    groups = []
    group = None
    for line in text.splitlines():
        if line.startswith("## "):
            heading = HEADING.fullmatch(line)
            group = None
            if heading:
                phase, title = heading.groups()
                group = {"title": title.strip(), "phase": int(phase) if phase else None,
                         "entries": []}
                groups.append(group)
        if match := ENTRY.fullmatch(line.strip()):
            if group is None:
                raise ValueError(f"chapter outside curriculum heading: {path}")
            title, content = match.groups()
            group["entries"].append((content, title.replace("`", "")))
    if [p for g in groups for p, _ in g["entries"]] != learning_order(text):
        raise ValueError(f"learning path parse mismatch: {path}")
    if not groups or any(not g["entries"] for g in groups):
        raise ValueError(f"empty module: {path}")
    return groups


def require_equal(actual, expected, context):
    if actual != expected:
        raise ValueError(f"inventory mismatch: {context}")


def validate_inventory(data, root=ROOT, tracked=None):
    """Validate B's pending inventory against the approved authoring baseline.

    This checks source inventory and navigation, not assessment associations,
    immutable snapshot identity, browser runtime or consumer readiness.
    """
    root = Path(root)
    validate_manifest(data, root)
    if tracked is None:
        tracked = tracked_paths(root)
    require_equal(data["association_status"], "pending", "association status")
    if "docs/specs/learning-hub-foundation/assessment-matrix.json" not in tracked:
        raise ValueError("untracked authoring baseline")
    baseline = load_matrix(root)
    by_content = {paths["en"]: (identifier, paths)
                  for identifier, paths in baseline.items()}
    groups = {locale: read_learning_path(root, locale) for locale in LOCALES}
    for locale, entries in groups.items():
        expected_paths = [p for g in entries for p, _ in g["entries"]]
        require_equal(len(expected_paths), len(set(expected_paths)), f"{locale} duplicates")
        require_equal(set(expected_paths), {
            p for p in tracked if CHAPTER_PATH.fullmatch(p)
            and PurePosixPath(p).name == LOCALES[locale]
        }, f"{locale} chapter coverage")
        require_equal(len(entries), len(groups["en"]), f"{locale} module count")
        if f"docs/learning-path.{locale}.md" not in tracked:
            raise ValueError("untracked learning path")
    require_equal(set(by_content), {p for g in groups["en"] for p, _ in g["entries"]},
                  "stable ID baseline")
    require_equal(data["assets"], sorted(p for p in tracked if p.startswith("assets/")
                                         and is_image(p)), "global assets")
    for bank in data["banks"].values():
        for key, path in bank.items():
            if key != "schema_version" and path not in tracked:
                raise ValueError(f"untracked bank file: {path}")
    modules = data["modules"]
    require_equal(len(modules), len(groups["en"]), "module count")
    chapter_ids = []
    seen_modules = set()
    for i, module in enumerate(modules):
        group = groups["en"][i]
        module_id = group["entries"][0][0].split("/")[0]
        if module_id in seen_modules:
            raise ValueError(f"duplicate module: {module_id}")
        seen_modules.add(module_id)
        phase = group["phase"]
        kind = ("onboarding" if module_id == "getting-started" else
                "complementary" if module_id == "manual-programming-practices" else "phase")
        require_equal((module["id"], module["slug"], module["order"],
                       module["kind"], module["educational_phase"]),
                      (module_id, module_id, i, kind, phase), module_id)
        require_equal(len(module["chapters"]), len(group["entries"]), module_id)
        for locale, filename in LOCALES.items():
            localized = groups[locale][i]
            require_equal(localized["phase"], phase, f"{module_id}: {locale} phase")
            require_equal(module["title"][locale], localized["title"], f"{module_id}: title")
            index = f"{module_id}/{filename}"
            require_equal(module["index"][locale], index, f"{module_id}: index")
            if index not in tracked:
                raise ValueError(f"untracked index: {index}")
            require_equal(len(localized["entries"]), len(group["entries"]), f"{module_id}: count")
        for j, chapter in enumerate(module["chapters"]):
            content = group["entries"][j][0]
            folder = PurePosixPath(content).parent
            require_equal(folder.parts[0], module_id, "chapter module")
            identifier, expected_content = by_content[content]
            require_equal((chapter["id"], chapter["order"], chapter["slug"], chapter["kind"]),
                          (identifier, j, folder.name[3:],
                           "project" if module_id == "practical-projects" else "lesson"),
                          identifier)
            chapter_ids.append(identifier)
            require_equal(chapter["content"], expected_content, f"{identifier}: content")
            for locale in LOCALES:
                path, title = groups[locale][i]["entries"][j]
                require_equal(path, expected_content[locale], f"{identifier}: locale order")
                require_equal(chapter["title"][locale], title, f"{identifier}: title")
            files = sorted(p for p in tracked if p.startswith(folder.as_posix() + "/")
                           and p not in expected_content.values())
            require_equal(chapter["assets"], [p for p in files if is_image(p)],
                          f"{identifier}: assets")
            require_equal(chapter["resources"], [p for p in files if not is_image(p)],
                          f"{identifier}: resources")
            for field in ASSOCIATIONS:
                require_equal(chapter[field], [], f"{identifier}: pending {field}")
            if module_id == "external-libraries":
                require_equal(chapter.get("dependency_paths"), ["requirements-external.txt"],
                              f"{identifier}: dependency paths")
                if "requirements-external.txt" not in tracked:
                    raise ValueError("untracked requirements")
            elif "dependency_paths" in chapter:
                raise ValueError(f"unexpected dependency paths: {identifier}")
            if "local_python" in chapter:
                raise ValueError(f"unverified local Python version: {identifier}")
            if identifier == "practical-projects.file-organizer":
                require_equal(chapter["execution"], "local_only", identifier)
                require_equal(chapter.get("execution_reason"), LOCAL_REASON, identifier)
            else:
                require_equal(chapter["execution"], "unverified", identifier)
    require_equal(len(chapter_ids), len(set(chapter_ids)), "duplicate chapter IDs")
    all_chapters = [chapter for module in modules for chapter in module["chapters"]]
    for i, chapter in enumerate(all_chapters):
        require_equal(chapter["previous_id"], chapter_ids[i - 1] if i else None,
                      f"{chapter['id']}: previous")
        require_equal(chapter["next_id"], chapter_ids[i + 1] if i + 1 < len(chapter_ids) else None,
                      f"{chapter['id']}: next")
    return data


def load_inventory(root=ROOT, path="curriculum/manifest.json"):
    """Load a tracked, pending authoring inventory from a Git checkout."""
    root = Path(root)
    tracked = tracked_paths(root)
    if path not in tracked:
        raise ValueError(f"untracked manifest: {path}")
    return validate_inventory(load_manifest(root, path), root, tracked)

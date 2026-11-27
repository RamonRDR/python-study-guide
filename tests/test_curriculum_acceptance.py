"""AC-08 and AC-09 acceptance across authoring and immutable consumer gates."""
from collections import Counter
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from curriculum_consumer import (
    DEFAULT_LOCK, export_snapshot, load_lock, validate_snapshot, verify_snapshot,
)
from curriculum_inventory import load_inventory
from curriculum_manifest import read_json

APPROVED_08D = "b94ced2ce19e3fe8790078d057fc11126c1aacc8"
MANIFEST = "curriculum/manifest.json"


def git(repo, *args):
    result = subprocess.run(["git", "--no-replace-objects", "-C", str(repo), *args],
                            check=True, capture_output=True)
    return result.stdout.decode().strip()


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def canonical_paths(data, root):
    """Independently enumerate canonical indexed records and manifest references."""
    paths = {MANIFEST, *data["assets"]}
    for bank in data["banks"].values():
        paths.update(value for key, value in bank.items() if key != "schema_version")
    for module in data["modules"]:
        paths.update(module["index"].values())
        for chapter in module["chapters"]:
            paths.update(chapter["content"].values())
            for field in ("assets", "resources", "dependency_paths"):
                paths.update(chapter.get(field, []))
    for bank in ("quizzes", "exercises"):
        index = read_json(root / data["banks"][bank]["index"])
        for entry in index["records"]:
            paths.add(entry["path"])
            if bank == "exercises":
                record = read_json(root / entry["path"])
                paths.update((record["starter_path"], record["solution_path"]))
    for bank, field, folder in (
        ("interviews", "question_ids", "interviews/questions"),
        ("mocks", "mock_ids", "interviews/mocks"),
    ):
        index = read_json(root / data["banks"][bank]["index"])
        paths.update(f"{folder}/{identifier}.json" for identifier in index[field])
    return paths


class CurriculumAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ac08-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def lock_for(self, revision):
        data = copy.deepcopy(load_lock(DEFAULT_LOCK))
        data["revision"] = revision
        path = self.root / "external-lock.json"
        write_json(path, data)
        return path

    def test_authoring_and_two_reviewed_revisions_agree(self):
        authoring = load_inventory(ROOT)
        lock = self.lock_for(APPROVED_08D)
        with export_snapshot(ROOT, DEFAULT_LOCK) as original:
            original_data = validate_snapshot(ROOT, DEFAULT_LOCK, original)
            with export_snapshot(ROOT, lock) as current:
                current_data = validate_snapshot(ROOT, lock, current)
                self.assertEqual(authoring, original_data)
                self.assertEqual(authoring, current_data)
                paths = canonical_paths(authoring, ROOT)
                self.assertEqual(paths, canonical_paths(original_data, original))
                self.assertEqual(paths, canonical_paths(current_data, current))
                for path in sorted(paths):
                    with self.subTest(path=path):
                        expected = (ROOT / path).read_bytes()
                        self.assertEqual((original / path).read_bytes(), expected)
                        self.assertEqual((current / path).read_bytes(), expected)

    def test_ac09_handoff_content_pin(self):
        # This is the reviewed 09A squash, not the handoff commit or a moving ref.
        fixture = ROOT / "tests/fixtures/learning-hub/handoff-lock.json"
        lock = load_lock(fixture)
        self.assertEqual(lock["revision"], "03e91ff9952f2b02293f16a11260d166eb00ea8a")
        self.assertEqual(lock["versions"], load_lock(DEFAULT_LOCK)["versions"])
        external = self.root / "handoff-lock.json"
        write_json(external, lock)
        with export_snapshot(ROOT, external) as candidate:
            data = validate_snapshot(ROOT, external, candidate)
            self.assertEqual(data["association_status"], "complete")
            self.assertFalse((candidate / fixture.relative_to(ROOT)).exists())
            with export_snapshot(ROOT, DEFAULT_LOCK) as historical:
                previous = validate_snapshot(ROOT, DEFAULT_LOCK, historical)
                self.assertEqual(data, previous)
                paths = canonical_paths(data, candidate)
                self.assertEqual(paths, canonical_paths(previous, historical))
                for path in sorted(paths):
                    with self.subTest(path=path):
                        self.assertEqual((candidate / path).read_bytes(),
                                         (historical / path).read_bytes())
        print(f"AC-09 handoff pin validated: {lock['revision']}; "
              f"{len(paths)} canonical paths match historical content.")

    def test_curriculum_and_execution_contract(self):
        manifest = read_json(ROOT / MANIFEST)
        modules = manifest["modules"]
        chapters = [c for m in modules for c in m["chapters"]]
        self.assertEqual(len(modules), 14)
        self.assertEqual(len(chapters), 115)
        self.assertEqual(Counter(c["kind"] for c in chapters), {"lesson": 107, "project": 8})
        self.assertEqual(len({c["id"] for c in chapters}), 115)
        self.assertEqual(len({p for c in chapters for p in c["content"].values()}), 345)
        self.assertEqual(len({p for m in modules for p in m["index"].values()}), 42)
        self.assertEqual(sum(len(c["resources"]) for c in chapters), 243)
        self.assertEqual(len(manifest["assets"]), 6)
        self.assertEqual(Counter(c["execution"] for c in chapters),
                         {"unverified": 114, "local_only": 1})
        local = next(c for c in chapters if c["execution"] == "local_only")
        self.assertEqual(local["id"], "practical-projects.file-organizer")
        self.assertEqual(set(local["execution_reason"]), {"en", "pt-BR", "es"})
        self.assertEqual(sum(bool(c.get("dependency_paths")) for c in chapters), 4)
        self.assertTrue(all(c.get("dependency_paths", []) in ([], ["requirements-external.txt"])
                            for c in chapters))
        self.assertTrue(all("local_python" not in c for c in chapters))
        all_ids = set()
        for field, unique, links in (("quiz_ids", 160, 160), ("exercise_ids", 30, 30),
                                     ("interview_ids", 60, 75), ("mock_ids", 3, 3)):
            values = [identifier for c in chapters for identifier in c[field]]
            self.assertEqual(len(values), links)
            self.assertEqual(len(set(values)), unique)
            self.assertFalse(all_ids.intersection(values))
            all_ids.update(values)
        self.assertEqual(len(all_ids), 253)

    def test_strict_integer_and_float_boundary(self):
        path = self.root / "numbers.json"
        path.write_text('{"large":9007199254740993,"negative":-9007199254740993,'
                        '"float":1.0,"boolean":true}', encoding="utf-8")
        data = read_json(path)
        self.assertEqual(data["large"], 9007199254740993)
        self.assertEqual(data["negative"], -9007199254740993)
        self.assertIs(type(data["large"]), int)
        self.assertIs(type(data["float"]), float)
        self.assertIs(type(data["boolean"]), bool)
        path.write_text('{"large":1e999}', encoding="utf-8")
        with self.assertRaises(ValueError):
            read_json(path)

    def test_valid_commit_identity_is_not_semantic_acceptance(self):
        # Every mutation is a new, local, test-only commit. Git identity must
        # succeed first, so failures cannot be attributed to mixed revisions.
        repo = self.root / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        git(repo, "fetch", "--no-tags", str(ROOT), APPROVED_08D)
        git(repo, "config", "user.name", "Consumer Fixture")
        git(repo, "config", "user.email", "fixture@example.invalid")
        git(repo, "config", "commit.gpgsign", "false")
        git(repo, "config", "core.autocrlf", "false")
        original = read_json(ROOT / MANIFEST)
        first = original["modules"][0]["chapters"][0]
        quiz = read_json(ROOT / original["banks"]["quizzes"]["index"])["records"][0]
        for case, message in (
            ("version", "schema_version"),
            ("unsafe_path", "path"),
            ("missing_locale", "path"),
            ("wrong_association", "association mismatch"),
            ("duplicate_record_key", "duplicate JSON key"),
            ("nonfinite_interview_record", "nonfinite JSON number"),
        ):
            with self.subTest(case=case):
                git(repo, "checkout", "--detach", "-f", APPROVED_08D)
                data = copy.deepcopy(original)
                if case == "version":
                    data["schema_version"] = "99.0.0"
                elif case == "unsafe_path":
                    data["modules"][0]["chapters"][0]["content"]["en"] = "../README.md"
                elif case == "missing_locale":
                    (repo / first["content"]["es"]).unlink()
                elif case == "wrong_association":
                    data["modules"][0]["chapters"][0]["quiz_ids"] = []
                elif case == "duplicate_record_key":
                    path = repo / quiz["path"]
                    raw = path.read_text(encoding="utf-8")
                    path.write_text('{"id":"duplicate",' + raw.lstrip()[1:], encoding="utf-8")
                elif case == "nonfinite_interview_record":
                    index = read_json(repo / data["banks"]["interviews"]["index"])
                    path = repo / "interviews/questions" / (index["question_ids"][0] + ".json")
                    raw = path.read_text(encoding="utf-8")
                    path.write_text('{"nonfinite":1e999,' + raw.lstrip()[1:], encoding="utf-8")
                if case in {"version", "unsafe_path", "wrong_association"}:
                    write_json(repo / MANIFEST, data)
                git(repo, "add", "-A")
                git(repo, "commit", "-qm", "fixture: " + case)
                lock = self.lock_for(git(repo, "rev-parse", "HEAD"))
                with export_snapshot(repo, lock) as snapshot:
                    self.assertIn(MANIFEST, verify_snapshot(repo, lock, snapshot))
                    with self.assertRaisesRegex(ValueError, message):
                        validate_snapshot(repo, lock, snapshot)


if __name__ == "__main__":
    unittest.main()

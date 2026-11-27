"""Independent build-time consumer fixture; never execute snapshot code."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from curriculum_consumer import (
    export_snapshot, load_lock, validate_snapshot, verify_snapshot, validate_navigation,
)
from curriculum_manifest import read_json

LOCK = ROOT / "tests/fixtures/learning-hub/consumer-lock.json"
PENDING = "fd598868c99ae1e7217cbe3b7ab5af5cfb393132"


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args],
                                   stderr=subprocess.PIPE).decode().strip()


class ConsumerFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lock = load_lock(LOCK)
        cls.staging = export_snapshot(ROOT, LOCK)
        cls.snapshot = cls.staging.__enter__()
        cls.addClassCleanup(cls.staging.__exit__, None, None, None)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def candidate_lock(self, revision=None, **changes):
        data = copy.deepcopy(self.lock)
        if revision is not None:
            data["revision"] = revision
        data.update(changes)
        path = self.root / "candidate.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def copy_snapshot(self):
        path = self.root / "snapshot"
        shutil.copytree(self.snapshot, path)
        return path

    def test_real_approved_revision(self):
        data = validate_snapshot(ROOT, LOCK, self.snapshot)
        self.assertEqual(data["association_status"], "complete")
        self.assertEqual(len(data["modules"]), 14)
        chapters = [c for m in data["modules"] for c in m["chapters"]]
        self.assertEqual(len(chapters), 115)
        self.assertEqual(sum(len(c["content"]) for c in chapters), 345)
        self.assertEqual(sum(len(c["quiz_ids"]) for c in chapters), 160)
        self.assertEqual(sum(len(c["exercise_ids"]) for c in chapters), 30)
        self.assertEqual(sum(len(c["interview_ids"]) for c in chapters), 75)
        self.assertEqual(sum(len(c["mock_ids"]) for c in chapters), 3)
        self.assertFalse((self.snapshot / ".git").exists())
        self.assertFalse((self.snapshot / "tests/fixtures/learning-hub/consumer-lock.json").exists())

    def test_abbreviated_ref_and_unknown_revision(self):
        for revision in (self.lock["revision"][:10], "main", "0" * 40):
            path = self.candidate_lock(revision)
            with self.subTest(revision=revision), self.assertRaises(ValueError):
                with export_snapshot(ROOT, path):
                    self.fail("unapproved revision exported")

    def test_exact_supported_versions(self):
        for field in self.lock["versions"]:
            versions = dict(self.lock["versions"], **{field: "99.0.0"})
            with self.subTest(field=field), self.assertRaises(ValueError):
                load_lock(self.candidate_lock(versions=versions))
        with self.assertRaises(ValueError):
            load_lock(self.candidate_lock(lock_version="2.0.0"))

    def test_lock_strict_json_and_unknown_field(self):
        path = self.root / "bad.json"
        for raw in ('{"revision":"a","revision":"b"}', '{"value":NaN}',
                    '{"value":1e999}'):
            path.write_text(raw, encoding="utf-8")
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                load_lock(path)
        with self.assertRaises(ValueError):
            load_lock(self.candidate_lock(extra="unexpected"))

    def test_wrong_revision_and_pending_snapshot(self):
        path = self.candidate_lock(PENDING)
        with self.assertRaisesRegex(ValueError, "blob|tree"):
            verify_snapshot(ROOT, path, self.snapshot)
        with export_snapshot(ROOT, path) as snapshot:
            with self.assertRaisesRegex(ValueError, "complete"):
                validate_snapshot(ROOT, path, snapshot)

    def test_mixed_revision_file(self):
        stage = self.copy_snapshot()
        with export_snapshot(ROOT, self.candidate_lock(PENDING)) as previous:
            shutil.copyfile(previous / "curriculum/manifest.json",
                            stage / "curriculum/manifest.json")
        with self.assertRaisesRegex(ValueError, "blob"):
            validate_snapshot(ROOT, LOCK, stage)

    def test_modified_missing_and_extra_files(self):
        stage = self.copy_snapshot()
        file = stage / "curriculum/manifest.json"
        original = file.read_bytes()
        file.write_bytes(original + b" ")
        with self.assertRaisesRegex(ValueError, "blob"):
            verify_snapshot(ROOT, LOCK, stage)
        file.unlink()
        with self.assertRaisesRegex(ValueError, "tree"):
            verify_snapshot(ROOT, LOCK, stage)
        file.write_bytes(original)
        (stage / "extra.txt").write_text("not pinned", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "tree"):
            verify_snapshot(ROOT, LOCK, stage)

    def test_symlink_rejected_even_with_correct_bytes(self):
        stage = self.copy_snapshot()
        file = stage / "curriculum/manifest.json"
        external = self.root / "outside.json"
        shutil.copyfile(file, external)
        file.unlink()
        file.symlink_to(external)
        with self.assertRaisesRegex(ValueError, "regular"):
            verify_snapshot(ROOT, LOCK, stage)

    def test_lock_cannot_be_inside_snapshot(self):
        stage = self.copy_snapshot()
        path = stage / "consumer-lock.json"
        shutil.copyfile(LOCK, path)
        with self.assertRaisesRegex(ValueError, "outside"):
            verify_snapshot(ROOT, path, stage)

    def test_navigation_negative_cases(self):
        manifest = read_json(self.snapshot / "curriculum/manifest.json")
        for field, value in (("order", 99), ("previous_id", "missing.chapter")):
            changed = copy.deepcopy(manifest)
            changed["modules"][0]["chapters"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_navigation(changed)
        changed = copy.deepcopy(manifest)
        changed["modules"][0]["chapters"][1]["id"] = changed["modules"][0]["chapters"][0]["id"]
        with self.assertRaises(ValueError):
            validate_navigation(changed)

    def test_valid_update_rejected_candidate_and_rollback(self):
        # Local test-only Git repository: real commit objects, no remote service.
        repo = self.root / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        git(repo, "fetch", "--no-tags", str(ROOT), self.lock["revision"])
        git(repo, "checkout", "--detach", "FETCH_HEAD")
        git(repo, "config", "user.name", "Consumer Fixture")
        git(repo, "config", "user.email", "fixture@example.invalid")
        git(repo, "config", "commit.gpgsign", "false")
        git(repo, "config", "core.autocrlf", "false")
        chapter = repo / "getting-started/01-install-python/README.md"
        chapter.write_bytes(chapter.read_bytes() + b"\n<!-- fixture update -->\n")
        git(repo, "add", str(chapter))
        git(repo, "commit", "-qm", "fixture: valid content update")
        revision = git(repo, "rev-parse", "HEAD")
        candidate = self.candidate_lock(revision)
        with export_snapshot(repo, candidate) as staged:
            selected = validate_snapshot(repo, candidate, staged)
            self.assertEqual(selected["association_status"], "complete")
            self.assertTrue((staged / chapter.relative_to(repo)).read_bytes().endswith(b"<!-- fixture update -->\n"))
        active = load_lock(candidate)
        self.assertEqual(active["revision"], revision)

        # A valid Git commit is not sufficient if its schema is not supported.
        schema = repo / "schemas/curriculum-manifest.schema.json"
        schema.write_bytes(schema.read_bytes() + b" ")
        git(repo, "add", str(schema))
        git(repo, "commit", "-qm", "fixture: incompatible schema")
        bad = self.candidate_lock(git(repo, "rev-parse", "HEAD"))
        with export_snapshot(repo, bad) as staged:
            with self.assertRaisesRegex(ValueError, "trusted schema"):
                validate_snapshot(repo, bad, staged)
        self.assertEqual(active["revision"], revision)
        # Rollback reselects and validates the original explicit pin.
        with export_snapshot(repo, LOCK) as staged:
            validate_snapshot(repo, LOCK, staged)
            active = load_lock(LOCK)
        self.assertEqual(active["revision"], self.lock["revision"])

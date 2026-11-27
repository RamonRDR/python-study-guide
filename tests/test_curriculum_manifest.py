"""Sprint 08A: synthetic manifest contract tests, not a published curriculum."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from curriculum_manifest import load_manifest, validate_manifest

LOCALES = ("en", "pt-BR", "es")


def localized(value):
    return {locale: value for locale in LOCALES}


def paths(directory):
    return {locale: f"{directory}/README{suffix}.md"
            for locale, suffix in zip(LOCALES, ("", ".pt-BR", ".es"))}


def fixture():
    return {
        "schema_version": "1.0.0",
        "default_locale": "en",
        "supported_locales": list(LOCALES),
        "association_status": "pending",
        "assets": ["assets/banner.png"],
        "banks": {
            "quizzes": {
                "schema_version": "1.0.0", "index": "quizzes/quiz-index.json",
                "index_schema": "schemas/quiz-index.schema.json",
                "record_schema": "schemas/quiz.schema.json",
            },
            "exercises": {
                "schema_version": "1.0.0",
                "index": "exercises/problem-solving/exercise-index.json",
                "index_schema": "schemas/exercise-index.schema.json",
                "record_schema": "schemas/exercise.schema.json",
            },
            "interviews": {"schema_version": "0.1.0", "index": "interviews/interview-index.json"},
            "mocks": {"schema_version": "0.1.0", "index": "interviews/mocks/mock-index.json"},
        },
        "modules": [{
            "id": "getting-started", "order": 0, "slug": "getting-started",
            "kind": "onboarding", "educational_phase": None,
            "title": localized("Getting started"), "index": paths("getting-started"),
            "chapters": [{
                "id": "getting-started.install-python", "order": 0,
                "slug": "install-python", "kind": "lesson",
                "title": localized("Install Python"),
                "content": paths("getting-started/01-install-python"),
                "assets": [], "resources": ["getting-started/01-install-python/example.py"],
                "previous_id": None, "next_id": None,
                "quiz_ids": [], "exercise_ids": [], "interview_ids": [], "mock_ids": [],
                "execution": "unverified",
            }],
        }],
    }


class CurriculumManifestTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.data = fixture()
        self.chapter = self.data["modules"][0]["chapters"][0]
        files = self.data["assets"] + self.chapter["resources"]
        files += list(self.data["modules"][0]["index"].values())
        files += list(self.chapter["content"].values())
        files += [value for bank in self.data["banks"].values()
                  for key, value in bank.items() if key != "schema_version"]
        for path in files:
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("fixture", encoding="utf-8")
        self.manifest = self.root / "manifest.json"

    def write(self, data=None):
        self.manifest.write_text(json.dumps(self.data if data is None else data), encoding="utf-8")

    def test_valid_fixture(self):
        self.write()
        self.assertEqual(load_manifest(self.root, "manifest.json"), self.data)

    def test_invalid_root_metadata(self):
        variants = [
            ("schema_version", "2.0.0"), ("default_locale", "es"),
            ("supported_locales", ["en", "es"]), ("association_status", "unknown"),
            ("modules", []), ("extra", 1),
        ]
        for key, value in variants:
            with self.subTest(key=key):
                data = copy.deepcopy(self.data)
                data[key] = value
                with self.assertRaises(ValueError):
                    validate_manifest(data, self.root)

    def test_missing_required_and_locale(self):
        for key in tuple(self.chapter):
            with self.subTest(key=key):
                data = copy.deepcopy(self.data)
                del data["modules"][0]["chapters"][0][key]
                with self.assertRaises(ValueError):
                    validate_manifest(data, self.root)
        del self.chapter["title"]["es"]
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)

    def test_strict_order_types(self):
        for value in (-1, True, 1.0, "1"):
            with self.subTest(value=value):
                self.chapter["order"] = value
                with self.assertRaises(ValueError):
                    validate_manifest(self.data, self.root)

    def test_bank_version_and_path(self):
        bank = self.data["banks"]["interviews"]
        bank["schema_version"] = "1.0.0"
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)
        bank["schema_version"] = "0.1.0"
        bank["index"] = "quizzes/quiz-index.json"
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)

    def test_execution_metadata(self):
        self.chapter["execution"] = "browser_compatible"
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)
        self.chapter["execution"] = "local_only"
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)
        self.chapter["execution_reason"] = localized("Requires local Python")
        validate_manifest(self.data, self.root)
        self.chapter["execution"] = "unverified"
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)

    def test_unsafe_and_missing_paths(self):
        for path in ("../escape", "/absolute", "C:/absolute", "assets//banner.png",
                     "assets/./banner.png", "assets\\banner.png", "https://example.org/a",
                     "assets/%2e%2e/a", "assets/missing.png", "assets/"):
            with self.subTest(path=path):
                self.chapter["assets"] = [path]
                with self.assertRaises(ValueError):
                    validate_manifest(self.data, self.root)

    def test_wrong_locale_path(self):
        self.chapter["content"]["es"] = self.chapter["content"]["en"]
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)

    def test_symlink_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            outside = Path(directory) / "outside.txt"
            outside.write_text("outside", encoding="utf-8")
            link = self.root / "assets/link.txt"
            try:
                link.symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            self.chapter["assets"] = ["assets/link.txt"]
            with self.assertRaises(ValueError):
                validate_manifest(self.data, self.root)

    def test_invalid_json(self):
        for raw in ('{"x": 1, "x": 2}', '{"x": NaN}', '{"x": Infinity}',
                    '{"x": -Infinity}', '{"x": 1e999}', '{"x": }'):
            with self.subTest(raw=raw):
                self.manifest.write_text(raw, encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_manifest(self.root, "manifest.json")

    def test_duplicate_reference_and_blank_title(self):
        self.chapter["quiz_ids"] = ["quiz.example", "quiz.example"]
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)
        self.chapter["quiz_ids"] = []
        self.chapter["title"]["en"] = "   "
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)

    def test_module_kind_phase_consistency(self):
        module = self.data["modules"][0]
        module["educational_phase"] = 1
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)
        module["kind"] = "phase"
        validate_manifest(self.data, self.root)

    def test_dependency_paths(self):
        self.chapter["dependency_paths"] = ["requirements.txt"]
        with self.assertRaises(ValueError):
            validate_manifest(self.data, self.root)
        (self.root / "requirements.txt").write_text("", encoding="utf-8")
        self.chapter["local_python"] = "3.13"
        validate_manifest(self.data, self.root)

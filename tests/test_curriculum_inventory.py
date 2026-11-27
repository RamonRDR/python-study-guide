"""Sprint 08B: published inventory and negative authoring regressions."""
import copy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from curriculum_manifest import read_json
from curriculum_inventory import (
    load_inventory, tracked_paths, validate_inventory,
)

MANIFEST = ROOT / "curriculum/manifest.json"


class CurriculumInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_json(MANIFEST)
        cls.tracked = tracked_paths(ROOT)

    def setUp(self):
        self.manifest = copy.deepcopy(self.data)

    def reject(self):
        with self.assertRaises(ValueError):
            validate_inventory(self.manifest, ROOT, self.tracked)

    def test_published_inventory(self):
        data = load_inventory(ROOT)
        modules = data["modules"]
        chapters = [chapter for module in modules for chapter in module["chapters"]]
        self.assertEqual(len(modules), 14)
        self.assertEqual(len(chapters), 115)
        self.assertEqual(sum(c["kind"] == "lesson" for c in chapters), 107)
        self.assertEqual(sum(c["kind"] == "project" for c in chapters), 8)
        self.assertEqual(len({c["id"] for c in chapters}), 115)
        self.assertEqual(len({p for c in chapters for p in c["content"].values()}), 345)
        self.assertEqual(sum(len(c["resources"]) for c in chapters), 243)
        self.assertEqual(len(data["assets"]), 6)

    def test_historical_ids_and_endpoints(self):
        chapters = [c for m in self.manifest["modules"] for c in m["chapters"]]
        ids = {c["id"] for c in chapters}
        self.assertTrue({"problem-solving.debugging", "problem-solving.refactoring",
                         "problem-solving.mixed"}.issubset(ids))
        self.assertIsNone(chapters[0]["previous_id"])
        self.assertIsNone(chapters[-1]["next_id"])
        for left, right in zip(chapters, chapters[1:]):
            self.assertEqual(left["next_id"], right["id"])
            self.assertEqual(right["previous_id"], left["id"])

    def test_duplicate_module_id(self):
        self.manifest["modules"][1]["id"] = self.manifest["modules"][0]["id"]
        self.reject()

    def test_duplicate_chapter_id(self):
        chapters = self.manifest["modules"][0]["chapters"]
        chapters[1]["id"] = chapters[0]["id"]
        self.reject()

    def test_wrong_order_and_missing_chapter(self):
        self.manifest["modules"][0]["chapters"][1]["order"] = 0
        self.reject()
        self.manifest = copy.deepcopy(self.data)
        self.manifest["modules"][0]["chapters"].pop()
        self.reject()

    def test_wrong_previous_next(self):
        self.manifest["modules"][1]["chapters"][0]["previous_id"] = None
        self.reject()

    def test_wrong_title_and_phase(self):
        self.manifest["modules"][0]["chapters"][0]["title"]["es"] = "Incorrect"
        self.reject()
        self.manifest = copy.deepcopy(self.data)
        self.manifest["modules"][1]["educational_phase"] = 2
        self.reject()

    def test_wrong_slug_and_content(self):
        self.manifest["modules"][0]["chapters"][0]["slug"] = "different"
        self.reject()
        self.manifest = copy.deepcopy(self.data)
        chapters = self.manifest["modules"][0]["chapters"]
        chapters[0]["content"] = copy.deepcopy(chapters[1]["content"])
        self.reject()

    def test_wrong_module_index(self):
        self.manifest["modules"][0]["index"] = copy.deepcopy(
            self.manifest["modules"][1]["index"])
        self.reject()

    def test_missing_resource_and_asset(self):
        chapter = next(c for m in self.manifest["modules"] for c in m["chapters"]
                       if c["resources"])
        chapter["resources"].pop()
        self.reject()
        self.manifest = copy.deepcopy(self.data)
        self.manifest["assets"].pop()
        self.reject()

    def test_extra_resource_outside_chapter(self):
        self.manifest["modules"][0]["chapters"][0]["resources"].append("README.md")
        self.reject()

    def test_untracked_content_rejected(self):
        path = self.manifest["modules"][0]["chapters"][0]["content"]["es"]
        with self.assertRaises(ValueError):
            validate_inventory(self.manifest, ROOT, self.tracked - {path})

    def test_unlisted_tracked_chapter_rejected(self):
        with self.assertRaises(ValueError):
            validate_inventory(self.manifest, ROOT, self.tracked | {
                "fundamentals/99-unlisted/README.md",
            })

    def test_pending_associations_only(self):
        self.manifest["association_status"] = "complete"
        self.reject()
        self.manifest = copy.deepcopy(self.data)
        self.manifest["modules"][0]["chapters"][0]["quiz_ids"] = ["quiz.example"]
        self.reject()

    def test_execution_metadata(self):
        module = next(m for m in self.manifest["modules"] if m["id"] == "external-libraries")
        module["chapters"][0].pop("dependency_paths")
        self.reject()
        self.manifest = copy.deepcopy(self.data)
        chapter = next(c for m in self.manifest["modules"] for c in m["chapters"]
                       if c["id"] == "practical-projects.file-organizer")
        self.assertEqual(chapter["execution"], "local_only")
        chapter["execution"] = "unverified"
        chapter.pop("execution_reason")
        self.reject()

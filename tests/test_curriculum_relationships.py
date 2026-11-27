"""Complete relationship contract: canonical associations and fail-closed gates."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from curriculum_manifest import read_json
from curriculum_relationships import (
    association_map, preliminary_bank, read_index, validate_associations, validate_relationships,
)


class CurriculumRelationshipTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_json(ROOT / "curriculum/manifest.json")
        cls.expected = association_map(cls.data, ROOT)

    def setUp(self):
        self.data = copy.deepcopy(self.__class__.data)
        self.chapters = [c for m in self.data["modules"] for c in m["chapters"]]

    def reject(self):
        with self.assertRaises(ValueError):
            validate_associations(self.data, self.expected)

    def test_complete_manifest(self):
        validate_relationships(self.data, ROOT)
        for field, total in (("quiz_ids", 160), ("exercise_ids", 30),
                             ("interview_ids", 60), ("mock_ids", 3)):
            ids = [i for c in self.chapters for i in c[field]]
            self.assertEqual(len(set(ids)), total)
            if field != "interview_ids":
                self.assertEqual(len(ids), total)
        self.assertEqual(self.data["association_status"], "complete")
        self.assertEqual(self.chapters[-1]["mock_ids"],
                         ["mock.junior-30", "mock.mid-45", "mock.senior-60"])

    def test_pending_rejected(self):
        self.data["association_status"] = "pending"
        self.reject()

    def test_missing_quiz(self):
        next(c for c in self.chapters if c["quiz_ids"])["quiz_ids"].pop()
        self.reject()

    def test_duplicate_exercise(self):
        chapter = next(c for c in self.chapters if c["exercise_ids"])
        chapter["exercise_ids"].append(chapter["exercise_ids"][0])
        self.reject()

    def test_wrong_quiz_owner(self):
        owner = next(c for c in self.chapters if c["quiz_ids"])
        other = next(c for c in self.chapters if c is not owner)
        other["quiz_ids"].append(owner["quiz_ids"].pop())
        self.reject()

    def test_missing_interview_prerequisite(self):
        next(c for c in self.chapters if c["interview_ids"])["interview_ids"].pop()
        self.reject()

    def test_invented_interview_prerequisite(self):
        source = next(c for c in self.chapters if c["interview_ids"])
        target = next(c for c in self.chapters if not c["interview_ids"])
        target["interview_ids"].append(source["interview_ids"][0])
        self.reject()

    def test_wrong_mock_lesson(self):
        self.chapters[0]["mock_ids"].append(self.chapters[-1]["mock_ids"].pop())
        self.reject()

    def test_mock_order(self):
        self.chapters[-1]["mock_ids"].reverse()
        self.reject()

    def test_unknown_id(self):
        self.chapters[0]["quiz_ids"].append("quiz.not-indexed")
        self.reject()

    def test_index_version_and_strict_json(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "index.json"
            for raw in (
                '{"schema_version":"9.0.0"}',
                '{"schema_version":"1.0.0","schema_version":"1.0.0"}',
                '{"schema_version":"1.0.0","x":NaN}',
                '{"schema_version":"1.0.0","x":1e999}',
            ):
                path.write_text(raw, encoding="utf-8")
                with self.subTest(raw=raw), self.assertRaises(ValueError):
                    read_index(root, {"index": "index.json", "schema_version": "1.0.0"})
            path.write_text('{"schema_version":"1.0.0","x":9007199254740993}',
                            encoding="utf-8")
            self.assertEqual(read_index(root, {"index": "index.json",
                                              "schema_version": "1.0.0"})["x"],
                             9007199254740993)

    def test_preliminary_records_use_strict_json(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            questions = root / "interviews/questions"
            questions.mkdir(parents=True)
            (root / "interviews/interview-index.json").write_text(
                '{"schema_version":"0.1.0","question_ids":["python.example"]}',
                encoding="utf-8",
            )
            path = questions / "python.example.json"
            descriptor = {"schema_version": "0.1.0", "index": "interviews/interview-index.json"}
            for raw in ('{"id":"python.example","x":Infinity}',
                        '{"id":"python.example","x":1e999}',
                        '{"id":"python.example","id":"python.example"}'):
                path.write_text(raw, encoding="utf-8")
                with self.subTest(raw=raw), self.assertRaises(ValueError):
                    preliminary_bank(root, descriptor, "question_ids",
                                     "interviews/questions",
                                     lambda _: self.fail("lenient loader must not run"), None)

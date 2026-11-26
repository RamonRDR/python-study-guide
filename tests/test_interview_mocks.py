"""Check the Sprint 06 mock contract, cross-references and localized views."""
from collections import Counter
import copy
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest

from scripts.interview_records import load_bank, SUFFIXES
from scripts.interview_mocks import load_mocks, validate_mock, render_mocks, CHAPTER, START, END

ROOT = Path(__file__).resolve().parents[1]


class InterviewMocksTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions = load_bank(ROOT)
        cls.mocks = load_mocks(ROOT)
        cls.by_id = {q["id"]: q for q in cls.questions}

    def test_complete_question_distribution(self):
        self.assertEqual(len(self.questions), 60)
        self.assertEqual(Counter(q["level"] for q in self.questions),
                         {"junior": 24, "mid": 24, "senior": 12})
        behavioral = [q for q in self.questions if q["topic"] == "behavioral-international"]
        self.assertEqual(Counter(q["level"] for q in behavioral),
                         {"junior": 1, "mid": 1, "senior": 1})

    def test_mock_levels_durations_and_references(self):
        self.assertEqual([(m["level"], m["duration_minutes"]) for m in self.mocks],
                         [("junior", 30), ("mid", 45), ("senior", 60)])
        for m in self.mocks:
            self.assertEqual(validate_mock(m, self.by_id, ROOT), [], m["id"])
            self.assertEqual(sum(m["time_allocation"].values()), m["duration_minutes"])
            self.assertEqual(sum(r["points"] for r in m["rubric"]), 100)
            self.assertEqual(len(m["question_ids"]), 4)
            self.assertEqual(len(m["question_ids"]), len(set(m["question_ids"])))
            self.assertTrue(all(self.by_id[q]["level"] == m["level"] for q in m["question_ids"]))

    def test_invalid_mock_records_are_rejected(self):
        mutations = [
            (lambda m: m.update(duration_minutes=31), "invalid time allocation or duration"),
            (lambda m: m["time_allocation"].update(coding=True), "invalid time allocation or duration"),
            (lambda m: m["time_allocation"].update(coding=12), "invalid time allocation or duration"),
            (lambda m: m["time_allocation"].update(extra=1), "invalid time allocation or duration"),
            (lambda m: m["question_ids"].__setitem__(2, m["question_ids"][1]), "invalid or mismatched question references"),
            (lambda m: m["question_ids"].pop(), "invalid or mismatched question references"),
            (lambda m: m["question_ids"].reverse(), "first question must be behavioral"),
            (lambda m: m["question_ids"].__setitem__(1, "missing.question"), "invalid or mismatched question references"),
            (lambda m: m["question_ids"].__setitem__(1, "api.object-authorization"), "invalid or mismatched question references"),
            (lambda m: m["question_ids"].__setitem__(0, "python.conversion-contract"), "one behavioral question per mock required"),
            (lambda m: m.update(exercise_id="problem-solving.missing",
                                exercise_path="exercises/problem-solving/missing/exercise.json"),
             "exercise reference escapes repository or is missing"),
            (lambda m: m.update(exercise_id="problem-solving.sorted-pair-multiplicity",
                                exercise_path="exercises/problem-solving/sorted-pair-multiplicity/exercise.json"),
             "exercise difficulty mismatch for this mock"),
            (lambda m: m.update(exercise_path="../exercise.json"), "invalid exercise reference"),
            (lambda m: m.update(exercise_path="exercises/problem-solving/binary-insertion-index/exercise.json"), "invalid exercise reference"),
            (lambda m: m["instructions"].pop("es"), "invalid localized field: instructions"),
            (lambda m: m["rubric"][0].update(points=True), "invalid rubric dimension"),
            (lambda m: m["rubric"][0].update(points=24), "invalid rubric dimension"),
            (lambda m: m["rubric"][0].update(partial_points=25), "invalid rubric dimension"),
            (lambda m: m["rubric"][0]["indicators"]["en"].clear(), "invalid rubric dimension"),
            (lambda m: m["rubric"][0]["indicators"]["es"].append("Extra"), "unaligned indicator counts"),
            (lambda m: m["rubric"].__setitem__(1, copy.deepcopy(m["rubric"][0])), "duplicate rubric dimension"),
            (lambda m: m.update(improvement={"en": "", "pt-BR": "", "es": ""}), "invalid localized field: improvement"),
        ]
        # All mutations start from a known valid record; unrelated defects cannot
        # satisfy the assertion for the rule being exercised.
        self.assertEqual(validate_mock(self.mocks[0], self.by_id, ROOT), [])
        self.assertIn("python.conversion-contract", self.by_id)
        self.assertEqual(self.by_id["python.conversion-contract"]["level"], "junior")
        for i, (mutate, expected) in enumerate(mutations):
            with self.subTest(case=i):
                m = copy.deepcopy(self.mocks[0])
                mutate(m)
                self.assertIn(expected, validate_mock(m, self.by_id, ROOT))

    def test_invalid_mock_index(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            mock_dir = root / "interviews/mocks"
            mock_dir.mkdir(parents=True)
            index = mock_dir / "mock-index.json"
            ids = [m["id"] for m in self.mocks]
            for invalid, expected in (
                ([], "invalid preliminary mock index"),
                ({"schema_version": "9.0.0", "mock_ids": ids}, "invalid preliminary mock index"),
                ({"schema_version": "0.1.0", "mock_ids": [ids[0]] * 3}, "invalid mock IDs"),
                ({"schema_version": "0.1.0", "mock_ids": ["../escape", *ids[1:]]}, "invalid mock IDs"),
                ({"schema_version": "0.1.0", "mock_ids": ids}, "mock index and files disagree"),
            ):
                with self.subTest(index=invalid):
                    index.write_text(json.dumps(invalid), encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, expected):
                        load_mocks(root)

    def test_generated_views(self):
        for locale, filename in SUFFIXES.items():
            text = (ROOT / CHAPTER / filename).read_text(encoding="utf-8")
            self.assertEqual(text.count(START), 1)
            self.assertEqual(text.count(END), 1)
            block = text.split(START)[1].split(END)[0]
            self.assertEqual(block, render_mocks(self.mocks, locale))


if __name__ == "__main__":
    unittest.main()

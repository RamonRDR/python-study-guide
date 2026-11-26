"""Check the Sprint 06 mock contract, cross-references and localized views."""
from collections import Counter
import copy
from pathlib import Path
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
            self.assertEqual(len(m["question_ids"]), len(set(m["question_ids"])))
            self.assertTrue(all(self.by_id[q]["level"] == m["level"] for q in m["question_ids"]))

    def test_invalid_mock_records_are_rejected(self):
        mutations = [
            lambda m: m.update(duration_minutes=31),
            lambda m: m["time_allocation"].update(coding=True),
            lambda m: m["time_allocation"].update(coding=12),
            lambda m: m["time_allocation"].update(extra=1),
            lambda m: m["question_ids"].append(m["question_ids"][0]),
            lambda m: m["question_ids"].__setitem__(0, "missing.question"),
            lambda m: m.update(question_ids=["api.object-authorization"]),
            lambda m: m.update(exercise_id="problem-solving.missing"),
            lambda m: m.update(exercise_id="problem-solving.sorted-pair-multiplicity"),
            lambda m: m.update(exercise_path="../exercise.json"),
            lambda m: m.update(exercise_path="exercises/problem-solving/binary-insertion-index/exercise.json"),
            lambda m: m["instructions"].pop("es"),
            lambda m: m["rubric"][0].update(points=True),
            lambda m: m["rubric"][0].update(points=24),
            lambda m: m["rubric"][0].update(partial_points=25),
            lambda m: m["rubric"][0]["indicators"]["en"].clear(),
            lambda m: m["rubric"][0]["indicators"]["es"].append("Extra"),
            lambda m: m["rubric"][1].update(id=m["rubric"][0]["id"]),
            lambda m: m.update(improvement={"en": "", "pt-BR": "", "es": ""}),
        ]
        for i, mutate in enumerate(mutations):
            with self.subTest(case=i):
                m = copy.deepcopy(self.mocks[0])
                mutate(m)
                self.assertTrue(validate_mock(m, self.by_id, ROOT))

    def test_generated_views(self):
        for locale, filename in SUFFIXES.items():
            text = (ROOT / CHAPTER / filename).read_text(encoding="utf-8")
            self.assertEqual(text.count(START), 1)
            self.assertEqual(text.count(END), 1)
            block = text.split(START)[1].split(END)[0]
            self.assertEqual(block, render_mocks(self.mocks, locale))


if __name__ == "__main__":
    unittest.main()

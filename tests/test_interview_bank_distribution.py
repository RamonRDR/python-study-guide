"""Preserve the approved technical question-bank coverage."""
from collections import Counter
from pathlib import Path
import unittest

from scripts.interview_records import load_bank

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "interview-fundamentals": (3, 2, 1),
    "python-fundamentals": (4, 3, 1),
    "data-structures-algorithms": (3, 3, 1),
    "oop": (3, 3, 2),
    "python-internals": (2, 4, 2),
    "testing-debugging": (3, 3, 1),
    "backend-apis": (2, 2, 1),
    "databases-sql": (2, 2, 1),
    "software-engineering": (1, 1, 1),
}
PILOT_IDS = {
    "interview.clarify-contract", "python.mutable-default",
    "algorithms.duplicate-membership", "oop.replaceable-collaborator",
    "internals.nested-copy", "sql.zero-child-count",
    "internals.gil-workload", "api.object-authorization",
    "engineering.architecture-tradeoffs",
}


class TechnicalBankCoverageTests(unittest.TestCase):
    def test_technical_distribution(self):
        questions = load_bank(ROOT)
        technical = [q for q in questions if q["topic"] != "behavioral-international"]
        self.assertEqual(len(technical), 57)
        counts = Counter((q["topic"], q["level"]) for q in technical)
        expected = {
            (topic, level): count
            for topic, values in EXPECTED.items()
            for level, count in zip(("junior", "mid", "senior"), values)
        }
        self.assertEqual(counts, expected)

    def test_original_pilot_ids_are_preserved(self):
        from scripts.interview_records import read_json

        index = read_json(ROOT / "interviews/interview-index.json")
        self.assertEqual(set(index["pilot_question_ids"]), PILOT_IDS)
        self.assertEqual(len(index["pilot_question_ids"]), len(PILOT_IDS))


if __name__ == "__main__":
    unittest.main()

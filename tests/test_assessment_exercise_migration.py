"""Canonical exercise migration: grade only explicit trusted repository fixtures."""
from collections import Counter
from copy import deepcopy
from pathlib import Path
import runpy
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assessment_grading import case_passes, exact_equal
from assessment_records import load_index, load_matrix, read_json
from test_problem_solving_expansion import APPROVED
from test_assessment_pilot import PILOT_EXERCISES

BANK = ROOT / "exercises" / "problem-solving"
SLUGS = ("vowel-counter", *APPROVED)
NEW_CONTAINERS = {
    "binary-target-range", "descending-insertion-sort", "label-counts",
    "merge-inventory", "merge-sorted-lists", "recursive-flatten",
    "refactor-score-summary", "unique-in-order", "inventory-reconciliation",
}
VOWEL_WRONGS = (
    "lowercase_only", "unique_vowels", "normalized_string", "includes_y",
    "returns_boolean", "returns_too_early",
)


class ExerciseMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_index("exercise", ROOT,
                                 "exercises/problem-solving/exercise-index.json",
                                 load_matrix(ROOT))
        cls.by_id = {r["id"]: r for r in cls.records}

    def test_canonical_inventory(self):
        self.assertEqual(len(self.records), 30)
        self.assertEqual(set(self.by_id), {"problem-solving." + s for s in SLUGS})
        self.assertEqual({p.parent.name for p in BANK.glob("*/exercise.json")},
                         set(SLUGS))
        self.assertEqual(Counter(r["difficulty"] for r in self.records),
                         {"easy": 12, "medium": 12, "hard": 6})
        self.assertEqual(sum(len(r["tests"]["cases"]) for r in self.records), 192)
        self.assertEqual(sum(len(self.by_id[i]["tests"]["cases"])
                             for i in PILOT_EXERCISES), 24)
        self.assertEqual(Counter(r["practice_mode"] for r in self.records),
                         {"implement": 26, "debug": 2, "refactor": 2})
        for r in self.records:
            with self.subTest(id=r["id"]):
                self.assertEqual(r["schema_version"], "1.0.0")
                self.assertEqual(r["execution"], "unverified")
                self.assertEqual(r["allowed_dependencies"], [])
                self.assertEqual(r["local_python"], "3.13")
                slug = r["id"].split(".", 1)[1]
                self.assertIs(r["tests"]["new_container"], slug in NEW_CONTAINERS)
                self.assertEqual(r["solution_path"],
                                 f"exercises/problem-solving/{slug}/solution.py")
                self.assertEqual(r["starter_path"],
                                 f"exercises/problem-solving/{slug}/starter.py")

    def test_legacy_compatibility_index(self):
        legacy = read_json(BANK / "expansion-index.json")
        self.assertEqual(legacy["status"], "preliminary")
        self.assertEqual(len(legacy["exercises"]), 29)
        self.assertEqual({r["id"] for r in legacy["exercises"]},
                         set(self.by_id) - {"problem-solving.vowel-counter"})

    def test_all_reference_and_wrong_candidates(self):
        # Fixed allowlist and file names, not executable paths from records.
        for slug in SLUGS:
            record = self.by_id["problem-solving." + slug]
            with self.subTest(slug=slug):
                cases = record["tests"]["cases"]
                new_container = record["tests"]["new_container"]
                fn = record["tests"]["function_name"]
                reference = runpy.run_path(str(BANK / slug / "solution.py"))[fn]
                self.assertTrue(all(case_passes(reference, case, new_container=new_container)
                                    for case in cases))
                namespace = runpy.run_path(str(BANK / slug / "test_solution.py"))
                names = VOWEL_WRONGS if slug == "vowel-counter" else ("wrong_solution",)
                for name in names:
                    self.assertTrue(any(not case_passes(namespace[name], case,
                                                       new_container=new_container)
                                        for case in cases), name)

    def test_starter_modes_through_canonical_grader(self):
        for slug in SLUGS:
            record = self.by_id["problem-solving." + slug]
            with self.subTest(slug=slug):
                cases = record["tests"]["cases"]
                starter = runpy.run_path(str(BANK / slug / "starter.py"))[
                    record["tests"]["function_name"]]
                passed = sum(case_passes(starter, case,
                                         new_container=record["tests"]["new_container"])
                             for case in cases)
                mode = record["practice_mode"]
                if mode == "refactor":
                    self.assertEqual(passed, len(cases))
                elif mode == "debug":
                    self.assertGreater(passed, 0)
                    self.assertLess(passed, len(cases))
                else:
                    self.assertEqual(passed, 0)

    def test_large_integer_and_nested_alias(self):
        factorial = self.by_id["problem-solving.recursive-factorial"]
        case = next(c for c in factorial["tests"]["cases"] if c["args"] == [20])
        self.assertIs(type(case["expected"]), int)
        self.assertEqual(case["expected"], 2432902008176640000)
        self.assertGreater(case["expected"], 2**53 - 1)
        nested = {"args": [[[1], [2]]], "expected": [[1], [2]]}
        self.assertFalse(case_passes(list, nested, new_container=True))
        self.assertTrue(case_passes(deepcopy, nested, new_container=True))
        self.assertFalse(exact_equal({"n": [True]}, {"n": [1]}))

    def test_timing_metadata(self):
        timed = {r["id"]: r for r in self.records if "timed_practice" in r}
        self.assertEqual(set(timed), {"problem-solving.timed-threshold-count",
                                     "problem-solving.timed-longest-streak"})
        self.assertEqual({r["timed_practice"]["duration_minutes"] for r in timed.values()},
                         {10, 20})
        for r in timed.values():
            self.assertEqual(r["timed_practice"]["duration_minutes"], r["estimated_minutes"])
            self.assertIs(r["timed_practice"]["independent_first_attempt"], True)
            self.assertEqual(r["timed_practice"]["grading"], "self_assessment")


if __name__ == "__main__":
    unittest.main()

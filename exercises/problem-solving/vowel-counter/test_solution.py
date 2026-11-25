"""Validate the pilot contract against trusted, finite implementations only."""

import json
from pathlib import Path
import runpy
import unittest


ROOT = Path(__file__).resolve().parent
RECORD = json.loads((ROOT / "exercise.json").read_text(encoding="utf-8"))
REFERENCE = runpy.run_path(str(ROOT / "solution.py"))["count_vowels"]
CASES = RECORD["tests"]["cases"]


def failing_case_ids(candidate):
    """Check exact type and value; exceptions also fail a case."""
    failures = []
    for case in CASES:
        try:
            result = candidate(*case["args"])
        except Exception:
            failures.append(case["id"])
            continue
        expected = case["expected"]
        if type(result) is not type(expected) or result != expected:
            failures.append(case["id"])
    return failures


def lowercase_only(text):
    return sum(character in "aeiou" for character in text)


def unique_vowels(text):
    return len(set(text) & set("aeiouAEIOU"))


def normalized_string(text):
    return sum(character in "aeiou" for character in text.lower())


def includes_y(text):
    return sum(character in "aeiouAEIOUyY" for character in text)


def returns_boolean(text):
    return any(character in "aeiouAEIOU" for character in text)


def returns_too_early(text):
    for character in text:
        return int(character in "aeiouAEIOU")
    return 0


class VowelCounterTests(unittest.TestCase):
    def test_record_interface(self):
        self.assertEqual(RECORD["id"], "problem-solving.vowel-counter")
        self.assertEqual(RECORD["chapter_id"], "problem-solving.strings-and-numbers")
        self.assertEqual(RECORD["tests"]["interface"], "function_call")
        self.assertEqual(RECORD["tests"]["function_name"], "count_vowels")
        self.assertEqual(RECORD["tests"]["comparison"], "exact_type_and_value")
        self.assertEqual(RECORD["execution"], "unverified")
        self.assertEqual(RECORD["allowed_dependencies"], [])
        self.assertEqual(RECORD["local_python"], "3.13")
        self.assertGreater(RECORD["tests"]["timeout_ms"], 0)
        self.assertEqual(len(CASES), len({case["id"] for case in CASES}))
        self.assertTrue(CASES)
        for case in CASES:
            self.assertEqual(len(case["args"]), 1)
            self.assertIs(type(case["args"][0]), str)
            self.assertIs(type(case["expected"]), int)

    def test_reference_passes_all_cases(self):
        self.assertEqual(failing_case_ids(REFERENCE), [])

    def test_examples_agree_with_reference_and_cases(self):
        for example in RECORD["examples"]:
            with self.subTest(example=example):
                self.assertIs(type(example["expected"]), int)
                self.assertEqual(REFERENCE(*example["args"]), example["expected"])
                self.assertTrue(any(
                    case["args"] == example["args"] and
                    case["expected"] == example["expected"]
                    for case in CASES
                ))

    def test_rejects_representative_wrong_solutions(self):
        for candidate, case_id in (
            (lowercase_only, "uppercase"),
            (unique_vowels, "repeated"),
            (normalized_string, "accents-and-unicode"),
            (includes_y, "no-vowels"),
            (returns_boolean, "empty"),
            (returns_too_early, "vowels-at-end"),
        ):
            with self.subTest(candidate=candidate.__name__):
                self.assertIn(case_id, failing_case_ids(candidate))

    def test_exception_fails_case(self):
        def broken(_text):
            raise ValueError("Known test fixture")

        self.assertEqual(failing_case_ids(broken), [case["id"] for case in CASES])

    def test_localized_fields_present(self):
        locales = {"en", "pt-BR", "es"}
        for field in ("title", "prompt", "constraints", "hints", "explanation"):
            self.assertEqual(set(RECORD[field]), locales)
            self.assertTrue(all(RECORD[field].values()))
        for locale in locales:
            self.assertEqual(len(RECORD["hints"][locale]), 3)
            self.assertEqual(len(RECORD["constraints"][locale]), 3)
        for field in ("time", "space"):
            self.assertEqual(set(RECORD["complexity"][field]), locales)
            self.assertTrue(all(RECORD["complexity"][field].values()))
        for example in RECORD["examples"]:
            self.assertEqual(set(example["explanation"]), locales)
        repository = ROOT.parents[2]
        for prerequisite in RECORD["prerequisite_paths"]:
            self.assertEqual(set(prerequisite), locales)
            for path in prerequisite.values():
                self.assertTrue((repository / path).is_file(), path)
        self.assertEqual(repository / RECORD["starter_path"], ROOT / "starter.py")
        self.assertEqual(repository / RECORD["solution_path"], ROOT / "solution.py")


if __name__ == "__main__":
    unittest.main()

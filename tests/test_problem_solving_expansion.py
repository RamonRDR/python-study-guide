"""Validate explicitly approved Phase 11 expansion fixtures, never learner code."""

from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
from io import StringIO
import json
from pathlib import Path
import runpy
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
ROOT = REPOSITORY / "exercises" / "problem-solving"
LOCALES = {"en", "pt-BR", "es"}

# Only these repository-owned, reviewed paths may be executed by this suite.
APPROVED = (
    "ascii-digit-counter",
    "sum-digits",
    "literal-palindrome",
    "unique-in-order",
    "label-counts",
    "first-repeated-label",
    "merge-inventory",
    "clamp-value",
    "recursive-factorial",
    "recursive-power",
    "linear-first-index",
    "binary-insertion-index",
    "descending-insertion-sort",
    "unordered-pair-count",
    "has-duplicate",
    "debug-positive-count",
    "debug-negative-window",
    "refactor-shipping-fee",
    "refactor-score-summary",
    "total-short-lengths",
    "most-frequent-label",
    "longest-distinct-substring",
    "recursive-flatten",
    "binary-target-range",
    "merge-sorted-lists",
    "sorted-pair-multiplicity",
    "inventory-reconciliation",
    "timed-threshold-count",
    "timed-longest-streak",
)


def exact_equal(actual, expected):
    """Compare JSON-compatible values recursively, without bool/int coercion."""
    if type(actual) is not type(expected):
        return False
    if isinstance(expected, list):
        return len(actual) == len(expected) and all(
            exact_equal(a, b) for a, b in zip(actual, expected)
        )
    if isinstance(expected, dict):
        if actual.keys() != expected.keys():
            return False
        return all(
            exact_equal(actual[key], value) for key, value in expected.items()
        )
    return actual == expected


def failures(candidate, cases, *, new_container=False):
    """Return case IDs failing output, mutation, return type or silence rules."""
    result = []
    for case in cases:
        args = deepcopy(case["args"])
        before = deepcopy(args)
        output = StringIO()
        errors = StringIO()
        try:
            with redirect_stdout(output), redirect_stderr(errors):
                actual = candidate(*args)
        except Exception:
            result.append(case["id"])
            continue
        if (
            not exact_equal(actual, case["expected"])
            or not exact_equal(args, before)
            or output.getvalue()
            or errors.getvalue()
            or (
                new_container
                and isinstance(actual, (list, dict))
                and any(actual is arg for arg in args)
            )
        ):
            result.append(case["id"])
    return result


class ExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = {
            slug: json.loads((ROOT / slug / "exercise.json").read_text(
                encoding="utf-8"
            ))
            for slug in APPROVED
        }

    def test_catalog_and_ids(self):
        index = json.loads((ROOT / "expansion-index.json").read_text(
            encoding="utf-8"
        ))
        self.assertEqual(index["status"], "preliminary")
        self.assertEqual(len(index["exercises"]), len(APPROVED))
        self.assertEqual(
            {entry["id"] for entry in index["exercises"]},
            {"problem-solving." + slug for slug in APPROVED},
        )
        for entry in index["exercises"]:
            slug = entry["id"].split(".", 1)[1]
            with self.subTest(slug=slug):
                record = self.records[slug]
                self.assertEqual(record["id"], entry["id"])
                self.assertEqual(record["practice_mode"], entry["practice_mode"])
                self.assertEqual(
                    entry["path"],
                    (ROOT / slug / "exercise.json").relative_to(
                        REPOSITORY
                    ).as_posix(),
                )
                chapter = REPOSITORY / entry["chapter_path"]
                slug_to_id = {"13-debugging-challenges": "debugging",
                              "14-refactoring-challenges": "refactoring",
                              "15-mixed-challenges": "mixed"}
                self.assertEqual(record["chapter_id"], "problem-solving." +
                                 slug_to_id.get(chapter.name, chapter.name[3:]))
                for name in ("README.md", "README.pt-BR.md", "README.es.md"):
                    self.assertTrue((chapter / name).is_file(), name)

    def test_full_bank_distribution_and_timed_metadata(self):
        from collections import Counter

        pilot = json.loads((ROOT / "vowel-counter" / "exercise.json").read_text(
            encoding="utf-8"
        ))
        records = [pilot, *self.records.values()]
        self.assertEqual(len(records), 30)
        self.assertEqual(len({record["id"] for record in records}), 30)
        self.assertEqual(Counter(record["difficulty"] for record in records),
                         {"easy": 12, "medium": 12, "hard": 6})
        self.assertEqual(sum(len(record["tests"]["cases"]) for record in records),
                         192)
        timed = [record for record in records if "timed_practice" in record]
        self.assertEqual({record["id"] for record in timed}, {
            "problem-solving.timed-threshold-count",
            "problem-solving.timed-longest-streak",
        })
        self.assertEqual({record["timed_practice"]["duration_minutes"]
                          for record in timed}, {10, 20})
        for record in timed:
            self.assertEqual(record["chapter_id"], "problem-solving.timed-live-coding")
            self.assertEqual(record["timed_practice"]["duration_minutes"],
                             record["estimated_minutes"])
            self.assertIs(record["timed_practice"]["independent_first_attempt"], True)
            self.assertEqual(record["timed_practice"]["grading"], "self_assessment")
            self.assertEqual(record["execution"], "unverified")

    def test_record_contract_and_locales(self):
        for slug, record in self.records.items():
            with self.subTest(slug=slug):
                directory = ROOT / slug
                self.assertIn(record["difficulty"], {"easy", "medium", "hard"})
                self.assertGreater(record["estimated_minutes"], 0)
                self.assertTrue(record["concepts"])
                self.assertEqual(len(record["concepts"]), len(set(record["concepts"])))
                self.assertEqual(record["execution"], "unverified")
                self.assertEqual(record["allowed_dependencies"], [])
                self.assertEqual(record["local_python"], "3.13")
                self.assertEqual(record["tests"]["interface"], "function_call")
                self.assertEqual(
                    record["tests"]["comparison"], "exact_type_and_value"
                )
                self.assertGreater(record["tests"]["timeout_ms"], 0)
                for field in ("title", "prompt", "constraints", "hints",
                              "explanation"):
                    self.assertEqual(set(record[field]), LOCALES)
                    self.assertTrue(all(record[field].values()))
                for locale in LOCALES:
                    self.assertEqual(len(record["hints"][locale]), 3)
                    self.assertTrue(all(record["hints"][locale]))
                    self.assertTrue(all(record["constraints"][locale]))
                for field in ("time", "space", "assumptions"):
                    self.assertEqual(set(record["complexity"][field]), LOCALES)
                    self.assertTrue(all(record["complexity"][field].values()))
                for field, filename in (
                    ("starter_path", "starter.py"),
                    ("solution_path", "solution.py"),
                ):
                    self.assertEqual(
                        record[field],
                        (directory / filename).relative_to(REPOSITORY).as_posix(),
                    )
                self.assertTrue(record["prerequisite_paths"])
                for group in record["prerequisite_paths"]:
                    self.assertEqual(set(group), LOCALES)
                    for path in group.values():
                        prerequisite = (REPOSITORY / path).resolve()
                        self.assertTrue(prerequisite.is_relative_to(REPOSITORY))
                        self.assertTrue(prerequisite.is_file(), path)
                cases = record["tests"]["cases"]
                self.assertGreaterEqual(len(cases), 5)
                self.assertEqual(len(cases), len({c["id"] for c in cases}))
                for example in record["examples"]:
                    self.assertEqual(set(example["explanation"]), LOCALES)
                    self.assertTrue(any(
                        exact_equal(c["args"], example["args"])
                        and exact_equal(c["expected"], example["expected"])
                        for c in cases
                    ))

    def test_reference_implementations(self):
        for slug, record in self.records.items():
            with self.subTest(slug=slug):
                solution = runpy.run_path(str(ROOT / slug / "solution.py"))
                candidate = solution[record["tests"]["function_name"]]
                self.assertEqual(
                    failures(candidate, record["tests"]["cases"],
                             new_container=True),
                    [],
                )

    def test_known_wrong_implementations_are_rejected(self):
        for slug, record in self.records.items():
            with self.subTest(slug=slug):
                wrong = runpy.run_path(
                    str(ROOT / slug / "test_solution.py")
                )["wrong_solution"]
                self.assertTrue(failures(wrong, record["tests"]["cases"]))

    def test_starters_match_practice_modes(self):
        for slug, record in self.records.items():
            with self.subTest(slug=slug):
                namespace = runpy.run_path(str(ROOT / slug / "starter.py"))
                candidate = namespace[record["tests"]["function_name"]]
                failed = failures(candidate, record["tests"]["cases"])
                if record["practice_mode"] == "refactor":
                    self.assertEqual(failed, [])
                elif record["practice_mode"] == "debug":
                    self.assertTrue(failed)
                    self.assertLess(len(failed), len(record["tests"]["cases"]))
                else:
                    self.assertEqual(record["practice_mode"], "implement")
                    self.assertEqual(len(failed), len(record["tests"]["cases"]))

    def test_advanced_and_timed_against_independent_oracles(self):
        """Exercise real trusted references against small deterministic domains."""
        from itertools import combinations, combinations_with_replacement, product

        def reference(slug):
            self.assertIn(slug, APPROVED)
            return runpy.run_path(str(ROOT / slug / "solution.py"))[
                self.records[slug]["tests"]["function_name"]
            ]

        def check(candidate, args, expected):
            self.assertEqual(
                failures(candidate, [{"id": "oracle", "args": args,
                                      "expected": expected}], new_container=True),
                [],
                (candidate.__name__, args, expected),
            )

        distinct = reference("longest-distinct-substring")
        for length in range(6):
            for chars in product("ab🙂", repeat=length):
                text = "".join(chars)
                best = max(
                    (end - start for start in range(length + 1)
                     for end in range(start, length + 1)
                     if len(set(text[start:end])) == end - start),
                    default=0,
                )
                check(distinct, [text], best)

        flatten = reference("recursive-flatten")
        for depth in range(11):
            nested = [0, -1, 0]
            for _ in range(depth):
                nested = [[], nested, []]
            check(flatten, [nested], [0, -1, 0])

        bounds = reference("binary-target-range")
        pairs = reference("sorted-pair-multiplicity")
        merge = reference("merge-sorted-lists")
        sorted_inputs = [
            list(values) for length in range(5)
            for values in combinations_with_replacement((-2, 0, 2), length)
        ]
        for values in sorted_inputs:
            for target in range(-4, 5):
                matches = [i for i, value in enumerate(values) if value == target]
                check(bounds, [values, target],
                      [matches[0], matches[-1]] if matches else [-1, -1])
                expected = sum(a + b == target for a, b in combinations(values, 2))
                check(pairs, [values, target], expected)
            for other in sorted_inputs:
                check(merge, [values, other], sorted(values + other))

        count = reference("timed-threshold-count")
        streak = reference("timed-longest-streak")
        for length in range(5):
            for sequence in product((-1, 0, 1), repeat=length):
                values = list(sequence)
                for threshold in (-1, 0, 1, 2):
                    check(count, [values, threshold],
                          len([value for value in values if value >= threshold]))
                    best = max(
                        (end - start for start in range(length + 1)
                         for end in range(start, length + 1)
                         if all(value >= threshold for value in values[start:end])),
                        default=0,
                    )
                    check(streak, [values, threshold], best)

        reconcile = reference("inventory-reconciliation")
        rows = [("a", 0), ("a", 1), ("b", 1)]
        inputs = [
            [list(row) for row in sequence] for length in range(3)
            for sequence in product(rows, repeat=length)
        ]
        for expected in inputs:
            for actual in inputs:
                labels = list(dict.fromkeys(row[0] for row in expected + actual))
                output = []
                for label in labels:
                    before = sum(q for key, q in expected if key == label)
                    after = sum(q for key, q in actual if key == label)
                    if before != after:
                        output.append([label, before, after, after - before])
                check(reconcile, [expected, actual], output)

    def test_comparator_rejects_nested_type_coercion(self):
        self.assertFalse(exact_equal(True, 1))
        self.assertFalse(exact_equal({"a": True}, {"a": 1}))
        self.assertFalse(exact_equal([1.0], [1]))
        self.assertTrue(exact_equal({"a": [1, None]}, {"a": [1, None]}))

    def test_comparator_rejects_mutation_and_output(self):
        cases = [{"id": "case", "args": [[1]], "expected": 1}]

        def mutates(values):
            values.append(2)
            return 1

        def prints(values):
            print(values)
            return 1

        self.assertEqual(failures(mutates, cases), ["case"])
        self.assertEqual(failures(prints, cases), ["case"])


if __name__ == "__main__":
    unittest.main()

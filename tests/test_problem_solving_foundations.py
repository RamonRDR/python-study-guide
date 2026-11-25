"""Deterministic tests for the Phase 11 shared teaching examples."""

from pathlib import Path
import runpy
import unittest


ROOT = Path(__file__).resolve().parents[1] / "problem-solving-and-live-coding"


def load_example(chapter: str, filename: str) -> dict:
    return runpy.run_path(str(ROOT / chapter / "examples" / filename))


class ProblemSolvingFoundationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.minutes = load_example("01-problem-solving-fundamentals", "study_minutes.py")
        cls.capacity = load_example("02-constraints-and-edge-cases", "capacity.py")
        cls.counts = load_example("03-algorithmic-complexity", "operation_counts.py")
        cls.recursion = load_example("04-recursion", "recursive_sum.py")
        cls.search = load_example("05-searching-algorithms", "search.py")
        cls.sort = load_example("06-sorting-algorithms", "sort.py")
        cls.patterns = load_example("07-problem-solving-patterns", "patterns.py")

    def test_qualifying_minutes_contract(self):
        function = self.minutes["qualifying_minutes"]
        values = [12, 20, 25, 20]
        self.assertEqual(function(values), 65)
        self.assertEqual(values, [12, 20, 25, 20])
        self.assertEqual(function([]), 0)
        self.assertEqual(function([19]), 0)
        self.assertEqual(function([2, 3], 2), 5)

    def test_capacity_boundaries(self):
        function = self.capacity["accepts_group"]
        for group, expected in ((0, False), (1, True), (5, True), (6, False)):
            with self.subTest(group=group):
                self.assertIs(function(group, 5), expected)

    def test_capacity_invalid_inputs(self):
        function = self.capacity["accepts_group"]
        for args in ((True, 5), (1, False), (-1, "x"), (1.0, 5)):
            with self.subTest(args=args), self.assertRaises(TypeError):
                function(*args)
        for args in ((-1, 5), (2, 0)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                function(*args)

    def test_operation_counts(self):
        for size, expected in ((0, (0, 0, 0)), (1, (1, 1, 0)),
                               (4, (4, 16, 2)), (8, (8, 64, 3)),
                               (16, (16, 256, 4)), (10, (10, 100, 3))):
            with self.subTest(size=size):
                actual = tuple(self.counts[name](size) for name in
                               ("scan_count", "pair_count", "halving_count"))
                self.assertEqual(actual, expected)

    def test_recursive_and_iterative_sum(self):
        for name in ("recursive_sum", "iterative_sum"):
            function = self.recursion[name]
            for n, expected in ((0, 0), (1, 1), (4, 10), (100, 5050)):
                with self.subTest(name=name, n=n):
                    self.assertEqual(function(n), expected)
            for n in (-1, 101):
                with self.subTest(name=name, n=n), self.assertRaises(ValueError):
                    function(n)
            with self.assertRaises(TypeError):
                function(True)

    def test_linear_search_first_match(self):
        function = self.search["linear_search"]
        self.assertEqual(function([8, 4, 4, 9], 4), 1)
        self.assertEqual(function([4], 4), 0)
        self.assertEqual(function([], 4), -1)
        self.assertEqual(function([1, 2], 4), -1)

    def test_binary_search_boundaries_and_duplicates(self):
        function = self.search["binary_search"]
        cases = (([], 4, -1), ([4], 4, 0), ([4], 3, -1),
                 ([2, 4, 4, 7, 9], 4, 1), ([2, 4, 7], 1, -1),
                 ([2, 4, 7], 8, -1), ([2, 4, 7], 5, -1),
                 ([2, 4, 7], 7, 2), ([4, 4, 4], 4, 0))
        for values, target, expected in cases:
            with self.subTest(values=values, target=target):
                before = values.copy()
                self.assertEqual(function(values, target), expected)
                self.assertEqual(values, before)

    def test_sort_preserves_values_and_input(self):
        for name in ("bubble_sort", "selection_sort", "insertion_sort"):
            function = self.sort[name]
            for values in ([], [1], [1, 2, 3], [3, 2, 1],
                           [4, 2, 2, 1], [0, -2, 0, 5]):
                with self.subTest(name=name, values=values):
                    before = values.copy()
                    result = function(values)
                    self.assertEqual(result, sorted(before))
                    self.assertEqual(values, before)
                    self.assertIsNot(result, values)

    def test_frequency_map(self):
        function = self.patterns["frequencies"]
        self.assertEqual(function([]), {})
        self.assertEqual(function(["a", "b", "a"]), {"a": 2, "b": 1})

    def test_two_pointer_distinct_indices(self):
        function = self.patterns["has_pair_sum"]
        for values, target, expected in (([], 8, False), ([4], 8, False),
                                         ([4, 4], 8, True),
                                         ([1, 3, 6, 8], 9, True),
                                         ([1, 3, 6, 8], 7, True),
                                         ([-5, -1, 2], -3, True),
                                         ([1, 3, 6], 10, False)):
            with self.subTest(values=values, target=target):
                self.assertIs(function(values, target), expected)

    def test_sliding_window(self):
        function = self.patterns["max_window_sum"]
        self.assertEqual(function([4, -1, 3, 2], 2), 5)
        self.assertEqual(function([-4, -2, -3], 2), -5)
        self.assertEqual(function([-4, -2], 1), -2)
        self.assertEqual(function([1, 2, 3], 3), 6)
        for values, size in (([], 1), ([1], 0), ([1], 2)):
            with self.subTest(values=values, size=size), self.assertRaises(ValueError):
                function(values, size)
        with self.assertRaises(TypeError):
            function([1], True)


if __name__ == "__main__":
    unittest.main()

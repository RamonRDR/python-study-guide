"""Acceptance tests for the reading-progress example (R1–R4)."""

import contextlib
import io
import unittest

from reading_progress import remaining_pages


class ReadingProgressTests(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(remaining_pages(20, 7), 13)

    def test_boundaries(self):
        for total, read, expected in ((20, 0, 20), (20, 20, 0), (0, 0, 0)):
            with self.subTest(total=total, read=read):
                self.assertEqual(remaining_pages(total, read), expected)

    def test_invalid_ranges(self):
        for total, read in ((-1, 0), (20, -1), (20, 21)):
            with self.subTest(total=total, read=read):
                with self.assertRaises(ValueError):
                    remaining_pages(total, read)

    def test_invalid_types(self):
        for total, read in (("20", 7), (20, 7.0), (True, 0), (20, False)):
            with self.subTest(total=total, read=read):
                with self.assertRaises(TypeError):
                    remaining_pages(total, read)

    def test_type_error_precedes_value_error(self):
        with self.assertRaises(TypeError):
            remaining_pages(-1, "7")

    def test_int_subclass(self):
        class PageCount(int):
            pass

        self.assertEqual(remaining_pages(PageCount(20), 7), 13)

    def test_no_terminal_output(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = remaining_pages(20, 7)
        self.assertEqual(result, 13)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()

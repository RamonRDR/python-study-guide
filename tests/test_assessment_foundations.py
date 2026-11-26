"""Acceptance tests for the six foundation modules, without running learner code."""
from collections import Counter
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assessment_grading import grade_quiz
from assessment_records import load_index, load_matrix, read_json
from assessment_foundation_fixtures import EXPECTED, CODE_FIXTURES
from test_assessment_pilot import RESPONSES

MODULES = (
    "getting-started", "fundamentals", "strings-and-numbers",
    "collections", "program-flow", "functions",
)


class FoundationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapters = load_matrix(ROOT)
        all_quizzes = load_index("quiz", ROOT, "quizzes/quiz-index.json", cls.chapters)
        cls.quizzes = [q for q in all_quizzes if q["chapter_id"].split(".")[0] in MODULES]
        cls.by_id = {q["id"]: q for q in cls.quizzes}

    def test_exact_foundations_allocation_and_index(self):
        matrix = read_json(ROOT / "docs/specs/learning-hub-foundation/assessment-matrix.json")
        expected = Counter({
            (c["chapter_id"], difficulty): n
            for group in matrix["modules"] if group["module"] in MODULES
            for c in group["chapters"] for difficulty, n in c["allocation"].items() if n
        })
        actual = Counter((q["chapter_id"], q["difficulty"]) for q in self.quizzes)
        self.assertEqual(actual, expected)
        self.assertEqual(len(self.quizzes), 78)
        self.assertEqual(Counter(q["difficulty"] for q in self.quizzes),
                         {"easy": 37, "medium": 30, "hard": 11})
        self.assertEqual(sum(q["xp"] for q in self.quizzes), 1300)

    def test_new_record_grading(self):
        self.assertEqual(len(EXPECTED), 68)
        self.assertFalse(set(EXPECTED) & set(RESPONSES))
        self.assertEqual(set(self.by_id), set(EXPECTED) | set(RESPONSES))
        for identifier, (right, wrong) in EXPECTED.items():
            with self.subTest(id=identifier):
                quiz = self.by_id[identifier]
                self.assertTrue(grade_quiz(quiz, right))
                self.assertFalse(grade_quiz(quiz, wrong))

    def test_balanced_truth_values(self):
        counts = Counter(q["answer"]["value"] for q in self.quizzes
                         if q["type"] == "true_false")
        self.assertGreaterEqual(min(counts[True], counts[False]), 5)
        self.assertLessEqual(abs(counts[True] - counts[False]), 2)

    def test_trusted_literal_code_fixtures(self):
        # All executable strings are constants authored in the trusted test
        # module, NOT values taken from records, responses or the browser.
        self.assertEqual(set(CODE_FIXTURES), {
            q["id"] for q in self.quizzes if q["id"] in EXPECTED and "code" in q
        })
        for identifier, (displayed, executable, output, exception) in CODE_FIXTURES.items():
            with self.subTest(id=identifier):
                quiz = self.by_id[identifier]
                self.assertEqual(quiz["code"], displayed)
                stdout, stderr = StringIO(), StringIO()
                with redirect_stdout(stdout), redirect_stderr(stderr):
                    if exception is not None:
                        with self.assertRaises(exception):
                            exec(compile(executable, "<trusted fixture>", "exec"), {})
                    else:
                        exec(compile(executable, "<trusted fixture>", "exec"), {})
                self.assertEqual(stdout.getvalue(), output)
                self.assertEqual(stderr.getvalue(), "")
                if quiz["type"] == "output_prediction":
                    self.assertTrue(grade_quiz(quiz, output))


if __name__ == "__main__":
    unittest.main()

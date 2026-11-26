"""Full-bank acceptance: exact allocations, trusted fixtures and locale navigation."""
from collections import Counter
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assessment_grading import grade_quiz
from assessment_records import load_index, load_matrix, read_json
from assessment_foundation_fixtures import EXPECTED as FOUNDATION
from assessment_expansion_fixtures import EXPECTED, CODE_FIXTURES
from test_assessment_pilot import RESPONSES


class ExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapters = load_matrix(ROOT)
        cls.quizzes = load_index("quiz", ROOT, "quizzes/quiz-index.json", cls.chapters)
        cls.by_id = {q["id"]: q for q in cls.quizzes}

    def test_complete_matrix(self):
        matrix = read_json(ROOT / "docs/specs/learning-hub-foundation/assessment-matrix.json")
        expected = Counter({
            (c["chapter_id"], difficulty): n
            for group in matrix["modules"] for c in group["chapters"]
            for difficulty, n in c["allocation"].items() if n
        })
        self.assertEqual(Counter((q["chapter_id"], q["difficulty"]) for q in self.quizzes),
                         expected)
        self.assertEqual(len(self.quizzes), 160)
        self.assertEqual(Counter(q["difficulty"] for q in self.quizzes),
                         {"easy": 64, "medium": 67, "hard": 29})
        self.assertEqual(sum(q["xp"] for q in self.quizzes), 2850)
        self.assertEqual(
            {p.relative_to(ROOT).as_posix() for p in (ROOT / "quizzes/questions").rglob("*.json")},
            {f"quizzes/questions/{q['id']}.json" for q in self.quizzes},
        )

    def test_expansion_responses(self):
        self.assertEqual(len(EXPECTED), 82)
        self.assertFalse(set(EXPECTED) & (set(FOUNDATION) | set(RESPONSES)))
        self.assertEqual(set(self.by_id), set(EXPECTED) | set(FOUNDATION) | set(RESPONSES))
        for identifier, (right, wrong) in EXPECTED.items():
            with self.subTest(id=identifier):
                quiz = self.by_id[identifier]
                self.assertTrue(grade_quiz(quiz, right))
                self.assertFalse(grade_quiz(quiz, wrong))

    def test_expansion_diversity(self):
        kinds = Counter(self.by_id[i]["type"] for i in EXPECTED)
        self.assertEqual(set(kinds), {"multiple_choice", "true_false", "error_identification",
                                      "output_prediction", "objective_code_completion"})
        self.assertLess(kinds["output_prediction"], 30)
        truth = Counter(q["answer"]["value"] for q in self.quizzes if q["type"] == "true_false")
        self.assertGreaterEqual(min(truth[True], truth[False]), 5)
        self.assertLessEqual(abs(truth[True] - truth[False]), 4)

    def test_literal_code_fixtures(self):
        self.assertEqual(set(CODE_FIXTURES), {
            identifier for identifier in EXPECTED if "code" in self.by_id[identifier]
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

    def test_trilingual_catalog_navigation(self):
        for suffix in ("", ".pt-BR", ".es"):
            with self.subTest(locale=suffix):
                path = ROOT / f"quizzes/README{suffix}.md"
                content = path.read_text(encoding="utf-8")
                targets = re.findall(r"\]\(questions/(quiz\.[a-z0-9.-]+)\.json\)", content)
                self.assertEqual(Counter(targets), Counter(self.by_id.keys()))
                self.assertIn("../exercises/problem-solving/exercise-index.json", content)


if __name__ == "__main__":
    unittest.main()

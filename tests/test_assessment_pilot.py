"""Verify the published pilot, using only trusted repository fixtures."""
from collections import Counter
from copy import deepcopy
from pathlib import Path
import runpy
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assessment_grading import case_passes, grade_quiz
from assessment_records import load_index, load_matrix, read_json, validate_record

QUIZ_INDEX = "quizzes/quiz-index.json"
EXERCISE_INDEX = "exercises/problem-solving/exercise-index.json"
PILOT_EXERCISES = {
    "problem-solving.vowel-counter", "problem-solving.binary-insertion-index",
    "problem-solving.inventory-reconciliation",
}
RESPONSES = {
    "quiz.interpreter-purpose": ("interpreter", "editor"),
    "quiz.collection-membership": ("set", "list"),
    "quiz.editor-replaces-interpreter": (False, True),
    "quiz.type-hints-runtime": (False, True),
    "quiz.unclosed-print": ("syntax-error", "name-error"),
    "quiz.missing-required-argument": ("type-error", "value-error"),
    "quiz.print-literal": ("Ready\n", "Ready"),
    "quiz.range-stop": ("2\n4\n", "2\n4\n6\n"),
    "quiz.return-keyword": ("return", "print"),
    "quiz.dictionary-fallback": ("get", "pop"),
}


class AssessmentPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapters = load_matrix(ROOT)
        all_quizzes = load_index("quiz", ROOT, QUIZ_INDEX, cls.chapters)
        cls.quizzes = [q for q in all_quizzes if q["id"] in RESPONSES]
        all_exercises = load_index("exercise", ROOT, EXERCISE_INDEX, cls.chapters)
        cls.exercises = [r for r in all_exercises if r["id"] in PILOT_EXERCISES]

    def test_quiz_inventory_and_allocation(self):
        self.assertEqual({q["id"] for q in self.quizzes}, set(RESPONSES))
        self.assertEqual(len(self.quizzes), 10)
        self.assertEqual(Counter(q["type"] for q in self.quizzes), {
            "multiple_choice": 2, "true_false": 2, "error_identification": 2,
            "output_prediction": 2, "objective_code_completion": 2,
        })
        self.assertEqual(Counter(q["difficulty"] for q in self.quizzes),
                         {"easy": 7, "medium": 3})
        self.assertEqual(sum(q["xp"] for q in self.quizzes), 130)
        actual = Counter((q["chapter_id"], q["difficulty"]) for q in self.quizzes)
        matrix = read_json(ROOT / "docs/specs/learning-hub-foundation/assessment-matrix.json")
        allocation = {(c["chapter_id"], d): count
                      for m in matrix["modules"] for c in m["chapters"]
                      for d, count in c["allocation"].items()}
        for key, count in actual.items():
            self.assertLessEqual(count, allocation[key])

    def test_quiz_grading(self):
        for q in self.quizzes:
            with self.subTest(id=q["id"]):
                right, wrong = RESPONSES[q["id"]]
                self.assertTrue(grade_quiz(q, right))
                self.assertFalse(grade_quiz(q, wrong))

    def test_pilot_code_semantics(self):
        quizzes = {q["id"]: q for q in self.quizzes}
        # Execute only literal fixtures here, never record or learner source.
        from contextlib import redirect_stdout
        from io import StringIO

        self.assertEqual(quizzes["quiz.unclosed-print"]["code"], 'print("Ready"')
        with self.assertRaises(SyntaxError):
            compile('print("Ready"', "<fixture>", "exec")
        self.assertEqual(quizzes["quiz.missing-required-argument"]["code"],
                         "def show_city(city):\n    print(city)\n\nshow_city()")
        def show_city(city):
            print(city)
        with self.assertRaises(TypeError):
            show_city()
        self.assertEqual(quizzes["quiz.print-literal"]["code"], 'print("Ready")')
        self.assertEqual(quizzes["quiz.range-stop"]["code"],
                         "for number in range(2, 6, 2):\n    print(number)")
        output = StringIO()
        with redirect_stdout(output):
            print("Ready")
        self.assertTrue(grade_quiz(quizzes["quiz.print-literal"], output.getvalue()))
        output = StringIO()
        with redirect_stdout(output):
            for number in range(2, 6, 2):
                print(number)
        self.assertTrue(grade_quiz(quizzes["quiz.range-stop"], output.getvalue()))
        self.assertEqual(quizzes["quiz.return-keyword"]["code"],
                         "def double(number):\n    ____ number * 2")
        def double(number):
            return number * 2
        self.assertEqual(double(4), 8)
        self.assertEqual(quizzes["quiz.dictionary-fallback"]["code"],
                         'stock = {"pen": 3}\nquantity = stock.____("notebook", 0)')
        stock = {"pen": 3}
        self.assertEqual(stock.get("notebook", 0), 0)
        self.assertEqual(stock, {"pen": 3})
        self.assertEqual(stock.get("pen", 0), 3)

    def test_exercise_inventory(self):
        self.assertEqual({r["id"] for r in self.exercises}, PILOT_EXERCISES)
        self.assertEqual(Counter(r["difficulty"] for r in self.exercises),
                         {"easy": 1, "medium": 1, "hard": 1})
        self.assertEqual(sum(len(r["tests"]["cases"]) for r in self.exercises), 24)
        all_records = [read_json(path) for path in
                       (ROOT / "exercises/problem-solving").glob("*/exercise.json")]
        self.assertEqual(len(all_records), 30)
        self.assertTrue(PILOT_EXERCISES <= {
            r["id"] for r in all_records if r.get("schema_version") == "1.0.0"
        })
        self.assertEqual(sum(len(r["tests"]["cases"]) for r in all_records), 192)

    def test_trusted_references_and_wrong_candidates(self):
        for record in self.exercises:
            with self.subTest(id=record["id"]):
                name = record["tests"]["function_name"]
                reference = runpy.run_path(str(ROOT / record["solution_path"]))[name]
                cases = record["tests"]["cases"]
                new_container = record["tests"]["new_container"]
                self.assertTrue(all(case_passes(reference, case, new_container=new_container)
                                    for case in cases))
                path = (ROOT / record["solution_path"]).with_name("test_solution.py")
                wrong = runpy.run_path(str(path))
                names = ("lowercase_only", "unique_vowels", "normalized_string",
                         "includes_y", "returns_boolean", "returns_too_early")
                candidates = [wrong[n] for n in names] if record["id"].endswith(
                    ".vowel-counter") else [wrong["wrong_solution"]]
                for candidate in candidates:
                    self.assertTrue(any(not case_passes(candidate, case,
                                                       new_container=new_container)
                                        for case in cases), candidate.__name__)

    def test_conflicting_expected_values(self):
        for original in self.exercises:
            record = deepcopy(original)
            case = deepcopy(record["tests"]["cases"][0])
            case["id"] = "contradictory"
            case["expected"] = None
            record["tests"]["cases"].append(case)
            with self.subTest(id=record["id"]):
                with self.assertRaisesRegex(ValueError, "contradictory"):
                    validate_record("exercise", record, ROOT, self.chapters)

    def test_nested_container_aliases(self):
        case = {"args": [[[1]]], "expected": [[1]]}
        self.assertFalse(case_passes(lambda rows: list(rows), case, new_container=True))
        self.assertTrue(case_passes(deepcopy, case, new_container=True))
        nested = {"args": [[[1]]], "expected": [1]}
        self.assertFalse(case_passes(lambda rows: rows[0], nested, new_container=True))
        self.assertTrue(case_passes(lambda rows: list(rows[0]), nested, new_container=True))
        mapping = {"args": [{"items": [1]}], "expected": {"items": [1]}}
        self.assertFalse(case_passes(dict, mapping, new_container=True))
        self.assertTrue(case_passes(deepcopy, mapping, new_container=True))


if __name__ == "__main__":
    unittest.main()

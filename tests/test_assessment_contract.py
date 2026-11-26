"""Contract tests; fixtures are not published assessment records."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from assessment_records import (read_json, validate_record, load_index, load_matrix)
from assessment_grading import exact_equal, grade_quiz, case_passes

LOCALES = ("en", "pt-BR", "es")


def localized(value):
    return {locale: copy.deepcopy(value) for locale in LOCALES}


class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.paths = {}
        for locale, filename in zip(LOCALES, ("README.md", "README.pt-BR.md", "README.es.md")):
            path = "fundamentals/02-print-and-input/" + filename
            self.paths[locale] = path
            self.write(path, "## Output\n")
        self.chapters = {"fundamentals.print-and-input": self.paths}
        self.quiz = {
            "schema_version": "1.0.0", "id": "quiz.fixture",
            "chapter_id": "fundamentals.print-and-input", "difficulty": "easy",
            "xp": 10, "type": "multiple_choice", "prompt": localized("Select."),
            "explanation": localized("Explanation."), "hints": localized(["Hint."]),
            "prerequisites": [{"paths": self.paths, "sections": localized("Output")}],
            "choices": [{"id": "one", "text": localized("One")},
                        {"id": "two", "text": localized("Two")}],
            "answer": {"choice_id": "one"},
        }
        folder = "exercises/problem-solving/fixture/"
        for name in ("starter.py", "solution.py"):
            self.write(folder + name, "def sample(value):\n    return value\n")
        self.exercise = {
            "schema_version": "1.0.0", "id": "problem-solving.fixture",
            "chapter_id": "fundamentals.print-and-input", "difficulty": "easy",
            "estimated_minutes": 10, "title": localized("Fixture"),
            "prompt": localized("Return the value."), "concepts": ["return"],
            "constraints": localized(["Keep inputs unchanged."]),
            "examples": [{"args": [1], "expected": 1, "explanation": localized("One.")}],
            "starter_path": folder + "starter.py", "solution_path": folder + "solution.py",
            "hints": localized(["First.", "Second.", "Third."]),
            "explanation": localized("Return."), "complexity": {
                "time": localized("O(1)"), "space": localized("O(1)"),
                "assumptions": localized("Bounded input.")},
            "tests": {"interface": "function_call", "function_name": "sample",
                      "comparison": "exact_type_and_value", "timeout_ms": 2000,
                      "new_container": False,
                      "cases": [{"id": "one", "args": [1], "expected": 1}]},
            "execution": "unverified", "allowed_dependencies": [], "local_python": "3.13",
            "prerequisite_paths": [self.paths], "practice_mode": "implement",
        }

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def validate(self, kind, record):
        validate_record(kind, record, self.root, self.chapters)

    def test_matrix(self):
        chapters = load_matrix(ROOT)
        self.assertEqual(len(chapters), 115)

    def test_all_quiz_types_and_grading(self):
        for kind in ("multiple_choice", "error_identification", "true_false",
                     "output_prediction", "objective_code_completion"):
            with self.subTest(kind=kind):
                q = copy.deepcopy(self.quiz)
                q["type"] = kind
                if kind in ("multiple_choice", "error_identification"):
                    right, wrong = "one", "two"
                else:
                    del q["choices"]
                    if kind == "true_false":
                        q["answer"] = {"value": True}
                        right, wrong = True, False
                    else:
                        q["answer"] = {"accepted": ["x\ny"], "comparison": "exact"}
                        right, wrong = "x\ny", "x\r\ny"
                self.validate("quiz", q)
                self.assertTrue(grade_quiz(q, right))
                self.assertFalse(grade_quiz(q, wrong))
        q["type"] = "output_prediction"
        q["answer"]["comparison"] = "normalize_lf"
        self.validate("quiz", q)
        self.assertTrue(grade_quiz(q, "x\r\ny"))
        self.assertFalse(grade_quiz(q, "x\ny "))

    def test_strict_answer_types(self):
        q = copy.deepcopy(self.quiz)
        q["type"] = "true_false"
        del q["choices"]
        q["answer"] = {"value": True}
        with self.assertRaises(ValueError):
            grade_quiz(q, 1)
        with self.assertRaises(ValueError):
            grade_quiz(self.quiz, "missing")

    def test_quiz_invalid_variants(self):
        for mutation, diagnostic in (
            (lambda q: q.update(schema_version="2.0.0"), "schema_version"),
            (lambda q: q["prompt"].pop("es"), "prompt"),
            (lambda q: q.update(xp=True), "xp"),
            (lambda q: q.update(xp=10.0), "xp"),
            (lambda q: q.update(xp=20), "XP"),
            (lambda q: q["choices"][1].update(id="one"), "duplicate choice"),
            (lambda q: q["answer"].update(choice_id="missing"), "unknown choice"),
            (lambda q: q.update(chapter_id="unknown.chapter"), "unknown chapter"),
            (lambda q: q["prerequisites"][0]["sections"].update(es="Absent"), "heading"),
            (lambda q: q.update(extra="no"), "Additional properties"),
            (lambda q: q["prerequisites"][0]["paths"].update(es="../README.es.md"), "path"),
        ):
            with self.subTest(diagnostic=diagnostic):
                self.validate("quiz", self.quiz)
                q = copy.deepcopy(self.quiz)
                mutation(q)
                with self.assertRaisesRegex(ValueError, diagnostic):
                    self.validate("quiz", q)

    def test_exercise_contract(self):
        self.validate("exercise", self.exercise)
        for mutation, diagnostic in (
            (lambda e: e["tests"]["cases"].append(copy.deepcopy(e["tests"]["cases"][0])), "duplicate case"),
            (lambda e: e["examples"][0].update(expected=True), "example"),
            (lambda e: e.update(solution_path="../outside.py"), "path"),
            (lambda e: e["tests"].update(timeout_ms=0), "timeout_ms"),
            (lambda e: e.update(allowed_dependencies=["requests"]), "allowed_dependencies"),
            (lambda e: e.update(execution="browser_compatible"), "execution"),
        ):
            with self.subTest(diagnostic=diagnostic):
                e = copy.deepcopy(self.exercise)
                mutation(e)
                with self.assertRaisesRegex(ValueError, diagnostic):
                    self.validate("exercise", e)

    def test_strict_json(self):
        for payload in ('{"a":1,"a":2}', '{"x":NaN}', '{"x":Infinity}', '{"x":1e999}', '{'):
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    read_json(self.write("bad.json", payload))
        self.assertEqual(read_json(self.write("large.json", "2432902008176640000")),
                         2432902008176640000)

    def test_index_references(self):
        path = "quizzes/questions/quiz.fixture.json"
        self.write(path, json.dumps(self.quiz))
        index = {"schema_version": "1.0.0", "records": [{"id": "quiz.fixture", "path": path}]}
        target = self.write("index.json", json.dumps(index))
        self.assertEqual(load_index("quiz", self.root, "index.json", self.chapters), [self.quiz])
        for records, diagnostic in (
            (index["records"] * 2, "duplicate"),
            ([{"id": "quiz.other", "path": path}], "path"),
            ([{"id": "quiz.absent", "path": "quizzes/questions/quiz.absent.json"}], "path"),
        ):
            target.write_text(json.dumps({**index, "records": records}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, diagnostic):
                load_index("quiz", self.root, "index.json", self.chapters)

    def test_exercise_index_and_large_integer(self):
        record = copy.deepcopy(self.exercise)
        big = 2432902008176640000
        record["examples"][0].update(args=[big], expected=big)
        record["tests"]["cases"][0].update(args=[big], expected=big)
        self.validate("exercise", record)
        self.assertTrue(case_passes(lambda n: n, record["tests"]["cases"][0]))
        path = "exercises/problem-solving/fixture/exercise.json"
        self.write(path, json.dumps(record))
        index = {"schema_version": "1.0.0", "records": [
            {"id": record["id"], "path": path}]}
        self.write("exercise-index.json", json.dumps(index))
        self.assertEqual(load_index("exercise", self.root, "exercise-index.json",
                                    self.chapters), [record])

    def test_symlink_escape_and_invalid_paths(self):
        from assessment_records import safe_file
        for path in ("../outside", "/tmp/outside", "C:/outside", "./index.json",
                     "foo//bar", "foo\\bar"):
            with self.subTest(path=path):
                with self.assertRaisesRegex(ValueError, "path"):
                    safe_file(self.root, path)
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "outside.txt"
            target.write_text("fixture", encoding="utf-8")
            try:
                (self.root / "escape.txt").symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation unavailable")
            with self.assertRaisesRegex(ValueError, "escaping path"):
                safe_file(self.root, "escape.txt")

    def test_normalized_duplicate_answers(self):
        q = copy.deepcopy(self.quiz)
        q["type"] = "output_prediction"
        del q["choices"]
        q["answer"] = {"accepted": ["x\ny"], "comparison": "normalize_lf"}
        self.validate("quiz", q)
        q["answer"]["accepted"].append("x\r\ny")
        with self.assertRaisesRegex(ValueError, "duplicate normalized answer"):
            self.validate("quiz", q)

    def test_exact_comparison_and_trusted_candidate(self):
        self.assertFalse(exact_equal({"a": [True]}, {"a": [1]}))
        self.assertFalse(exact_equal([1.0], [1]))
        self.assertTrue(exact_equal({"a": [1, None]}, {"a": [1, None]}))
        case = {"args": [[1]], "expected": [1]}
        self.assertTrue(case_passes(lambda x: list(x), case, new_container=True))
        self.assertFalse(case_passes(lambda x: x, case, new_container=True))
        self.assertFalse(case_passes(lambda x: [True], case))
        def mutates(x):
            x.append(2)
            return [1]
        def noisy(x):
            print("unexpected")
            return [1]
        self.assertFalse(case_passes(mutates, case))
        self.assertFalse(case_passes(noisy, case))
        self.assertEqual(case["args"], [[1]])


if __name__ == "__main__":
    unittest.main()

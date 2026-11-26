"""Behavioral tests for the backend, SQL and engineering lessons."""
from contextlib import closing
import importlib.util
from pathlib import Path
import sqlite3
import unittest

ROOT = Path(__file__).resolve().parents[1] / "technical-interview-preparation"


def load_example(chapter, name):
    path = ROOT / chapter / "examples" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BackendTests(unittest.TestCase):
    def test_parse_quantity_distinguishes_invalid_input(self):
        m = load_example("15-exceptions-testing-and-debugging-review", "parse_quantity")
        self.assertEqual(m.parse_quantity("0"), 0)
        self.assertEqual(m.parse_quantity(" 12 "), 12)
        for invalid in ("", "1.5", "-1", None, True):
            with self.subTest(invalid=invalid):
                with self.assertRaises(m.InvalidQuantity):
                    m.parse_quantity(invalid)
        with self.assertRaises(m.InvalidQuantity) as caught:
            m.parse_quantity("abc")
        self.assertIsInstance(caught.exception.__cause__, ValueError)

    def test_routing_contract(self):
        m = load_example("16-http-rest-and-backend-fundamentals", "route_catalog")
        self.assertEqual(m.route("GET", "/lessons"),
                         (200, {"Content-Type": "application/json"}, [{"id": 1}]))
        self.assertEqual(m.route("GET", "/missing")[0], 404)
        status, headers, _ = m.route("POST", "/lessons")
        self.assertEqual(status, 405)
        self.assertEqual(headers["Allow"], "GET")
        first = m.route("GET", "/lessons")[2]
        first[0]["id"] = 99
        self.assertEqual(m.route("GET", "/lessons")[2], [{"id": 1}])

    def test_object_authorization_and_payload_contract(self):
        m = load_example("17-api-contracts-authentication-and-authorization", "note_access")
        notes = {1: ("learner-a", "draft")}
        status, headers, body = m.read_note(None, 1, notes)
        self.assertEqual(status, 401)
        self.assertEqual(headers["WWW-Authenticate"], "Bearer")
        self.assertNotIn("draft", str(body))
        self.assertEqual(m.read_note("learner-b", 1, notes)[0], 403)
        self.assertNotIn("draft", str(m.read_note("learner-b", 1, notes)[2]))
        self.assertEqual(m.read_note("learner-a", 1, notes)[2], {"text": "draft"})
        self.assertEqual(m.read_note("learner-a", 2, notes)[0], 404)
        self.assertEqual(m.validate_title({"title": "  SQL  "}), "SQL")
        for invalid in (None, [], {}, {"title": True}, {"title": " "},
                        {"title": "SQL", "owner": "other"}, {"title": "x" * 81}):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                m.validate_title(invalid)

    def test_relational_constraints_and_selection(self):
        m = load_example("18-relational-databases-and-sql", "lesson_catalog")
        with closing(sqlite3.connect(":memory:", autocommit=True)) as db:
            m.create_catalog(db)
            m.add_lesson(db, "Python", 30)
            m.add_lesson(db, "SQL", 20)
            m.add_lesson(db, "Testing", 20)
            self.assertEqual(m.short_lessons(db, 20), [("SQL", 20), ("Testing", 20)])
            self.assertEqual(m.short_lessons(db, 0), [])
            for title, minutes in (("Python", 10), (None, 20), ("Bad", 0)):
                with self.subTest(title=title, minutes=minutes):
                    with self.assertRaises(sqlite3.IntegrityError):
                        m.add_lesson(db, title, minutes)
            self.assertEqual(len(m.short_lessons(db, 100)), 3)

    def test_left_join_counts_and_foreign_keys(self):
        m = load_example("19-joins-aggregations-and-data-relationships", "group_progress")
        with closing(sqlite3.connect(":memory:", autocommit=True)) as db:
            m.create_tables(db)
            db.executemany("INSERT INTO groups VALUES (?, ?)", [(1, "A"), (2, "B"), (3, "C")])
            db.executemany("INSERT INTO tasks VALUES (?, ?, ?)",
                           [(1, 1, 1), (2, 1, 1), (3, 1, 0), (4, 2, 0)])
            self.assertEqual(m.completed_by_group(db), [("A", 2), ("B", 0), ("C", 0)])
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO tasks VALUES (?, ?, ?)", (5, 99, 1))

    def test_transaction_rolls_back_and_parameters_remain_data(self):
        m = load_example("20-transactions-indexes-and-sql-safety", "credit_transfer")
        with closing(sqlite3.connect(":memory:", autocommit=False)) as db:
            m.create_accounts(db)
            db.executemany("INSERT INTO accounts VALUES (?, ?, ?)",
                           [(1, "A", 10), (2, "B", 2)])
            db.commit()
            m.transfer(db, 1, 2, 3)
            self.assertEqual(m.balances(db), [(1, 7), (2, 5)])
            for source, target, amount in ((1, 99, 2), (99, 2, 2), (1, 2, 8),
                                           (1, 1, 1), (1, 2, True), (1, 2, 0)):
                with self.subTest(source=source, target=target, amount=amount):
                    with self.assertRaises(ValueError):
                        m.transfer(db, source, target, amount)
                self.assertEqual(m.balances(db), [(1, 7), (2, 5)])
            self.assertEqual(m.find_account(db, "A"), [(1,)])
            self.assertEqual(m.find_account(db, "' OR 1=1 --"), [])
            self.assertEqual(m.balances(db), [(1, 7), (2, 5)])
            indexes = db.execute("PRAGMA index_list(accounts)").fetchall()
            self.assertIn("idx_accounts_name", [row[1] for row in indexes])

    def test_engineering_boundary_and_data_contract(self):
        m = load_example("21-software-engineering-and-technical-decisions", "progress_report")
        calls = []

        def load(learner):
            calls.append(learner)
            return [1, 2, 2]

        self.assertEqual(m.progress_report("learner-a", load), {"completed": 2})
        self.assertEqual(calls, ["learner-a"])
        self.assertEqual(m.progress_report("learner-b", lambda _: []), {"completed": 0})
        with self.assertRaises(ValueError):
            m.progress_report("", load)
        self.assertEqual(calls, ["learner-a"])
        with self.assertRaises(ValueError):
            m.progress_report("learner-a", lambda _: [True])
        with self.assertRaises(RuntimeError):
            def failing(_):
                raise RuntimeError("dependency unavailable")
            m.progress_report("learner-a", failing)


if __name__ == "__main__":
    unittest.main()

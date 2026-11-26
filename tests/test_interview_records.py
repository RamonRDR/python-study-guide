"""Validate the preliminary interview record contract and its rendered lesson."""
import copy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.interview_records import (
    load_bank, read_json, render_questions, validate_question,
)

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "interviews"
CHAPTER = ROOT / "technical-interview-preparation/22-technical-interview-question-bank"


class InterviewRecordsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_bank(ROOT)
        cls.first = cls.records[0]

    def test_published_records_and_rendered_views(self):
        self.assertGreaterEqual(len(self.records), 9)
        self.assertEqual(len({q["id"] for q in self.records}), len(self.records))
        for q in self.records:
            self.assertEqual(validate_question(q, ROOT), [], q["id"])
        for locale, suffix in (("en", ""), ("pt-BR", ".pt-BR"), ("es", ".es")):
            text = (CHAPTER / f"README{suffix}.md").read_text(encoding="utf-8")
            block = text.split("<!-- interview-questions:start -->\n")[1]
            block = block.split("<!-- interview-questions:end -->")[0]
            self.assertEqual(block, render_questions(self.records, locale))

    def test_pilot_has_three_questions_per_level(self):
        index = json.loads((BANK / "interview-index.json").read_text(encoding="utf-8"))
        pilot = index["pilot_question_ids"]
        self.assertEqual(len(pilot), 9)
        self.assertEqual(len(set(pilot)), 9)
        selected = [q for q in self.records if q["id"] in pilot]
        self.assertEqual(len(selected), 9)
        for level in ("junior", "mid", "senior"):
            self.assertEqual(sum(q["level"] == level for q in selected), 3)

    def test_duplicate_json_keys_and_invalid_indexes_are_rejected(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            bank = root / "interviews"
            bank.mkdir()
            index_path = bank / "interview-index.json"
            index_path.write_text('{"id":"first","id":"second"}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                read_json(index_path)

            index = json.loads((BANK / "interview-index.json").read_text(encoding="utf-8"))
            invalid_indexes = [
                [],
                {**index, "schema_version": "9.0.0"},
                {**index, "question_ids": [index["question_ids"][0]] * 9},
                {**index, "pilot_question_ids": index["pilot_question_ids"][:-1]},
                {**index, "question_ids": ["../escape"]},
                index,  # No corresponding question files in the temporary bank.
            ]
            for value in invalid_indexes:
                with self.subTest(value=value):
                    index_path.write_text(json.dumps(value), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        load_bank(root)

    def test_invalid_records_are_rejected(self):
        mutations = [
            lambda q: q.pop("expected_answer"),
            lambda q: q.update(id="Invalid ID"),
            lambda q: q.update(level="easy"),
            lambda q: q.update(topic="unknown"),
            lambda q: q["prompt"].pop("es"),
            lambda q: q["examples"].update(en=" "),
            lambda q: q.update(common_errors={"en": [], "pt-BR": [], "es": []}),
            lambda q: q["follow_ups"]["es"].append("Extra"),
            lambda q: q["rubric"][0].update(points=True),
            lambda q: q["rubric"][0].update(points=0),
            lambda q: q["rubric"].append(copy.deepcopy(q["rubric"][0])),
            lambda q: q["rubric"][0]["criterion"].pop("pt-BR"),
            lambda q: q.update(prerequisites=[]),
            lambda q: q["prerequisites"][0]["paths"].update(en="../README.md"),
            lambda q: q["prerequisites"][0]["paths"].update(en="README.md"),
            lambda q: q["prerequisites"][0]["sections"].update(en="Missing section"),
            lambda q: q["prerequisites"][0]["paths"].update(es=q["prerequisites"][0]["paths"]["en"]),
            lambda q: q.update(extra="unsupported"),
        ]
        for i, mutate in enumerate(mutations):
            with self.subTest(case=i):
                record = copy.deepcopy(self.first)
                mutate(record)
                self.assertTrue(validate_question(record, ROOT))


if __name__ == "__main__":
    unittest.main()

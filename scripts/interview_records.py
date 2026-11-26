"""Preliminary interview-bank validation and deterministic Markdown rendering.

Not a final schema or automatic semantic grader. Run from the repository root.
"""
import argparse
import json
from pathlib import Path, PurePosixPath
import re

LOCALES = ("en", "pt-BR", "es")
SUFFIXES = {"en": "README.md", "pt-BR": "README.pt-BR.md", "es": "README.es.md"}
LEVELS = {"junior", "mid", "senior"}
TOPICS = {
    "interview-fundamentals", "python-fundamentals", "data-structures-algorithms",
    "oop", "python-internals", "testing-debugging", "backend-apis",
    "databases-sql", "software-engineering", "behavioral-international",
}
ID = re.compile(r"[a-z0-9]+(?:[.-][a-z0-9]+)+")
TEXT = ("prompt", "expected_answer", "explanation", "intent", "examples")
LISTS = ("common_errors", "follow_ups")
FIELDS = {"id", "topic", "level", *TEXT, *LISTS, "rubric", "prerequisites"}
CHAPTER = Path("technical-interview-preparation/22-technical-interview-question-bank")
START = "<!-- interview-questions:start -->\n"
END = "<!-- interview-questions:end -->"


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def locale_map(value, predicate):
    return isinstance(value, dict) and set(value) == set(LOCALES) and all(
        predicate(item) for item in value.values()
    )


def valid_id(value):
    return isinstance(value, str) and ID.fullmatch(value) is not None


def valid_path(value, locale, root):
    if not nonblank(value) or "\\" in value or ":" in value:
        return False
    path = PurePosixPath(value)
    if (path.is_absolute() or path.as_posix() != value
            or ".." in path.parts or path.name != SUFFIXES[locale]
            or len(path.parts) != 3
            or path.parts[0] != "technical-interview-preparation"
            or not re.fullmatch(r"(?:0[1-9]|1[0-9]|2[013])-[a-z0-9-]+", path.parts[1])):
        return False
    actual = root / value
    return actual.resolve().is_relative_to(root.resolve()) and actual.is_file()


def validate_question(record, root):
    """Return structural errors; semantic/translation review is still manual."""
    errors = []
    if not isinstance(record, dict) or set(record) != FIELDS:
        return ["question fields differ from preliminary contract"]
    if not valid_id(record["id"]):
        errors.append("invalid id")
    for key, allowed in (("topic", TOPICS), ("level", LEVELS)):
        if not isinstance(record[key], str) or record[key] not in allowed:
            errors.append(f"invalid {key}")
    for field in TEXT:
        if not locale_map(record[field], nonblank):
            errors.append(f"invalid localized text: {field}")
    for field in LISTS:
        value = record[field]
        if not locale_map(value, lambda v: isinstance(v, list) and bool(v)
                          and all(nonblank(x) for x in v)):
            errors.append(f"invalid localized list: {field}")
        elif len({len(v) for v in value.values()}) != 1:
            errors.append(f"unaligned list length: {field}")
    rubric = record["rubric"]
    if not isinstance(rubric, list) or not rubric:
        errors.append("missing rubric")
    else:
        ids = set()
        for item in rubric:
            if (not isinstance(item, dict) or set(item) != {"id", "points", "criterion"}
                    or not valid_id(item["id"])
                    or type(item["points"]) is not int or item["points"] <= 0
                    or not locale_map(item["criterion"], nonblank)):
                errors.append("invalid rubric criterion")
                continue
            if item["id"] in ids:
                errors.append("duplicate rubric criterion id")
            ids.add(item["id"])
    prerequisites = record["prerequisites"]
    if not isinstance(prerequisites, list) or not prerequisites:
        errors.append("missing prerequisites")
    else:
        for item in prerequisites:
            if (not isinstance(item, dict) or set(item) != {"paths", "sections"}
                    or not locale_map(item["paths"], nonblank)
                    or not locale_map(item["sections"], nonblank)):
                errors.append("invalid prerequisite")
                continue
            paths, sections = item["paths"], item["sections"]
            if any(not valid_path(paths[l], l, root) for l in LOCALES):
                errors.append("invalid prerequisite path")
                continue
            if len({PurePosixPath(p).parent for p in paths.values()}) != 1:
                errors.append("prerequisite locales refer to different lessons")
            for locale in LOCALES:
                lines = (root / paths[locale]).read_text(encoding="utf-8").splitlines()
                if "## " + sections[locale] not in lines:
                    errors.append(f"missing prerequisite section: {locale}")
    return errors


def read_json(path):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def load_bank(root):
    bank = root / "interviews"
    index_path = bank / "interview-index.json"
    if not index_path.resolve().is_relative_to(root.resolve()):
        raise ValueError("index path escapes repository")
    index = read_json(index_path)
    if (not isinstance(index, dict)
            or set(index) != {"schema_version", "question_ids", "pilot_question_ids"}
            or index["schema_version"] != "0.1.0"):
        raise ValueError("unsupported preliminary interview index")
    ids = index["question_ids"]
    pilot = index["pilot_question_ids"]
    for values in (ids, pilot):
        if not isinstance(values, list) or not values or not all(valid_id(x) for x in values) or len(set(values)) != len(values):
            raise ValueError("invalid or duplicate question ids")
    if len(pilot) != 9 or not set(pilot).issubset(ids):
        raise ValueError("invalid pilot ids")
    directory = bank / "questions"
    if {p.name for p in directory.glob("*.json")} != {f"{i}.json" for i in ids}:
        raise ValueError("index and question files disagree")
    records = []
    for question_id in ids:
        path = directory / f"{question_id}.json"
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("question path escapes repository")
        q = read_json(path)
        if not isinstance(q, dict) or q.get("id") != question_id:
            raise ValueError(f"question id mismatch: {question_id}")
        errors = validate_question(q, root)
        if errors:
            raise ValueError(f"{question_id}: {errors}")
        records.append(q)
    selected = [q for q in records if q["id"] in pilot]
    if any(sum(q["level"] == level for q in selected) != 3 for level in LEVELS):
        raise ValueError("pilot must contain three questions per level")
    return records


LABELS = {
    "en": ("Expected answer", "Explanation", "Interviewer intent", "Common errors",
           "Follow-ups", "Example", "Self-assessment rubric", "Prerequisites", "Maximum"),
    "pt-BR": ("Resposta esperada", "Explicação", "Intenção do entrevistador", "Erros comuns",
              "Perguntas complementares", "Exemplo", "Rubrica de autoavaliação", "Pré-requisitos", "Máximo"),
    "es": ("Respuesta esperada", "Explicación", "Intención del entrevistador", "Errores comunes",
           "Preguntas de seguimiento", "Ejemplo", "Rúbrica de autoevaluación", "Requisitos previos", "Máximo"),
}


def render_questions(records, locale):
    """Generate learner-visible sections from the single canonical JSON source."""
    labels = LABELS[locale]
    lines = []
    for q in records:
        lines.extend([f"### {q['id']}", "", f"`{q['level']}` · `{q['topic']}`", "",
                      q["prompt"][locale], "", "<details>", "<summary>" + labels[0] + "</summary>", "",
                      q["expected_answer"][locale], "", f"**{labels[1]}:** {q['explanation'][locale]}",
                      "", f"**{labels[2]}:** {q['intent'][locale]}", "", f"**{labels[3]}**", ""])
        lines.extend(f"- {x}" for x in q["common_errors"][locale])
        lines.extend(["", f"**{labels[4]}**", ""])
        lines.extend(f"- {x}" for x in q["follow_ups"][locale])
        lines.extend(["", f"**{labels[5]}**", "", q["examples"][locale], "",
                      f"**{labels[6]}**", ""])
        lines.extend(f"- {x['points']} — {x['criterion'][locale]}" for x in q["rubric"])
        lines.extend(["", f"{labels[8]}: {sum(x['points'] for x in q['rubric'])}", "",
                      "</details>", "", f"**{labels[7]}**", ""])
        for p in q["prerequisites"]:
            # Both directories are at the same curriculum depth.
            path = p["paths"][locale]
            lines.append(f"- [{p['sections'][locale]}](../../{path})")
        lines.append("")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="refresh the three generated sections")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    records = load_bank(root)
    for locale, name in SUFFIXES.items():
        path = root / CHAPTER / name
        text = path.read_text(encoding="utf-8")
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError(f"missing or repeated generated markers: {path}")
        before, rest = text.split(START)
        block, after = rest.split(END)
        expected = render_questions(records, locale)
        if args.write:
            path.write_text(before + START + expected + END + after, encoding="utf-8")
        elif block != expected:
            raise ValueError(f"stale generated questions: {path}")
    print(f"Validated {len(records)} interview questions in three languages.")


if __name__ == "__main__":
    main()

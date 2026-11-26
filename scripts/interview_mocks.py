"""Preliminary timed mock records. Manual self-assessment, not a grader."""
import argparse
from pathlib import Path
from scripts.interview_records import (
    LOCALES, SUFFIXES, load_bank, locale_map, nonblank, read_json, valid_id,
)

CHAPTER = Path("technical-interview-preparation/24-mock-interviews-and-self-assessment")
START = "<!-- interview-mocks:start -->\n"
END = "<!-- interview-mocks:end -->"
PHASES = ("introduction", "questions", "coding", "tests", "discussion")
TIMING = {
    "junior": (3, 7, 13, 4, 3),
    "mid": (5, 10, 20, 5, 5),
    "senior": (5, 15, 25, 5, 10),
}
RUBRIC = {
    "technical-knowledge": (25, 12),
    "problem-solving": (25, 12),
    "communication": (20, 10),
    "tests-and-edge-cases": (15, 7),
    "engineering-judgment": (15, 7),
}
FIELDS = {
    "id", "level", "duration_minutes", "title", "question_ids",
    "exercise_id", "exercise_path", "time_allocation", "instructions",
    "rubric", "self_evaluation", "improvement",
}


def validate_mock(record, questions, root):
    errors = []
    if not isinstance(record, dict) or set(record) != FIELDS:
        return ["mock fields differ from preliminary contract"]
    level = record["level"]
    if not isinstance(level, str) or level not in TIMING:
        return ["invalid mock level"]
    if not valid_id(record["id"]):
        errors.append("invalid mock ID")
    times = record["time_allocation"]
    if (not isinstance(times, dict) or set(times) != set(PHASES)
            or any(type(v) is not int or v <= 0 for v in times.values())
            or tuple(times[k] for k in PHASES) != TIMING[level]
            or type(record["duration_minutes"]) is not int
            or record["duration_minutes"] != sum(TIMING[level])):
        errors.append("invalid time allocation or duration")
    for field in ("title", "instructions", "self_evaluation", "improvement"):
        if not locale_map(record[field], nonblank):
            errors.append(f"invalid localized field: {field}")
    ids = record["question_ids"]
    if (not isinstance(ids, list) or len(ids) != 4
            or not all(valid_id(x) for x in ids)
            or len(set(ids)) != len(ids)
            or any(x not in questions or questions[x]["level"] != level for x in ids)):
        errors.append("invalid or mismatched question references")
    elif sum(questions[x]["topic"] == "behavioral-international" for x in ids) != 1:
        errors.append("one behavioral question per mock required")
    else:
        if questions[ids[0]]["topic"] != "behavioral-international":
            errors.append("first question must be behavioral")
    exercise_id, path = record["exercise_id"], record["exercise_path"]
    if (not valid_id(exercise_id) or not exercise_id.startswith("problem-solving.")
            or path != f"exercises/problem-solving/{exercise_id.removeprefix('problem-solving.')}/exercise.json"):
        errors.append("invalid exercise reference")
    else:
        actual = root / path
        if not actual.resolve().is_relative_to(root.resolve()) or not actual.is_file():
            errors.append("exercise reference escapes repository or is missing")
        else:
            try:
                exercise = read_json(actual)
                if exercise.get("id") != exercise_id:
                    errors.append("exercise ID mismatch")
                expected = {"junior": "easy", "mid": "medium", "senior": "hard"}[level]
                if exercise.get("difficulty") != expected:
                    errors.append("exercise difficulty mismatch for this mock")
                for locale, filename in SUFFIXES.items():
                    lesson = actual.parent / filename
                    if not lesson.resolve().is_relative_to(root.resolve()) or not lesson.is_file():
                        errors.append(f"missing localized exercise instructions: {locale}")
            except (ValueError, OSError, AttributeError):
                errors.append("invalid exercise record")
    rubric = record["rubric"]
    if not isinstance(rubric, list) or len(rubric) != len(RUBRIC):
        errors.append("invalid rubric dimensions")
    else:
        seen = set()
        for item in rubric:
            if (not isinstance(item, dict)
                    or set(item) != {"id", "points", "partial_points", "label", "indicators"}
                    or not isinstance(item["id"], str) or item["id"] not in RUBRIC
                    or type(item["points"]) is not int or type(item["partial_points"]) is not int
                    or (item["points"], item["partial_points"]) != RUBRIC[item["id"]]
                    or not locale_map(item["label"], nonblank)
                    or not locale_map(item["indicators"], lambda v: isinstance(v, list)
                                      and len(v) >= 2 and all(nonblank(x) for x in v))):
                errors.append("invalid rubric dimension")
                continue
            if item["id"] in seen:
                errors.append("duplicate rubric dimension")
            seen.add(item["id"])
            if len({len(v) for v in item["indicators"].values()}) != 1:
                errors.append("unaligned indicator counts")
        if seen != set(RUBRIC):
            errors.append("missing rubric dimension")
    return errors


def load_mocks(root):
    directory = root / "interviews/mocks"
    index_path = directory / "mock-index.json"
    if not index_path.resolve().is_relative_to(root.resolve()):
        raise ValueError("mock index escapes repository")
    index = read_json(index_path)
    if (not isinstance(index, dict) or set(index) != {"schema_version", "mock_ids"}
            or index["schema_version"] != "0.1.0"):
        raise ValueError("invalid preliminary mock index")
    ids = index["mock_ids"]
    if (not isinstance(ids, list) or len(ids) != 3 or not all(valid_id(x) for x in ids)
            or len(set(ids)) != 3 or "mock-index" in ids):
        raise ValueError("invalid mock IDs")
    if {p.name for p in directory.glob("*.json")} != {"mock-index.json", *(f"{i}.json" for i in ids)}:
        raise ValueError("mock index and files disagree")
    questions = {q["id"]: q for q in load_bank(root)}
    records = []
    for mock_id in ids:
        path = directory / f"{mock_id}.json"
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("mock path escapes repository")
        record = read_json(path)
        if not isinstance(record, dict) or record.get("id") != mock_id:
            raise ValueError("mock ID mismatch")
        errors = validate_mock(record, questions, root)
        if errors:
            raise ValueError(f"{mock_id}: {errors}")
        records.append(record)
    if [m["level"] for m in records] != list(TIMING):
        raise ValueError("expected junior, mid and senior mocks in order")
    return records


LABELS = {
    "en": ("Duration (minutes)", "Phase", "Minutes", "Introduction", "Technical questions", "Live coding",
           "Tests", "Discussion", "Question sequence", "Exercise", "Scoring rubric", "Self-evaluation", "Improvement"),
    "pt-BR": ("Duração (minutos)", "Etapa", "Minutos", "Apresentação", "Perguntas técnicas", "Live coding",
              "Testes", "Discussão", "Sequência de perguntas", "Exercício", "Rubrica de pontuação", "Autoavaliação", "Melhoria"),
    "es": ("Duración (minutos)", "Etapa", "Minutos", "Presentación", "Preguntas técnicas", "Live coding",
           "Pruebas", "Discusión", "Secuencia de preguntas", "Ejercicio", "Rúbrica de puntuación", "Autoevaluación", "Mejora"),
}


def render_mocks(records, locale):
    lab = LABELS[locale]
    filename = SUFFIXES[locale]
    lines = []
    for m in records:
        lines.extend([f"## {m['title'][locale]}", "", f"`{m['id']}` · `{m['level']}`",
                      "", f"**{lab[0]}:** {m['duration_minutes']}", "", m["instructions"][locale],
                      "", f"| {lab[1]} | {lab[2]} |", "| --- | ---: |"])
        lines.extend(f"| {lab[i+3]} | {m['time_allocation'][phase]} |"
                     for i, phase in enumerate(PHASES))
        lines.extend(["", f"**{lab[8]}**", ""])
        for i, question_id in enumerate(m["question_ids"]):
            # GitHub heading slugs remove punctuation such as dots from these ASCII IDs.
            anchor = question_id.replace(".", "")
            lines.append(f"{i+1}. [`{question_id}`](../22-technical-interview-question-bank/{filename}#{anchor})")
        exercise = Path(m["exercise_path"]).parent.as_posix()
        lines.extend(["", f"**{lab[9]}:** [`{m['exercise_id']}`](../../{exercise}/{filename})",
                      "", f"### {lab[10]}", ""])
        for r in m["rubric"]:
            lines.extend([f"**{r['label'][locale]} (0 / {r['partial_points']} / {r['points']})**", ""])
            lines.extend(f"- {indicator}" for indicator in r["indicators"][locale])
            lines.append("")
        lines.extend([f"**{lab[11]}:** {m['self_evaluation'][locale]}", "",
                      f"**{lab[12]}:** {m['improvement'][locale]}", ""])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    records = load_mocks(root)
    for locale, filename in SUFFIXES.items():
        path = root / CHAPTER / filename
        text = path.read_text(encoding="utf-8")
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError(f"invalid generated mock markers: {path}")
        before, rest = text.split(START)
        block, after = rest.split(END)
        expected = render_mocks(records, locale)
        if args.write:
            path.write_text(before + START + expected + END + after, encoding="utf-8")
        elif block != expected:
            raise ValueError(f"stale generated mocks: {path}")
    print(f"Validated {len(records)} timed mocks in three languages.")


if __name__ == "__main__":
    main()

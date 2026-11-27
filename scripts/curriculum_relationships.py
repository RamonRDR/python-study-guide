"""Resolve typed curriculum references from canonical assessment banks.

No learner code is executed. Authoring/consumer identity is a separate gate.
"""
from pathlib import Path
import json
import sys

from assessment_records import ID, canonical_record_path, load_index, schema_validate
from curriculum_manifest import ROOT, manifest_file, read_json, validate_manifest
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.interview_records import load_bank
from scripts.interview_mocks import load_mocks

FIELDS = ("quiz_ids", "exercise_ids", "interview_ids", "mock_ids")
MOCK_LESSON = "technical-interview-preparation.mock-interviews-and-self-assessment"


def read_index(root, descriptor):
    data = read_json(manifest_file(root, descriptor["index"]))
    if not isinstance(data, dict) or data.get("schema_version") != descriptor["schema_version"]:
        raise ValueError("unsupported bank index version")
    return data


def checked_path(root, path, tracked):
    if tracked is not None and path not in tracked:
        raise ValueError(f"untracked bank path: {path}")
    return manifest_file(root, path)


def check_coverage(root, pattern, expected, tracked):
    actual = {p.relative_to(root).as_posix() for p in root.glob(pattern) if p.is_file()}
    if actual != set(expected):
        raise ValueError(f"bank file coverage mismatch: {pattern}")
    if tracked is not None and not actual.issubset(tracked):
        raise ValueError(f"untracked bank files: {pattern}")


def versioned_bank(root, kind, descriptor, chapters, tracked):
    checked_path(root, descriptor["index"], tracked)
    for field in ("index_schema", "record_schema"):
        read_json(checked_path(root, descriptor[field], tracked))
    index = read_index(root, descriptor)
    schema_validate(kind + "-index", index)
    paths = []
    for entry in index["records"]:
        path = canonical_record_path(kind, entry["id"])
        if path != entry["path"]:
            raise ValueError("noncanonical record path")
        checked_path(root, path, tracked)
        paths.append(path)
    pattern = ("quizzes/questions/*.json" if kind == "quiz" else
               "exercises/problem-solving/*/exercise.json")
    check_coverage(root, pattern, paths, tracked)
    records = load_index(kind, root, descriptor["index"], chapters)
    if kind == "exercise":
        for record in records:
            for field in ("starter_path", "solution_path"):
                checked_path(root, record[field], tracked)
    if any(record["schema_version"] != descriptor["schema_version"] for record in records):
        raise ValueError("record version differs from declared bank version")
    return records


def preliminary_bank(root, descriptor, field, directory, loader, tracked):
    checked_path(root, descriptor["index"], tracked)
    index = read_index(root, descriptor)
    ids = index.get(field)
    if (not isinstance(ids, list) or not ids
            or any(not isinstance(i, str) or ID.fullmatch(i) is None for i in ids)
            or len(ids) != len(set(ids))):
        raise ValueError("invalid preliminary bank IDs")
    paths = [f"{directory}/{i}.json" for i in ids]
    expected = paths + ([descriptor["index"]] if field == "mock_ids" else [])
    check_coverage(root, f"{directory}/*.json", expected, tracked)
    # Strictly decode every record before invoking the existing preliminary
    # contract validators. Their historical schema/version remains unchanged.
    records = [read_json(checked_path(root, p, tracked)) for p in paths]
    validated = loader(root)
    if records != validated or [r.get("id") for r in records] != ids:
        raise ValueError("preliminary bank records disagree with index")
    return records


def association_map(data, root=ROOT, tracked=None):
    """Build exact reverse/ownership lists in canonical bank index order."""
    root = Path(root)
    validate_manifest(data, root)
    chapters = {c["id"]: c["content"] for m in data["modules"] for c in m["chapters"]}
    count = sum(len(m["chapters"]) for m in data["modules"])
    if len(chapters) != count:
        raise ValueError("duplicate chapter ID")
    by_path = {p["en"]: identifier for identifier, p in chapters.items()}
    if len(by_path) != count:
        raise ValueError("duplicate chapter content")
    result = {identifier: {field: [] for field in FIELDS} for identifier in chapters}

    banks = data["banks"]
    quizzes = versioned_bank(root, "quiz", banks["quizzes"], chapters, tracked)
    exercises = versioned_bank(root, "exercise", banks["exercises"], chapters, tracked)
    questions = preliminary_bank(root, banks["interviews"], "question_ids",
                                 "interviews/questions", load_bank, tracked)
    mocks = preliminary_bank(root, banks["mocks"], "mock_ids",
                             "interviews/mocks", load_mocks, tracked)
    if tuple(map(len, (quizzes, exercises, questions, mocks))) != (160, 30, 60, 3):
        raise ValueError("canonical bank counts differ from approved inventory")
    ids = [r["id"] for bank in (quizzes, exercises, questions, mocks) for r in bank]
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate ID across banks")

    for field, records in (("quiz_ids", quizzes), ("exercise_ids", exercises)):
        for record in records:
            result[record["chapter_id"]][field].append(record["id"])

    for question in questions:
        owners = set()
        for prerequisite in question["prerequisites"]:
            paths = prerequisite["paths"]
            identifier = by_path.get(paths["en"])
            if identifier is None or chapters[identifier] != paths:
                raise ValueError(f"unknown or inconsistent interview prerequisite: {question['id']}")
            owners.add(identifier)
        for identifier in owners:
            result[identifier]["interview_ids"].append(question["id"])

    question_ids = {r["id"] for r in questions}
    exercise_ids = {r["id"] for r in exercises}
    if MOCK_LESSON not in result:
        raise ValueError("missing mock lesson")
    for mock in mocks:
        if (not set(mock["question_ids"]).issubset(question_ids)
                or mock["exercise_id"] not in exercise_ids
                or mock["exercise_path"] != canonical_record_path("exercise", mock["exercise_id"])):
            raise ValueError(f"dangling or noncanonical mock reference: {mock['id']}")
        result[MOCK_LESSON]["mock_ids"].append(mock["id"])
    return result


def validate_associations(data, expected):
    if data["association_status"] != "complete":
        raise ValueError("complete assessment associations required")
    chapters = [c for m in data["modules"] for c in m["chapters"]]
    if len(chapters) != len(expected) or {c["id"] for c in chapters} != set(expected):
        raise ValueError("association chapter coverage mismatch")
    for chapter in chapters:
        for field in FIELDS:
            if chapter[field] != expected[chapter["id"]][field]:
                raise ValueError(f"association mismatch: {chapter['id']}: {field}")
    return data


def validate_relationships(data, root=ROOT, tracked=None):
    """Reject incomplete or incorrect relationships; not a consumer SHA gate."""
    if data["association_status"] != "complete":
        raise ValueError("complete assessment associations required")
    return validate_associations(data, association_map(data, root, tracked))


def main():
    """Emit a deterministic reference map for authoring (no record bodies)."""
    from curriculum_manifest import load_manifest
    data = load_manifest(ROOT)
    expected = association_map(data, ROOT)
    print("CURRICULUM_ASSOCIATIONS=" + json.dumps(
        {key: {f: v for f, v in fields.items() if v}
         for key, fields in expected.items() if any(fields.values())},
        separators=(",", ":"), ensure_ascii=False,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

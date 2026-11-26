"""Validate versioned assessment records and relationships without executing code."""
import json
import keyword
import math
from pathlib import Path, PurePosixPath
import re

from jsonschema import Draft202012Validator, validators

from assessment_grading import exact_equal, normalize_text

ROOT = Path(__file__).resolve().parents[1]
LOCALES = {"en": "README.md", "pt-BR": "README.pt-BR.md", "es": "README.es.md"}
XP = {"easy": 10, "medium": 20, "hard": 30}
MODULES = {
    "getting-started": (6, 8), "fundamentals": (6, 12),
    "strings-and-numbers": (4, 12), "collections": (6, 16),
    "program-flow": (8, 16), "functions": (9, 14),
    "comments-and-documentation": (6, 8), "errors-files-and-modules": (5, 12),
    "standard-library": (9, 10), "external-libraries": (4, 8),
    "practical-projects": (8, 8), "manual-programming-practices": (4, 8),
    "problem-solving-and-live-coding": (16, 14),
    "technical-interview-preparation": (24, 14),
}
ID = re.compile(r"[a-z0-9]+(?:[.-][a-z0-9]+)+")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
FUNCTION_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
STRICT = validators.extend(
    Draft202012Validator,
    type_checker=Draft202012Validator.TYPE_CHECKER.redefine_many({
        "integer": lambda checker, value: type(value) is int,
        "number": lambda checker, value: (
            type(value) is int or (type(value) is float and math.isfinite(value))
        ),
    }),
)


def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    def reject(value):
        raise ValueError(f"nonfinite JSON number: {value}")

    def finite_float(value):
        result = float(value)
        if not math.isfinite(result):
            reject(value)
        return result

    return json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=pairs,
        parse_constant=reject, parse_float=finite_float,
    )


def safe_file(root, value):
    """Require canonical relative POSIX paths resolving to files inside root."""
    if not isinstance(value, str) or not value or any(
        token in value for token in ("\\", ":", "\x00")
    ):
        raise ValueError(f"invalid path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or path.as_posix() != value or ".." in path.parts:
        raise ValueError(f"invalid path: {value!r}")
    try:
        actual = (root / value).resolve()
    except (OSError, RuntimeError) as exc:
        raise ValueError(f"invalid path: {value!r}") from exc
    if not actual.is_relative_to(root.resolve()) or not actual.is_file():
        raise ValueError(f"missing or escaping path: {value!r}")
    return actual


def schema_validate(kind, record):
    if kind not in {"quiz", "exercise", "quiz-index", "exercise-index"}:
        raise ValueError("unknown record kind")
    schema = read_json(ROOT / "schemas" / (kind + ".schema.json"))
    Draft202012Validator.check_schema(schema)
    errors = list(STRICT(schema).iter_errors(record))
    if errors:
        error = errors[0]
        location = ".".join(map(str, error.absolute_path)) or "record"
        raise ValueError(f"{location}: {error.message}")


def chapter_id(module, folder):
    slug = folder[3:]
    if module == "problem-solving-and-live-coding":
        slug = {"debugging-challenges": "debugging",
                "refactoring-challenges": "refactoring",
                "mixed-challenges": "mixed"}.get(slug, slug)
        module = "problem-solving"
    return module + "." + slug


def load_matrix(root):
    """Check the approved planning inventory, not the future consumer manifest."""
    matrix = read_json(safe_file(
        root, "docs/specs/learning-hub-foundation/assessment-matrix.json"
    ))
    if (not isinstance(matrix, dict) or set(matrix) != {"baseline_revision", "modules"}
            or matrix["baseline_revision"] != "bf56305f42d10ab7c5b31c2b70f6c38140353db4"
            or not isinstance(matrix["modules"], list)):
        raise ValueError("invalid assessment matrix")
    chapters = {}
    totals = {key: 0 for key in XP}
    seen_modules = set()
    for group in matrix["modules"]:
        if (not isinstance(group, dict) or set(group) != {"module", "chapters"}
                or not isinstance(group["module"], str)
                or group["module"] not in MODULES or group["module"] in seen_modules
                or not isinstance(group["chapters"], list)):
            raise ValueError("invalid or duplicate module")
        module = group["module"]
        seen_modules.add(module)
        expected_count, expected_total = MODULES[module]
        expected_dirs = {
            path.parent.name for path in (root / module).glob("[0-9][0-9]-*/README.md")
        }
        seen_dirs = set()
        module_total = 0
        for item in group["chapters"]:
            if (not isinstance(item, dict)
                    or set(item) != {"chapter_id", "paths", "concept", "allocation"}
                    or not isinstance(item["paths"], dict)
                    or set(item["paths"]) != set(LOCALES)
                    or not isinstance(item["concept"], str) or not item["concept"].strip()):
                raise ValueError("invalid matrix chapter")
            paths = item["paths"]
            if not all(isinstance(path, str) for path in paths.values()):
                raise ValueError("invalid localized matrix path")
            folder = PurePosixPath(paths["en"]).parent.name
            if folder not in expected_dirs or folder in seen_dirs:
                raise ValueError("unknown or duplicate matrix chapter path")
            seen_dirs.add(folder)
            identifier = chapter_id(module, folder)
            if item["chapter_id"] != identifier or identifier in chapters:
                raise ValueError("invalid or duplicate chapter ID")
            for locale, filename in LOCALES.items():
                if paths[locale] != f"{module}/{folder}/{filename}":
                    raise ValueError("invalid localized matrix path")
                safe_file(root, paths[locale])
            allocation = item["allocation"]
            if (not isinstance(allocation, dict) or set(allocation) != set(XP)
                    or any(type(n) is not int or n < 0 for n in allocation.values())):
                raise ValueError("invalid allocation")
            for key, count in allocation.items():
                totals[key] += count
                module_total += count
            chapters[identifier] = paths
        if (seen_dirs != expected_dirs or len(seen_dirs) != expected_count
                or module_total != expected_total):
            raise ValueError(f"matrix coverage or allocation mismatch: {module}")
    if (seen_modules != set(MODULES) or len(chapters) != 115
            or totals != {"easy": 64, "medium": 67, "hard": 29}):
        raise ValueError("matrix totals differ from approved allocation")
    return chapters


def validate_prerequisite(paths, root, chapters):
    for path in paths.values():
        safe_file(root, path)
    if paths not in chapters.values():
        raise ValueError("prerequisite path map does not identify one known chapter")


def aligned_lists(record, fields):
    for field in fields:
        if len({len(v) for v in record[field].values()}) != 1:
            raise ValueError(f"unaligned localized lists: {field}")


def canonical_record_path(kind, identifier):
    if not isinstance(identifier, str) or ID.fullmatch(identifier) is None:
        raise ValueError("invalid record ID")
    if kind == "quiz" and identifier.startswith("quiz."):
        return f"quizzes/questions/{identifier}.json"
    if kind == "exercise" and identifier.startswith("problem-solving."):
        slug = identifier.removeprefix("problem-solving.")
        if SLUG.fullmatch(slug):
            return f"exercises/problem-solving/{slug}/exercise.json"
    raise ValueError("invalid record ID namespace")


def validate_record(kind, record, root, chapters):
    schema_validate(kind, record)
    canonical = canonical_record_path(kind, record["id"])
    if record["chapter_id"] not in chapters:
        raise ValueError("unknown chapter")
    if kind == "quiz":
        aligned_lists(record, ("hints",))
        if record["xp"] != XP[record["difficulty"]]:
            raise ValueError("XP does not match difficulty")
        primary = chapters[record["chapter_id"]]
        for prerequisite in record["prerequisites"]:
            paths = prerequisite["paths"]
            validate_prerequisite(paths, root, chapters)
            for locale, heading in prerequisite["sections"].items():
                lines = safe_file(root, paths[locale]).read_text(encoding="utf-8").splitlines()
                if not any(f"{'#' * level} {heading}" in lines for level in range(2, 7)):
                    raise ValueError(f"missing prerequisite heading: {locale}")
        if primary not in [p["paths"] for p in record["prerequisites"]]:
            raise ValueError("primary chapter missing from prerequisites")
        answer = record["answer"]
        if "choices" in record:
            ids = [c["id"] for c in record["choices"]]
            if any(SLUG.fullmatch(identifier) is None for identifier in ids):
                raise ValueError("invalid choice ID")
            if SLUG.fullmatch(answer["choice_id"]) is None:
                raise ValueError("invalid answer choice ID")
            if len(set(ids)) != len(ids):
                raise ValueError("duplicate choice ID")
            if answer["choice_id"] not in ids:
                raise ValueError("unknown choice ID")
            for locale in LOCALES:
                values = [c["text"][locale] for c in record["choices"]]
                if len(set(values)) != len(values):
                    raise ValueError(f"duplicate choice text: {locale}")
        if "accepted" in answer:
            values = [normalize_text(v, answer["comparison"]) for v in answer["accepted"]]
            if len(set(values)) != len(values):
                raise ValueError("duplicate normalized answer")
        return
    aligned_lists(record, ("hints", "constraints"))
    directory = PurePosixPath(canonical).parent
    for field, filename in (("starter_path", "starter.py"), ("solution_path", "solution.py")):
        if record[field] != (directory / filename).as_posix():
            raise ValueError(f"invalid {field} path")
        safe_file(root, record[field])
    for paths in record["prerequisite_paths"]:
        validate_prerequisite(paths, root, chapters)
    tests = record["tests"]
    name = tests["function_name"]
    if FUNCTION_NAME.fullmatch(name) is None or keyword.iskeyword(name):
        raise ValueError("invalid function_name")
    cases = tests["cases"]
    if any(SLUG.fullmatch(case["id"]) is None for case in cases):
        raise ValueError("invalid case ID")
    if any(SLUG.fullmatch(concept) is None for concept in record["concepts"]):
        raise ValueError("invalid concept ID")
    if len({case["id"] for case in cases}) != len(cases):
        raise ValueError("duplicate case ID")
    for index, case in enumerate(cases):
        for previous in cases[:index]:
            if (exact_equal(case["args"], previous["args"])
                    and not exact_equal(case["expected"], previous["expected"])):
                raise ValueError("contradictory expected values for identical arguments")
    for example in record["examples"]:
        if not any(exact_equal(case["args"], example["args"])
                   and exact_equal(case["expected"], example["expected"])
                   for case in cases):
            raise ValueError("example is absent from cases")
    if "timed_practice" in record:
        if (record["practice_mode"] != "implement"
                or record["timed_practice"]["duration_minutes"] != record["estimated_minutes"]):
            raise ValueError("invalid timed practice metadata")


def load_index(kind, root, index_path, chapters):
    if kind not in {"quiz", "exercise"}:
        raise ValueError("unknown index kind")
    index = read_json(safe_file(root, index_path))
    schema_validate(kind + "-index", index)
    seen, records = set(), []
    for entry in index["records"]:
        identifier = entry["id"]
        if identifier in seen:
            raise ValueError("duplicate index ID")
        seen.add(identifier)
        expected_path = canonical_record_path(kind, identifier)
        if entry["path"] != expected_path:
            raise ValueError("index path does not match ID")
        record = read_json(safe_file(root, entry["path"]))
        validate_record(kind, record, root, chapters)
        if record["id"] != identifier:
            raise ValueError("index ID differs from record ID")
        records.append(record)
    return records

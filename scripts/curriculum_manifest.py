"""Structural and confined-file validation for curriculum manifest 1.0.0.

This is the Sprint 08A boundary, not full inventory or consumer acceptance.
Do not execute source code or load remote schemas.
"""
from pathlib import Path, PurePosixPath

from assessment_records import STRICT, read_json, safe_file
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/curriculum-manifest.schema.json"
LOCALES = {"en": "README.md", "pt-BR": "README.pt-BR.md", "es": "README.es.md"}


def manifest_file(root, value):
    """Require an unencoded canonical POSIX file path inside the snapshot."""
    if not isinstance(value, str) or "%" in value or any(ord(c) < 32 or ord(c) == 127 for c in value):
        raise ValueError(f"invalid manifest path: {value!r}")
    return safe_file(root, value)


def validate_locale_paths(root, paths):
    """Require each language's README in the same directory."""
    parents = set()
    for locale, filename in LOCALES.items():
        value = paths[locale]
        manifest_file(root, value)
        path = PurePosixPath(value)
        if path.name != filename:
            raise ValueError(f"incorrect locale path: {locale}: {value}")
        parents.add(path.parent)
    if len(parents) != 1:
        raise ValueError("localized paths refer to different directories")


def validate_manifest(data, root=ROOT):
    """Raise ValueError for structural or path failures; return validated data.

    Bank contents, exact inventory, associations and navigation are later
    Sprint 08 gates. A structural pass alone never authorizes consumption.
    """
    schema = read_json(SCHEMA)
    Draft202012Validator.check_schema(schema)
    error = next(STRICT(schema).iter_errors(data), None)
    if error is not None:
        location = ".".join(map(str, error.absolute_path)) or "manifest"
        raise ValueError(f"{location}: {error.message}")
    for path in data["assets"]:
        manifest_file(root, path)
    for bank in data["banks"].values():
        for field, path in bank.items():
            if field != "schema_version":
                manifest_file(root, path)
    for module in data["modules"]:
        validate_locale_paths(root, module["index"])
        for chapter in module["chapters"]:
            validate_locale_paths(root, chapter["content"])
            for field in ("assets", "resources", "dependency_paths"):
                for path in chapter.get(field, []):
                    manifest_file(root, path)
    return data


def load_manifest(root=ROOT, path="curriculum/manifest.json"):
    """Read strict UTF-8 JSON without numeric coercion, then validate."""
    root = Path(root)
    return validate_manifest(read_json(manifest_file(root, path)), root)

"""Validate the repository paths and multilingual document layout."""

from __future__ import annotations

from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRECTORIES = (
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "assets",
    "comments-and-documentation/01-comments/examples",
    "docs/ai-assisted-development",
    "docs/localized",
    "exercises",
    "external-libraries",
    "functions",
    "fundamentals",
    "practical-projects",
    "scripts",
    "standard-library",
    "tests",
)

REQUIRED_FILES = (
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/content-suggestion.yml",
    ".github/ISSUE_TEMPLATE/learning-question.yml",
    ".github/ISSUE_TEMPLATE/private-contact-request.yml",
    ".github/ISSUE_TEMPLATE/translation-improvement.yml",
    ".github/pull_request_template.md",
    ".github/workflows/quality-checks.yml",
    "AGENTS.md",
    "AUTHORS.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "SUPPORT.md",
    "comments-and-documentation/README.md",
    "comments-and-documentation/README.pt-BR.md",
    "comments-and-documentation/README.es.md",
    "comments-and-documentation/01-comments/README.md",
    "comments-and-documentation/01-comments/README.pt-BR.md",
    "comments-and-documentation/01-comments/README.es.md",
    "docs/project-structure.en.md",
    "docs/project-structure.pt-BR.md",
    "docs/project-structure.es.md",
    "docs/roadmap.en.md",
    "docs/roadmap.pt-BR.md",
    "docs/roadmap.es.md",
    "scripts/check_internal_links.py",
    "scripts/example_manifest.txt",
    "scripts/run_examples.py",
    "scripts/validate_repository_structure.py",
)

LOCALIZED_DOCUMENT_GROUPS = {
    "README.md": (
        "docs/localized/README.pt-BR.md",
        "docs/localized/README.es.md",
    ),
    "AUTHORS.md": (
        "docs/localized/AUTHORS.pt-BR.md",
        "docs/localized/AUTHORS.es.md",
    ),
    "CONTRIBUTING.md": (
        "docs/localized/CONTRIBUTING.pt-BR.md",
        "docs/localized/CONTRIBUTING.es.md",
    ),
    "CODE_OF_CONDUCT.md": (
        "docs/localized/CODE_OF_CONDUCT.pt-BR.md",
        "docs/localized/CODE_OF_CONDUCT.es.md",
    ),
    "SECURITY.md": (
        "docs/localized/SECURITY.pt-BR.md",
        "docs/localized/SECURITY.es.md",
    ),
    "SUPPORT.md": (
        "docs/localized/SUPPORT.pt-BR.md",
        "docs/localized/SUPPORT.es.md",
    ),
}

FORBIDDEN_LOCALIZED_ROOT_FILES = tuple(
    localized_path.name
    for localized_paths in LOCALIZED_DOCUMENT_GROUPS.values()
    for localized_path in map(Path, localized_paths)
)


def relative_link(source: Path, target: Path) -> str:
    """Return the expected POSIX relative link from source to target."""

    source_parent = source.parent
    source_parts = source_parent.parts
    target_parts = target.parts

    shared_length = 0
    for source_part, target_part in zip(source_parts, target_parts):
        if source_part != target_part:
            break
        shared_length += 1

    upward = [".."] * (len(source_parts) - shared_length)
    downward = list(target_parts[shared_length:])
    return "/".join(upward + downward) or target.name


def validate_required_paths() -> list[str]:
    """Report missing required files and directories."""

    errors: list[str] = []
    for relative_path in REQUIRED_DIRECTORIES:
        if not (REPOSITORY_ROOT / relative_path).is_dir():
            errors.append(f"Missing required directory: {relative_path}")

    for relative_path in REQUIRED_FILES:
        if not (REPOSITORY_ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    return errors


def validate_localized_documents() -> list[str]:
    """Check canonical root files and their localized navigation links."""

    errors: list[str] = []

    for forbidden_name in FORBIDDEN_LOCALIZED_ROOT_FILES:
        if (REPOSITORY_ROOT / forbidden_name).exists():
            errors.append(
                f"Localized GitHub-recognized document must not be at root: "
                f"{forbidden_name}"
            )

    for canonical_name, localized_names in LOCALIZED_DOCUMENT_GROUPS.items():
        canonical_path = Path(canonical_name)
        canonical_absolute = REPOSITORY_ROOT / canonical_path
        if not canonical_absolute.is_file():
            continue

        canonical_text = canonical_absolute.read_text(encoding="utf-8")
        for localized_name in localized_names:
            localized_path = Path(localized_name)
            localized_absolute = REPOSITORY_ROOT / localized_path
            if not localized_absolute.is_file():
                errors.append(f"Missing localized document: {localized_name}")
                continue

            expected_localized_link = localized_path.as_posix()
            if expected_localized_link not in canonical_text:
                errors.append(
                    f"{canonical_name} does not link to {expected_localized_link}"
                )

            localized_text = localized_absolute.read_text(encoding="utf-8")
            expected_canonical_link = relative_link(localized_path, canonical_path)
            if expected_canonical_link not in localized_text:
                errors.append(
                    f"{localized_name} does not link back to "
                    f"{expected_canonical_link}"
                )

    return errors


def validate_example_manifest() -> list[str]:
    """Check that the example manifest references unique repository files."""

    errors: list[str] = []
    manifest_path = REPOSITORY_ROOT / "scripts/example_manifest.txt"
    if not manifest_path.is_file():
        return errors

    seen: set[str] = set()
    entries = 0
    for line_number, raw_line in enumerate(
        manifest_path.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        entry = raw_line.strip()
        if not entry or entry.startswith("#"):
            continue

        entries += 1
        if entry in seen:
            errors.append(
                f"Duplicate example manifest entry on line {line_number}: {entry}"
            )
            continue
        seen.add(entry)

        path = Path(entry)
        if path.is_absolute() or ".." in path.parts:
            errors.append(
                f"Unsafe example manifest entry on line {line_number}: {entry}"
            )
        elif path.suffix != ".py":
            errors.append(
                f"Example manifest entry is not a Python file on line "
                f"{line_number}: {entry}"
            )
        elif not (REPOSITORY_ROOT / path).is_file():
            errors.append(f"Example manifest file does not exist: {entry}")

    if entries == 0:
        errors.append("Example manifest contains no executable examples.")

    return errors


def main() -> int:
    """Run structural checks and return a shell-friendly exit code."""

    errors = [
        *validate_required_paths(),
        *validate_localized_documents(),
        *validate_example_manifest(),
    ]

    if errors:
        print("Repository structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Repository structure is valid: required paths, localized documents, "
        "and the safe-example manifest are consistent."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

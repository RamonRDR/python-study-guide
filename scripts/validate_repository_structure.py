"""Validate repository paths, localization, examples, and visual assets."""

from __future__ import annotations

from pathlib import Path
import re
import struct
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
XLINK_HREF = "{http://www.w3.org/1999/xlink}href"

REQUIRED_DIRECTORIES = (
    ".github/ISSUE_TEMPLATE", ".github/workflows", "assets",
    "comments-and-documentation/01-comments/examples",
    "comments-and-documentation/03-meaningful-names/examples",
    "comments-and-documentation/04-task-markers/examples",
    "comments-and-documentation/05-comments-vs-logging/examples",
    "docs/ai-assisted-development", "docs/localized", "exercises",
    "external-libraries", "functions", "fundamentals",
    "practical-projects", "scripts", "standard-library", "tests",
)
REQUIRED_FILES = (
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/content-suggestion.yml",
    ".github/ISSUE_TEMPLATE/learning-question.yml",
    ".github/ISSUE_TEMPLATE/private-contact-request.yml",
    ".github/ISSUE_TEMPLATE/translation-improvement.yml",
    ".github/pull_request_template.md", ".github/workflows/quality-checks.yml",
    "AGENTS.md", "AUTHORS.md", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md",
    "LICENSE", "README.md", "SECURITY.md", "SUPPORT.md", "assets/README.md",
    "assets/banner.png", "assets/banner.svg", "assets/logo-mark.png",
    "assets/logo.png", "assets/repository-preview.png",
    "assets/repository-preview.svg", "comments-and-documentation/README.md",
    "comments-and-documentation/README.pt-BR.md",
    "comments-and-documentation/README.es.md",
    "comments-and-documentation/01-comments/README.md",
    "comments-and-documentation/01-comments/README.pt-BR.md",
    "comments-and-documentation/01-comments/README.es.md",
    "comments-and-documentation/03-meaningful-names/README.md",
    "comments-and-documentation/03-meaningful-names/README.pt-BR.md",
    "comments-and-documentation/03-meaningful-names/README.es.md",
    "comments-and-documentation/04-task-markers/README.md",
    "comments-and-documentation/04-task-markers/README.pt-BR.md",
    "comments-and-documentation/04-task-markers/README.es.md",
    "comments-and-documentation/05-comments-vs-logging/README.md",
    "comments-and-documentation/05-comments-vs-logging/README.pt-BR.md",
    "comments-and-documentation/05-comments-vs-logging/README.es.md",
    "docs/project-structure.en.md", "docs/project-structure.pt-BR.md",
    "docs/project-structure.es.md", "docs/roadmap.en.md",
    "docs/roadmap.pt-BR.md", "docs/roadmap.es.md",
    "scripts/check_internal_links.py", "scripts/example_manifest.txt",
    "scripts/run_examples.py", "scripts/validate_repository_structure.py",
    "tests/test_check_internal_links.py",
    "tests/test_validate_repository_structure.py",
)
LOCALIZED_DOCUMENT_GROUPS = {
    "README.md": ("docs/localized/README.pt-BR.md", "docs/localized/README.es.md"),
    "AUTHORS.md": ("docs/localized/AUTHORS.pt-BR.md", "docs/localized/AUTHORS.es.md"),
    "CONTRIBUTING.md": ("docs/localized/CONTRIBUTING.pt-BR.md", "docs/localized/CONTRIBUTING.es.md"),
    "CODE_OF_CONDUCT.md": ("docs/localized/CODE_OF_CONDUCT.pt-BR.md", "docs/localized/CODE_OF_CONDUCT.es.md"),
    "SECURITY.md": ("docs/localized/SECURITY.pt-BR.md", "docs/localized/SECURITY.es.md"),
    "SUPPORT.md": ("docs/localized/SUPPORT.pt-BR.md", "docs/localized/SUPPORT.es.md"),
}
PNG_ASSET_DIMENSIONS = {
    "assets/banner.png": (1200, 400),
    "assets/logo-mark.png": (384, 384),
    "assets/logo.png": (650, 283),
    "assets/repository-preview.png": (1280, 640),
}
SVG_PNG_PAIRS = (
    ("assets/banner.svg", "assets/banner.png"),
    ("assets/repository-preview.svg", "assets/repository-preview.png"),
)


def relative_link(source: Path, target: Path) -> str:
    source_parts, target_parts = source.parent.parts, target.parts
    shared = 0
    for left, right in zip(source_parts, target_parts):
        if left != right:
            break
        shared += 1
    return "/".join([".."] * (len(source_parts) - shared) + list(target_parts[shared:])) or target.name


def validate_required_paths() -> list[str]:
    errors = [f"Missing required directory: {path}" for path in REQUIRED_DIRECTORIES if not (REPOSITORY_ROOT / path).is_dir()]
    errors.extend(f"Missing required file: {path}" for path in REQUIRED_FILES if not (REPOSITORY_ROOT / path).is_file())
    return errors


def validate_localized_documents() -> list[str]:
    errors: list[str] = []
    forbidden = {Path(path).name for paths in LOCALIZED_DOCUMENT_GROUPS.values() for path in paths}
    errors.extend(f"Localized GitHub-recognized document must not be at root: {name}" for name in forbidden if (REPOSITORY_ROOT / name).exists())
    for canonical_name, localized_names in LOCALIZED_DOCUMENT_GROUPS.items():
        canonical_path = Path(canonical_name)
        canonical_file = REPOSITORY_ROOT / canonical_path
        if not canonical_file.is_file():
            continue
        canonical_text = canonical_file.read_text(encoding="utf-8")
        for localized_name in localized_names:
            localized_path = Path(localized_name)
            localized_file = REPOSITORY_ROOT / localized_path
            if not localized_file.is_file():
                errors.append(f"Missing localized document: {localized_name}")
                continue
            if localized_path.as_posix() not in canonical_text:
                errors.append(f"{canonical_name} does not link to {localized_name}")
            if relative_link(localized_path, canonical_path) not in localized_file.read_text(encoding="utf-8"):
                errors.append(f"{localized_name} does not link back to {relative_link(localized_path, canonical_path)}")
    return errors


def validate_example_manifest() -> list[str]:
    errors: list[str] = []
    manifest = REPOSITORY_ROOT / "scripts/example_manifest.txt"
    if not manifest.is_file():
        return errors
    seen: set[str] = set()
    entries = 0
    for line_number, raw_line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        entry = raw_line.strip()
        if not entry or entry.startswith("#"):
            continue
        entries += 1
        path = Path(entry)
        if entry in seen:
            errors.append(f"Duplicate example manifest entry on line {line_number}: {entry}")
        seen.add(entry)
        if path.is_absolute() or ".." in path.parts:
            errors.append(f"Unsafe example manifest entry on line {line_number}: {entry}")
        elif path.suffix != ".py":
            errors.append(f"Example manifest entry is not a Python file on line {line_number}: {entry}")
        elif not (REPOSITORY_ROOT / path).is_file():
            errors.append(f"Example manifest file does not exist: {entry}")
    if entries == 0:
        errors.append("Example manifest contains no executable examples.")
    return errors


def read_png_dimensions(path: Path) -> tuple[int, int]:
    header = path.read_bytes()[:24]
    if len(header) < 24 or header[:8] != PNG_SIGNATURE or header[12:16] != b"IHDR":
        raise ValueError("invalid PNG header")
    width, height = struct.unpack(">II", header[16:24])
    if not width or not height:
        raise ValueError("PNG dimensions must be positive")
    return width, height


def parse_svg_dimension(value: str | None) -> int:
    match = re.fullmatch(r"\s*(\d+(?:\.0+)?)\s*(?:px)?\s*", value or "")
    if not match:
        raise ValueError(f"unsupported dimension: {value!r}")
    return int(float(match.group(1)))


def local_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def validate_visual_assets() -> list[str]:
    errors: list[str] = []
    png_dimensions: dict[str, tuple[int, int]] = {}
    for relative_path, expected in PNG_ASSET_DIMENSIONS.items():
        path = REPOSITORY_ROOT / relative_path
        if not path.is_file():
            continue
        try:
            actual = read_png_dimensions(path)
        except (OSError, ValueError) as error:
            errors.append(f"Invalid PNG asset {relative_path}: {error}")
            continue
        png_dimensions[relative_path] = actual
        if actual != expected:
            errors.append(f"Unexpected PNG dimensions for {relative_path}: expected {expected[0]}x{expected[1]}, found {actual[0]}x{actual[1]}")

    repository_root = REPOSITORY_ROOT.resolve()
    for svg_relative, png_relative in SVG_PNG_PAIRS:
        svg_path = REPOSITORY_ROOT / svg_relative
        if not svg_path.is_file():
            continue
        try:
            root = ET.parse(svg_path).getroot()
        except (OSError, ET.ParseError) as error:
            errors.append(f"Invalid SVG asset {svg_relative}: {error}")
            continue
        try:
            canvas = (parse_svg_dimension(root.get("width")), parse_svg_dimension(root.get("height")))
        except ValueError as error:
            errors.append(f"Invalid SVG canvas for {svg_relative}: {error}")
            canvas = None
        if canvas and png_dimensions.get(png_relative) and canvas != png_dimensions[png_relative]:
            errors.append(f"SVG canvas mismatch for {svg_relative}: expected {png_dimensions[png_relative]}, found {canvas}")
        view_box = root.get("viewBox", "").split()
        if len(view_box) != 4:
            errors.append(f"{svg_relative} must include a four-value viewBox.")
        elif canvas:
            try:
                if (float(view_box[2]), float(view_box[3])) != tuple(map(float, canvas)):
                    errors.append(f"{svg_relative} viewBox dimensions do not match its canvas.")
            except ValueError:
                errors.append(f"{svg_relative} contains a non-numeric viewBox.")
        if root.get("role") != "img":
            errors.append(f"{svg_relative} must declare role=\"img\".")
        titles = [item for item in root.iter() if local_name(item) == "title" and "".join(item.itertext()).strip()]
        descriptions = [item for item in root.iter() if local_name(item) == "desc" and "".join(item.itertext()).strip()]
        if not titles:
            errors.append(f"{svg_relative} must include a non-empty <title>.")
        if not descriptions:
            errors.append(f"{svg_relative} must include a non-empty <desc>.")
        ids = {item.get("id") for item in root.iter() if item.get("id")}
        labels = root.get("aria-labelledby", "").split()
        if len(labels) < 2 or any(label not in ids for label in labels):
            errors.append(f"{svg_relative} must use valid aria-labelledby references.")
        references = {item.get(attribute) for item in root.iter() if local_name(item) == "image" for attribute in ("href", XLINK_HREF) if item.get(attribute)}
        for reference in sorted(references):
            parsed = urlsplit(reference)
            if parsed.scheme or reference.startswith("#"):
                continue
            decoded = unquote(parsed.path)
            reference_path = Path(decoded)
            if reference_path.is_absolute() or re.match(r"^[A-Za-z]:", decoded):
                errors.append(f"{svg_relative} contains an absolute local reference: {reference}")
                continue
            candidate = (svg_path.parent / reference_path).resolve()
            try:
                candidate.relative_to(repository_root)
            except ValueError:
                errors.append(f"{svg_relative} contains a reference outside the repository: {reference}")
                continue
            if not candidate.is_file():
                errors.append(f"{svg_relative} references a missing local file: {reference}")
    return errors


def main() -> int:
    errors = [*validate_required_paths(), *validate_localized_documents(), *validate_example_manifest(), *validate_visual_assets()]
    if errors:
        print("Repository structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Repository structure is valid: required paths, localized documents, the safe-example manifest, and visual assets are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

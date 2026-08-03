"""Validate relative links in Markdown files without external dependencies."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRECTORIES = {".git", ".venv", "venv", "__pycache__"}

REFERENCE_LINK_PATTERN = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
HTML_LINK_PATTERN = re.compile(
    r"<(?:a|img)\b[^>]*(?:href|src)=[\"']([^\"']+)[\"']",
    re.IGNORECASE,
)
FENCE_PATTERN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
INLINE_CODE_PATTERN = re.compile(r"(`+)(.+?)\1")
MARKDOWN_ESCAPE_PATTERN = re.compile(
    r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])"
)


@dataclass(frozen=True)
class LinkProblem:
    """Describe one internal link that does not resolve to a repository path."""

    source: Path
    line_number: int
    target: str
    resolved_path: Path


def iter_markdown_files() -> list[Path]:
    """Return tracked-style Markdown paths while ignoring generated environments."""

    return sorted(
        path
        for path in REPOSITORY_ROOT.rglob("*.md")
        if not any(part in EXCLUDED_DIRECTORIES for part in path.parts)
    )


def remove_fenced_code(text: str) -> str:
    """Replace fenced code while preserving the opening delimiter requirements."""

    cleaned_lines: list[str] = []
    open_fence: tuple[str, int] | None = None

    for line in text.splitlines():
        match = FENCE_PATTERN.match(line)

        if open_fence is not None:
            fence_character, minimum_length = open_fence
            if match:
                marker = match.group(1)
                trailing_text = match.group(2)
                if (
                    marker[0] == fence_character
                    and len(marker) >= minimum_length
                    and not trailing_text.strip()
                ):
                    open_fence = None
            cleaned_lines.append("")
            continue

        if match:
            marker = match.group(1)
            open_fence = (marker[0], len(marker))
            cleaned_lines.append("")
            continue

        cleaned_lines.append(INLINE_CODE_PATTERN.sub("", line))

    return "\n".join(cleaned_lines)


def is_escaped(text: str, index: int) -> bool:
    """Return whether the character at index is preceded by an odd slash count."""

    slash_count = 0
    current = index - 1
    while current >= 0 and text[current] == "\\":
        slash_count += 1
        current -= 1
    return slash_count % 2 == 1


def iter_inline_markdown_destinations(text: str) -> list[tuple[int, str]]:
    """Parse inline Markdown destinations with balanced parentheses and escapes."""

    destinations: list[tuple[int, str]] = []
    search_position = 0

    while True:
        opening = text.find("](", search_position)
        if opening == -1:
            break
        if is_escaped(text, opening) or is_escaped(text, opening + 1):
            search_position = opening + 2
            continue

        destination_start = opening + 2
        position = destination_start
        nested_parentheses = 0
        quote_character: str | None = None
        inside_angle_destination = False

        while position < len(text):
            character = text[position]
            if character == "\\" and position + 1 < len(text):
                position += 2
                continue

            if inside_angle_destination:
                if character == ">":
                    inside_angle_destination = False
                position += 1
                continue

            if quote_character is not None:
                if character == quote_character:
                    quote_character = None
                position += 1
                continue

            if character == "<" and not text[destination_start:position].strip():
                inside_angle_destination = True
            elif character in {'"', "'"}:
                quote_character = character
            elif character == "(":
                nested_parentheses += 1
            elif character == ")":
                if nested_parentheses == 0:
                    raw_target = text[destination_start:position]
                    line_number = text.count("\n", 0, opening) + 1
                    destinations.append((line_number, raw_target))
                    position += 1
                    break
                nested_parentheses -= 1

            position += 1
        else:
            search_position = opening + 2
            continue

        search_position = position

    return destinations


def first_unescaped_whitespace(text: str) -> int | None:
    """Locate Markdown title separation without splitting escaped spaces."""

    for index, character in enumerate(text):
        if character.isspace() and not is_escaped(text, index):
            return index
    return None


def unescape_markdown(text: str) -> str:
    """Remove backslashes used to escape ASCII punctuation in destinations."""

    return MARKDOWN_ESCAPE_PATTERN.sub(r"\1", text)


def normalize_target(raw_target: str) -> str:
    """Remove Markdown title syntax, angle brackets, and escape markers."""

    target = raw_target.strip()
    if target.startswith("<"):
        closing_angle = target.find(">")
        if closing_angle != -1:
            return unescape_markdown(target[1:closing_angle].strip())

    whitespace_index = first_unescaped_whitespace(target)
    if whitespace_index is not None:
        target = target[:whitespace_index]

    return unescape_markdown(target.strip())


def find_targets(text: str) -> list[tuple[int, str]]:
    """Find Markdown, reference-style, and simple HTML link targets."""

    targets = [
        (line_number, normalize_target(raw_target))
        for line_number, raw_target in iter_inline_markdown_destinations(text)
    ]

    for pattern in (REFERENCE_LINK_PATTERN, HTML_LINK_PATTERN):
        for match in pattern.finditer(text):
            line_number = text.count("\n", 0, match.start()) + 1
            targets.append((line_number, normalize_target(match.group(1))))

    return sorted(targets, key=lambda item: item[0])


def resolve_internal_target(source: Path, target: str) -> Path | None:
    """Resolve one repository-local target or return None when it is external."""

    if not target or target.startswith("#"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None

    decoded_path = unquote(parsed.path)
    if not decoded_path:
        return None

    if decoded_path.startswith("/"):
        return (REPOSITORY_ROOT / decoded_path.lstrip("/")).resolve()

    return (source.parent / decoded_path).resolve()


def validate_links() -> tuple[int, list[LinkProblem]]:
    """Validate every repository-local path referenced by Markdown files."""

    checked_links = 0
    problems: list[LinkProblem] = []

    for markdown_file in iter_markdown_files():
        text = remove_fenced_code(markdown_file.read_text(encoding="utf-8"))
        for line_number, target in find_targets(text):
            resolved_path = resolve_internal_target(markdown_file, target)
            if resolved_path is None:
                continue

            checked_links += 1
            try:
                resolved_path.relative_to(REPOSITORY_ROOT)
            except ValueError:
                problems.append(
                    LinkProblem(markdown_file, line_number, target, resolved_path)
                )
                continue

            if not resolved_path.exists():
                problems.append(
                    LinkProblem(markdown_file, line_number, target, resolved_path)
                )

    return checked_links, problems


def main() -> int:
    """Run the link check and return a shell-friendly exit code."""

    markdown_files = iter_markdown_files()
    checked_links, problems = validate_links()

    print(
        f"Checked {checked_links} internal links across "
        f"{len(markdown_files)} Markdown files."
    )

    if not problems:
        print("All internal Markdown paths resolve successfully.")
        return 0

    print("Broken or unsafe internal links:", file=sys.stderr)
    for problem in problems:
        source = problem.source.relative_to(REPOSITORY_ROOT)
        try:
            resolved = problem.resolved_path.relative_to(REPOSITORY_ROOT)
        except ValueError:
            resolved = problem.resolved_path
        print(
            f"- {source}:{problem.line_number}: {problem.target!r} -> {resolved}",
            file=sys.stderr,
        )

    return 1


if __name__ == "__main__":
    raise SystemExit(main())

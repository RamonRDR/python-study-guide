"""Validate relative links in Markdown files without external dependencies."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRECTORIES = {".git", ".venv", "venv", "__pycache__"}
EXTERNAL_SCHEMES = {"data", "http", "https", "javascript", "mailto", "tel"}

MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_LINK_PATTERN = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
HTML_LINK_PATTERN = re.compile(
    r"<(?:a|img)\b[^>]*(?:href|src)=[\"']([^\"']+)[\"']",
    re.IGNORECASE,
)
INLINE_CODE_PATTERN = re.compile(r"`[^`]*`")


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
    """Replace fenced code lines so example links are not treated as navigation."""

    cleaned_lines: list[str] = []
    fence_marker: str | None = None

    for line in text.splitlines():
        stripped = line.lstrip()
        marker = None
        if stripped.startswith("```"):
            marker = "```"
        elif stripped.startswith("~~~"):
            marker = "~~~"

        if marker:
            if fence_marker is None:
                fence_marker = marker
            elif fence_marker == marker:
                fence_marker = None
            cleaned_lines.append("")
            continue

        cleaned_lines.append("" if fence_marker else INLINE_CODE_PATTERN.sub("", line))

    return "\n".join(cleaned_lines)


def normalize_target(raw_target: str) -> str:
    """Remove Markdown title syntax and angle brackets from one link target."""

    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")].strip()

    return target.split(maxsplit=1)[0].strip()


def find_targets(text: str) -> list[tuple[int, str]]:
    """Find Markdown, reference-style, and simple HTML link targets."""

    targets: list[tuple[int, str]] = []
    for pattern in (
        MARKDOWN_LINK_PATTERN,
        REFERENCE_LINK_PATTERN,
        HTML_LINK_PATTERN,
    ):
        for match in pattern.finditer(text):
            line_number = text.count("\n", 0, match.start()) + 1
            targets.append((line_number, normalize_target(match.group(1))))
    return targets


def resolve_internal_target(source: Path, target: str) -> Path | None:
    """Resolve one repository-local target or return None when it is external."""

    if not target or target.startswith("#"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or parsed.netloc:
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

"""Validate the ordered, localized navigation of published chapters and projects."""

from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys


LOCALES = {
    "en": ("README.md", "← Previous", "Module index", "Next →"),
    "pt-BR": ("README.pt-BR.md", "← Anterior", "Índice do módulo", "Próximo →"),
    "es": ("README.es.md", "← Anterior", "Índice del módulo", "Siguiente →"),
}
CHAPTER_PATTERN = r"[a-z][a-z0-9-]*/\d{2}-[a-z0-9-]+/README(?:\.pt-BR|\.es)?\.md"
CHAPTER_PATH = re.compile(CHAPTER_PATTERN)
PATH_ENTRY = re.compile(r"\d+\.\s+(?:✅\s+)?\[.*\]\(\.\./(" + CHAPTER_PATTERN + r")\)")


def learning_order(text: str) -> list[str]:
    """Read numbered chapter links in the published master learning path."""
    return [
        match.group(1)
        for line in text.splitlines()
        if (match := PATH_ENTRY.fullmatch(line.strip()))
    ]


def navigation_line(order: list[str], position: int, locale: str) -> str:
    """Return the exact expected previous, module index and next links."""
    filename, previous, index, following = LOCALES[locale]
    chapter = PurePosixPath(order[position])
    start = chapter.parent.as_posix()
    index_path = (chapter.parent.parent / filename).as_posix()
    links = []
    if position > 0:
        links.append(f"[{previous}]({posixpath.relpath(order[position - 1], start)})")
    links.append(f"[{index}]({posixpath.relpath(index_path, start)})")
    if position + 1 < len(order):
        links.append(f"[{following}]({posixpath.relpath(order[position + 1], start)})")
    return " · ".join(links)


def block(place: str, navigation: str) -> list[str]:
    return [
        f"<!-- chapter-navigation:{place} -->",
        navigation,
        f"<!-- /chapter-navigation:{place} -->",
    ]


def check_blocks(text: str, expected: str) -> list[str]:
    """Require identical navigation immediately after the header and at EOF."""
    lines = text.rstrip().splitlines()
    errors = []
    selectors = [
        i for i, line in enumerate(lines)
        if "[🇺🇸 English]" in line and "[🇪🇸 Español]" in line
    ]
    if len(selectors) != 1:
        errors.append("Expected exactly one language selector.")
    else:
        start = selectors[0] + 1
        while start < len(lines) and not lines[start].strip():
            start += 1
        if start < len(lines) and lines[start].strip() == "</div>":
            start += 1
        while start < len(lines) and not lines[start].strip():
            start += 1
        if lines[start:start + 3] != block("top", expected):
            errors.append("Missing or incorrect top navigation.")
    if lines[-3:] != block("bottom", expected):
        errors.append("Missing or incorrect bottom navigation.")
    for place in ("top", "bottom"):
        for marker in (block(place, expected)[0], block(place, expected)[2]):
            if lines.count(marker) != 1:
                errors.append(f"Expected exactly one marker: {marker}")
    return errors


def validate_documents(documents: dict[str, str], tracked: set[str]) -> list[str]:
    """Validate full coverage, locale alignment and reciprocal ordered neighbors."""
    errors = []
    canonical_order = None
    for locale, (filename, *_labels) in LOCALES.items():
        master = f"docs/learning-path.{locale}.md"
        order = learning_order(documents.get(master, ""))
        expected_files = {
            p for p in tracked
            if CHAPTER_PATH.fullmatch(p) and PurePosixPath(p).name == filename
        }
        if not order:
            errors.append(f"{master}: no chapter entries found.")
        if len(order) != len(set(order)):
            errors.append(f"{master}: duplicate chapter entries.")
        for path in sorted(expected_files - set(order)):
            errors.append(f"{master}: unlisted chapter {path}.")
        for path in sorted(set(order) - expected_files):
            errors.append(f"{master}: unknown chapter or wrong locale {path}.")
        stems = [PurePosixPath(p).parent.as_posix() for p in order]
        if canonical_order is None:
            canonical_order = stems
        elif stems != canonical_order:
            errors.append(f"{master}: chapter order differs from English.")
        for position, path in enumerate(order):
            if path not in expected_files:
                continue
            index = (PurePosixPath(path).parent.parent / filename).as_posix()
            if index not in tracked:
                errors.append(f"{path}: missing localized module index {index}.")
            if path not in documents:
                errors.append(f"{path}: chapter text unavailable.")
                continue
            expected = navigation_line(order, position, locale)
            errors.extend(f"{path}: {problem}" for problem in check_blocks(
                documents[path], expected
            ))
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True
    )
    tracked = set(result.stdout.decode("utf-8").split("\0"))
    relevant = {p for p in tracked if CHAPTER_PATH.fullmatch(p)}
    relevant.update(f"docs/learning-path.{locale}.md" for locale in LOCALES)
    documents = {}
    for path in sorted(relevant):
        try:
            documents[path] = (root / path).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            print(f"{path}: {exc}", file=sys.stderr)
            return 1
    errors = validate_documents(documents, tracked)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(
        f"Validated navigation in {len(relevant) - len(LOCALES)} chapter/project "
        f"documents across {len(LOCALES)} languages."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Check tracked Markdown language families without third-party dependencies."""

from pathlib import Path
import subprocess
import sys


LOCALES = ("pt-BR", "es")


def missing_versions(paths: set[str]) -> list[str]:
    """Return missing siblings for English documents and orphan translations."""
    markdown = {p for p in paths if p.endswith(".md")}
    errors = []
    localized = {}
    for path in sorted(markdown):
        for locale in LOCALES:
            if path.endswith(f".{locale}.md"):
                stem = path.removesuffix(f".{locale}.md")
                if stem.startswith("docs/localized/"):
                    root = stem.removeprefix("docs/localized/")
                    candidates = [f"{root}.md"]
                else:
                    candidates = [f"{stem}.md", f"{stem}.en.md"]
                canonical = next((p for p in candidates if p in markdown), None)
                if canonical is None:
                    errors.append(f"Missing English source for {path}")
                else:
                    localized.setdefault(canonical, set()).add(locale)
                break
    for path in sorted(markdown):
        if any(path.endswith(f".{locale}.md") for locale in LOCALES):
            continue
        stem = path.removesuffix(".md").removesuffix(".en")
        if "/" not in path:
            stem = f"docs/localized/{stem}"
        for locale in LOCALES:
            expected = f"{stem}.{locale}.md"
            if expected not in markdown:
                errors.append(f"Missing {locale} version of {path}: {expected}")
            elif locale not in localized.get(path, set()):
                errors.append(f"Ambiguous language family for {path}: {expected}")
    return errors


def main() -> int:
    root = str(Path(__file__).resolve().parents[1])
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True
    )
    paths = set(result.stdout.decode("utf-8").split("\0"))
    errors = missing_versions(paths)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print("All tracked Markdown documents have EN, PT-BR and ES versions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Run the repository examples explicitly approved for automated execution."""

from __future__ import annotations

from pathlib import Path
import os
import subprocess
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = Path(__file__).with_name("example_manifest.txt")
EXECUTION_TIMEOUT_SECONDS = 10


def load_manifest() -> list[Path]:
    """Load unique repository-relative Python paths from the example manifest."""

    if not MANIFEST_PATH.is_file():
        raise FileNotFoundError(f"Example manifest not found: {MANIFEST_PATH}")

    examples: list[Path] = []
    seen: set[Path] = set()

    for line_number, raw_line in enumerate(
        MANIFEST_PATH.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        entry = raw_line.strip()
        if not entry or entry.startswith("#"):
            continue

        relative_path = Path(entry)
        if relative_path.is_absolute() or ".." in relative_path.parts:
            raise ValueError(
                f"Unsafe manifest entry on line {line_number}: {entry!r}"
            )
        if relative_path.suffix != ".py":
            raise ValueError(
                f"Manifest entry must reference a .py file on line "
                f"{line_number}: {entry!r}"
            )
        if relative_path in seen:
            raise ValueError(
                f"Duplicate manifest entry on line {line_number}: {entry!r}"
            )

        seen.add(relative_path)
        examples.append(relative_path)

    if not examples:
        raise ValueError("The example manifest does not contain executable files.")

    return examples


def run_example(relative_path: Path) -> tuple[bool, str, str]:
    """Execute one approved example and capture its output."""

    absolute_path = (REPOSITORY_ROOT / relative_path).resolve()
    try:
        absolute_path.relative_to(REPOSITORY_ROOT)
    except ValueError as error:
        raise ValueError(f"Example escapes the repository: {relative_path}") from error

    if not absolute_path.is_file():
        raise FileNotFoundError(f"Example not found: {relative_path}")

    environment = os.environ.copy()
    environment["PYTHONUTF8"] = "1"

    try:
        completed = subprocess.run(
            [sys.executable, str(absolute_path)],
            cwd=REPOSITORY_ROOT,
            env=environment,
            capture_output=True,
            text=True,
            timeout=EXECUTION_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        return False, stdout, f"Timed out after {EXECUTION_TIMEOUT_SECONDS}s.\n{stderr}"

    return completed.returncode == 0, completed.stdout, completed.stderr


def indent_output(text: str) -> str:
    """Indent captured process output for readable workflow logs."""

    stripped = text.rstrip()
    if not stripped:
        return "    <no output>"
    return "\n".join(f"    {line}" for line in stripped.splitlines())


def main() -> int:
    """Execute every approved example and return a shell-friendly exit code."""

    try:
        examples = load_manifest()
    except (FileNotFoundError, ValueError) as error:
        print(f"Example manifest error: {error}", file=sys.stderr)
        return 1

    failures: list[Path] = []
    print(f"Running {len(examples)} approved Python examples.")

    for relative_path in examples:
        print(f"\n==> {relative_path}")
        try:
            succeeded, stdout, stderr = run_example(relative_path)
        except (FileNotFoundError, ValueError) as error:
            print(f"    ERROR: {error}", file=sys.stderr)
            failures.append(relative_path)
            continue

        print("  stdout:")
        print(indent_output(stdout))
        if stderr:
            print("  stderr:")
            print(indent_output(stderr))

        if succeeded:
            print("  result: passed")
        else:
            print("  result: failed", file=sys.stderr)
            failures.append(relative_path)

    if failures:
        print("\nExamples that failed:", file=sys.stderr)
        for relative_path in failures:
            print(f"- {relative_path}", file=sys.stderr)
        return 1

    print("\nAll approved examples completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

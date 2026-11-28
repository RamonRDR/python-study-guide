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
    "problem-solving-and-live-coding",
    "getting-started", "manual-programming-practices", "practical-projects", "scripts", "standard-library", "tests",
)
REQUIRED_FILES = (
    "problem-solving-and-live-coding/16-timed-live-coding/README.md",
    "problem-solving-and-live-coding/16-timed-live-coding/README.pt-BR.md",
    "problem-solving-and-live-coding/16-timed-live-coding/README.es.md",
    "exercises/problem-solving/longest-distinct-substring/README.md",
    "exercises/problem-solving/longest-distinct-substring/README.pt-BR.md",
    "exercises/problem-solving/longest-distinct-substring/README.es.md",
    "exercises/problem-solving/longest-distinct-substring/exercise.json",
    "exercises/problem-solving/longest-distinct-substring/starter.py",
    "exercises/problem-solving/longest-distinct-substring/solution.py",
    "exercises/problem-solving/longest-distinct-substring/test_solution.py",
    "exercises/problem-solving/recursive-flatten/README.md",
    "exercises/problem-solving/recursive-flatten/README.pt-BR.md",
    "exercises/problem-solving/recursive-flatten/README.es.md",
    "exercises/problem-solving/recursive-flatten/exercise.json",
    "exercises/problem-solving/recursive-flatten/starter.py",
    "exercises/problem-solving/recursive-flatten/solution.py",
    "exercises/problem-solving/recursive-flatten/test_solution.py",
    "exercises/problem-solving/binary-target-range/README.md",
    "exercises/problem-solving/binary-target-range/README.pt-BR.md",
    "exercises/problem-solving/binary-target-range/README.es.md",
    "exercises/problem-solving/binary-target-range/exercise.json",
    "exercises/problem-solving/binary-target-range/starter.py",
    "exercises/problem-solving/binary-target-range/solution.py",
    "exercises/problem-solving/binary-target-range/test_solution.py",
    "exercises/problem-solving/merge-sorted-lists/README.md",
    "exercises/problem-solving/merge-sorted-lists/README.pt-BR.md",
    "exercises/problem-solving/merge-sorted-lists/README.es.md",
    "exercises/problem-solving/merge-sorted-lists/exercise.json",
    "exercises/problem-solving/merge-sorted-lists/starter.py",
    "exercises/problem-solving/merge-sorted-lists/solution.py",
    "exercises/problem-solving/merge-sorted-lists/test_solution.py",
    "exercises/problem-solving/sorted-pair-multiplicity/README.md",
    "exercises/problem-solving/sorted-pair-multiplicity/README.pt-BR.md",
    "exercises/problem-solving/sorted-pair-multiplicity/README.es.md",
    "exercises/problem-solving/sorted-pair-multiplicity/exercise.json",
    "exercises/problem-solving/sorted-pair-multiplicity/starter.py",
    "exercises/problem-solving/sorted-pair-multiplicity/solution.py",
    "exercises/problem-solving/sorted-pair-multiplicity/test_solution.py",
    "exercises/problem-solving/inventory-reconciliation/README.md",
    "exercises/problem-solving/inventory-reconciliation/README.pt-BR.md",
    "exercises/problem-solving/inventory-reconciliation/README.es.md",
    "exercises/problem-solving/inventory-reconciliation/exercise.json",
    "exercises/problem-solving/inventory-reconciliation/starter.py",
    "exercises/problem-solving/inventory-reconciliation/solution.py",
    "exercises/problem-solving/inventory-reconciliation/test_solution.py",
    "exercises/problem-solving/timed-threshold-count/README.md",
    "exercises/problem-solving/timed-threshold-count/README.pt-BR.md",
    "exercises/problem-solving/timed-threshold-count/README.es.md",
    "exercises/problem-solving/timed-threshold-count/exercise.json",
    "exercises/problem-solving/timed-threshold-count/starter.py",
    "exercises/problem-solving/timed-threshold-count/solution.py",
    "exercises/problem-solving/timed-threshold-count/test_solution.py",
    "exercises/problem-solving/timed-longest-streak/README.md",
    "exercises/problem-solving/timed-longest-streak/README.pt-BR.md",
    "exercises/problem-solving/timed-longest-streak/README.es.md",
    "exercises/problem-solving/timed-longest-streak/exercise.json",
    "exercises/problem-solving/timed-longest-streak/starter.py",
    "exercises/problem-solving/timed-longest-streak/solution.py",
    "exercises/problem-solving/timed-longest-streak/test_solution.py",
    "problem-solving-and-live-coding/09-collections/README.md",
    "problem-solving-and-live-coding/09-collections/README.pt-BR.md",
    "problem-solving-and-live-coding/09-collections/README.es.md",
    "problem-solving-and-live-coding/10-functions-and-recursion/README.md",
    "problem-solving-and-live-coding/10-functions-and-recursion/README.pt-BR.md",
    "problem-solving-and-live-coding/10-functions-and-recursion/README.es.md",
    "problem-solving-and-live-coding/11-searching-and-sorting/README.md",
    "problem-solving-and-live-coding/11-searching-and-sorting/README.pt-BR.md",
    "problem-solving-and-live-coding/11-searching-and-sorting/README.es.md",
    "problem-solving-and-live-coding/12-algorithms-and-complexity/README.md",
    "problem-solving-and-live-coding/12-algorithms-and-complexity/README.pt-BR.md",
    "problem-solving-and-live-coding/12-algorithms-and-complexity/README.es.md",
    "problem-solving-and-live-coding/13-debugging-challenges/README.md",
    "problem-solving-and-live-coding/13-debugging-challenges/README.pt-BR.md",
    "problem-solving-and-live-coding/13-debugging-challenges/README.es.md",
    "problem-solving-and-live-coding/14-refactoring-challenges/README.md",
    "problem-solving-and-live-coding/14-refactoring-challenges/README.pt-BR.md",
    "problem-solving-and-live-coding/14-refactoring-challenges/README.es.md",
    "problem-solving-and-live-coding/15-mixed-challenges/README.md",
    "problem-solving-and-live-coding/15-mixed-challenges/README.pt-BR.md",
    "problem-solving-and-live-coding/15-mixed-challenges/README.es.md",
    "exercises/problem-solving/ascii-digit-counter/README.md",
    "exercises/problem-solving/ascii-digit-counter/README.pt-BR.md",
    "exercises/problem-solving/ascii-digit-counter/README.es.md",
    "exercises/problem-solving/ascii-digit-counter/exercise.json",
    "exercises/problem-solving/ascii-digit-counter/starter.py",
    "exercises/problem-solving/ascii-digit-counter/solution.py",
    "exercises/problem-solving/ascii-digit-counter/test_solution.py",
    "exercises/problem-solving/sum-digits/README.md",
    "exercises/problem-solving/sum-digits/README.pt-BR.md",
    "exercises/problem-solving/sum-digits/README.es.md",
    "exercises/problem-solving/sum-digits/exercise.json",
    "exercises/problem-solving/sum-digits/starter.py",
    "exercises/problem-solving/sum-digits/solution.py",
    "exercises/problem-solving/sum-digits/test_solution.py",
    "exercises/problem-solving/literal-palindrome/README.md",
    "exercises/problem-solving/literal-palindrome/README.pt-BR.md",
    "exercises/problem-solving/literal-palindrome/README.es.md",
    "exercises/problem-solving/literal-palindrome/exercise.json",
    "exercises/problem-solving/literal-palindrome/starter.py",
    "exercises/problem-solving/literal-palindrome/solution.py",
    "exercises/problem-solving/literal-palindrome/test_solution.py",
    "exercises/problem-solving/unique-in-order/README.md",
    "exercises/problem-solving/unique-in-order/README.pt-BR.md",
    "exercises/problem-solving/unique-in-order/README.es.md",
    "exercises/problem-solving/unique-in-order/exercise.json",
    "exercises/problem-solving/unique-in-order/starter.py",
    "exercises/problem-solving/unique-in-order/solution.py",
    "exercises/problem-solving/unique-in-order/test_solution.py",
    "exercises/problem-solving/label-counts/README.md",
    "exercises/problem-solving/label-counts/README.pt-BR.md",
    "exercises/problem-solving/label-counts/README.es.md",
    "exercises/problem-solving/label-counts/exercise.json",
    "exercises/problem-solving/label-counts/starter.py",
    "exercises/problem-solving/label-counts/solution.py",
    "exercises/problem-solving/label-counts/test_solution.py",
    "exercises/problem-solving/first-repeated-label/README.md",
    "exercises/problem-solving/first-repeated-label/README.pt-BR.md",
    "exercises/problem-solving/first-repeated-label/README.es.md",
    "exercises/problem-solving/first-repeated-label/exercise.json",
    "exercises/problem-solving/first-repeated-label/starter.py",
    "exercises/problem-solving/first-repeated-label/solution.py",
    "exercises/problem-solving/first-repeated-label/test_solution.py",
    "exercises/problem-solving/merge-inventory/README.md",
    "exercises/problem-solving/merge-inventory/README.pt-BR.md",
    "exercises/problem-solving/merge-inventory/README.es.md",
    "exercises/problem-solving/merge-inventory/exercise.json",
    "exercises/problem-solving/merge-inventory/starter.py",
    "exercises/problem-solving/merge-inventory/solution.py",
    "exercises/problem-solving/merge-inventory/test_solution.py",
    "exercises/problem-solving/clamp-value/README.md",
    "exercises/problem-solving/clamp-value/README.pt-BR.md",
    "exercises/problem-solving/clamp-value/README.es.md",
    "exercises/problem-solving/clamp-value/exercise.json",
    "exercises/problem-solving/clamp-value/starter.py",
    "exercises/problem-solving/clamp-value/solution.py",
    "exercises/problem-solving/clamp-value/test_solution.py",
    "exercises/problem-solving/recursive-factorial/README.md",
    "exercises/problem-solving/recursive-factorial/README.pt-BR.md",
    "exercises/problem-solving/recursive-factorial/README.es.md",
    "exercises/problem-solving/recursive-factorial/exercise.json",
    "exercises/problem-solving/recursive-factorial/starter.py",
    "exercises/problem-solving/recursive-factorial/solution.py",
    "exercises/problem-solving/recursive-factorial/test_solution.py",
    "exercises/problem-solving/recursive-power/README.md",
    "exercises/problem-solving/recursive-power/README.pt-BR.md",
    "exercises/problem-solving/recursive-power/README.es.md",
    "exercises/problem-solving/recursive-power/exercise.json",
    "exercises/problem-solving/recursive-power/starter.py",
    "exercises/problem-solving/recursive-power/solution.py",
    "exercises/problem-solving/recursive-power/test_solution.py",
    "exercises/problem-solving/linear-first-index/README.md",
    "exercises/problem-solving/linear-first-index/README.pt-BR.md",
    "exercises/problem-solving/linear-first-index/README.es.md",
    "exercises/problem-solving/linear-first-index/exercise.json",
    "exercises/problem-solving/linear-first-index/starter.py",
    "exercises/problem-solving/linear-first-index/solution.py",
    "exercises/problem-solving/linear-first-index/test_solution.py",
    "exercises/problem-solving/binary-insertion-index/README.md",
    "exercises/problem-solving/binary-insertion-index/README.pt-BR.md",
    "exercises/problem-solving/binary-insertion-index/README.es.md",
    "exercises/problem-solving/binary-insertion-index/exercise.json",
    "exercises/problem-solving/binary-insertion-index/starter.py",
    "exercises/problem-solving/binary-insertion-index/solution.py",
    "exercises/problem-solving/binary-insertion-index/test_solution.py",
    "exercises/problem-solving/descending-insertion-sort/README.md",
    "exercises/problem-solving/descending-insertion-sort/README.pt-BR.md",
    "exercises/problem-solving/descending-insertion-sort/README.es.md",
    "exercises/problem-solving/descending-insertion-sort/exercise.json",
    "exercises/problem-solving/descending-insertion-sort/starter.py",
    "exercises/problem-solving/descending-insertion-sort/solution.py",
    "exercises/problem-solving/descending-insertion-sort/test_solution.py",
    "exercises/problem-solving/unordered-pair-count/README.md",
    "exercises/problem-solving/unordered-pair-count/README.pt-BR.md",
    "exercises/problem-solving/unordered-pair-count/README.es.md",
    "exercises/problem-solving/unordered-pair-count/exercise.json",
    "exercises/problem-solving/unordered-pair-count/starter.py",
    "exercises/problem-solving/unordered-pair-count/solution.py",
    "exercises/problem-solving/unordered-pair-count/test_solution.py",
    "exercises/problem-solving/has-duplicate/README.md",
    "exercises/problem-solving/has-duplicate/README.pt-BR.md",
    "exercises/problem-solving/has-duplicate/README.es.md",
    "exercises/problem-solving/has-duplicate/exercise.json",
    "exercises/problem-solving/has-duplicate/starter.py",
    "exercises/problem-solving/has-duplicate/solution.py",
    "exercises/problem-solving/has-duplicate/test_solution.py",
    "exercises/problem-solving/debug-positive-count/README.md",
    "exercises/problem-solving/debug-positive-count/README.pt-BR.md",
    "exercises/problem-solving/debug-positive-count/README.es.md",
    "exercises/problem-solving/debug-positive-count/exercise.json",
    "exercises/problem-solving/debug-positive-count/starter.py",
    "exercises/problem-solving/debug-positive-count/solution.py",
    "exercises/problem-solving/debug-positive-count/test_solution.py",
    "exercises/problem-solving/debug-negative-window/README.md",
    "exercises/problem-solving/debug-negative-window/README.pt-BR.md",
    "exercises/problem-solving/debug-negative-window/README.es.md",
    "exercises/problem-solving/debug-negative-window/exercise.json",
    "exercises/problem-solving/debug-negative-window/starter.py",
    "exercises/problem-solving/debug-negative-window/solution.py",
    "exercises/problem-solving/debug-negative-window/test_solution.py",
    "exercises/problem-solving/refactor-shipping-fee/README.md",
    "exercises/problem-solving/refactor-shipping-fee/README.pt-BR.md",
    "exercises/problem-solving/refactor-shipping-fee/README.es.md",
    "exercises/problem-solving/refactor-shipping-fee/exercise.json",
    "exercises/problem-solving/refactor-shipping-fee/starter.py",
    "exercises/problem-solving/refactor-shipping-fee/solution.py",
    "exercises/problem-solving/refactor-shipping-fee/test_solution.py",
    "exercises/problem-solving/refactor-score-summary/README.md",
    "exercises/problem-solving/refactor-score-summary/README.pt-BR.md",
    "exercises/problem-solving/refactor-score-summary/README.es.md",
    "exercises/problem-solving/refactor-score-summary/exercise.json",
    "exercises/problem-solving/refactor-score-summary/starter.py",
    "exercises/problem-solving/refactor-score-summary/solution.py",
    "exercises/problem-solving/refactor-score-summary/test_solution.py",
    "exercises/problem-solving/total-short-lengths/README.md",
    "exercises/problem-solving/total-short-lengths/README.pt-BR.md",
    "exercises/problem-solving/total-short-lengths/README.es.md",
    "exercises/problem-solving/total-short-lengths/exercise.json",
    "exercises/problem-solving/total-short-lengths/starter.py",
    "exercises/problem-solving/total-short-lengths/solution.py",
    "exercises/problem-solving/total-short-lengths/test_solution.py",
    "exercises/problem-solving/most-frequent-label/README.md",
    "exercises/problem-solving/most-frequent-label/README.pt-BR.md",
    "exercises/problem-solving/most-frequent-label/README.es.md",
    "exercises/problem-solving/most-frequent-label/exercise.json",
    "exercises/problem-solving/most-frequent-label/starter.py",
    "exercises/problem-solving/most-frequent-label/solution.py",
    "exercises/problem-solving/most-frequent-label/test_solution.py",
    "exercises/problem-solving/expansion-index.json",
    "tests/test_problem_solving_expansion.py",
    "problem-solving-and-live-coding/08-strings-and-numbers/README.md",
    "exercises/problem-solving/vowel-counter/README.md",
    "problem-solving-and-live-coding/08-strings-and-numbers/README.pt-BR.md",
    "exercises/problem-solving/vowel-counter/README.pt-BR.md",
    "problem-solving-and-live-coding/08-strings-and-numbers/README.es.md",
    "exercises/problem-solving/vowel-counter/README.es.md",
    "exercises/problem-solving/vowel-counter/exercise.json",
    "exercises/problem-solving/vowel-counter/starter.py",
    "exercises/problem-solving/vowel-counter/solution.py",
    "exercises/problem-solving/vowel-counter/test_solution.py",
    "tests/test_problem_solving_pilot.py",
    "problem-solving-and-live-coding/README.md",
    "problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md",
    "problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md",
    "problem-solving-and-live-coding/03-algorithmic-complexity/README.md",
    "problem-solving-and-live-coding/04-recursion/README.md",
    "problem-solving-and-live-coding/05-searching-algorithms/README.md",
    "problem-solving-and-live-coding/06-sorting-algorithms/README.md",
    "problem-solving-and-live-coding/07-problem-solving-patterns/README.md",
    "problem-solving-and-live-coding/README.pt-BR.md",
    "problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md",
    "problem-solving-and-live-coding/02-constraints-and-edge-cases/README.pt-BR.md",
    "problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md",
    "problem-solving-and-live-coding/04-recursion/README.pt-BR.md",
    "problem-solving-and-live-coding/05-searching-algorithms/README.pt-BR.md",
    "problem-solving-and-live-coding/06-sorting-algorithms/README.pt-BR.md",
    "problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md",
    "problem-solving-and-live-coding/README.es.md",
    "problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md",
    "problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md",
    "problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md",
    "problem-solving-and-live-coding/04-recursion/README.es.md",
    "problem-solving-and-live-coding/05-searching-algorithms/README.es.md",
    "problem-solving-and-live-coding/06-sorting-algorithms/README.es.md",
    "problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md",
    "problem-solving-and-live-coding/01-problem-solving-fundamentals/examples/study_minutes.py",
    "problem-solving-and-live-coding/02-constraints-and-edge-cases/examples/capacity.py",
    "problem-solving-and-live-coding/03-algorithmic-complexity/examples/operation_counts.py",
    "problem-solving-and-live-coding/04-recursion/examples/recursive_sum.py",
    "problem-solving-and-live-coding/05-searching-algorithms/examples/search.py",
    "problem-solving-and-live-coding/06-sorting-algorithms/examples/sort.py",
    "problem-solving-and-live-coding/07-problem-solving-patterns/examples/patterns.py",
    "docs/specs/learning-hub-foundation/prerequisite-map.md",
    "docs/specs/learning-hub-foundation/prerequisite-map.pt-BR.md",
    "docs/specs/learning-hub-foundation/prerequisite-map.es.md",
    "tests/test_problem_solving_foundations.py",
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
    "docs/assets/learning-hub/banner.png",
    "docs/assets/learning-hub/study-python-en.svg",
    "docs/assets/learning-hub/study-python-pt-br.svg",
    "docs/assets/learning-hub/study-python-es.svg",
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
    "getting-started/README.md",
    "getting-started/README.pt-BR.md",
    "getting-started/README.es.md",
    "getting-started/01-install-python/README.md",
    "getting-started/01-install-python/README.pt-BR.md",
    "getting-started/01-install-python/README.es.md",
    "getting-started/02-configure-vscode/README.md",
    "getting-started/02-configure-vscode/README.pt-BR.md",
    "getting-started/02-configure-vscode/README.es.md",
    "getting-started/03-run-your-first-program/README.md",
    "getting-started/03-run-your-first-program/README.pt-BR.md",
    "getting-started/03-run-your-first-program/README.es.md",
    "getting-started/03-run-your-first-program/examples/first_program.py",
    "getting-started/04-virtual-environments/README.md",
    "getting-started/04-virtual-environments/README.pt-BR.md",
    "getting-started/04-virtual-environments/README.es.md",
    "getting-started/05-packages-and-dependencies/README.md",
    "getting-started/05-packages-and-dependencies/README.pt-BR.md",
    "getting-started/05-packages-and-dependencies/README.es.md",
    "getting-started/06-git-and-version-control/README.md",
    "getting-started/06-git-and-version-control/README.pt-BR.md",
    "getting-started/06-git-and-version-control/README.es.md",
    "manual-programming-practices/README.md",
    "manual-programming-practices/README.pt-BR.md",
    "manual-programming-practices/README.es.md",
    "manual-programming-practices/01-manual-coding-and-debugging/README.md",
    "manual-programming-practices/01-manual-coding-and-debugging/README.pt-BR.md",
    "manual-programming-practices/01-manual-coding-and-debugging/README.es.md",
    "manual-programming-practices/02-specification-driven-development/README.md",
    "manual-programming-practices/02-specification-driven-development/README.pt-BR.md",
    "manual-programming-practices/02-specification-driven-development/README.es.md",
    "manual-programming-practices/03-test-driven-development/README.md",
    "manual-programming-practices/03-test-driven-development/README.pt-BR.md",
    "manual-programming-practices/03-test-driven-development/README.es.md",
    "manual-programming-practices/04-professional-workflow/README.md",
    "manual-programming-practices/04-professional-workflow/README.pt-BR.md",
    "manual-programming-practices/04-professional-workflow/README.es.md",
    "manual-programming-practices/03-test-driven-development/examples/reading_progress.py",
    "manual-programming-practices/03-test-driven-development/examples/test_reading_progress.py",
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
    # README presentation is independent of the frozen curriculum assets.
    "docs/assets/learning-hub/banner.png": (1280, 400),
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

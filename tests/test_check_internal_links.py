"""Regression tests for the dependency-free Markdown link checker."""

from pathlib import Path
import unittest

from scripts import check_internal_links


class MarkdownLinkParsingTests(unittest.TestCase):
    """Protect valid Markdown syntax from false quality-check failures."""

    def test_balanced_parentheses_are_preserved(self) -> None:
        targets = check_internal_links.find_targets(
            "[diagram](assets/image_(small).png)"
        )

        self.assertEqual(targets, [(1, "assets/image_(small).png")])

    def test_escaped_parentheses_are_unescaped(self) -> None:
        targets = check_internal_links.find_targets(
            r"[diagram](assets/image_\(small\).png)"
        )

        self.assertEqual(targets, [(1, "assets/image_(small).png")])

    def test_parentheses_in_a_title_do_not_end_the_link_early(self) -> None:
        targets = check_internal_links.find_targets(
            '[guide](docs/guide.md "Read this (first)")'
        )

        self.assertEqual(targets, [(1, "docs/guide.md")])

    def test_any_uri_scheme_is_external(self) -> None:
        source = Path("README.md")

        self.assertIsNone(
            check_internal_links.resolve_internal_target(
                source,
                "urn:isbn:0451450523",
            )
        )

    def test_longer_fence_is_not_closed_by_shorter_inner_fence(self) -> None:
        markdown = """````markdown
```text
[inside](missing.md)
```
````
[outside](README.md)
"""

        cleaned = check_internal_links.remove_fenced_code(markdown)
        targets = check_internal_links.find_targets(cleaned)

        self.assertEqual(targets, [(6, "README.md")])


if __name__ == "__main__":
    unittest.main()

"""Regression tests for public documentation language families."""

import unittest

from scripts.check_documentation_languages import missing_versions


class DocumentationLanguagesTests(unittest.TestCase):
    def test_supported_families(self):
        paths = {
            "AGENTS.md", "docs/localized/AGENTS.pt-BR.md",
            "docs/localized/AGENTS.es.md",
            "docs/roadmap.en.md", "docs/roadmap.pt-BR.md", "docs/roadmap.es.md",
            "docs/adr/README.md", "docs/adr/README.pt-BR.md",
            "docs/adr/README.es.md", "example.py",
        }
        self.assertEqual(missing_versions(paths), [])

    def test_missing_translation(self):
        errors = missing_versions({"docs/adr/0004.md", "docs/adr/0004.es.md"})
        self.assertEqual(len(errors), 1)
        self.assertIn("docs/adr/0004.pt-BR.md", errors[0])

    def test_orphan_translation(self):
        errors = missing_versions({"docs/adr/0004.es.md"})
        self.assertEqual(len(errors), 1)
        self.assertIn("Missing English source", errors[0])

    def test_ambiguous_english_sources(self):
        paths = {"docs/a.md", "docs/a.en.md", "docs/a.pt-BR.md", "docs/a.es.md"}
        self.assertTrue(missing_versions(paths))


if __name__ == "__main__":
    unittest.main()

"""Regression tests for curriculum navigation, including locale boundaries."""

import unittest

from scripts.check_chapter_navigation import (
    LOCALES,
    block,
    navigation_line,
    validate_documents,
)


def fixture():
    documents = {}
    tracked = set()
    stems = ["fundamentals/01-first", "fundamentals/02-second", "collections/01-third"]
    for locale, (filename, *_labels) in LOCALES.items():
        order = [f"{stem}/{filename}" for stem in stems]
        master = f"docs/learning-path.{locale}.md"
        documents[master] = "\n".join(
            f"{i + 1}. [Chapter](../{path})" for i, path in enumerate(order)
        )
        tracked.add(master)
        for module in ("fundamentals", "collections"):
            tracked.add(f"{module}/{filename}")
        for i, path in enumerate(order):
            tracked.add(path)
            nav = navigation_line(order, i, locale)
            documents[path] = "\n".join([
                "# Chapter",
                "",
                "[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · "
                "[🇪🇸 Español](README.es.md)",
                "",
                *block("top", nav),
                "",
                "Lesson content.",
                "",
                *block("bottom", nav),
                "",
            ])
    return documents, tracked


class ChapterNavigationTests(unittest.TestCase):
    def test_valid_trilingual_sequence(self):
        documents, tracked = fixture()
        self.assertEqual(validate_documents(documents, tracked), [])
        first = documents["fundamentals/01-first/README.md"]
        self.assertNotIn("← Previous", first)
        last = documents["collections/01-third/README.es.md"]
        self.assertNotIn("Siguiente →", last)
        self.assertIn("../../fundamentals/02-second/README.es.md", last)

    def test_wrong_locale_across_module_boundary(self):
        documents, tracked = fixture()
        path = "fundamentals/02-second/README.pt-BR.md"
        documents[path] = documents[path].replace(
            "../../collections/01-third/README.pt-BR.md",
            "../../collections/01-third/README.md",
        )
        errors = validate_documents(documents, tracked)
        self.assertTrue(any(path in error and "top" in error for error in errors))
        self.assertTrue(any(path in error and "bottom" in error for error in errors))

    def test_skipped_neighbor(self):
        documents, tracked = fixture()
        path = "fundamentals/01-first/README.md"
        documents[path] = documents[path].replace(
            "../02-second/README.md", "../../collections/01-third/README.md"
        )
        self.assertTrue(validate_documents(documents, tracked))

    def test_missing_bottom_block(self):
        documents, tracked = fixture()
        path = "fundamentals/01-first/README.md"
        documents[path] = documents[path].split("<!-- chapter-navigation:bottom -->")[0]
        self.assertTrue(any("bottom" in e for e in validate_documents(documents, tracked)))

    def test_duplicate_marker(self):
        documents, tracked = fixture()
        path = "fundamentals/01-first/README.md"
        documents[path] += "\n<!-- chapter-navigation:top -->\n"
        self.assertTrue(any("exactly one marker" in e for e in validate_documents(documents, tracked)))

    def test_wrong_order_in_translation(self):
        documents, tracked = fixture()
        master = "docs/learning-path.es.md"
        documents[master] = "\n".join(reversed(documents[master].splitlines()))
        self.assertTrue(any("differs from English" in e for e in validate_documents(documents, tracked)))

    def test_unlisted_chapter(self):
        documents, tracked = fixture()
        tracked.add("fundamentals/03-omitted/README.md")
        self.assertTrue(any("unlisted chapter" in e for e in validate_documents(documents, tracked)))

    def test_missing_localized_index(self):
        documents, tracked = fixture()
        tracked.remove("collections/README.pt-BR.md")
        self.assertTrue(any("missing localized module index" in e for e in validate_documents(documents, tracked)))

    def test_duplicate_master_entry(self):
        documents, tracked = fixture()
        master = "docs/learning-path.en.md"
        documents[master] += "\n" + documents[master].splitlines()[0]
        self.assertTrue(any("duplicate chapter entries" in e for e in validate_documents(documents, tracked)))


    def test_prepend_getting_started_preserves_cross_module_navigation(self):
        documents, tracked = fixture()
        for locale, (filename, previous, index, following) in LOCALES.items():
            master = f"docs/learning-path.{locale}.md"
            start = f"getting-started/01-install-python/{filename}"
            first = f"fundamentals/01-first/{filename}"
            documents[master] = f"1. [Install Python](../{start})\n" + documents[master]
            tracked.update({start, f"getting-started/{filename}"})
            nav = (
                f"[{index}](../{filename}) · "
                f"[{following}](../../fundamentals/01-first/{filename})"
            )
            documents[start] = "\n".join([
                "# Install Python", "",
                "[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · "
                "[🇪🇸 Español](README.es.md)", "",
                *block("top", nav), "", "Lesson content.", "",
                *block("bottom", nav), "",
            ])
            old = f"[{index}](../{filename})"
            new = f"[{previous}](../../getting-started/01-install-python/{filename}) · {old}"
            documents[first] = documents[first].replace(old, new)
        self.assertEqual(validate_documents(documents, tracked), [])
        path = "fundamentals/01-first/README.pt-BR.md"
        documents[path] = documents[path].replace(
            "../../getting-started/01-install-python/README.pt-BR.md",
            "../../getting-started/01-install-python/README.md",
        )
        self.assertTrue(any(path in error for error in validate_documents(documents, tracked)))

    def test_extended_onboarding_has_reciprocal_fundamentals_boundary(self):
        for locale, (filename, previous, index, following) in LOCALES.items():
            order = [
                f"getting-started/{slug}/{filename}"
                for slug in (
                    "01-install-python",
                    "02-configure-vscode",
                    "03-run-your-first-program",
                    "04-virtual-environments",
                    "05-packages-and-dependencies",
                    "06-git-and-version-control",
                )
            ] + [f"fundamentals/01-how-python-runs-a-program/{filename}"]
            with self.subTest(locale=locale):
                self.assertEqual(
                    navigation_line(order, 4, locale),
                    f"[{previous}](../04-virtual-environments/{filename}) · "
                    f"[{index}](../{filename}) · "
                    f"[{following}](../06-git-and-version-control/{filename})",
                )
                self.assertEqual(
                    navigation_line(order, 5, locale),
                    f"[{previous}](../05-packages-and-dependencies/{filename}) · "
                    f"[{index}](../{filename}) · "
                    f"[{following}](../../fundamentals/01-how-python-runs-a-program/{filename})",
                )
                self.assertEqual(
                    navigation_line(order, 6, locale),
                    f"[{previous}](../../getting-started/06-git-and-version-control/{filename}) · "
                    f"[{index}](../{filename})",
                )


if __name__ == "__main__":
    unittest.main()

# Tests

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

This directory already contains regression tests for the dependency-free repository quality tools. GitHub Actions runs them with:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Current tests protect Markdown link parsing and repository-structure validation, including visual-asset metadata, SVG accessibility, and safe local references.

Historical documentation planned educational testing content, beginning with simple assertions and later introducing `pytest` for executable examples and practical projects.

Navigation regression tests enforce the same ordered master learning path in all three languages, exact previous/index/next links at the top and bottom, cross-module boundaries, and coverage of tracked chapter/project READMEs. Run `python scripts/check_chapter_navigation.py` from the repository root to check the complete curriculum.

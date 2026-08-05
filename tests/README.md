# Tests

This directory already contains regression tests for the dependency-free repository quality tools. GitHub Actions runs them with:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Current tests protect Markdown link parsing and repository-structure validation, including visual-asset metadata, SVG accessibility, and safe local references.

Educational testing content remains planned. That learning path will begin with simple assertions and later introduce `pytest` for executable examples and practical projects.

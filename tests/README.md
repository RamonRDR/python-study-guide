# Tests

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

This directory contains regression tests for repository quality tools, including the assessment contract. Install `requirements-assessment.txt` in a virtual environment before running the suite. GitHub Actions runs it with:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Current tests protect Markdown link parsing and repository-structure validation, including visual-asset metadata, SVG accessibility, and safe local references.

Historical documentation planned educational testing content, beginning with simple assertions and later introducing `pytest` for executable examples and practical projects.

Navigation regression tests enforce the same ordered master learning path in all three languages, exact previous/index/next links at the top and bottom, cross-module boundaries, and coverage of tracked chapter/project READMEs. Run `python scripts/check_chapter_navigation.py` from the repository root to check the complete curriculum.

The foundation tests require the approved chapter/difficulty allocation, exact index coverage and deterministic grading; trusted literal code fixtures are executed, never arbitrary code loaded from question records. Pilot regressions remain covered.

The expansion suite verifies the complete 160-question matrix, 2,850 XP, 82 new response fixtures, trusted literal code fixtures, question-type diversity and all three catalog indexes. Foundation and pilot regressions remain active; no learner-supplied code is executed.

The exercise migration suite verifies the complete 30-record index, all 192 existing cases, the explicit no-alias flags, exact large integers, practice modes, timed metadata and trusted reference/wrong implementations. The 29-entry historical expansion index and its regression suite remain intact. Browser runtime and timeout enforcement are not tested here.

The consolidated AC-07 tests check both canonical indexes together, 190 unique record IDs, 160 independent correct/incorrect quiz response fixtures, shared Python source inventory and invalid-record rejection through both index loaders. Prior trusted exercise discrimination, fixture and regression suites remain active. See [AC-07 implementation evidence](../docs/specs/learning-hub-foundation/acceptance-criteria.md).

Sprint 08A adds [test_curriculum_manifest.py](test_curriculum_manifest.py). Sprint 08A acceptance: a Draft 2020-12 schema and strict structural/path validation with synthetic positive and negative fixtures, including independent bank versions, localized paths, execution metadata and invalid JSON. Inventory and navigation (B), bank relationships (C), pinned consumer (D) and consolidated acceptance (E) remain pending. The structural validator alone does not certify a published snapshot. Exact-head CI and review are required; no new test result is asserted here.

Sprint 08B adds [test_curriculum_inventory.py](test_curriculum_inventory.py). Tests check the complete tracked inventory, historical IDs, order, navigation, localized titles, assets, resources, dependency metadata and rejection of pending association violations. CI also runs the authoring inventory CLI. No consumer revision or browser execution test is claimed.

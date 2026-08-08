# Project Structure

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

This document describes the structure currently tracked in the repository. Planned directories are not shown as if they already existed.

## Current repository map

```text
python-study-guide/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   └── quality-checks.yml
│   └── pull_request_template.md
├── AGENTS.md
├── AUTHORS.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── assets/
├── comments-and-documentation/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-comments/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── business_rule_comments.py
│   │       ├── unnecessary_comments.py
│   │       └── useful_comments.py
│   ├── 02-docstrings/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── class_docstrings.py
│   │       ├── function_docstrings.py
│   │       └── inspect_docstrings.py
│   ├── 03-meaningful-names/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── booleans_and_units.py
│   │       ├── refactor_for_intent.py
│   │       └── vague_and_clear_names.py
│   ├── 04-task-markers/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── actionable_markers.py
│   │       ├── scan_markers.py
│   │       └── temporary_workaround.py
│   ├── 05-comments-vs-logging/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── application_and_library_logging.py
│   │       ├── comments_vs_logging.py
│   │       └── logging_levels.py
│   └── 06-pep8-and-readability/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── imports_and_names.py
│           ├── readable_layout.py
│           └── refactor_for_readability.py
├── docs/
│   ├── ai-assisted-development/
│   ├── localized/
│   ├── project-structure.en.md
│   ├── project-structure.pt-BR.md
│   ├── project-structure.es.md
│   ├── roadmap.en.md
│   ├── roadmap.pt-BR.md
│   └── roadmap.es.md
├── exercises/
├── external-libraries/
├── functions/
├── fundamentals/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-how-python-runs-a-program/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       └── hello_world.py
│   ├── 02-print-and-input/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── interactive_greeting.py
│   │       └── output_basics.py
│   ├── 03-variables-and-naming/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── learning_profile.py
│   │       └── variable_basics.py
│   ├── 04-built-in-data-types/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── same_looking_values.py
│   │       └── value_catalog.py
│   ├── 05-type-and-isinstance/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── check_type_families.py
│   │       └── inspect_types.py
│   └── 06-type-conversion/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── conversion_basics.py
│           └── conversion_surprises.py
├── practical-projects/
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
├── strings-and-numbers/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-string-creation-and-indexing/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── fixed_position_text.py
│   │       └── string_basics.py
│   ├── 02-common-string-methods/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── normalize_text.py
│   │       └── split_and_join.py
│   └── 03-int-float-and-bool/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── numeric_behavior.py
│           └── truth_and_precision.py
└── tests/
```

## Root file guide

- `AGENTS.md`: repository-wide instructions for contributors and AI agents.
- `AUTHORS.md`: canonical authorship, maintenance, and contribution-credit record.
- `CODE_OF_CONDUCT.md`: community behavior and private-reporting policy recognized by GitHub.
- `CONTRIBUTING.md`: contribution workflow and quality expectations.
- `LICENSE`: MIT License applied to the repository.
- `README.md`: canonical English repository entry point.
- `SECURITY.md`: security scope and private vulnerability-reporting policy.
- `SUPPORT.md`: support routing and project-support boundaries.

## Directory guide

- `.github/`: collaboration configuration, issue forms, pull request template, and GitHub Actions workflow.
- `assets/`: original visual identity, exported assets, editable compositions, palette, accessibility guidance, and usage rules.
- `comments-and-documentation/`: complete Phase 6 learning path. Reviewed chapters are available for comments, docstrings, meaningful names, task markers, comments versus logging, and PEP 8 and readability, each in English, Brazilian Portuguese, and Spanish with safe executable examples.
- `docs/`: roadmaps, project architecture, localized project documents, policies, and responsible AI-assisted development guidance.
- `exercises/`: focused practice activities connected to learning chapters.
- `external-libraries/`: future guides to third-party packages.
- `functions/`: future learning path for functions, parameters, returns, scope, and type hints.
- `fundamentals/`: complete Phase 1 learning path. Its six chapters teach how Python runs a program, how to use `print()` and `input()`, how assignment and naming work, how to recognize and inspect common built-in data types, and how to convert compatible values deliberately, with aligned multilingual explanations and executable examples.
- `practical-projects/`: future small projects combining several concepts.
- `scripts/`: dependency-free maintenance tools used locally and by GitHub Actions.
- `standard-library/`: future guides to modules distributed with Python.
- `strings-and-numbers/`: Phase 2 learning path, currently in progress. Its first three reviewed chapters cover string creation, common string methods, integer and floating-point behavior, division, floating-point approximation, truth values, and Boolean semantics in English, Brazilian Portuguese, and Spanish with safe executable examples.
- `tests/`: regression tests for repository quality tools and later educational code.

## Chapter directory rule

Each learning chapter contains:

- a canonical English `README.md`;
- Brazilian Portuguese and Spanish localized README files;
- an `examples/` directory when executable examples improve the topic;
- only complete, reviewable material rather than empty placeholders.

## Naming and language conventions

Repository directories, file names, variables, functions, classes, and other code identifiers use English. Explanatory documents are offered in English, Brazilian Portuguese, and Spanish.

English uses canonical root files recognized automatically by GitHub. Brazilian Portuguese and Spanish versions of those documents are stored in `docs/localized/`. Learning chapters keep their localized README files beside the English version for direct navigation.

## Maintenance rule

A pull request that moves, creates, or removes significant paths must update this structure in the same change. New executable examples must also be reviewed for unattended execution and registered in `scripts/example_manifest.txt` when approved for CI.

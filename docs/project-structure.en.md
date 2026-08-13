# Project Structure

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

This document describes the structure currently tracked in the repository. Planned directories are not presented as completed learning sections.

## Current repository map

```text
python-study-guide/
├── .github/
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
├── collections/
├── docs/
├── exercises/
├── external-libraries/
├── functions/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-defining-and-calling-functions/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── define_and_call.py
│   │       ├── execution_order.py
│   │       └── repeated_calls.py
│   ├── 02-parameters-and-arguments/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── book_details.py
│   │       ├── greet_people.py
│   │       └── score_status.py
│   └── 03-return-values/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── calculate_total.py
│           ├── classify_score.py
│           └── find_first_even.py
├── fundamentals/
├── practical-projects/
├── program-flow/
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
├── strings-and-numbers/
└── tests/
```

Completed learning sections contain their own chapter indexes and example directories. The active Functions subtree is expanded here because Phase 5 is currently being developed chapter by chapter.

## Directory guide

- `.github/`: collaboration configuration and GitHub Actions.
- `assets/`: project visual identity and usage guidance.
- `comments-and-documentation/`: complete Phase 6 learning path.
- `collections/`: complete Phase 3 learning path.
- `docs/`: learning paths, roadmaps, structure documentation, localized project documents, and responsible-development guidance.
- `exercises/`: focused practice activities.
- `external-libraries/`: future third-party package guides.
- `functions/`: Phase 5 in progress. Chapters 01–03 cover defining and calling functions, parameters and arguments, return values, `None`, branch-specific and early returns, tuple results, `print()` versus `return`, and complete input-to-output tracing.
- `fundamentals/`: complete Phase 1 learning path.
- `practical-projects/`: future integrated projects.
- `program-flow/`: complete Phase 4 learning path.
- `scripts/`: dependency-free repository quality tools.
- `standard-library/`: future standard-library guides.
- `strings-and-numbers/`: complete Phase 2 learning path.
- `tests/`: regression tests for repository quality tooling and later educational code.

## Chapter directory rule

Each learning chapter contains a canonical English `README.md`, Brazilian Portuguese and Spanish localized READMEs, and an `examples/` directory when executable examples improve the topic.

## Naming and language conventions

Repository paths and code identifiers use English. Explanations are offered in English, Brazilian Portuguese, and Spanish.

## Maintenance rule

A pull request that creates, moves, or removes significant paths must update these structure documents in the same change. Approved unattended examples must also be registered in `scripts/example_manifest.txt`.

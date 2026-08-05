# Project Structure

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

This document describes the structure currently tracked in the repository. Planned directories are not shown as if they already existed.

## Current repository map

```text
python-study-guide/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.yml
│   │   ├── config.yml
│   │   ├── content-suggestion.yml
│   │   ├── learning-question.yml
│   │   ├── private-contact-request.yml
│   │   └── translation-improvement.yml
│   ├── workflows/
│   │   └── quality-checks.yml
│   └── pull_request_template.md
├── .gitignore
├── AGENTS.md
├── AUTHORS.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── assets/
│   ├── README.md
│   ├── banner.png
│   ├── banner.svg
│   ├── logo-mark.png
│   ├── logo.png
│   ├── repository-preview.png
│   └── repository-preview.svg
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
│   └── 02-docstrings/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── class_docstrings.py
│           ├── function_docstrings.py
│           └── inspect_docstrings.py
├── docs/
│   ├── ai-assisted-development/
│   │   ├── README.en.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── localized/
│   │   ├── AUTHORS.pt-BR.md
│   │   ├── AUTHORS.es.md
│   │   ├── CODE_OF_CONDUCT.pt-BR.md
│   │   ├── CODE_OF_CONDUCT.es.md
│   │   ├── CONTRIBUTING.pt-BR.md
│   │   ├── CONTRIBUTING.es.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── SECURITY.pt-BR.md
│   │   ├── SECURITY.es.md
│   │   ├── SUPPORT.pt-BR.md
│   │   └── SUPPORT.es.md
│   ├── project-structure.en.md
│   ├── project-structure.pt-BR.md
│   ├── project-structure.es.md
│   ├── roadmap.en.md
│   ├── roadmap.pt-BR.md
│   └── roadmap.es.md
├── exercises/
│   └── README.md
├── external-libraries/
│   └── README.md
├── functions/
│   └── README.md
├── fundamentals/
│   └── README.md
├── practical-projects/
│   └── README.md
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
│   └── README.md
└── tests/
    ├── README.md
    ├── test_check_internal_links.py
    └── test_validate_repository_structure.py
```

## Root file guide

- `.gitignore`: prevents local Python artifacts and other generated files from being committed.
- `AGENTS.md`: repository-wide instructions for contributors and AI agents.
- `AUTHORS.md`: canonical English project authorship, maintenance, and contribution-credit record.
- `CODE_OF_CONDUCT.md`: canonical English community behavior and private-reporting policy recognized by GitHub.
- `CONTRIBUTING.md`: canonical English contribution workflow and quality expectations recognized by GitHub.
- `LICENSE`: the MIT License applied to the repository.
- `README.md`: canonical English repository entry point recognized by GitHub.
- `SECURITY.md`: canonical English security scope and private vulnerability-reporting policy recognized by GitHub.
- `SUPPORT.md`: canonical English support routing and project-support boundaries.

## Directory guide

- `.github/`: GitHub collaboration and automation configuration. The pull request template requests scope, verification, language alignment, AI-assistance disclosure, privacy checks, and reviewer notes. Issue forms separate bug reports, content suggestions, learning questions, translation improvements, and privacy-safe requests for a private reporting channel. The quality workflow compiles Python files, runs regression tests and approved examples, checks internal Markdown paths, and validates repository structure.
- `assets/`: original project visual identity, including the banner, primary logo, compact mark, repository preview, editable SVG compositions, palette documentation, accessibility guidance, and usage rules.
- `comments-and-documentation/`: learning path for comments, docstrings, naming, task markers, logging decisions, PEP 8, and readable code. Complete chapters are available in `01-comments/` and `02-docstrings/`, each with English, Brazilian Portuguese, and Spanish explanations plus executable examples.
- `docs/`: roadmaps, project architecture, policies, and multilingual reference documents. `ai-assisted-development/` explains responsible use of ChatGPT and Codex. `localized/` stores Brazilian Portuguese and Spanish versions of canonical root documents while keeping GitHub-recognized community files unambiguous.
- `exercises/`: focused practice activities connected to learning chapters.
- `external-libraries/`: future guides to third-party packages installed separately.
- `functions/`: future learning path for function creation, parameters, arguments, return values, scope, type hints, and collaboration between functions.
- `fundamentals/`: future learning path for variables, data types, input, output, strings, numbers, collections, and control flow.
- `practical-projects/`: future small projects that combine multiple concepts.
- `scripts/`: dependency-free maintenance tools used locally and by GitHub Actions to run approved examples, check internal links, and validate repository structure.
- `standard-library/`: future guides to modules distributed with Python.
- `tests/`: regression tests for repository quality tools, followed later by automated tests for educational examples and practical projects.

## Naming and language conventions

Repository directories, file names, variables, functions, classes, and other code identifiers use English. Explanatory documents are offered in English, Brazilian Portuguese, and Spanish.

English uses the canonical root files recognized automatically by GitHub. Brazilian Portuguese and Spanish versions of those documents are stored in `docs/localized/`. Learning sections may keep localized README files beside the English chapter when that improves navigation.

## Maintenance rule

A pull request that moves, creates, or removes significant paths should update this structure in the same change. Planned chapter directories should be added only when they contain useful material, rather than as empty placeholders.

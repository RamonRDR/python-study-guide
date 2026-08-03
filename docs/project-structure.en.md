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
│   │   └── translation-improvement.yml
│   └── pull_request_template.md
├── .gitignore
├── AGENTS.md
├── AUTHORS.md
├── AUTHORS.pt-BR.md
├── AUTHORS.es.md
├── CODE_OF_CONDUCT.md
├── CODE_OF_CONDUCT.pt-BR.md
├── CODE_OF_CONDUCT.es.md
├── CONTRIBUTING.md
├── CONTRIBUTING.pt-BR.md
├── CONTRIBUTING.es.md
├── LICENSE
├── README.md
├── README.pt-BR.md
├── README.es.md
├── SECURITY.md
├── SECURITY.pt-BR.md
├── SECURITY.es.md
├── SUPPORT.md
├── SUPPORT.pt-BR.md
├── SUPPORT.es.md
├── assets/
│   └── README.md
├── comments-and-documentation/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── 01-comments/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── business_rule_comments.py
│           ├── unnecessary_comments.py
│           └── useful_comments.py
├── docs/
│   ├── ai-assisted-development/
│   │   ├── README.en.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
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
├── standard-library/
│   └── README.md
└── tests/
    └── README.md
```

## Root file guide

- `.gitignore`: prevents local Python artifacts and other generated files from being committed.
- `AGENTS.md`: repository-wide instructions for contributors and AI agents.
- `AUTHORS...`: multilingual project authorship, maintenance, and contribution-credit records.
- `CODE_OF_CONDUCT...`: expected community behavior, unacceptable conduct, private reporting guidance, and proportionate enforcement principles.
- `CONTRIBUTING...`: multilingual contribution workflow and quality expectations.
- `LICENSE`: the MIT License applied to the repository.
- `README...`: multilingual entry points to the project.
- `SECURITY...`: supported security scope, safe research expectations, and private vulnerability-reporting guidance.
- `SUPPORT...`: routes questions and reports to the appropriate channel and defines the boundaries of project support.

## Directory guide

- `.github/`: GitHub collaboration configuration. The pull request template requests scope, verification, language alignment, AI-assistance disclosure, privacy checks, and reviewer notes. The issue forms separate bug reports, content suggestions, and translation improvements, while `config.yml` disables unstructured blank issues for contributors and links to contribution, support, security, and conduct guidance.
- `assets/`: policy and future home for original logos, banners, diagrams, screenshots, and repository preview images.
- `comments-and-documentation/`: learning path for comments, docstrings, naming, task markers, logging decisions, PEP 8, and readable code. The first chapter is available in `01-comments/`.
- `docs/`: roadmaps, project architecture, policies, and multilingual reference documents. The `ai-assisted-development/` directory explains responsible use of ChatGPT and Codex in the project workflow.
- `exercises/`: focused practice activities connected to learning chapters.
- `external-libraries/`: future guides to third-party packages installed separately.
- `functions/`: future learning path for function creation, parameters, arguments, return values, scope, type hints, and collaboration between functions.
- `fundamentals/`: future learning path for variables, data types, input, output, strings, numbers, collections, and control flow.
- `practical-projects/`: future small projects that combine multiple concepts.
- `standard-library/`: future guides to modules distributed with Python.
- `tests/`: automated tests for executable examples and projects as they are added.

## Naming and language conventions

Repository directories, file names, variables, functions, classes, and other code identifiers use English. Explanatory documents are offered in English, Brazilian Portuguese, and Spanish.

English is represented by the default `README.md` when the document is a primary GitHub entry point. Documents inside `docs/` may use the explicit `.en.md`, `.pt-BR.md`, and `.es.md` suffixes.

GitHub collaboration templates use English as the repository's default language and explicitly allow submissions in English, Brazilian Portuguese, or Spanish.

## Maintenance rule

A pull request that moves, creates, or removes significant paths should update this structure in the same change. Planned chapter directories should be added only when they contain useful material, rather than as empty placeholders.

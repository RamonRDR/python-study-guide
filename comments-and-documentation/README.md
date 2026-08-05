<div align="center">

# Comments, Documentation, and Readability

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

This section teaches how to make Python code easier to understand, explain, maintain, and observe. The sequence begins with comments and advances through docstrings, naming, task markers, logging decisions, and PEP 8 readability.

## Learning path

| Chapter | Main focus | Level | Status |
|---|---|---|---|
| [01. Comments](01-comments/README.md) | Explain decisions and non-obvious context without narrating the code | Beginner | Available |
| [02. Docstrings](02-docstrings/README.md) | Document modules, functions, classes, and methods | Beginner | Available |
| 03. Meaningful names | Make code express intention through clear names and small abstractions | Beginner | Planned |
| 04. Task markers | Use `TODO`, `FIXME`, `NOTE`, and related conventions responsibly | Beginner to intermediate | Planned |
| 05. Comments versus logging | Separate source-code explanation from runtime observation | Intermediate | Planned |
| 06. PEP 8 and readability | Apply style guidance while understanding its purpose and limits | Beginner to intermediate | Planned |

## Prerequisite guidance

- **01. Comments:** no formal prerequisite. Basic familiarity with variables and conditionals is helpful, but not required.
- **02. Docstrings:** basic familiarity with functions is recommended. The module, class, and method examples can also be understood conceptually before those topics are studied in depth.
- **03. Meaningful names:** basic knowledge of variables and functions is recommended.
- **04. Task markers:** the comments chapter is recommended. Familiarity with issues and version control is helpful.
- **05. Comments versus logging:** the comments chapter is recommended. Basic knowledge of program execution and exceptions will be helpful.
- **06. PEP 8 and readability:** basic Python syntax plus the comments and meaningful-names chapters are recommended.

Planned prerequisites may be refined when each chapter is written. Estimated study time is published only after a chapter has complete, reviewable content.

## Recommended sequence

Study the chapters in numerical order. Each chapter can also be consulted independently after its prerequisites are understood.

```text
01. Comments
        ↓
02. Docstrings
        ↓
03. Meaningful names
        ↓
04. Task markers
        ↓
05. Comments versus logging
        ↓
06. PEP 8 and readability
```

## Section goals

By the end of this learning path, you should be able to:

- distinguish comments, docstrings, documentation, type hints, and logs;
- explain decisions without repeating obvious code;
- choose names that reveal intention, units, state, and responsibility;
- record technical tasks with enough context to remain useful;
- decide when runtime information belongs in logging;
- apply PEP 8 recommendations with judgment instead of treating them as Python syntax;
- review code for clarity, accuracy, privacy, and maintainability.

## Current chapter

After studying [Comments in Python](01-comments/README.md), continue with [Docstrings in Python](02-docstrings/README.md). Both chapters include multilingual explanations, executable examples, an exercise, and a quick-reference summary.

## Directory structure

```text
comments-and-documentation/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-comments/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── business_rule_comments.py
│       ├── unnecessary_comments.py
│       └── useful_comments.py
└── 02-docstrings/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── class_docstrings.py
        ├── function_docstrings.py
        └── inspect_docstrings.py
```

Future chapter directories will be added when their complete content is prepared. Empty placeholders are intentionally avoided so that every tracked chapter directory contains useful material.

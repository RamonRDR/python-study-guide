<div align="center">

# Comments, Documentation, and Readability

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

This section teaches how to make Python code easier to understand, explain, maintain, and observe. It is the completed pilot learning section of the Python Study Guide.

## Learning path

| Chapter | Main focus | Level | Status |
|---|---|---|---|
| [01. Comments](01-comments/README.md) | Explain decisions and non-obvious context without narrating the code | Beginner | Available |
| [02. Docstrings](02-docstrings/README.md) | Document modules, functions, classes, and methods | Beginner | Available |
| [03. Meaningful names](03-meaningful-names/README.md) | Express intention through clear names and small abstractions | Beginner | Available |
| [04. Task markers](04-task-markers/README.md) | Use `TODO`, `FIXME`, `NOTE`, and related conventions responsibly | Beginner to intermediate | Available |
| [05. Comments versus logging](05-comments-vs-logging/README.md) | Separate source-code explanation from runtime observation | Intermediate | Available |
| [06. PEP 8 and readability](06-pep8-and-readability/README.md) | Apply style guidance while understanding its purpose and limits | Beginner to intermediate | Available |

## Prerequisite guidance

- **01. Comments:** no formal prerequisite. Basic familiarity with variables and conditionals is helpful, but not required.
- **02. Docstrings:** basic familiarity with functions is recommended. Module, class, and method examples can also be understood conceptually before those topics are studied in depth.
- **03. Meaningful names:** basic familiarity with variables and functions is recommended.
- **04. Task markers:** the comments chapter is recommended. Familiarity with issues and version control is helpful.
- **05. Comments versus logging:** the comments chapter is recommended. Basic knowledge of program execution and exceptions is helpful.
- **06. PEP 8 and readability:** basic Python syntax plus the comments and meaningful-names chapters are recommended.

Study the chapters in numerical order when following the complete path. Each chapter can also be consulted independently after its prerequisites are understood.

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
- apply PEP 8 recommendations with judgment instead of treating them as syntax;
- review code for clarity, accuracy, privacy, and maintainability.

## Current chapter

Complete the path with [PEP 8 and Readability in Python](06-pep8-and-readability/README.md). Every chapter includes multilingual explanations, executable examples, an exercise, a checklist, and a quick-reference summary.

## Directory structure

```text
comments-and-documentation/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-comments/
├── 02-docstrings/
├── 03-meaningful-names/
├── 04-task-markers/
├── 05-comments-vs-logging/
└── 06-pep8-and-readability/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── imports_and_names.py
        ├── readable_layout.py
        └── refactor_for_readability.py
```

<div align="center">

# Errors, Files, and Modules

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

This section begins the transition from small in-memory programs to programs that must cope with failures, persistent data, and code organized across files.

Phase 7 starts with exception handling, then moves into deliberately raising exceptions, working safely with files and structured text data, and finally organizing Python code with imports, modules, and packages.

## Learning path

| Chapter | Main focus | Level | Status |
|---|---|---|---|
| [01. `try`, `except`, `else`, and `finally`](01-try-except-else-finally/README.md) | Handle expected runtime failures while keeping normal and cleanup paths explicit | Beginner to intermediate | Available |
| 02. Raising and Custom Exceptions | Signal invalid states deliberately with `raise` and introduce simple custom exceptions | Intermediate | Planned |
| 03. `open()` and `with` | Read and write text files while managing resources safely | Beginner to intermediate | Planned |
| 04. TXT, CSV, and JSON | Work with common text-based data formats and their boundaries | Intermediate | Planned |
| 05. Imports, Modules, and Packages | Split code into reusable files and understand Python's import model | Intermediate | Planned |

## Prerequisite guidance

Before starting this phase, learners should be comfortable with:

- conditions and Boolean logic;
- loops;
- functions, parameters, and return values;
- basic type conversion;
- reading simple tracebacks conceptually;
- the difference between source-code comments and runtime behavior.

The complete beginner path through Phases 1–6 provides all of these foundations.

## Recommended sequence

Study the chapters in numerical order when following the complete curriculum:

```text
01. Handle exceptions
        ↓
02. Raise exceptions deliberately
        ↓
03. Open and manage files
        ↓
04. Read and write common data formats
        ↓
05. Organize code with modules and packages
```

The sequence is intentional. Before a program starts depending on files and multiple modules, it should have a clear model for what happens when an operation cannot complete normally.

## Section goals

By the end of Phase 7, you should be able to:

- distinguish normal control flow from exception-driven control flow;
- handle specific runtime exceptions without hiding unrelated failures;
- use `else` and `finally` deliberately;
- raise appropriate exceptions when a function cannot honor its contract;
- open, read, and write files using safe resource-management patterns;
- work with plain text, CSV, and JSON at a beginner-friendly level;
- separate parsing, validation, transformation, and persistence responsibilities;
- import code from modules and packages;
- explain how files, exceptions, functions, and modules connect in a small real program.

## Current chapter

Start with [Handling Exceptions with `try`, `except`, `else`, and `finally`](01-try-except-else-finally/README.md).

The first chapter focuses on **handling exceptions that already occur**. Creating exceptions deliberately with `raise` is reserved for Chapter 02 so the two responsibilities remain easy to distinguish.

## Directory structure

```text
errors-files-and-modules/
├── README.md
├── README.pt-BR.md
├── README.es.md
└── 01-try-except-else-finally/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── parse_integer.py
        ├── safe_divide.py
        └── trace_try_else_finally.py
```

Planned chapter directories are added only when their content is actually published.

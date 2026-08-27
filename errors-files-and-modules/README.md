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
| [02. Raising and Custom Exceptions](02-raise-and-custom-exceptions/README.md) | Signal invalid states deliberately with `raise`, re-raise or chain failures deliberately, and introduce simple custom exceptions | Intermediate | Available |
| [03. `open()` and `with`](03-open-and-with/README.md) | Open, read, write, and append text files while managing file resources safely with `with` | Beginner to intermediate | Available |
| [04. TXT, CSV, and JSON](04-txt-csv-and-json/README.md) | Parse, write, convert, and validate common text-based data formats with format-aware tools | Intermediate | Available |
| [05. Imports, Modules, and Packages](05-imports-modules-and-packages/README.md) | Split code into reusable files, organize regular packages, and understand Python's import and execution context | Intermediate | Available |

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

## Phase status

Phase 7 is complete. Finish the section with [Organizing Code with Imports, Modules, and Packages](05-imports-modules-and-packages/README.md).

Chapters 01–02 establish exception handling and deliberate exception signaling. Chapter 03 adds safe text-file lifetime and I/O. Chapter 04 adds TXT, CSV, and JSON data boundaries. Chapter 05 closes the phase with explicit imports, modules, regular packages, `__name__`, the main guard, search context, relative imports, `python -m`, and dependency design.

## Directory structure

```text
errors-files-and-modules/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-try-except-else-finally/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── parse_integer.py
│       ├── safe_divide.py
│       └── trace_try_else_finally.py
├── 02-raise-and-custom-exceptions/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── custom_exception.py
│       ├── exception_chaining.py
│       └── validate_score.py
├── 03-open-and-with/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── append_text.py
│       ├── handle_missing_file.py
│       └── write_and_read_text.py
├── 04-txt-csv-and-json/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── csv_records.py
│       ├── handle_invalid_json.py
│       ├── json_document.py
│       └── text_records.py
└── 05-imports-modules-and-packages/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── grade_tools.py
        ├── import_standard_library.py
        ├── main_guard.py
        ├── module_demo.py
        ├── package_demo.py
        └── study_tools/
            ├── __init__.py
            └── formatting.py
```

All five planned Phase 7 chapter directories are now published.

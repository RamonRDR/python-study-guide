<div align="center">

# Standard Library

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Python ships with a broad standard library. These modules solve common problems without requiring third-party installation, but each tool still has its own contracts, trade-offs, and failure modes.

Phase 8 builds on the import model from Phase 7 and studies a focused set of modules that appear frequently in real Python programs.

## Learning path

| Chapter | Main focus | Level | Status |
|---|---|---|---|
| [01. `pathlib`](01-pathlib/README.md) | Represent, compose, inspect, create, read, and discover filesystem paths with path-aware objects | Intermediate | Available |
| 02. `datetime` | Work with dates, times, durations, parsing, formatting, and arithmetic | Intermediate | Planned |
| 03. `json` | Use the `json` module beyond basic file persistence, including serialization options and stricter contracts | Intermediate | Planned |
| 04. `csv` | Work with CSV dialects, quoting, readers, writers, and tabular text boundaries | Intermediate | Planned |
| 05. `logging` | Configure loggers, handlers, formatters, levels, and application versus library logging | Intermediate | Planned |
| 06. `collections` | Use specialized containers such as `Counter`, `defaultdict`, and `deque` | Intermediate | Planned |
| 07. `itertools` | Build efficient iterator pipelines with reusable iteration tools | Intermediate | Planned |
| 08. `decimal` | Perform exact decimal arithmetic with explicit rounding and context | Intermediate | Planned |
| 09. `os` and `shutil` | Work with environment, low-level filesystem operations, copying, moving, and directory trees | Intermediate | Planned |

## Prerequisite guidance

Before starting this phase, learners should be comfortable with:

- functions and return values;
- collections and iteration;
- exceptions;
- files and context managers;
- imports, modules, and packages.

The complete path through Phases 1-7 provides those foundations.

## Recommended sequence

Study the chapters in order when following the complete curriculum:

```text
01. Model filesystem paths with pathlib
        ↓
02. Model dates and durations with datetime
        ↓
03. Deepen JSON handling
        ↓
04. Deepen CSV handling
        ↓
05. Configure runtime logging
        ↓
06. Use specialized collections
        ↓
07. Compose iterator pipelines
        ↓
08. Use exact decimal arithmetic
        ↓
09. Work with OS and filesystem utilities
```

The order is intentional. It starts from familiar file-oriented work, then moves through time, data formats, diagnostics, containers, iteration, numeric precision, and lower-level system utilities.

## Section goals

By the end of Phase 8, you should be able to:

- choose standard-library tools instead of reinventing common infrastructure;
- read official module documentation with more confidence;
- understand that a module name is not a complete usage contract;
- combine standard-library modules with functions, exceptions, files, and packages;
- recognize overlapping APIs and choose by intent;
- preserve deterministic behavior where order and environment can vary;
- write small programs that rely only on Python and its standard library.

## Phase status

Phase 8 is in progress. Chapter 01 introduces [`pathlib`](01-pathlib/README.md) as the first focused standard-library module.

Later chapters will revisit `json`, `csv`, and `logging` at a deeper library level. Their earlier appearances taught file formats or broader design concepts; this phase studies the modules themselves, their APIs, and their trade-offs.

## Directory structure

```text
standard-library/
├── README.md
├── README.pt-BR.md
├── README.es.md
└── 01-pathlib/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── discover_python_files.py
        ├── inspect_paths.py
        ├── path_parts.py
        └── text_workspace.py
```

New chapter directories will be added as the phase progresses.

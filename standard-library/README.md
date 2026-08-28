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
| [02. `datetime`](02-datetime/README.md) | Work with dates, times, durations, parsing, formatting, timezone awareness, and arithmetic | Intermediate | Available |
| [03. `json`](03-json/README.md) | Control serialization and decoding contracts, strict numeric behavior, hooks, custom values, duplicate names, and deterministic output | Intermediate | Available |
| [04. `csv`](04-csv/README.md) | Control dialects, quoting, escaping, row shape, sniffing, and tabular text contracts | Intermediate | Available |
| [05. `logging`](05-logging/README.md) | Engineer logger hierarchy, configuration, contextual records, queue-based delivery, concurrency, and runtime logging contracts | Intermediate | Available |
| [06. `collections`](06-collections/README.md) | Use specialized containers, mapping layers, tuple records, reordering tools, wrapper bases, and collection interfaces by explicit operation contracts | Intermediate | Available |
| [07. `itertools`](07-itertools/README.md) | Compose lazy iterator pipelines with explicit consumption, buffering, grouping, alignment, and combinatoric contracts | Intermediate | Available |
| [08. `decimal`](08-decimal/README.md) | Control decimal representation, precision, rounding, quantization, contexts, signals, and validation contracts | Intermediate | Available |
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

Phase 8 is in progress. Chapter 01 introduces [`pathlib`](01-pathlib/README.md), Chapter 02 adds [`datetime`](02-datetime/README.md), Chapter 03 deepens [`json`](03-json/README.md), Chapter 04 deepens [`csv`](04-csv/README.md), Chapter 05 deepens [`logging`](05-logging/README.md), Chapter 06 adds [`collections`](06-collections/README.md), Chapter 07 adds [`itertools`](07-itertools/README.md), and Chapter 08 adds [`decimal`](08-decimal/README.md) with exact decimal representation, explicit precision and rounding policies, quantization, contexts, signals, traps, and validation boundaries. The next planned chapter is `os` and `shutil`.

Chapters 03, 04, 05, 06, and 08 deepen topics that appeared earlier in the curriculum. Their earlier appearances taught file formats, logging design, built-in collection models, or binary floating-point behavior; this phase studies the standard-library modules themselves, their APIs, and their trade-offs.

## Directory structure

```text
standard-library/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-pathlib/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── discover_python_files.py
│       ├── inspect_paths.py
│       ├── path_parts.py
│       └── text_workspace.py
├── 02-datetime/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── date_arithmetic.py
│       ├── duration_seconds.py
│       ├── parse_and_format.py
│       └── utc_conversion.py
├── 03-json/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── decimal_decode.py
│       ├── deterministic_json.py
│       ├── reject_duplicate_keys.py
│       └── strict_numbers.py
├── 04-csv/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── dialect_round_trip.py
│       ├── quote_none_escape.py
│       ├── sniff_delimiter.py
│       └── validate_dict_rows.py
├── 05-logging/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── context_filter.py
│       ├── dict_config_routing.py
│       ├── queue_listener.py
│       └── stacklevel_helper.py
├── 06-collections/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── bounded_deque.py
│       ├── chainmap_config.py
│       ├── counter_inventory.py
│       └── defaultdict_grouping.py
├── 07-itertools/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── combinatoric_options.py
│       ├── groupby_runs.py
│       ├── lazy_pipeline.py
│       └── pairwise_deltas.py
└── 08-decimal/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── exact_amounts.py
        ├── local_context_precision.py
        ├── monitor_rounding.py
        └── validate_scale.py
```

New chapter directories will be added as the phase progresses.

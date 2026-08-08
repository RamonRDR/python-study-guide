<div align="center">

# Strings and Numbers

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

This section is Phase 2 of the main Python Study Guide learning sequence. It builds on Fundamentals by going deeper into Python text and numeric values before the guide introduces collections and program flow.

## Learning path

| Chapter | Main focus | Level | Status |
|---|---|---|---|
| [01. String creation and indexing](01-string-creation-and-indexing/README.md) | Create strings and read positions and ranges safely | Beginner | Available |
| [02. Common string methods](02-common-string-methods/README.md) | Transform, search, split, and join text | Beginner | Available |
| [03. `int`, `float`, and `bool`](03-int-float-and-bool/README.md) | Deepen integer, floating-point, and Boolean behavior | Beginner | Available |
| [04. Numeric built-ins](04-numeric-builtins/README.md) | Use `round()`, `abs()`, `min()`, `max()`, and `sum()` appropriately | Beginner | Available |

## Prerequisite guidance

- **01. String creation and indexing:** complete Phase 1 first. You should understand variables, `str`, `int`, `type()`, type conversion, and basic program execution.
- **02. Common string methods:** complete Chapter 01 first. You should understand string immutability, indexing, slicing, and the difference between the original string and a string result produced without mutating it.
- **03. `int`, `float`, and `bool`:** complete Chapter 02 first. Phase 1 already introduced these types; this chapter deepens numeric behavior, floating-point precision, and truth values.
- **04. Numeric built-ins:** complete the numeric-type chapter first so the helper functions are learned in context rather than as an isolated list.

Study the chapters in numerical order when following the complete path.

```text
01. String creation and indexing
        ↓
02. Common string methods
        ↓
03. int, float, and bool
        ↓
04. round(), abs(), min(), max(), and sum()
```

## Section goals

By the end of this learning path, you should be able to:

- create and inspect text values confidently;
- read string positions and ranges with indexing and slicing;
- use common string operations while respecting immutability;
- distinguish and use common numeric and logical value types;
- apply frequently used numeric built-ins appropriately;
- connect text input, type conversion, and numeric computation;
- recognize when a text or numeric operation produces a result value without mutating the original value.

## Section status

Phase 2 is complete. Its final chapter, [Numeric Built-ins](04-numeric-builtins/README.md), connects numeric behavior with `round()`, `abs()`, `min()`, `max()`, and `sum()`. The next curriculum phase is Collections.

## Directory structure

```text
strings-and-numbers/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-string-creation-and-indexing/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── fixed_position_text.py
│       └── string_basics.py
├── 02-common-string-methods/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── normalize_text.py
│       └── split_and_join.py
├── 03-int-float-and-bool/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── numeric_behavior.py
│       └── truth_and_precision.py
└── 04-numeric-builtins/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── numeric_summary.py
        └── rounding_behavior.py
```

The directory tree reflects the complete Phase 2 learning path. All four planned chapters are now available in English, Brazilian Portuguese, and Spanish.

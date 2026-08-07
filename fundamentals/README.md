<div align="center">

# Fundamentals

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

This section begins the main Python Study Guide learning sequence. It assumes no previous programming experience and builds the mental model needed to write, save, execute, inspect, and gradually expand Python programs.

## Learning path

| Chapter | Main focus | Level | Status |
|---|---|---|---|
| [01. How Python runs a program](01-how-python-runs-a-program/README.md) | Create, execute, modify, and correct a first Python file | Absolute beginner | Available |
| [02. `print()` and `input()`](02-print-and-input/README.md) | Display information and receive text from a user | Absolute beginner | Available |
| [03. Variables and naming](03-variables-and-naming/README.md) | Store values and choose understandable identifiers | Beginner | Available |
| [04. Built-in data types](04-built-in-data-types/README.md) | Recognize common value categories and their source notation | Beginner | Available |
| [05. `type()` and `isinstance()`](05-type-and-isinstance/README.md) | Inspect exact types and verify compatible type families | Beginner | Available |
| 06. Type conversion | Convert compatible values deliberately | Beginner | Planned |

## Prerequisite guidance

- **01. How Python runs a program:** no previous programming experience is required. Python must be installed, and the learner needs access to a plain-text or code editor and a terminal.
- **02. `print()` and `input()`:** complete Chapter 01 first. The learner should be able to create, save, and execute a `.py` file from the terminal.
- **03. Variables and naming:** complete Chapter 02 first. The learner should understand `print()`, `input()`, and why an input result must be stored before it can be reused.
- **04. Built-in data types:** complete Chapter 03 first. The learner should understand assignment, reassignment, and how variable names refer to values.
- **05. `type()` and `isinstance()`:** complete Chapter 04 first. The learner should recognize `str`, `int`, `float`, `bool`, and `None` values and understand that values have types.
- Later chapters build on the ability to store, display, recognize, and inspect values through clear names.

Study the chapters in numerical order when following the complete path.

```text
01. How Python runs a program
        ↓
02. print() and input()
        ↓
03. Variables and naming
        ↓
04. Built-in data types
        ↓
05. type() and isinstance()
        ↓
06. Type conversion
```

## Section goals

By the end of this learning path, you should be able to:

- create and execute Python source files;
- display information and receive basic user input;
- store values using meaningful variable names;
- recognize common built-in data types;
- inspect values with `type()` and `isinstance()`;
- convert compatible values between basic types;
- read simple output and basic error messages.

## Current chapter

Continue with [`type()` and `isinstance()`](05-type-and-isinstance/README.md). It explains exact type inspection, compatibility checks, tuples of accepted types, and the important relationship between `bool` and `int`.

## Directory structure

```text
fundamentals/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-how-python-runs-a-program/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       └── hello_world.py
├── 02-print-and-input/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── interactive_greeting.py
│       └── output_basics.py
├── 03-variables-and-naming/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── learning_profile.py
│       └── variable_basics.py
├── 04-built-in-data-types/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── same_looking_values.py
│       └── value_catalog.py
└── 05-type-and-isinstance/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── check_type_families.py
        └── inspect_types.py
```

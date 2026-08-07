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
| 03. Variables and naming | Store values and choose understandable identifiers | Beginner | Planned |
| 04. Built-in data types | Recognize Python's fundamental value categories | Beginner | Planned |
| 05. `type()` and `isinstance()` | Inspect and verify value types | Beginner | Planned |
| 06. Type conversion | Convert compatible values deliberately | Beginner | Planned |

## Prerequisite guidance

- **01. How Python runs a program:** no previous programming experience is required. Python must be installed, and the learner needs access to a plain-text or code editor and a terminal.
- **02. `print()` and `input()`:** complete Chapter 01 first. The learner should be able to create, save, and execute a `.py` file from the terminal.
- Later chapters build on the ability to display values, receive text, and rerun a program after each change.

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

Continue with [Output with `print()` and Input with `input()`](02-print-and-input/README.md). It explains program output, terminal input, function calls, prompts, multiple displayed values, `sep`, `end`, and the text returned by `input()`.

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
└── 02-print-and-input/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── interactive_greeting.py
        └── output_basics.py
```

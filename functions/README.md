<div align="center">

# Functions

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Full learning path](../docs/learning-path.en.md) · [Roadmap](../docs/roadmap.en.md)

Functions is Phase 5 of the main Python Study Guide learning sequence.

Program Flow taught how execution branches and repeats. This phase teaches how to **name behavior, pass data into behavior, return results, control scope, describe interfaces, and compose small pieces into clearer programs**.

## Prerequisite

Complete [Phase 4: Program Flow](../program-flow/README.md) first.

You should already be comfortable with:

- variables and built-in data types;
- strings, numbers, and collections;
- Boolean conditions;
- `if`, `elif`, and `else`;
- `match` and `case`;
- `for` and `while`;
- `range()`, `enumerate()`, and `zip()`;
- `break`, `continue`, and loop `else`;
- choosing and combining flow tools by intent.

## Learning path

| Chapter | Main focus | Status |
|---|---|---|
| [01. Defining and Calling Functions](01-defining-and-calling-functions/README.md) | Create named behavior with `def`, call it, reuse it, and trace execution | Available |
| [02. Parameters and Arguments](02-parameters-and-arguments/README.md) | Receive required input values through positional and basic keyword arguments | Available |
| 03. Return Values | Send useful results back to the caller | Planned |
| 04. Scope | Understand where names are visible and how lookup works | Planned |
| 05. Type Hints | Describe expected inputs and outputs without changing runtime behavior by themselves | Planned |
| 06. Default Values | Design optional arguments safely and clearly | Planned |
| 07. `*args` and `**kwargs` | Receive variable numbers of positional and keyword arguments | Planned |
| 08. Functions Working Together | Compose functions while keeping responsibilities clear | Planned |
| 09. Data Flow Between Functions | Trace inputs, transformations, outputs, and ownership across calls | Planned |

Study the chapters in order when following the complete beginner path.

## Why definition and calling come first

A function becomes much easier to understand when two ideas are stable first:

```text
definition = describe and name behavior
call       = execute that behavior now
```

Chapter 01 isolates those ideas before adding data exchange.

Chapter 02 adds required parameters, positional arguments, and basic keyword arguments so one function can work with different inputs. Chapter 03 will add return values. Later chapters will build scope, type hints, defaults, flexible argument collection, composition, and explicit data flow on top of the same definition/call model.

## Phase progression

```text
define and call
    ↓
parameters and arguments
    ↓
return values
    ↓
scope
    ↓
type hints
    ↓
default values
    ↓
*args and **kwargs
    ↓
functions working together
    ↓
data flow between functions
```

## Scope boundary

Phase 5 focuses on ordinary user-defined functions and the movement of execution and data around them.

It does not require:

- exception handling with `try` and `except`;
- file handling;
- modules and packages as a main topic;
- external libraries;
- decorators;
- generators;
- advanced functional-programming patterns.

Those concepts appear later or require dedicated treatment.

## Start here

Begin with [01. Defining and Calling Functions](01-defining-and-calling-functions/README.md), then continue with [02. Parameters and Arguments](02-parameters-and-arguments/README.md).

After Chapter 02, the next planned chapter is **03. Return Values**.

**Phase 5 is now in progress with two reviewed chapters available.**

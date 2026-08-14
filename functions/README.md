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
| [03. Return Values](03-return-values/README.md) | Send useful results back to the caller and trace complete input-to-output flow | Available |
| [04. Scope](04-scope/README.md) | Understand local and global names, lookup, shadowing, and explicit global rebinding | Available |
| [05. Type Hints](05-type-hints/README.md) | Describe expected inputs and outputs without enforcing types at runtime by themselves | Available |
| [06. Default Values](06-default-values/README.md) | Design optional arguments safely, including definition-time defaults and mutable-default safety | Available |
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

Chapter 02 adds required parameters, positional arguments, and basic keyword arguments so one function can work with different inputs. Chapter 03 completes the first data round trip with return values, `None`, branch-specific returns, and the distinction between returning and printing. Chapter 04 adds local and global scope, name lookup, shadowing, statement-level scope behavior, and cautious use of `global`. Chapter 05 adds parameter and return type hints, collection annotations, unions with `None`, and the distinction between static type information and runtime enforcement. Chapter 06 adds default values, selective overrides, definition-time evaluation, and the safe `None` pattern for fresh mutable objects. Later chapters build flexible argument collection, composition, and explicit data flow on top of the same model.

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
- advanced functional-programming patterns;
- advanced typing constructs such as generics, protocols, and overloads.

Those concepts appear later or require dedicated treatment.

## Start here

Begin with [01. Defining and Calling Functions](01-defining-and-calling-functions/README.md), continue with [02. Parameters and Arguments](02-parameters-and-arguments/README.md), then study [03. Return Values](03-return-values/README.md), [04. Scope](04-scope/README.md), [05. Type Hints](05-type-hints/README.md), and [06. Default Values](06-default-values/README.md).

After Chapter 06, the next planned chapter is **07. `*args` and `**kwargs`**.

**Phase 5 is now in progress with six reviewed chapters available.**

<div align="center">

# Program Flow

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Full learning path](../docs/learning-path.en.md) · [Roadmap](../docs/roadmap.en.md)

Program Flow is Phase 4 of the main Python Study Guide learning sequence.

Earlier phases taught how values are created, inspected, transformed, and organized. This phase teaches how those values influence **what runs, how many times it runs, when repetition stops, and how flow tools can be combined deliberately**.

## Prerequisite

Complete [Phase 3: Collections](../collections/README.md) first.

You should already be comfortable with:

- variables and built-in data types;
- strings and numeric expressions;
- Boolean values and basic comparisons;
- lists, tuples, dictionaries, and sets;
- `in` and `not in` as membership tests;
- choosing a collection according to the relationship between values.

## Learning path

| Chapter | Main focus | Status |
|---|---|---|
| [01. Conditions, Comparisons, and Boolean Logic](01-conditions-comparisons-and-boolean-logic/README.md) | Build trustworthy truth expressions before using them to control execution | Available |
| [02. `if`, `elif`, and `else`](02-if-elif-and-else/README.md) | Choose which block of code runs | Available |
| [03. `match` and `case`: Structural Pattern Matching](03-match-and-case/README.md) | Match values and data structures against patterns | Available |
| [04. `for` Loops and Iteration](04-for-loops-and-iteration/README.md) | Repeat work for items from an iterable | Available |
| [05. `range()`, `enumerate()`, and `zip()`](05-range-enumerate-and-zip/README.md) | Count, track positions, and coordinate iteration | Available |
| [06. `while` Loops and State-Driven Repetition](06-while-loops-and-state-driven-repetition/README.md) | Repeat while a condition remains truthy and state evolves | Available |
| [07. `break`, `continue`, and Loop `else`](07-break-continue-and-loop-else/README.md) | Stop early, skip one iteration, and distinguish normal loop completion from `break` | Available |
| [08. Choosing and Combining Program Flow](08-choosing-and-combining-program-flow/README.md) | Select and combine flow tools by intent | Available |

Study the chapters in order when following the complete beginner path.

## Why conditions come before `if`

A decision statement is only as clear as the condition that controls it.

This phase therefore starts by separating two ideas:

```text
condition = a question Python can interpret for truth
decision = what the program does because of that condition
```

Chapter 01 focuses on the first idea. Chapter 02 adds the second by using those conditions to select which block executes. Chapter 03 introduces structural pattern matching when the shape or pattern of a value is the important question. Chapter 04 shifts from selection to iterable-driven repetition. Chapter 05 adds helpers for numeric progressions, positions, and parallel iteration. Chapter 06 adds repetition controlled by changing state. Chapter 07 adds deliberate early exit, iteration skipping, and loop-completion handling. Chapter 08 closes the phase by choosing and combining all of those tools according to intent.

## Phase progression

```text
conditions
    ↓
decisions
    ↓
pattern matching
    ↓
for each item
    ↓
iteration helpers
    ↓
while a condition holds
    ↓
loop control
    ↓
choose and combine flow
```

## Scope boundary

Phase 4 teaches program flow without making later topics prerequisites.

It does not require:

- user-defined functions with `def`;
- exception handling with `try` and `except`;
- file handling;
- comprehensions as a shortcut for loops;
- external libraries.

Those concepts appear later in the roadmap.

## Start here

Begin with [01. Conditions, Comparisons, and Boolean Logic](01-conditions-comparisons-and-boolean-logic/README.md).

After Chapter 01, continue with [02. `if`, `elif`, and `else`](02-if-elif-and-else/README.md).

After Chapter 02, continue with [03. `match` and `case`: Structural Pattern Matching](03-match-and-case/README.md).

After Chapter 03, continue with [04. `for` Loops and Iteration](04-for-loops-and-iteration/README.md).

After Chapter 04, continue with [05. `range()`, `enumerate()`, and `zip()`](05-range-enumerate-and-zip/README.md).

After Chapter 05, continue with [06. `while` Loops and State-Driven Repetition](06-while-loops-and-state-driven-repetition/README.md).

After Chapter 06, continue with [07. `break`, `continue`, and Loop `else`](07-break-continue-and-loop-else/README.md).

After Chapter 07, finish the phase with [08. Choosing and Combining Program Flow](08-choosing-and-combining-program-flow/README.md).

**Phase 4 is complete with eight reviewed chapters.** The next planned learning phase is Phase 5: Functions.

# Specification-Driven Development

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../01-manual-coding-and-debugging/README.md) · [Module index](../README.md) · [Next →](../03-test-driven-development/README.md)
<!-- /chapter-navigation:top -->

## Goal

**Estimated time:** 40–60 minutes. Turn an ambiguous request into a small, testable contract before implementing it. Specification-driven development (SDD) is used here as a lightweight workflow, not a universal tool or mandatory document format. A specification describes observable behavior; implementation is one way to satisfy it.

## 1. From request to requirements

Fictional request: "Show how many pages remain in a book." Ask: what if the book has zero pages, all pages are read, or the input is invalid? For this exercise we choose the following contract explicitly, not because Python requires it.

| ID | Requirement |
| --- | --- |
| R1 | Function `remaining_pages(total_pages, pages_read)` returns an integer equal to total minus read. |
| R2 | Accept only integers, excluding bool; otherwise raise TypeError. |
| R3 | Both integers are nonnegative and pages_read cannot exceed total_pages; otherwise raise ValueError. |
| R4 | No input prompts, printing, files or network inside the function; the caller owns display. |

Out of scope: database, GUI, percentages, progress across books. Type errors take precedence over value errors when both occur. The contract accepts int subclasses except bool; no coercion of strings or floats.

## 2. Acceptance criteria

| ID | Input | Expected |
| --- | --- | --- |
| AC1 | (20, 7) | 13 |
| AC2 | (20, 0); (20, 20); (0, 0) | 20; 0; 0 |
| AC3 | (-1, 0); (20, -1); (20, 21) | ValueError |
| AC4 | ("20", 7); (20, 7.0); (True, 0); (20, False) | TypeError |
| AC5 | valid call | no output on stdout or stderr |

Acceptance criteria connect requirements to observable evidence. Tests can encode them; tests alone cannot establish every possible requirement.

## 3. Plan, tasks and decision record

Create a small `specification.md` in your own practice folder with the contract, examples and exclusions. Create `plan.md`: validate types, validate ranges, compute result, verify tests. Break it into tasks with completion checks. Do not code all tasks at once; use the next lesson's incremental tests.

An ADR (architecture decision record) records context, decision and consequences. Example: choose a pure function over an interactive script so the result can be reused and tested without terminal I/O. Trade-off: the caller must handle displaying or collecting data. Record this in `adr-0001.md`; larger projects may use a directory. ADRs record significant decisions, not every line of code.

## 4. Change control and independent practice

Suppose someone asks to accept a string "20". Do not silently change the implementation: clarify the need, update the contract and acceptance criteria, revise tests, implement and review. For now the contract rejects strings. Write your own specification for a different simple function, including normal, boundary and invalid cases; exchange it with someone or reread it as a reviewer. Can they implement it without guessing?

SDD answers **what and why**. TDD helps verify **how behavior is implemented** in small steps. Neither replaces understanding, design or human review. See the project's [specification](../../docs/specs/learning-hub-foundation/specification.md) and [ADR index](../../docs/adr/README.md) for a larger real example, not a required format for every small program.

**Quick reference:** request → clarify → requirements and exclusions → acceptance criteria → plan/tasks → decisions → tests and implementation → review.

<!-- chapter-navigation:bottom -->
[← Previous](../01-manual-coding-and-debugging/README.md) · [Module index](../README.md) · [Next →](../03-test-driven-development/README.md)
<!-- /chapter-navigation:bottom -->

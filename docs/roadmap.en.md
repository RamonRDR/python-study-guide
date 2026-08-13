# Python Study Guide Roadmap

[🇺🇸 English](roadmap.en.md) · [🇧🇷 Português](roadmap.pt-BR.md) · [🇪🇸 Español](roadmap.es.md)

This roadmap tracks both the educational curriculum and the repository foundation that supports it. Phase numbers describe the intended learning sequence, while repository work may prepare later sections earlier when doing so establishes useful standards.

## Status legend

- **Complete:** the planned scope is available and reviewed.
- **In progress:** useful material exists, but the planned scope is not finished.
- **Planned:** the phase has not started as a complete learning section.

## Current progress

| Phase | Status | Current result |
|---|---|---|
| 0. Project foundation | Complete | Foundation available, audited, and officially completed |
| 1. Fundamentals | Complete | Six reviewed chapters cover execution, input/output, variables and naming, built-in data types, type inspection, and type conversion |
| 2. Strings and numbers | Complete | Four reviewed chapters cover string creation, common methods, numeric and Boolean behavior, floating-point precision, and common numeric built-ins |
| 3. Collections | Complete | Six reviewed chapters cover lists, tuples, dictionaries, sets, and choosing a collection by intent |
| 4. Program flow | Complete | Eight reviewed chapters cover conditions, branching, structural pattern matching, `for`, iteration helpers, `while`, loop control, and choosing and combining flow tools by intent |
| 5. Functions | In progress | Five reviewed chapters cover `def`, calls, required inputs, returned values, scope, and type hints for function interfaces |
| 6. Comments, documentation, and clean code | Complete | Six reviewed chapters are available and the pilot educational section is officially complete |
| 7. Errors, files, and modules | Planned | Curriculum not started |
| 8. Standard library | Planned | Curriculum not started |
| 9. External libraries | Planned | Curriculum not started |
| 10. Practical projects | Planned | Curriculum not started |

Phases 0, 1, 2, 3, 4, and 6 are complete. Phase 5: Functions is in progress with definition, calling, input flow, return flow, scope, and type-hint interfaces now established; default values are next. Phase 6 continues to provide the editorial and quality model for later sections.

## Phase 0: Project foundation

### Completed

- [x] Multilingual root README files
- [x] Initial scalable project structure
- [x] Multilingual contribution guidelines
- [x] GitHub pull request and issue templates
- [x] Community standards and reporting guidance
- [x] Consistent editorial chapter format
- [x] MIT License
- [x] Project authorship and maintenance records
- [x] Pull-request-based workflow and protected `main` branch
- [x] Repository instructions for contributors and AI agents
- [x] Responsible AI-assisted development guide
- [x] Multilingual roadmap and project-structure documentation
- [x] Automated quality checks for Python files, approved examples, internal links, and repository structure
- [x] Original visual identity and repository assets
- [x] Final navigation, terminology, accessibility, and status audit
- [x] Officially mark Phase 0 as complete

### Planned non-blocking follow-up

- Refine and replace visual assets with high-quality exports after the final logo framing is complete.

## Phase 1: Fundamentals

- [x] [How Python runs a program](../fundamentals/01-how-python-runs-a-program/README.md)
- [x] [`print()` and `input()`](../fundamentals/02-print-and-input/README.md)
- [x] [Variables and naming](../fundamentals/03-variables-and-naming/README.md)
- [x] [Built-in data types](../fundamentals/04-built-in-data-types/README.md)
- [x] [`type()` and `isinstance()`](../fundamentals/05-type-and-isinstance/README.md)
- [x] [Type conversion](../fundamentals/06-type-conversion/README.md)

## Phase 2: Strings and numbers

- [x] [String creation and indexing](../strings-and-numbers/01-string-creation-and-indexing/README.md)
- [x] [Common string methods](../strings-and-numbers/02-common-string-methods/README.md)
- [x] [`int`, `float`, and `bool`](../strings-and-numbers/03-int-float-and-bool/README.md)
- [x] [Numeric built-ins: `round()`, `abs()`, `min()`, `max()`, and `sum()`](../strings-and-numbers/04-numeric-builtins/README.md)

## Phase 3: Collections

- [x] [List creation, indexing, and slicing](../collections/01-list-creation-and-indexing/README.md)
- [x] [Modifying lists and common list methods](../collections/02-modifying-lists-and-methods/README.md)
- [x] [Tuples and immutability](../collections/03-tuples-and-immutability/README.md)
- [x] [Dictionaries: keys and values](../collections/04-dictionaries-keys-and-values/README.md)
- [x] [Sets and unique values](../collections/05-sets-and-unique-values/README.md)
- [x] [Choosing the right collection](../collections/06-choosing-the-right-collection/README.md)

## Phase 4: Program flow

See the [section learning path](../program-flow/README.md).

- [x] [Conditions, comparisons, and Boolean logic](../program-flow/01-conditions-comparisons-and-boolean-logic/README.md)
- [x] [`if`, `elif`, and `else`](../program-flow/02-if-elif-and-else/README.md)
- [x] [`match` and `case`: structural pattern matching](../program-flow/03-match-and-case/README.md)
- [x] [`for` loops and iteration](../program-flow/04-for-loops-and-iteration/README.md)
- [x] [`range()`, `enumerate()`, and `zip()`](../program-flow/05-range-enumerate-and-zip/README.md)
- [x] [`while` loops and state-driven repetition](../program-flow/06-while-loops-and-state-driven-repetition/README.md)
- [x] [`break`, `continue`, and loop `else`](../program-flow/07-break-continue-and-loop-else/README.md)
- [x] [Choosing and combining program flow](../program-flow/08-choosing-and-combining-program-flow/README.md)

Phase 4 intentionally builds trustworthy conditions first, uses them for conditional branching, introduces structural pattern matching, moves into repetition with `for`, adds helpers for numeric progressions, positions, and parallel iteration, introduces state-driven repetition with `while`, adds deliberate loop control with `break`, `continue`, and loop `else`, and closes by teaching how to choose and combine those tools according to intent. Chapters 01–08 are complete and Phase 4 is officially complete.

## Phase 5: Functions

See the [section learning path](../functions/README.md).

- [x] [Defining and calling functions](../functions/01-defining-and-calling-functions/README.md)
- [x] [Parameters and arguments](../functions/02-parameters-and-arguments/README.md)
- [x] [Return values](../functions/03-return-values/README.md)
- [x] [Scope](../functions/04-scope/README.md)
- [x] [Type hints](../functions/05-type-hints/README.md)
- [ ] Default values
- [ ] `*args` and `**kwargs`
- [ ] Functions working together
- [ ] Data flow between functions

Phase 5 is in progress. Chapter 01 establishes `def`, calls, reuse, execution order, naming, `pass`, implicit `None`, and the connection with program flow. Chapter 02 adds required parameters, positional and basic keyword arguments, argument expressions, call errors, and input-flow tracing. Chapter 03 adds `return`, reusable results, branch-specific and early returns, `None`, and tuple returns. Chapter 04 adds local and global names, function-local namespaces, lookup, shadowing, `NameError`, `UnboundLocalError`, and cautious use of `global`. Chapter 05 adds parameter and return annotations, built-in and collection type hints, `-> None`, `str | None`, annotation metadata, and the distinction between static type information, runtime validation, and conversion. Default values are next.

## Phase 6: Comments, documentation, and clean code

See the [section learning path](../comments-and-documentation/README.md).

- [x] When and why to comment
- [x] When not to comment
- [x] Useful and harmful comments
- [x] Docstrings
- [x] Meaningful names and self-explanatory code
- [x] `TODO`, `FIXME`, `NOTE`, and related task markers
- [x] Comments versus logging
- [x] PEP 8 and readability

Phase 6 is officially complete and provides the editorial and quality model for the remaining learning sections.

## Phase 7: Errors, files, and modules

- `try`, `except`, `else`, and `finally`
- `raise` and custom exceptions
- `open()` and `with`
- TXT, CSV, and JSON
- Imports, modules, and packages

## Phase 8: Standard library

- `pathlib`
- `datetime`
- `json`
- `csv`
- `logging`
- `collections`
- `itertools`
- `decimal`
- `os` and `shutil`

## Phase 9: External libraries

- `pandas`
- `openpyxl`
- `requests`
- `pytest`

## Phase 10: Practical projects

- Grade calculator
- User registration
- Expense tracker
- CSV analyzer
- Report generator
- File organizer
- Fictional reconciliation workflow
- Simulated automation flow

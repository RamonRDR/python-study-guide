<div align="center">

# PEP 8 and Readability in Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: Comments versus logging](../05-comments-vs-logging/README.md)

PEP 8 is the style guide for Python code in the standard library and a widely used reference for Python projects. Its purpose is not to make every file visually identical. Its purpose is to improve readability and consistency so that readers spend less effort decoding presentation and more effort understanding behavior.

> **Guiding principle:** consistency supports readability, but project context and correctness come first.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner to intermediate |
| Prerequisites | Basic Python syntax; the comments and meaningful-names chapters are recommended |
| Estimated study time | 60 to 85 minutes |
| Main concepts | PEP 8, indentation, line length, imports, whitespace, naming, comparisons, exceptions, tools, project conventions |

## Learning objectives

By the end of this chapter, you should be able to:

- explain what PEP 8 is and what it is not;
- apply indentation, spacing, line-break, and blank-line conventions;
- organize imports and choose conventional names;
- write common comparisons and exception handling in readable forms;
- distinguish formatter, linter, type checker, and test responsibilities;
- follow project conventions without performing unrelated style rewrites;
- recognize when a deliberate exception is clearer or safer than strict conformity.

## 1. PEP 8 is guidance, not Python syntax

A program can be valid Python while ignoring many style recommendations. Conversely, beautifully formatted code can still contain incorrect logic.

PEP 8 focuses primarily on code layout, naming, comments, imports, and selected programming recommendations. A formatter or linter may enforce a project's chosen subset, but Python itself does not reject a function merely because two blank lines are missing.

Project-specific guidance takes precedence inside that project. Compatibility, correctness, and clarity are more important than cosmetic conformity.

## 2. Consistency has levels

A useful priority order is:

1. preserve correctness and compatibility;
2. follow the project's documented conventions;
3. remain consistent with the surrounding module;
4. use PEP 8 as the default when no stronger local rule exists.

Do not reformat an unrelated file merely because you noticed a style difference. Large cosmetic diffs hide behavioral changes and make review harder.

## 3. Use four spaces for each indentation level

Python uses indentation as syntax, so visual structure and program structure are connected. PEP 8 recommends four spaces per indentation level.

```python
def calculate_total(amount: float, tax_rate: float) -> float:
    tax_amount = amount * tax_rate
    return amount + tax_amount
```

Do not mix tabs and spaces. Configure the editor to insert spaces and display invisible characters when diagnosing indentation problems.

## 4. Wrap long expressions inside delimiters

Prefer implicit continuation inside parentheses, brackets, or braces:

```python
total = calculate_total(
    amount=1250.00,
    tax_rate=0.18,
)
```

Avoid backslashes for ordinary wrapping when delimiters make the structure clearer. Align continued lines so readers can distinguish arguments from the surrounding block.

## 5. Break before binary operators

For multi-line expressions, placing the operator before the continued operand keeps related operators and operands visually connected:

```python
total_amount = (
    subtotal
    - discount_amount
    + shipping_amount
)
```

Do not split an expression merely to satisfy a number. First consider a clearer name, an intermediate variable, or a smaller function.

## 6. Treat line length as a readability budget

PEP 8 recommends a maximum of 79 characters for code and 72 for flowing comments and docstrings. It also recognizes that teams may agree on longer limits, commonly up to 99 characters for code.

A line-length rule should reduce horizontal scanning and improve diffs. It should not produce a staircase of awkward fragments. URLs, generated text, long identifiers from external systems, and test data may require judgment.

## 7. Use blank lines to reveal structure

Use two blank lines around top-level functions and classes. Inside a class, separate methods with one blank line. Within a function, use blank lines sparingly to separate logical steps.

Too few blank lines turn code into a wall. Too many make closely related steps look disconnected.

## 8. Organize imports deliberately

Imports normally appear near the top of the file and are grouped as standard library, third-party packages, and local application imports, with a blank line between groups:

```python
import json
from pathlib import Path

import requests

from project.reports import build_report
```

Place one ordinary `import` per line. Avoid wildcard imports because they hide where names come from and complicate static analysis. Import placement may differ when optional dependencies, startup cost, or circular dependencies require a documented exception.

## 9. Whitespace should clarify, not decorate

Use spaces around assignment and comparison operators, after commas, and around binary operators. Avoid spaces immediately inside brackets or before a call's parentheses:

```python
result = calculate_total(amount, tax_rate=0.18)
coordinates = (10, 20)
mapping["account"] = account_code
```

Keyword arguments and unannotated default parameter values normally use no spaces around `=`, as in `tax_rate=0.18` and `def calculate(tax_rate=0.18):`. When a parameter annotation is combined with a default value, use spaces around `=`, as in `def calculate(tax_rate: float = 0.18):`.

## 10. Use conventional naming styles

Common conventions include:

- `snake_case` for functions, methods, and variables;
- `PascalCase` for classes and exceptions;
- `UPPER_SNAKE_CASE` for constants;
- a leading underscore for internal implementation details;
- `self` for the first instance-method parameter and `cls` for class methods.

```python
MAX_RETRY_COUNT = 3


class InvoiceProcessor:
    def process_invoice(self, invoice_id: str) -> None:
        is_ready = self._validate_invoice(invoice_id)
        if is_ready:
            self._save_invoice(invoice_id)
```

These conventions do not replace meaningful names. `processed_invoice_count` communicates more than a perfectly styled variable named `x`.

## 11. Write comparisons in idiomatic, explicit forms

Use identity checks for `None`, boolean values directly in conditions, and truth-value testing for empty containers when emptiness is the question:

```python
if result is None:
    handle_missing_result()

if is_active:
    start_worker()

if not records:
    return []
```

Use `isinstance()` when type checking is genuinely required. Do not use `is` to compare numbers or strings.

## 12. Prefer readable control flow

Guard clauses can keep the main path visible:

```python
def calculate_discount(customer: Customer) -> float:
    if not customer.is_eligible:
        return 0.0

    if customer.is_premium:
        return 0.15

    return 0.05
```

Deep nesting often signals that conditions, responsibilities, or names need refactoring. Do not flatten code mechanically if the resulting early returns obscure a required cleanup or transaction boundary.

## 13. Handle exceptions narrowly

Catch the exceptions you can meaningfully handle or translate:

```python
try:
    report = load_report(path)
except OSError as error:
    raise ReportLoadError(path) from error
```

Avoid a bare `except:` in ordinary application code because it also catches exceptions such as `KeyboardInterrupt` and `SystemExit`. Keep `try` blocks focused so readers can see which operation may fail.

## 14. Readability is larger than formatting

This code is compact but vague:

```python
def f(x):
    if x and len(x)>0:
        return sum(x)/len(x)
    return 0
```

A readable version reveals intention:

```python
def calculate_average(values: list[float]) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)
```

Formatting cannot repair an unclear abstraction, misleading name, hidden side effect, or oversized function. PEP 8 works together with design, comments, docstrings, tests, and type hints.

## 15. Formatters, linters, type checkers, and tests differ

A formatter rewrites presentation. A linter reports selected style problems and suspicious patterns. A type checker analyzes type contracts. Tests verify behavior chosen by the project.

Tools overlap, but none proves that code is correct or understandable. Configure them in versioned project files, run them in CI when appropriate, and avoid introducing a tool without documenting its scope and supported Python version.

## 16. Refactor style safely

Before a style-oriented refactor:

1. confirm whether behavior must remain unchanged;
2. keep the diff limited to the stated scope;
3. run tests before and after;
4. separate mechanical formatting from logic changes when practical;
5. preserve public names and interfaces unless the change is intentional;
6. review generated code, migrations, vendored code, and snapshots under their own rules.

A smaller diff is not merely prettier. It is easier to understand, review, revert, and trust.

## 17. Know when to deviate

A deliberate exception can be justified when strict conformity would reduce readability, break compatibility, conflict with an established project convention, or force unrelated churn.

When the reason is not obvious and will remain relevant, document it near the project configuration or code. Avoid personal style preferences that make one file behave differently from the rest of the project.

## 18. Examples in this repository

| File | Purpose |
|---|---|
| [`readable_layout.py`](examples/readable_layout.py) | Shows indentation, line wrapping, spacing, and a small entry point |
| [`imports_and_names.py`](examples/imports_and_names.py) | Demonstrates standard-library imports, constants, and descriptive names |
| [`refactor_for_readability.py`](examples/refactor_for_readability.py) | Replaces dense logic with focused, intention-revealing functions |

Run an example from the repository root:

```bash
python comments-and-documentation/06-pep8-and-readability/examples/readable_layout.py
```

## 19. Exercise

Refactor the following code without changing its result:

```python
def calc(x,y,z=False):
    if x!=None:
        if len(x)>0:
            r=sum(x)/len(x)
            if z==True:r=r-(r*y)
            return r
    return 0
```

Your revision should:

1. choose descriptive names;
2. use idiomatic `None`, boolean, and emptiness checks;
3. reduce unnecessary nesting;
4. add type hints that match the accepted inputs;
5. wrap lines clearly;
6. preserve the original behavior, including the empty-input result;
7. explain any deliberate deviation from the project's style rules.

## 20. Common mistakes

- treating PEP 8 as language syntax;
- reformatting unrelated code inside a behavioral PR;
- obeying line length while making expressions harder to read;
- using a formatter as a substitute for design;
- mixing tabs and spaces;
- grouping imports without considering optional or local constraints;
- renaming public interfaces only for cosmetic consistency;
- adding `# noqa` or similar suppressions without understanding the warning;
- assuming every Python project uses identical tool settings.

## 21. Review checklist

Before approving a readability change, verify:

- indentation and continuation are unambiguous;
- names reveal intention and follow project conventions;
- imports are understandable and minimally scoped;
- whitespace and blank lines expose structure;
- comparisons and exception handling express the intended semantics;
- comments explain decisions rather than formatting;
- no public interface changed accidentally;
- the diff contains no unrelated cleanup;
- automated tools and tests passed;
- any suppression or deviation has a durable reason.

## 22. Quick-reference summary

| Situation | Default |
|---|---|
| Indentation | Four spaces |
| Continuation | Parentheses, brackets, or braces |
| Code line length | 79 by PEP 8; project rules may differ |
| Top-level definitions | Two blank lines |
| Methods in a class | One blank line |
| Functions and variables | `snake_case` |
| Classes and exceptions | `PascalCase` |
| Constants | `UPPER_SNAKE_CASE` |
| Compare with `None` | `is None` / `is not None` |
| Empty container check | `if not items:` when emptiness is intended |
| Import order | Standard library, third party, local |
| Highest priority | Correctness, compatibility, and project consistency |

## 23. Run the repository checks

From the repository root:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

A clean formatter or linter result is useful evidence, not a replacement for human review.

## Official references

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python tutorial — Coding style](https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style)

[← Back to the section index](../README.md) · [← Previous chapter: Comments versus logging](../05-comments-vs-logging/README.md)

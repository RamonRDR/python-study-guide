<div align="center">

# Docstrings in Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: Comments](../01-comments/README.md)

A docstring explains the purpose and public use of a Python module, function, class, or method. Unlike an ordinary comment, a docstring is stored as documentation on the object and can be read by people, editors, documentation generators, `help()`, and introspection tools.

> **Guiding principle:** Write a docstring for the person who needs to use the object correctly without reading its entire implementation.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Basic familiarity with functions is recommended. The module, class, and method examples can be understood conceptually before those topics are studied in depth |
| Estimated study time | 45 to 65 minutes |
| Main concepts | docstring, `__doc__`, `help()`, `inspect.getdoc()`, modules, functions, classes, methods, parameters, return values, exceptions, PEP 257 |

## Learning objectives

By the end of this chapter, you should be able to:

- distinguish a docstring from a comment and an unused string literal;
- place docstrings correctly in modules, functions, classes, and methods;
- write useful one-line and multi-line docstrings;
- document behavior, parameters, return values, exceptions, side effects, and restrictions when relevant;
- access documentation through `__doc__`, `help()`, and `inspect.getdoc()`;
- understand the relationship between docstrings, type hints, README files, and external documentation;
- recognize that PEP 257 defines high-level conventions but does not impose one universal markup style;
- review docstrings for accuracy, clarity, privacy, and maintainability.

## 1. What a docstring is

A docstring is a string literal that appears as the first statement inside a module, function, class, or method definition.

```python
def greet(name):
    """Return a greeting for the provided name."""
    return f"Hello, {name}!"
```

Because the string is in the correct position, Python stores it in the function's `__doc__` attribute:

```python
print(greet.__doc__)
```

Output:

```text
Return a greeting for the provided name.
```

The same triple-quoted text in another position is only a string expression:

```python
def greet(name):
    result = f"Hello, {name}!"
    """This is not the function docstring."""
    return result
```

Here, `greet.__doc__` is `None` because the string is not the first statement.

### Triple quotes do not automatically create a docstring

Triple quotes create a string literal. Position gives that string its documentation role.

```python
message = """A regular multi-line string."""
```

This is a normal value assigned to `message`, not a docstring.

## 2. Why docstrings exist

A function signature and its implementation may show how code works, but users still need a stable explanation of how to call it safely.

Consider:

```python
def calculate_fee(amount, priority=False):
    ...
```

The signature does not fully answer:

- What does `amount` represent?
- Which unit or currency is expected?
- What changes when `priority` is `True`?
- What is returned?
- Can the function raise an exception?
- Does it modify external state?

A docstring can describe that public contract without forcing every user to inspect the implementation.

```python
def calculate_fee(amount_cents, priority=False):
    """Return the fictional service fee in cents.

    Args:
        amount_cents: Positive base amount expressed in cents.
        priority: Whether to apply the fictional priority rate.

    Returns:
        The calculated fee in cents.

    Raises:
        ValueError: If amount_cents is not positive.
    """
```

The code remains the source of executable behavior. The docstring is the human-readable map of the intended interface.

## 3. Correct placement

### Module docstrings

A module docstring normally appears near the beginning of a Python file, after a shebang or encoding declaration when either is present, and before imports.

```python
"""Utilities for the fictional reading-progress examples."""

from pathlib import Path
```

A module docstring can summarize the file's purpose and its main public objects.

### Function docstrings

A function docstring is the first statement after the function header.

```python
def convert_minutes_to_seconds(minutes):
    """Return the provided duration converted to seconds."""
    return minutes * 60
```

### Class docstrings

A class docstring describes the class's responsibility, important behavior, and public expectations.

```python
class ReadingProgress:
    """Track completed pages in a fictional reading session."""
```

### Method docstrings

A method docstring explains what the method does from the caller's perspective.

```python
class ReadingProgress:
    """Track completed pages in a fictional reading session."""

    def record_pages(self, pages):
        """Add completed pages without exceeding the total page count."""
```

The class docstring explains the object as a whole. Method docstrings explain individual operations.

## 4. One-line docstrings

Use a one-line docstring when the object's purpose is simple and can be stated accurately in one short sentence.

```python
def is_even(value):
    """Return whether value is an even integer."""
    return value % 2 == 0
```

Useful conventions from PEP 257 include:

- use triple double quotes even for one line;
- keep the opening and closing quotes on the same line;
- write a complete phrase ending with a period;
- describe the effect or result instead of repeating the signature.

Avoid:

```python
def is_even(value):
    """is_even(value) -> bool"""
```

The signature already exposes the parameter name, and type hints can expose expected types. The docstring should add meaning.

## 5. Multi-line docstrings

Use a multi-line docstring when users need more than a summary.

```python
def calculate_average(values):
    """Return the arithmetic mean of a non-empty sequence.

    Args:
        values: Numeric values included in the calculation.

    Returns:
        The arithmetic mean.

    Raises:
        ValueError: If values is empty.
    """
```

A practical structure is:

1. a short summary line;
2. a blank line;
3. additional explanation;
4. structured sections when the project uses them.

The summary should remain useful by itself because editors and documentation tools may display only that first line.

## 6. What belongs in a useful docstring

Not every function needs every possible section. Document what a caller must know.

### Purpose and behavior

State what the object offers.

```python
def normalize_identifier(raw_value):
    """Normalize a fictional identifier for display."""
```

### Parameters

Explain meaning, units, accepted forms, and important restrictions that names and type hints do not fully express.

```python
def schedule_retry(delay_seconds):
    """Schedule a retry after a non-negative delay.

    Args:
        delay_seconds: Waiting time in seconds. Zero schedules an immediate retry.
    """
```

### Return value

Explain the meaning of the returned value, especially when `None`, sentinel values, units, or multiple outcomes are possible.

```python
def find_label(code):
    """Return the matching label, or None when the code is unknown."""
```

### Exceptions

Document exceptions that are part of the public contract and that callers may reasonably handle.

```python
def load_percentage(text):
    """Convert text to a percentage from 0 through 100.

    Raises:
        ValueError: If text is not numeric or is outside the accepted range.
    """
```

Do not promise every internal exception that could possibly escape. Focus on intentional, relevant behavior.

### Side effects

Mention meaningful changes outside the return value.

```python
def save_report(path, content):
    """Write content to path, replacing an existing file."""
```

The replacement behavior matters even if the implementation is simple.

### Restrictions and assumptions

Document requirements that users cannot infer safely.

```python
def compare_snapshots(left, right):
    """Compare snapshots created with the same schema version."""
```

## 7. Docstrings for different objects

| Object | Typical documentation focus |
|---|---|
| Module | Purpose, main public objects, important usage or configuration notes |
| Function | Behavior, parameters, return value, exceptions, side effects, restrictions |
| Class | Responsibility, construction expectations, important state, public behavior |
| Method | Operation performed, state changes, result, exceptions |
| Property | Meaning of the exposed value and relevant constraints |
| Script | Purpose, command-line usage, inputs, outputs, environment, exit behavior when relevant |

Public objects usually need stronger documentation than small private helpers whose names and context are already clear. Project policy determines the exact threshold.

## 8. Docstrings, comments, type hints, and README files

These tools cooperate rather than compete.

```python
def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers."""
```

- The **name** communicates the main intention.
- The **type hints** describe expected data shapes.
- The **docstring** explains behavior and public expectations.
- A **comment** may explain a non-obvious implementation decision.
- A **README or guide** can teach a larger workflow involving several objects.

Do not duplicate the same sentence everywhere. Place each piece of information where its audience will naturally look for it.

## 9. Accessing docstrings at runtime

### `__doc__`

Objects with documentation expose it through `__doc__`.

```python
print(calculate_average.__doc__)
```

If no valid docstring is available, `__doc__` is commonly `None`.

### `help()`

The built-in help system uses available documentation and object metadata.

```python
help(calculate_average)
```

This is useful in an interactive Python session. Its complete presentation may vary with the environment.

### `inspect.getdoc()`

`inspect.getdoc()` retrieves and cleans documentation text.

```python
from inspect import getdoc

print(getdoc(calculate_average))
```

It removes common indentation and can retrieve inherited documentation for some object categories when no overriding docstring is provided.

## 10. Documentation styles and tools

Python defines what a docstring is, but it does not require one universal format for sections such as parameters and returns.

Common ecosystems include:

- plain PEP 257 prose;
- Google-style sections such as `Args`, `Returns`, and `Raises`;
- NumPy-style headings;
- reStructuredText fields used by tools such as Sphinx.

These are documentation conventions, not different Python syntaxes.

This guide uses a compact Google-style structure in larger examples because it is approachable for beginners. A real project should choose one style, document the choice, and apply it consistently.

### PEP 257 and formatting tools

PEP 257 describes high-level docstring semantics and conventions. Linters and documentation generators may add stricter project-specific rules. A tool warning should be understood in the context of that tool's configuration, not mistaken for a Python syntax error.

## 11. When a docstring is unnecessary or harmful

### Do not restate the name

```python
def add(a, b):
    """Add a and b."""
    return a + b
```

This may be acceptable in a deliberately tiny teaching example, but it provides little value in production documentation.

A better docstring would add a contract that is not obvious, or the function could remain undocumented if it is a private, trivial helper under the project's policy.

### Do not document false behavior

```python
def retry():
    """Retry the operation three times."""
    max_attempts = 5
```

An outdated docstring is a polished trap. Update documentation whenever behavior changes.

### Do not copy the implementation into prose

Avoid narrating every line. Document the interface and non-obvious guarantees.

### Do not expose private information

Docstrings are source code. They may appear in editors, generated websites, packages, logs, or public repositories.

Never include credentials, private URLs, personal data, confidential business rules, or proprietary internal details. Use original, fictional examples.

### Do not use a docstring to excuse an unclear interface

Better names, smaller functions, type hints, and a simpler design may solve the underlying problem before documentation is added.

## 12. Basic example

```python
def format_name(first_name, last_name):
    """Return a display name with surrounding whitespace removed."""
    return f"{first_name.strip()} {last_name.strip()}"
```

The docstring adds one useful guarantee: surrounding whitespace is removed. It does not narrate the f-string.

## 13. Practical example

```python
def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers.

    Args:
        values: Numbers included in the calculation.

    Returns:
        The arithmetic mean of the provided values.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)
```

The docstring communicates:

- the input must be non-empty;
- the result represents an arithmetic mean;
- callers can expect a `ValueError` for an empty sequence.

See the complete executable example in [`examples/function_docstrings.py`](examples/function_docstrings.py).

## 14. Common mistakes

### Placing the string after executable code

Only the first statement becomes the object's docstring.

### Confusing comments with docstrings

A comment is not available through normal object documentation:

```python
# Return the arithmetic mean.
def calculate_average(values):
    ...
```

### Repeating type hints without meaning

Weak:

```python
def load_items(limit: int) -> list[str]:
    """limit is an int and returns a list of strings."""
```

Better:

```python
def load_items(limit: int) -> list[str]:
    """Return at most limit fictional item labels in display order."""
```

### Documenting implementation details as permanent guarantees

Avoid promising a specific internal algorithm unless callers are allowed to depend on it.

### Using inconsistent styles in the same project

Consistency helps readers and documentation tools. Follow the repository's documented convention.

### Forgetting constructors and public methods

A well-documented class with unexplained construction requirements is still difficult to use.

## 15. Examples in this repository

| File | Purpose |
|---|---|
| [`function_docstrings.py`](examples/function_docstrings.py) | Shows module and function docstrings, parameters, returns, exceptions, and `__doc__` |
| [`class_docstrings.py`](examples/class_docstrings.py) | Shows class, constructor, and method docstrings |
| [`inspect_docstrings.py`](examples/inspect_docstrings.py) | Shows cleaned runtime access with `inspect.getdoc()` |

Run an example from the repository root:

```bash
python comments-and-documentation/02-docstrings/examples/function_docstrings.py
```

On systems where the command is named `python3`:

```bash
python3 comments-and-documentation/02-docstrings/examples/function_docstrings.py
```

## 16. Exercise

Review this function:

```python
def reserve_seats(available, requested):
    if requested <= 0:
        raise ValueError("requested must be positive")
    if requested > available:
        return False
    return True
```

Write a docstring that explains:

1. the function's purpose;
2. what `available` and `requested` represent;
3. what `True` and `False` mean;
4. when `ValueError` is raised;
5. no fictional rule beyond what the code actually guarantees.

One possible answer:

```python
def reserve_seats(available, requested):
    """Return whether the requested number of fictional seats is available.

    Args:
        available: Number of seats currently available.
        requested: Positive number of seats requested.

    Returns:
        True when all requested seats are available; otherwise False.

    Raises:
        ValueError: If requested is not positive.
    """
    if requested <= 0:
        raise ValueError("requested must be positive")
    if requested > available:
        return False
    return True
```

Several phrasings can be correct. Accuracy matters more than decorative detail.

## 17. Docstring review checklist

Before approving a docstring, ask:

- Is it in the correct position?
- Does the summary explain purpose or behavior?
- Is the documentation accurate for the current code?
- Are units, ranges, sentinel values, and important restrictions clear?
- Are relevant return values, exceptions, and side effects documented?
- Does it avoid repeating the signature and obvious implementation?
- Does it follow the project's selected style?
- Could a better name or simpler interface remove some explanation?
- Is any private, proprietary, personal, or identifiable information exposed?
- Would a user know how to call the object correctly without reading every line?

## 18. Quick-reference summary

| Situation | Preferred approach |
|---|---|
| Simple public function with an obvious contract | Use a concise one-line docstring |
| Behavior requires parameters, returns, or exceptions to be explained | Use a multi-line docstring |
| Information concerns an implementation decision | Use a comment |
| Information concerns expected types | Use type hints, with docstring clarification when meaning is still missing |
| A workflow spans several modules or setup steps | Use a README or guide |
| Documentation must be inspected interactively | Use `help()`, `__doc__`, or `inspect.getdoc()` |
| The docstring repeats the signature | Replace repetition with behavior and guarantees |
| The implementation changes | Review and update the docstring in the same change |
| A project uses Google, NumPy, or reStructuredText style | Follow the chosen project convention consistently |

## Official references

- [Python data model: `__doc__` attributes](https://docs.python.org/3/reference/datamodel.html)
- [Python built-in function: `help()`](https://docs.python.org/3/library/functions.html#help)
- [Python `inspect.getdoc()`](https://docs.python.org/3/library/inspect.html#inspect.getdoc)
- [PEP 257: Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 8: Documentation Strings](https://peps.python.org/pep-0008/#documentation-strings)

## Final principle

A useful docstring describes the contract a reader needs. It should reveal purpose and important guarantees without turning the implementation into a second, fragile copy written in prose.

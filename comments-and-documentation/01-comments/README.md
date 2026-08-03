<div align="center">

# Comments in Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section overview](../README.md)

Comments help readers understand decisions, constraints, and context that are not obvious from the code alone. They are valuable when they preserve reasoning. They become noise when they merely repeat what the code already says.

> **Guiding principle:** Code should explain what happens. Comments should explain why it happens when the reason is not obvious.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Basic familiarity with variables and conditionals is helpful, but not required |
| Estimated study time | 35 to 50 minutes |
| Main concepts | `#`, block comments, inline comments, useful context, outdated comments, `TODO`, `FIXME`, `NOTE` |

## Learning objectives

By the end of this chapter, you should be able to:

- recognize comment syntax in Python;
- distinguish comments from strings and docstrings;
- explain when a comment adds useful information;
- identify comments that only narrate obvious code;
- write comments for decisions, constraints, boundaries, and fictional business rules;
- use `TODO`, `FIXME`, and `NOTE` as clear project conventions;
- choose between a comment, a better name, a docstring, documentation, or logging;
- review comments for accuracy, clarity, privacy, and continued relevance.

## 1. What a comment is

A Python comment begins with a hash character (`#`) that is not inside a string literal and continues to the end of the physical line.

```python
# This entire line is a comment.
message = "Hello"  # This is an inline comment.
```

Comments are normally ignored by Python syntax and do not change the result of the program. Specially formatted comments can still be read by the source decoder or external tools, as explained below.

```python
score = 80
# score = 100
print(score)
```

Output:

```text
80
```

The commented assignment is not executed.

### A hash inside a string is not a comment

```python
label = "Ticket #42"
print(label)
```

The `#` character is part of the string because it appears between quotes.

### Special-purpose comments

A few comments follow conventions that give information to Python's source decoder, the operating system, or development tools. Examples include:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
value = load_value()  # type: ignore[assignment]
```

- A shebang on the first line may help Unix-like operating systems choose an interpreter when the file is executed directly.
- A valid encoding declaration on the first or second line tells Python how to decode the source file. Python 3 uses UTF-8 by default when no encoding declaration is present.
- Directives such as `# type: ignore`, `# noqa`, or formatter markers may be consumed by type checkers, linters, or formatters. Their exact behavior belongs to the relevant tool, not to ordinary comment execution.

Use tool directives only when they are necessary, narrow, and understandable. Explain or link to the reason when a suppression could hide a real problem.

## 2. Why comments exist

Code can express operations precisely, but it cannot always preserve the reason behind a decision.

Consider this condition:

```python
if days_before_event >= 14:
    apply_discount()
```

The code shows the rule, but it does not answer questions such as:

- Why is the boundary 14 days?
- Is the fourteenth day included intentionally?
- Is this a technical limitation or a fictional policy?
- Could the operator be changed from `>=` to `>` safely?

A useful comment can preserve that missing context:

```python
# The fictional policy includes the fourteenth day in the discount window.
if days_before_event >= 14:
    apply_discount()
```

The comment protects the reason behind the comparison. It helps prevent a future edit that looks harmless but changes the intended rule.

## 3. Syntax and forms

### Single-line comments

A comment may occupy a complete line:

```python
# Convert the temperature only after validating the selected scale.
temperature_celsius = convert_temperature(user_value)
```

PEP 8 recommends a space after `#` in ordinary prose comments.

```python
# Clear and conventional.
```

Avoid:

```python
#Harder to read.
```

### Inline comments

An inline comment appears on the same line as a statement:

```python
remaining_attempts -= 1  # The first attempt was already recorded.
```

PEP 8 recommends using inline comments sparingly, separating them from the statement with at least two spaces, and writing `# ` before the text.

Inline comments are most useful when a short reason belongs directly beside one statement. If the explanation is long, use a block comment above the relevant code instead.

### Block comments

A block comment consists of consecutive comment lines and usually explains the code that follows it.

```python
# The data source returns an empty value for days with no measurements.
# Treat that value as missing data instead of converting it to zero, because
# zero is a valid measurement in this fictional example.
measurement = read_measurement()
```

Keep the comment at the same indentation level as the code it describes:

```python
if measurement is None:
    # Missing measurements are reported separately from valid zero values.
    record_missing_measurement()
```

### Python has no dedicated multiline comment syntax

Python does not have a separate token such as `/* ... */` for multiline comments. Use multiple lines beginning with `#`:

```python
# This is a block comment.
# Each physical line begins with a hash.
```

Triple-quoted strings are string literals, not multiline comments:

```python
"""This is a string literal, not comment syntax."""
```

When a string literal is the first statement in a module, function, class, or method, it becomes a docstring and is available through `__doc__`. Docstrings are covered separately in this section of the guide.

## 4. When to use comments

### Explain a non-obvious reason

```python
# Retry once because the fictional simulator may need one cycle to become ready.
max_retries = 1
```

The assignment is simple. The reason for the limit is not.

### Preserve a fictional business rule

```python
# The fictional policy includes the registration date in the seven-day window.
if elapsed_days <= 7:
    allow_change = True
```

The comment explains the intended boundary. It does not claim that the rule belongs to a real organization.

### Document a technical constraint

```python
# Keep the file name in ASCII because the external teaching tool used in this
# example rejects non-ASCII paths.
output_name = "summary.txt"
```

The comment records a constraint that may not be visible from the assignment.

### Explain a workaround

```python
# Iterate over a copy because approved items are removed from the original.
for item in pending_items.copy():
    if is_approved(item):
        pending_items.remove(item)
```

A workaround comment should explain the risk being avoided. When possible, include a link to a public issue or documentation page that lets future maintainers verify whether the workaround is still needed.

### Clarify units or interpretation when a name cannot do enough

```python
poll_interval = 30  # Seconds required by the fictional simulator.
```

A better name may remove the need for the comment:

```python
poll_interval_seconds = 30
```

Prefer the clearer name unless the reason for the value still needs explanation.

## 5. When to avoid comments

### Do not narrate obvious code

```python
# Add one to the counter.
counter += 1
```

The comment repeats the operation without adding context.

A useful version would explain a reason that the code does not reveal:

```python
# Count the restored session as an attempt so retry limits remain consistent.
counter += 1
```

### Do not use comments to repair unclear names

Avoid:

```python
x = 14  # Number of days required for the early-registration discount.
```

Prefer:

```python
early_registration_days = 14
```

Use a comment only when the name still cannot explain the reason or boundary:

```python
early_registration_days = 14

# The fictional policy includes the fourteenth day in the discount window.
if days_before_event >= early_registration_days:
    apply_discount()
```

### Do not preserve disabled code without a reason

Avoid leaving large blocks of code commented out:

```python
# old_total = subtotal * 1.15
# print(old_total)
```

Version control already preserves previous implementations. Delete obsolete code unless there is a specific, temporary, and documented reason to keep it.

### Do not write comments that can become false silently

```python
# Retry three times.
max_retries = 5
```

The contradiction is more dangerous than having no comment. Update or remove comments whenever the related code changes.

### Never place secrets or private information in comments

Comments are stored in source files and may be committed, copied, indexed, or published.

Never include:

- passwords, tokens, API keys, or private URLs;
- personal or customer data;
- confidential rules or workflows;
- private employer, client, personal, or family project details;
- copied proprietary code or internal explanations.

Create original fictional examples from the ground up.

## 6. Comments and self-explanatory code

Comments are not the first solution to every readability problem.

Compare:

```python
# Check whether the user can access the event.
if a and not b and c:
    grant_access()
```

With clearer names:

```python
has_ticket = True
is_blocked = False
event_is_open = True

if has_ticket and not is_blocked and event_is_open:
    grant_access()
```

The second version reduces the need for explanation because the names expose the conditions.

A useful order of decisions is:

1. Can the code be simplified?
2. Can a name express the meaning?
3. Can a small function express the intention?
4. Is important reasoning still missing?
5. Add a comment for that remaining reasoning.

A comment should complement clear code, not excuse confusing code.

## 7. Comments, docstrings, documentation, and logging

These tools solve different problems.

| Tool | Main purpose | Typical audience | Available during execution? |
|---|---|---|---|
| Comment | Explain decisions or non-obvious context in source code | Maintainers and learners reading the source | Not through normal object documentation |
| Docstring | Describe the purpose and public use of a module, function, class, or method | Users of the code and maintainers | Yes, through `__doc__` and tools such as `help()` |
| README or guide | Explain installation, concepts, workflows, and broader usage | Learners, contributors, and users | Not part of program behavior |
| Logging | Record events, warnings, failures, and diagnostic context while a program runs | Operators, developers, and support teams | Yes |
| Type hint | Express expected types and support readers and analysis tools | Developers, learners, editors, and type checkers | Stored in annotations in many cases, but not enforced automatically by Python |

### Comment versus docstring

Use a comment to explain an implementation decision:

```python
# Preserve input order because the teaching report compares rows visually.
ordered_names = list(names)
```

Use a docstring to explain what a reusable function provides:

```python
def calculate_average(values):
    """Return the arithmetic mean of the provided values."""
```

### Comment versus logging

A comment cannot report what happened during a specific execution:

```python
# The file failed to open.
```

That sentence does not observe runtime behavior. Logging can record the event when it occurs:

```python
logger.error("Could not open the configuration file")
```

Do not replace runtime diagnostics with comments.

## 8. Basic example

Unnecessary comment:

```python
# Multiply the price by the quantity.
total = price * quantity
```

Better without the comment:

```python
total = price * quantity
```

Useful comment:

```python
# The fictional exercise stores prices in cents to keep all calculations in
# integers and avoid introducing decimal arithmetic in this beginner chapter.
total_cents = price_cents * quantity
```

The final comment explains a teaching and design decision, not the multiplication itself.

## 9. Practical example

```python
from datetime import date

EARLY_REGISTRATION_DAYS = 14
EARLY_DISCOUNT_PERCENT = 10


def calculate_registration_fee(
    base_fee_cents,
    event_date,
    registration_date,
):
    days_before_event = (event_date - registration_date).days

    # The fictional policy includes the fourteenth day in the discount window,
    # so this comparison must remain inclusive.
    if days_before_event >= EARLY_REGISTRATION_DAYS:
        discount_cents = base_fee_cents * EARLY_DISCOUNT_PERCENT // 100
        return base_fee_cents - discount_cents

    return base_fee_cents
```

The comment is useful because:

- the code already shows that `>=` is used;
- the comment explains why the equality case matters;
- the word *fictional* prevents the example from being mistaken for a real policy;
- a future maintainer knows that changing `>=` to `>` would alter the intended rule.

See the complete executable example in [`examples/business_rule_comments.py`](examples/business_rule_comments.py).

## 10. `TODO`, `FIXME`, and `NOTE`

Python does not assign built-in behavior to these labels. They are human and tooling conventions used by many projects.

### `TODO`

Use `TODO` for a specific improvement that remains to be completed.

Weak:

```python
# TODO: Improve this.
```

Better:

```python
# TODO: Replace the linear search after the catalog exceeds 10,000 items.
```

A strong `TODO` explains what must change and, when useful, the condition that makes it necessary. Projects may also include an issue number or owner according to their own policy.

### `FIXME`

Use `FIXME` for known incorrect, unsafe, or incomplete behavior that requires correction.

```python
# FIXME: Preserve leading zeros when postal codes are loaded from CSV.
```

A `FIXME` is not a substitute for reporting a serious defect. Follow the project's issue and security process when the impact requires it.

### `NOTE`

Use `NOTE` for important context that a maintainer could easily overlook.

```python
# NOTE: The sample data is intentionally unsorted for the ordering exercise.
```

Do not turn every observation into a `NOTE`. Reserve it for information that meaningfully affects understanding or maintenance.

## 11. Common mistakes

### Explaining what instead of why

```python
# Check whether the value is greater than zero.
if value > 0:
    process(value)
```

The condition already explains the operation.

### Writing a novel beside simple code

A long comment can hide a design problem. When the explanation becomes large, consider extracting a function, simplifying the code, or moving broader documentation to a guide.

### Referring to code by fragile position

Avoid:

```python
# The loop below changes the list used on line 42.
```

Line numbers and positions change. Refer to stable names and concepts instead.

### Using a comment as a task tracker with no context

```python
# TODO: Later.
```

This does not tell anyone what remains, why it matters, or how completion can be recognized.

### Commenting every line

Excessive comments force the reader to process two versions of the same logic. Comment only where the second voice contributes something the first voice cannot say clearly.

### Trusting a comment more than the code

The program executes the code, not the explanation. When they disagree, investigate the intended behavior, tests, and requirements before editing either one.

## 12. Examples in this repository

| File | Purpose |
|---|---|
| [`useful_comments.py`](examples/useful_comments.py) | Shows a comment that explains a non-obvious scheduling decision |
| [`unnecessary_comments.py`](examples/unnecessary_comments.py) | Compares line-by-line narration with clearer code |
| [`business_rule_comments.py`](examples/business_rule_comments.py) | Preserves the boundary of an original fictional rule |

Run an example from the repository root:

```bash
python comments-and-documentation/01-comments/examples/useful_comments.py
```

On systems where the command is named `python3`:

```bash
python3 comments-and-documentation/01-comments/examples/useful_comments.py
```

## 13. Exercise

Review this code:

```python
# Set the maximum number of attempts.
max_attempts = 3

# Set attempts to zero.
attempts = 0

# Loop while attempts is less than max attempts.
while attempts < max_attempts:
    # Print the attempt number.
    print(attempts + 1)

    # Add one to attempts.
    attempts += 1
```

Complete the following tasks:

1. Remove comments that only repeat the code.
2. Rename variables only if a clearer name is genuinely needed.
3. Add one useful fictional reason for the limit of three attempts.
4. Confirm that the revised code produces the same output.
5. Explain in your own words why your remaining comment adds information.

One possible revision:

```python
max_attempts = 3
attempts = 0

# The fictional practice terminal allows three tries before showing a hint.
while attempts < max_attempts:
    print(attempts + 1)
    attempts += 1
```

This is not the only valid answer. The important question is whether the comment preserves context that the code cannot express by itself.

## 14. Comment review checklist

Before keeping or adding a comment, ask:

- Is the information true?
- Does the code already say the same thing clearly?
- Could a better name or smaller function remove the need for the comment?
- Does the comment explain a reason, constraint, boundary, risk, or decision?
- Will a future change make this comment easy to forget or contradict?
- Is the language clear to the intended audience?
- Does it contain private, proprietary, personal, or identifying information?
- Can the explanation be verified through a public source or issue when needed?

## 15. Quick-reference summary

| Situation | Preferred approach |
|---|---|
| The code is unclear because names are vague | Improve the names first |
| A decision is not obvious from the code | Add a concise comment explaining why |
| A fictional rule has an important boundary | Comment the intended interpretation |
| A workaround depends on an external limitation | Explain the limitation and link to a public source when possible |
| A comment repeats the statement | Remove the comment |
| Old code is commented out | Delete it and rely on version control |
| A public function needs usage documentation | Write a docstring |
| Runtime behavior must be recorded | Use logging |
| Future work is specific and actionable | Use a clear `TODO` according to project policy |
| Known behavior is incorrect | Use `FIXME` and follow the project's defect process |
| Context is easy to overlook | Use `NOTE` sparingly |

## Official references

- [Python lexical analysis: comments](https://docs.python.org/3/reference/lexical_analysis.html#comments)
- [PEP 8: comments](https://peps.python.org/pep-0008/#comments)
- [PEP 257: docstring conventions](https://peps.python.org/pep-0257/)

## Final principle

A useful comment leaves the code easier to understand after the reader has processed both. If deleting the comment changes nothing about understanding, the code probably did not need it.

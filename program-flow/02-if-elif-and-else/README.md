<div align="center">

# `if`, `elif`, and `else`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Program Flow](../README.md) · [← Previous: Conditions, Comparisons, and Boolean Logic](../01-conditions-comparisons-and-boolean-logic/README.md)

Conditions answer questions. An `if` statement lets the program **do something because of the answer**.

The previous chapter built expressions such as `score >= 70`, `topic in topics`, and `has_access and is_active`. This chapter uses those expressions to choose which statements Python executes.

**Estimated study time:** 100–125 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain what conditional execution means;
- write a basic `if` statement;
- use a colon and indentation correctly;
- distinguish Python's indentation syntax from the PEP 8 recommendation of four spaces per level;
- explain what happens when an `if` condition is truthy or falsy;
- use `else` for a two-way decision;
- use one or more `elif` clauses for additional alternatives;
- explain why only the first truthy branch of one `if`/`elif` chain executes;
- order overlapping conditions deliberately;
- distinguish independent `if` statements from one mutually exclusive chain;
- combine `if` with `and`, `or`, `not`, membership tests, truthy collections, and `is None`;
- use modest nesting when a second decision only matters inside a first one;
- avoid leaving variables undefined because a branch did not run;
- recognize common beginner mistakes involving indentation, `=`, `==`, and branch ordering;
- prepare for repetition with `for` loops in the next chapter.

## 1. What conditional execution means

Until now, most examples have run from top to bottom with every statement being reached.

Conditional execution changes that pattern. Python evaluates a condition and uses its truth value to decide whether a block of statements should run.

The core idea is:

1. evaluate a condition;
2. if the condition is truthy, execute its indented block;
3. otherwise, skip that block;
4. continue with the code after the complete decision.

This is the first major point where your programs can follow different paths.

## 2. The basic `if` syntax

A basic `if` statement has a condition, a colon, and an indented block:

```python
if condition:
    statement
```

The word `if` starts the decision.

The expression after `if` is evaluated for truth. The colon `:` ends the clause header. The indented statements belong to the block controlled by that clause.

A real example:

```python
temperature = 24

if temperature >= 20:
    print("Comfortable temperature")
```

Output:

```text
Comfortable temperature
```

Because `temperature >= 20` is `True`, the indented `print()` runs.

## 3. The condition does not have to literally be `True` or `False`

Python uses truth-value testing for the expression after `if`.

This means both of these forms can control a decision:

```python
score = 82

if score >= 70:
    print("Passed")
```

and:

```python
topics = ["lists", "tuples"]

if topics:
    print("Topics available")
```

The first condition evaluates to the Boolean value `True`.

The second condition uses the truth value of a non-empty list. You learned that truth-value behavior in the previous chapter; `if` now gives it a practical purpose.

## 4. The colon is part of the syntax

Each `if`, `elif`, and `else` clause header ends with a colon.

Correct:

```python
age = 20

if age >= 18:
    print("Adult")
```

Missing the colon is a syntax error:

```python
age = 20

if age >= 18
    print("Adult")
```

The colon visually and syntactically separates the clause header from the block it controls.

## 5. Indentation defines the block

Python uses leading indentation to group statements into blocks.

```python
age = 20

if age >= 18:
    print("Adult")
    print("Access rule checked")

print("Done")
```

Output:

```text
Adult
Access rule checked
Done
```

Both indented `print()` calls belong to the `if` block.

The final `print("Done")` is no longer indented, so it is outside the block and runs after the decision.

## 6. Indentation is syntax; four spaces are a style recommendation

These are two related but different facts:

- Python uses indentation levels to determine how statements are grouped;
- PEP 8 recommends **four spaces per indentation level** for normal Python code.

This guide follows the PEP 8 recommendation:

```python
if age >= 18:
    print("Adult")
```

Do not remove the indentation:

```python
if age >= 18:
print("Adult")
```

And do not casually mix tabs and spaces. Python can reject inconsistent tab/space indentation with `TabError`.

For a beginner, the practical rule is simple: configure your editor to insert four spaces for each indentation level and stay consistent.

## 7. When the condition is truthy, the block runs

```python
score = 85

if score >= 70:
    print("Passed")

print("Result checked")
```

Output:

```text
Passed
Result checked
```

The condition is truthy, so Python enters the block. After the block finishes, execution continues with the following unindented statement.

## 8. When the condition is falsy, the block is skipped

```python
score = 50

if score >= 70:
    print("Passed")

print("Result checked")
```

Output:

```text
Result checked
```

The `print("Passed")` statement is skipped because `score >= 70` is false.

The program does not stop. It simply continues after the `if` block.

## 9. Use `if` when an action is optional

A standalone `if` is useful when something should happen only when one condition is satisfied, but nothing special is required otherwise.

```python
has_notification = True

if has_notification:
    print("New notification")

print("Application ready")
```

Output:

```text
New notification
Application ready
```

There is no requirement to add `else` to every `if` statement.

## 10. `else` creates a two-way decision

Use `else` when you need one block for the truthy case and another block for every remaining case.

```python
is_member = False

if is_member:
    print("Member price")
else:
    print("Standard price")
```

Output:

```text
Standard price
```

Exactly one of these two blocks runs.

## 11. `else` does not have a condition

The `else` clause means: **none of the earlier conditions in this chain selected a branch**.

Its syntax is therefore:

```python
if condition:
    statement_a
else:
    statement_b
```

Not:

```python
if condition:
    statement_a
else other_condition:
    statement_b
```

If you need another condition, use `elif`.

## 12. `elif` adds another condition to the same decision

`elif` is Python's spelling for another conditional branch in the same chain.

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Output:

```text
Result: Passed
```

Python checks the conditions from top to bottom.

`score >= 90` is false, so it continues to the `elif`. `score >= 70` is true, so that block runs and the rest of the chain is skipped.

## 13. A chain may contain zero or more `elif` clauses

The language grammar allows:

- one required `if` clause;
- zero or more `elif` clauses;
- an optional `else` clause.

A two-way decision needs no `elif`:

```python
if is_ready:
    print("Start")
else:
    print("Wait")
```

A multi-way decision can use several:

```python
level = 3

if level == 1:
    print("Beginner")
elif level == 2:
    print("Intermediate")
elif level == 3:
    print("Advanced")
else:
    print("Unknown level")
```

Output:

```text
Advanced
```

## 14. One `if`/`elif` chain selects at most one branch

This is one of the most important rules in the chapter.

Python evaluates conditions in order. As soon as one is truthy, Python executes that branch and skips the rest of the same chain.

```python
score = 95

if score >= 70:
    print("Passed")
elif score >= 90:
    print("Excellent")
```

Output:

```text
Passed
```

Both comparisons are mathematically true for `95`, but the second one is never reached because the first branch already won.

## 15. Condition order can change the result

When conditions overlap, order them deliberately.

A more specific threshold often needs to appear before a broader threshold:

```python
score = 95

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Passed")
else:
    print("Keep practicing")
```

Output:

```text
Excellent
```

This is not a Python rule that "larger numbers must come first." It is a design consequence of the first-truthy-branch rule.

Ask which conditions overlap, then order them according to the behavior you intend.

## 16. Later conditions in the same chain are not evaluated after a match

The language reference is stronger than saying later branches do not execute: after a branch is selected, later conditions in that `if` statement are not evaluated either.

```python
value = 10

if value > 0:
    print("Positive")
elif 10 / 0 > 1:
    print("Never reached")
```

Output:

```text
Positive
```

The division expression would fail if Python evaluated it. It is never reached because `value > 0` already selected the first branch.

This example demonstrates evaluation order, not a recommendation to hide unsafe expressions inside later branches.

## 17. Independent `if` statements are different

Two separate `if` statements represent two separate decisions.

```python
minutes = 50

if minutes >= 30:
    print("At least 30 minutes")

if minutes >= 45:
    print("At least 45 minutes")
```

Output:

```text
At least 30 minutes
At least 45 minutes
```

Both blocks can run because these are two independent statements.

## 18. Chain versus independent decisions

Compare the intent:

| Structure | Meaning |
|---|---|
| separate `if` statements | each condition is an independent question; multiple blocks may run |
| one `if`/`elif`/`else` chain | choose at most one branch from a set of alternatives |

Use independent `if` statements when several facts may all need actions.

Use an `if`/`elif` chain when the branches are alternatives within one decision.

Choosing the wrong structure can produce code that is syntactically valid but logically incorrect.

## 19. Combine conditions with `and`

The Boolean logic from Chapter 01 fits directly inside `if`.

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

Output:

```text
Entry allowed
```

The block runs only when both requirements are truthy.

## 20. Combine alternatives with `or`

```python
is_admin = False
is_editor = True

if is_admin or is_editor:
    print("Edit access")
```

Output:

```text
Edit access
```

Only one side needs to be truthy for the combined condition to be truthy.

Remember that `and` and `or` themselves return operands, but an `if` statement interprets the resulting value for truth.

## 21. Use `not` when the negative condition is clearer

```python
is_blocked = False

if not is_blocked:
    print("Account available")
```

Output:

```text
Account available
```

Prefer a condition that reads naturally. Too many layers of negation can make a decision harder to understand.

## 22. Membership tests make useful conditions

```python
topics = ["lists", "dictionaries", "sets"]

if "dictionaries" in topics:
    print("Dictionary topic found")
```

Output:

```text
Dictionary topic found
```

The same pattern works with `not in` when absence is the condition you care about.

## 23. Dictionary membership still checks keys by default

The rules from the Collections phase still apply inside an `if` statement.

```python
profile = {"name": "Ana", "level": "beginner"}

if "name" in profile:
    print("Name field exists")
```

Output:

```text
Name field exists
```

This checks whether `"name"` is a key. It does not search the dictionary values.

## 24. Truthy collections can simplify presence checks

An empty built-in collection is falsy; a non-empty one is truthy.

```python
tasks = ["review"]

if tasks:
    print("Tasks available")
```

Output:

```text
Tasks available
```

For a simple presence test, this is usually clearer than writing `if len(tasks) > 0:`.

The explicit `len()` form is not invalid. The truthy form is a common Python idiom when the actual length is not needed.

## 25. `not` works naturally with empty collections

```python
tasks = []

if not tasks:
    print("No tasks")
```

Output:

```text
No tasks
```

Because an empty list is falsy, `not tasks` becomes true.

## 26. Use identity checks for `None`

PEP 8 recommends comparing singleton values such as `None` with `is` or `is not`.

```python
next_topic = None

if next_topic is None:
    print("No next topic selected")
```

Output:

```text
No next topic selected
```

This is clearer and more precise than using `== None`.

## 27. Do not write `== True` when truth testing is the real intent

Suppose a name already represents whether something is active:

```python
is_active = True

if is_active:
    print("Active")
```

Output:

```text
Active
```

Writing `if is_active == True:` is usually unnecessary when you simply want Python to test the value for truth.

There are specialized situations where exact value or type comparisons matter, but they are not the normal beginner case for an `if` condition.

## 28. Nested `if` statements create decisions inside decisions

A block controlled by one `if` may contain another `if` statement.

```python
has_account = True
email_verified = True

if has_account:
    print("Account found")

    if email_verified:
        print("Email verified")
```

Output:

```text
Account found
Email verified
```

The second decision is reached only after the first condition is truthy.

## 29. Nest when the second question depends on reaching the first block

Nesting can communicate a dependency:

- first determine whether an account exists;
- only then evaluate something meaningful about that account.

But if two conditions simply form one joint requirement, `and` may be clearer:

```python
has_account = True
email_verified = True

if has_account and email_verified:
    print("Account ready")
```

Output:

```text
Account ready
```

Neither style is universally correct. Choose the structure that matches the relationship between the decisions.

## 30. Avoid deep nesting when a flatter decision is clearer

Several levels of nested `if` statements can become difficult to scan.

At this stage, prefer:

- clear Boolean expressions;
- a sensible `if`/`elif` chain;
- modest nesting only when it communicates real dependency.

Later phases will add functions and other techniques that can help organize larger decision logic.

## 31. Assigning names inside branches needs care

A branch may not run.

This code is unsafe:

```python
score = 50

if score >= 70:
    result = "Passed"

print(result)
```

Because the condition is false, `result` is never assigned. The later `print(result)` raises `NameError`.

One solution is to make sure every relevant path assigns the name:

```python
score = 50

if score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print(result)
```

Output:

```text
Keep practicing
```

## 32. An exhaustive chain can produce one value safely

When the final `else` handles every remaining case, a result name can be assigned in every branch.

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Output:

```text
Result: Passed
```

This pattern is useful when one decision chooses one value that later code needs.

## 33. Long conditions can use parentheses for readability

Parentheses allow an expression to continue across physical lines without a backslash.

```python
age = 22
has_ticket = True
is_blocked = False

if (
    age >= 18
    and has_ticket
    and not is_blocked
):
    print("Entry allowed")
```

Output:

```text
Entry allowed
```

The indentation of the body remains visually distinct from the lines that continue the condition.

Do not add parentheses just to make every condition look larger. Use them when they genuinely improve readability.

## 34. Prefer normal multi-line blocks in this guide

Python's grammar allows some simple suites on the same physical line as the header, but PEP 8 generally discourages compound one-line statements.

This guide prefers:

```python
if is_ready:
    print("Start")
```

rather than compressing the body onto the header line.

The multi-line form makes the block structure easier to see and leaves room for the decision to grow without becoming cramped.

## 35. When to use each form

Use a standalone `if` when:

- an action is optional;
- there is no special alternative action.

Use `if`/`else` when:

- exactly one of two paths should run.

Use `if`/`elif`/`else` when:

- you are choosing among several alternatives;
- the order of those alternatives is deliberate.

Use independent `if` statements when:

- more than one condition may need to trigger its own action.

Use modest nesting when:

- a later decision only makes sense after an earlier branch has been entered.

## 36. When to avoid adding more branches

An `if` statement is not automatically the best answer to every variation in data.

Be cautious when:

- a long chain is only mapping exact keys to exact values;
- several conditions repeat the same work;
- nesting becomes difficult to follow;
- the conditions describe data relationships that a dictionary or set could represent more directly.

You do not need to refactor every small decision. The goal is to notice when branch logic is describing behavior and when it is merely recreating a data structure.

## 37. Practical example: classify one study session

The following example combines `not`, `elif`, threshold ordering, and a final `else`:

```python
completed = True
minutes = 50

if not completed:
    status = "In progress"
elif minutes >= 60:
    status = "Completed: extended"
elif minutes >= 30:
    status = "Completed: focused"
else:
    status = "Completed: short"

print("Status:", status)
```

Output:

```text
Status: Completed: focused
```

The first branch handles unfinished sessions. Once completion is known, the remaining branches classify the duration from the more specific higher threshold to the broader lower threshold.

## 38. Approved example: `basic_if.py`

```python
temperature = 24

if temperature >= 20:
    print("Comfortable temperature")

print("Check complete")
```

Output:

```text
Comfortable temperature
Check complete
```

This example demonstrates the basic shape of `if` and shows that unindented code continues after the decision.

## 39. Approved example: `if_elif_else.py`

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Output:

```text
Result: Passed
```

This example demonstrates one mutually exclusive chain and deliberate threshold ordering.

## 40. Approved example: `independent_conditions.py`

```python
minutes = 50
completed = True

if completed:
    print("Session completed")

if minutes >= 30:
    print("At least 30 minutes")

if minutes >= 60:
    session_type = "Extended"
elif minutes >= 30:
    session_type = "Focused"
else:
    session_type = "Short"

print("Session type:", session_type)
```

Output:

```text
Session completed
At least 30 minutes
Session type: Focused
```

The first two `if` statements are independent, so both may run. The final chain chooses exactly one session type.

## 41. Common mistakes

### Mistake 1: forgetting the colon

Wrong:

```python
if score >= 70
    print("Passed")
```

Correct:

```python
if score >= 70:
    print("Passed")
```

### Mistake 2: removing the block indentation

Wrong:

```python
if score >= 70:
print("Passed")
```

Correct:

```python
if score >= 70:
    print("Passed")
```

### Mistake 3: using `=` instead of `==`

Wrong:

```python
if level = 2:
    print("Intermediate")
```

Correct:

```python
if level == 2:
    print("Intermediate")
```

Assignment and equality comparison are different operations.

### Mistake 4: expecting every truthy `elif` to run

A single `if`/`elif` chain stops after its first truthy branch.

Use separate `if` statements when multiple independent actions may be needed.

### Mistake 5: putting a broad overlapping condition first

```python
if score >= 70:
    print("Passed")
elif score >= 90:
    print("Excellent")
```

A score of `95` never reaches the second condition.

### Mistake 6: adding a condition after `else`

`else` has no condition. Use `elif` when another test is required.

### Mistake 7: assuming a name was assigned in a skipped branch

If later code needs a name, make sure the relevant execution paths assign it.

### Mistake 8: comparing every Boolean-looking name with `True`

Prefer:

```python
if is_ready:
    print("Ready")
```

when ordinary truth testing is the intent.

## 42. Exercise

Create a file named `study_decision.py`.

Start with:

```python
minutes = 42
completed = True
has_notes = False
```

Your program should:

1. print `"Session completed"` only when `completed` is truthy;
2. independently print `"Notes available"` only when `has_notes` is truthy;
3. create a `duration` name using one `if`/`elif`/`else` chain:
   - `"Long"` for 60 minutes or more;
   - `"Medium"` for 30 minutes or more;
   - `"Short"` otherwise;
4. print the final duration;
5. keep code identifiers and output text in English.

Expected output for the starting values:

```text
Session completed
Duration: Medium
```

Then change the three starting values and predict the output before running the program again.

## 43. Self-check

Without running this code first, predict its output:

```python
score = 92
has_bonus = True

if score >= 90 and has_bonus:
    print("Top result")
elif score >= 90:
    print("High score")
else:
    print("Standard result")

if has_bonus:
    print("Bonus recorded")
```

Answer:

```text
Top result
Bonus recorded
```

Why?

The first chain selects its first branch and skips the remaining branches in that chain. The final `if` is a separate decision, so it is evaluated independently.

## 44. Review checklist

Before moving on, make sure you can explain:

- [ ] what conditional execution means;
- [ ] the role of the condition, colon, and indented block in an `if` statement;
- [ ] why indentation is syntax while four spaces are a PEP 8 style recommendation;
- [ ] what happens when an `if` condition is falsy;
- [ ] when a standalone `if` is enough;
- [ ] how `else` creates the remaining path;
- [ ] how `elif` adds another tested alternative;
- [ ] why one `if`/`elif` chain selects at most one branch;
- [ ] why condition order matters when tests overlap;
- [ ] why later conditions in a matched chain are not evaluated;
- [ ] the difference between independent `if` statements and one chain;
- [ ] how `and`, `or`, `not`, membership, collection truthiness, and `is None` fit inside conditions;
- [ ] when modest nesting communicates a real dependency;
- [ ] why a name assigned only inside a skipped branch may remain undefined;
- [ ] why multi-line block formatting is preferred in this guide.

## 45. Quick reference

| Need | Typical form |
|---|---|
| Optional action | `if condition:` |
| Two alternatives | `if condition:` ... `else:` |
| Several alternatives | `if` ... `elif` ... `else` |
| Require both | `if condition_a and condition_b:` |
| Accept either | `if condition_a or condition_b:` |
| Negate a condition | `if not condition:` |
| Test membership | `if item in collection:` |
| Test absence | `if item not in collection:` |
| Test for `None` | `if value is None:` |
| Check a non-empty collection | `if collection:` |
| Check an empty collection | `if not collection:` |
| Multiple independent decisions | separate `if` statements |
| One exclusive decision | one `if`/`elif`/`else` chain |

Remember the progression:

**condition → choose a branch → execute its block → continue after the decision**

## Next step

The next chapter is **`for` Loops and Iteration**.

You now know how one condition can choose whether a block runs. Next, Python will learn to run a block repeatedly for items from strings, lists, tuples, dictionaries, sets, and other iterables.

## Official references

- [Python 3.13 language reference: Compound statements and the `if` statement](https://docs.python.org/3.13/reference/compound_stmts.html#if)
- [Python Tutorial: `if` Statements](https://docs.python.org/3.13/tutorial/controlflow.html#if-statements)
- [Python 3.13 language reference: Indentation](https://docs.python.org/3.13/reference/lexical_analysis.html#indentation)
- [PEP 8: Indentation and compound statements](https://peps.python.org/pep-0008/#indentation)

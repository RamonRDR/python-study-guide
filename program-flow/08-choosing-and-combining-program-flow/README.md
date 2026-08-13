<div align="center">

# Choosing and Combining Program Flow

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Program Flow](../README.md) · [← Previous: `break`, `continue`, and Loop `else`](../07-break-continue-and-loop-else/README.md)

Knowing each program-flow tool separately is only the beginning. Real programs usually need **selection and repetition to work together**.

This chapter closes Phase 4 by turning the previous tools into a decision system. The goal is not to use more syntax. The goal is to choose the **simplest control-flow structure that matches the real reason the program needs to branch or repeat**.

**Estimated study time:** 120–150 minutes.

**Python requirement:** Python 3.10 or later. This chapter combines `match` / `case` and `zip(..., strict=True)`, both introduced in Python 3.10.

## Learning goals

By the end of this chapter, you should be able to:

- choose `if`, `elif`, and `else` when Boolean conditions decide what runs;
- choose `match` when one subject is compared against clear patterns;
- choose `for` when items from an iterable drive repetition;
- choose `while` when changing state or a re-evaluated condition drives repetition;
- choose `range()`, `enumerate()`, and `zip()` according to the iteration need;
- use `break`, `continue`, and loop `else` only when they express a real control-flow requirement;
- combine decisions and loops without unnecessary nesting;
- distinguish mutually exclusive branches from independent conditions;
- prefer direct iteration over manual index management when the iterable is the real driver;
- trace combined flow one layer at a time;
- explain the intent of a control-flow structure in plain language;
- recognize when a larger flow should later be split into functions;
- review the complete Program Flow phase as one connected toolbox.

## 1. Start with the control question

Do not begin by asking:

> Which Python keyword can I use here?

Begin by asking:

> What determines the next step of this program?

That question usually points toward the right tool.

| Real question | First tool to consider |
|---|---|
| Should this block run? | `if` |
| Which one of several Boolean alternatives is true? | `if` / `elif` / `else` |
| Which pattern does one subject match? | `match` / `case` |
| What should happen for each item? | `for` |
| How many numeric steps should run? | `range()` with `for` |
| What is this item's position? | `enumerate()` |
| Which corresponding items belong together? | `zip()` |
| Should repetition continue while a condition remains true? | `while` |
| Is the result already known so the loop can stop? | `break` |
| Should this one iteration be skipped? | `continue` |
| Did the loop finish without `break`? | loop `else` |

This is a starting point, not a law. Several structures may be technically valid. Prefer the one whose shape explains the intent most clearly.

## 2. Choose by intent, not by habit

After learning a new feature, it is tempting to use it everywhere.

That reverses the design process.

Compare:

```text
Process each order in this list.
```

with:

```text
Keep trying while the balance is below the target.
```

The first naturally suggests `for`.

The second naturally suggests `while`.

A useful control-flow structure should make the program easier to describe.

## 3. Use `if` for Boolean rules

Use `if` when the important question can be expressed as a Boolean condition.

```python
temperature = 31

if temperature >= 30:
    print("Hot")
else:
    print("Mild")
```

`if` is especially natural for:

- ranges and inequalities;
- combined conditions with `and`, `or`, and `not`;
- membership tests;
- conditions involving several values.

Example:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

This is a Boolean-condition problem.

## 4. Mutually exclusive branches versus independent conditions

An `if` / `elif` / `else` chain represents alternatives where at most one branch should run.

```python
score = 82

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Ready")
else:
    print("Review")
```

Independent `if` statements ask independent questions:

```python
number = 12

if number > 0:
    print("Positive")

if number % 2 == 0:
    print("Even")
```

Both statements can run.

Ask:

> Can more than one answer be true at the same time?

If yes, independent `if` statements may be appropriate.

## 5. Order matters in `if` / `elif`

Consider:

```python
score = 95

if score >= 70:
    print("Ready")
elif score >= 90:
    print("Excellent")
```

`95` prints `"Ready"` because the first condition already succeeded.

A better order is:

```python
score = 95

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Ready")
```

When conditions overlap, put them in an order that preserves the intended categories.

## 6. Use `match` for patterns around one subject

`match` is useful when one subject is compared against several meaningful patterns.

```python
status = "running"

match status:
    case "queued":
        print("Waiting")
    case "running":
        print("Working")
    case "done":
        print("Finished")
    case _:
        print("Unknown")
```

The mental model is:

```text
Take this subject and determine which pattern it matches.
```

A wildcard fallback such as `case _:` normally belongs after the more specific patterns.

## 7. `match` does not replace `if`

This is naturally Boolean:

```python
amount = 125

if amount > 100:
    print("High amount")
```

This is naturally pattern-based:

```python
command = ["move", 3]

match command:
    case ["move", steps]:
        print(f"Move {steps} steps")
    case ["stop"]:
        print("Stop")
    case _:
        print("Unknown command")
```

Use `match` because patterns improve the model, not because the syntax is newer.

## 8. Use `for` when an iterable drives repetition

If the requirement says:

> For each item in this collection...

start by considering `for`.

```python
names = ["Ana", "Leo", "Mia"]

for name in names:
    print(name)
```

The iterable controls the repetition.

## 9. Prefer direct iteration over manual indexing

This is usually unnecessary:

```python
names = ["Ana", "Leo", "Mia"]
index = 0

while index < len(names):
    print(names[index])
    index += 1
```

The list itself is the real driver, so this is clearer:

```python
names = ["Ana", "Leo", "Mia"]

for name in names:
    print(name)
```

Use indices only when indices are actually part of the problem.

## 10. Use `while` when a condition or changing state drives repetition

```python
balance = 0
target = 100

while balance < target:
    balance += 25
    print(balance)
```

The program is saying:

```text
keep going while this condition remains true
```

That is the model `while` expresses.

## 11. `for` versus `while`

Ask what creates the next iteration.

| Repetition is controlled by... | Prefer considering... |
|---|---|
| items from an iterable | `for` |
| a numeric progression | `for` + `range()` |
| changing state or a condition | `while` |
| an indefinite process with a clear internal stop rule | deliberate `while True` + `break` |

Use the simplest truthful description.

## 12. Choose the iteration helper by the missing information

### `range()` for a numeric progression

```python
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
```

### `enumerate()` for item plus position

```python
tasks = ["read", "practice", "review"]

for position, task in enumerate(tasks, start=1):
    print(position, task)
```

### `zip()` for corresponding items

```python
names = ["Ana", "Leo"]
scores = [92, 81]

for name, score in zip(names, scores, strict=True):
    print(name, score)
```

The helpers answer different questions:

```text
range()      → which numeric progression?
enumerate()  → which item and which position?
zip()        → which corresponding items?
```

They support a `for` loop rather than replacing its iterable-driven model.

## 13. Use `zip(strict=True)` when equal length is a rule

By default, `zip()` stops when the shortest iterable is exhausted.

When equal lengths are an invariant of the data, use:

```python
for name, score in zip(names, scores, strict=True):
    print(name, score)
```

If one iterable is unexpectedly longer, `strict=True` raises an error instead of silently truncating the pairs.

If unequal lengths and truncation are intentional, ordinary `zip()` may be the correct choice.

## 14. Combine a loop with a decision when each item needs classification

A common structure is:

```text
for each item
    decide what this item means
```

Example:

```python
scores = [92, 67, 81, 45]

for score in scores:
    if score >= 90:
        label = "excellent"
    elif score >= 70:
        label = "ready"
    else:
        label = "review"

    print(f"{score}: {label}")
```

The outer structure answers **how repetition happens**.

The inner structure answers **what happens for this item**.

## 15. Build combined flow from the outside inward

Requirement:

> For every measurement, print only positive values.

First ask what repeats.

Answer:

```text
each measurement
```

So begin with `for`.

Then ask which measurements should be printed.

```python
measurements = [3, -1, 5, 0]

for measurement in measurements:
    if measurement > 0:
        print(measurement)
```

Choose the outer driver first, then add the decisions needed inside it.

## 16. Use `continue` when early skipping clarifies the main path

The same requirement can be written:

```python
measurements = [3, -1, 5, 0]

for measurement in measurements:
    if measurement <= 0:
        continue

    print(measurement)
```

This says:

```text
reject items that should not continue through the body
then keep the normal path less indented
```

Both versions are valid.

Use `continue` only when it improves readability.

## 17. Do not add `continue` when natural loop completion already says the same thing

This is unnecessary:

```python
for number in [1, 2, 3]:
    if number != 2:
        print(number)
        continue
```

The iteration would end naturally after `print()`.

A control statement should communicate a real change in flow.

## 18. Use `break` when more iterations cannot improve the answer

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for item in items:
    if item == target:
        print("Found")
        break
```

Once the first required match is found, examining later items would not change the answer.

That is a strong reason for `break`.

## 19. Use loop `else` when completion without `break` is meaningful

```python
items = ["pen", "book", "cable"]
target = "mug"

for item in items:
    if item == target:
        print("Found")
        break
else:
    print("Not found")
```

The loop `else` means:

```text
the loop completed without executing break
```

It does not mean that the last `if` condition was false.

## 20. A useful search pattern combines several tools cleanly

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for position, item in enumerate(items, start=1):
    if item == target:
        print(f"Found {target} at position {position}")
        break
else:
    print(f"{target} not found")
```

Each layer has one responsibility:

```text
enumerate() → expose position and item
for         → inspect items
if          → test for the target
break       → stop after the first match
else        → handle no-match completion
```

This is a healthy combination because the tools do not compete for the same job.

## 21. `while` combines naturally with decisions

```python
progress = 0

while progress < 3:
    progress += 1

    if progress == 2:
        print("Checkpoint")
    else:
        print("Progress", progress)
```

`while` decides whether another cycle exists.

`if` decides what happens during the current cycle.

## 22. `while` and `match` can model explicit states

```python
state = "queued"

while state != "done":
    match state:
        case "queued":
            print("Preparing")
            state = "running"
        case "running":
            print("Processing")
            state = "done"
        case _:
            print("Unknown state")
            break
```

The roles are distinct:

```text
while → continue until the workflow reaches its final state
match → choose the action for the current state
```

## 23. Keep `while` progress visible

The reader should be able to answer:

> What makes this loop move toward completion?

Prefer state updates that are easy to locate:

```python
attempt = 0

while attempt < 3:
    attempt += 1
    print(attempt)
```

Be cautious when the condition-driving state changes only inside some deeply nested branches.

## 24. Be careful with `continue` inside `while`

This can loop forever:

```python
count = 0

while count < 3:
    if count == 1:
        continue

    count += 1
```

When `count` becomes `1`, `continue` returns to the condition before `count` changes.

A safer shape is:

```python
count = 0

while count < 3:
    count += 1

    if count == 2:
        continue

    print(count)
```

The update happens before the possible `continue`.

The exact arrangement can vary, but every path must preserve progress.

## 25. Use `while True` only when the internal stop rule is clearer

A deliberate infinite condition can make sense when the real stop rule is inside the body:

```python
attempt = 0

while True:
    attempt += 1
    print(attempt)

    if attempt >= 3:
        break
```

But when the condition itself states the rule clearly:

```python
attempt = 0

while attempt < 3:
    attempt += 1
    print(attempt)
```

the direct condition is usually easier to understand.

Do not use `while True` as a default template.

## 26. Prefer one clear primary driver per loop

A useful readability guideline is:

> Each loop should have one main reason it continues.

For a `for` loop, that reason is usually:

```text
there is another item
```

For a `while` loop, it is usually:

```text
the condition is still true
```

`if`, `break`, and `continue` may refine the behavior, but the primary driver should remain visible.

This is a readability recommendation, not a Python syntax rule.

## 27. Flatten only when the flatter version is clearer

Nested conditions:

```python
values = [3, -1, 5, 0]

for value in values:
    if value > 0:
        if value % 2 == 1:
            print(value)
```

Combined condition:

```python
values = [3, -1, 5, 0]

for value in values:
    if value > 0 and value % 2 == 1:
        print(value)
```

Early skipping:

```python
values = [3, -1, 5, 0]

for value in values:
    if value <= 0:
        continue

    if value % 2 == 0:
        continue

    print(value)
```

All are possible.

Prefer the one that makes the successful path and the rejection rules easiest to explain.

## 28. Avoid overlapping helpers when one tool states the intent directly

This works:

```python
items = ["pen", "book", "mug"]

for index in range(len(items)):
    item = items[index]
    print(index, item)
```

But if the real need is position plus item:

```python
items = ["pen", "book", "mug"]

for index, item in enumerate(items):
    print(index, item)
```

the second version communicates the intention more directly.

## 29. Explain the flow in plain language before defending the syntax

Example:

```text
For each score:
    classify it into exactly one category;
    then print the score and category.
```

That maps naturally to:

```text
for
    if / elif / else
```

Another example:

```text
Keep processing while the workflow is not done.
For the current state, choose the matching action.
```

That maps naturally to:

```text
while
    match
```

If the plain-language explanation is confusing, the code may be doing too much.

## 30. Trace combined flow one layer at a time

Consider:

```python
values = [2, 5, 8]

for value in values:
    if value % 2 == 0:
        print(value)
```

Trace the outer loop first:

| Iteration | `value` |
|---|---:|
| 1 | 2 |
| 2 | 5 |
| 3 | 8 |

Then evaluate the inner condition:

| `value` | `value % 2 == 0` | Printed? |
|---:|---|---|
| 2 | `True` | yes |
| 5 | `False` | no |
| 8 | `True` | yes |

For a `while` loop, trace the state that controls the condition.

Layered tracing is easier than mentally executing every line at once.

## 31. Example 1: iterate and classify

File: [`examples/select_and_classify.py`](examples/select_and_classify.py)

```python
scores = [92, 67, 81, 45]

for score in scores:
    if score >= 90:
        label = "excellent"
    elif score >= 70:
        label = "ready"
    else:
        label = "review"

    print(f"{score}: {label}")
```

Output:

```text
92: excellent
67: review
81: ready
45: review
```

Why these tools?

- `for` because each score should be processed;
- `if` / `elif` / `else` because each score belongs to exactly one Boolean category.

## 32. Example 2: search with position and completion handling

File: [`examples/search_with_position.py`](examples/search_with_position.py)

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for position, item in enumerate(items, start=1):
    if item == target:
        print(f"Found {target} at position {position}")
        break
else:
    print(f"{target} not found")
```

Output:

```text
Found cable at position 3
```

Why these tools?

- `enumerate()` because both the item and human-friendly position matter;
- `for` because the iterable drives the search;
- `if` because equality decides whether the target was found;
- `break` because the first match is enough;
- loop `else` because exhaustion without `break` means "not found."

## 33. Example 3: state-driven workflow

File: [`examples/state_driven_workflow.py`](examples/state_driven_workflow.py)

```python
state = "queued"
processed_steps = 0

while state != "done":
    match state:
        case "queued":
            print("Preparing")
            state = "running"
        case "running":
            print("Processing")
            processed_steps += 1

            if processed_steps >= 2:
                state = "done"
        case _:
            print("Unknown state")
            break

print(f"Final state: {state}")
```

Output:

```text
Preparing
Processing
Processing
Final state: done
```

Why these tools?

- `while` because completion depends on evolving workflow state;
- `match` because one state selects one state-specific action;
- `if` because the running state has an additional threshold rule;
- `break` because an unknown state would invalidate the normal workflow.

## 34. Compare valid shapes before choosing

Requirement:

> Print positive values.

A direct form:

```python
values = [3, -1, 5]

for value in values:
    if value > 0:
        print(value)
```

An early-skip form:

```python
values = [3, -1, 5]

for value in values:
    if value <= 0:
        continue

    print(value)
```

A manual-index form:

```python
values = [3, -1, 5]
index = 0

while index < len(values):
    value = values[index]
    index += 1

    if value > 0:
        print(value)
```

All can produce the required output.

The first is usually clearest because:

- the collection drives repetition;
- the condition is simple;
- no early skip is needed;
- no manual index state is needed.

Correctness is necessary, but clarity still matters.

## 35. A decision recipe for program flow

When facing a new problem, ask:

1. **Selection or repetition?**
2. If selecting, is the rule **Boolean** or **pattern-based**?
3. If repeating, does the next cycle come from an **iterable** or a **condition**?
4. Does the `for` loop need `range()`, `enumerate()`, or `zip()`?
5. Does the normal loop path genuinely need `break` or `continue`?
6. Does completion without `break` have a meaningful result that loop `else` can express?

Do not choose every tool at once.

Build the structure from the requirement outward.

## 36. Common mistakes

### Choosing syntax before modeling the requirement

Weak:

```text
I need to use match somewhere.
```

Better:

```text
I have one value with several meaningful patterns.
match may fit this model.
```

### Traversing a normal collection with manual `while` indexing

If all you need is each item, `for` usually says that directly.

### Using `range(len(...))` when only items are needed

Do not manufacture indices automatically.

### Using `match` for ordered numeric ranges

Threshold logic is usually clearer with `if` / `elif`.

### Forgetting branch order

The first successful `elif` or matching `case` changes which later branches remain reachable.

### Hiding `while` progress

Verify that every path can move state toward termination.

### Adding too many `break` and `continue` statements

If the reader repeatedly asks where execution goes next, simplify the loop.

### Confusing loop `else` with `if` `else`

Indentation shows which statement owns the clause.

### Assuming fewer lines always means clearer code

Compactness and readability are not the same goal.

## 37. Exercise: design a combined flow

Given:

```python
events = ["ready", "skip", "running", "done", "running"]
```

Write a program that:

1. processes the events with `for`;
2. uses `enumerate(..., start=1)` for human-friendly positions;
3. uses `continue` when the event is `"skip"`;
4. uses `match` to distinguish `"ready"`, `"running"`, `"done"`, and unknown events;
5. prints the position and event for `"ready"` and `"running"`;
6. prints `Done at position X` and uses `break` for `"done"`;
7. uses loop `else` to print `No done event` only if the loop finishes without `"done"`.

Expected output:

```text
1: ready
3: running
Done at position 4
```

Before coding, write one sentence explaining the responsibility of each chosen tool.

## 38. Exercise review questions

After completing the exercise, answer:

- Why is `for` more natural than `while` for the outer repetition?
- Why is `enumerate()` more direct than `range(len(events))`?
- What does `continue` change for the `"skip"` event?
- Why does `break` suppress the loop `else`?
- Why is `match` reasonable for the event states?
- Could part of the logic be expressed with `if` instead?
- Which version would be easiest to explain to another beginner?

The last question matters. Readability is part of technical quality.

## 39. Review checklist

Before moving on, confirm that you can:

- [ ] explain the difference between selection and repetition;
- [ ] choose `if` for Boolean rules;
- [ ] choose `match` for patterns around one subject;
- [ ] distinguish mutually exclusive branches from independent conditions;
- [ ] choose `for` for iterable-driven repetition;
- [ ] choose `while` for state- or condition-driven repetition;
- [ ] choose `range()`, `enumerate()`, and `zip()` according to intent;
- [ ] decide when `zip(strict=True)` expresses an important invariant;
- [ ] use `break` only for a meaningful early exit;
- [ ] use `continue` only for a meaningful early end to the current iteration;
- [ ] explain loop `else` as completion without `break`;
- [ ] combine loops and decisions while keeping each responsibility clear;
- [ ] trace combined flow one layer at a time;
- [ ] identify the state that controls a `while` loop;
- [ ] recognize unnecessary manual indexing;
- [ ] recognize unnecessary nesting;
- [ ] explain a control-flow structure in plain language;
- [ ] recognize that larger flows will later benefit from functions.

## 40. Quick reference

| Need | Tool to consider | Main idea |
|---|---|---|
| Test one Boolean rule | `if` | run a block conditionally |
| Choose one ordered Boolean branch | `if` / `elif` / `else` | first true branch wins |
| Match one subject against patterns | `match` / `case` | first matching case wins |
| Process iterable items | `for` | iterable drives repetition |
| Generate integer progression | `range()` | produce arithmetic integer sequence |
| Process item plus position | `enumerate()` | pair positions with items |
| Process corresponding iterables | `zip()` | pair items by iteration position |
| Require equal-length zipped inputs | `zip(..., strict=True)` | make equal length an invariant |
| Repeat while state satisfies a rule | `while` | condition drives repetition |
| Stop the nearest loop now | `break` | early termination |
| Skip the rest of this iteration | `continue` | early iteration completion |
| Handle completion without `break` | loop `else` | no early break occurred |

## 41. The complete Phase 4 mental model

Program Flow now forms one connected progression:

```text
Build a trustworthy condition
        ↓
Choose a branch with if / elif / else
        ↓
Match structured alternatives with match / case
        ↓
Repeat for each iterable item with for
        ↓
Use range / enumerate / zip when iteration needs structure
        ↓
Repeat according to changing state with while
        ↓
Use break / continue / loop else when normal loop flow needs refinement
        ↓
Choose and combine only the tools that match the real requirement
```

The final step is not another syntax feature.

It is judgment.

## 42. Phase 4 completion and what comes next

By completing this chapter, you have finished the Program Flow phase of the Python Study Guide.

You can now reason about:

- conditions and Boolean logic;
- conditional branches;
- structural pattern matching;
- iterable-driven loops;
- numeric, position-aware, and parallel iteration helpers;
- state-driven loops;
- early termination and iteration skipping;
- normal loop completion;
- combinations of these tools.

This phase intentionally does not yet require:

- user-defined functions with `def`;
- parameters and return values;
- function scope;
- exception handling;
- file handling;
- comprehensions;
- modules and packages;
- external libraries.

As control flow grows, functions become the natural next tool because they let you **name and separate responsibilities**.

The next planned learning phase is **Phase 5: Functions**.

Return to the [full learning path](../../docs/learning-path.en.md) or the [roadmap](../../docs/roadmap.en.md) to continue when Phase 5 is published.

## References

Primary references used for this chapter:

- [Python 3.13 Tutorial: More Control Flow Tools](https://docs.python.org/3.13/tutorial/controlflow.html)
- [Python 3.13 Language Reference: Compound Statements](https://docs.python.org/3.13/reference/compound_stmts.html)
- [Python 3.13 Built-in Functions](https://docs.python.org/3.13/library/functions.html)
- [Python 3.13 Built-in Types: `range`](https://docs.python.org/3.13/library/stdtypes.html#ranges)

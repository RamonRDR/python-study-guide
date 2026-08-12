<div align="center">

# `while` Loops and State-Driven Repetition

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Program Flow](../README.md) · [← Previous: `range()`, `enumerate()`, and `zip()`](../05-range-enumerate-and-zip/README.md)

A `for` loop repeats work by consuming items from an iterable. A `while` loop answers a different question:

**Should this work happen again based on the program's current state?**

This chapter introduces repetition controlled by a condition that is tested again before every iteration.

**Estimated study time:** 105–130 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain what a `while` loop is and why it exists;
- write the basic `while condition:` syntax with correct indentation;
- explain that the condition is tested before every iteration;
- recognize that a `while` body may execute zero times;
- connect `while` conditions to truth-value testing from earlier chapters;
- describe the cycle of initial state, condition, body, state update, and re-evaluation;
- update state deliberately so a finite loop can make progress toward termination;
- use counters, accumulators, and thresholds with `while`;
- explain why a loop does not need to land exactly on a numeric boundary to stop;
- distinguish iterable-driven `for` loops from state-driven `while` loops;
- recognize common causes of infinite loops;
- inspect whether an update moves state toward or away from the stopping condition;
- understand that more than one variable can participate in the loop condition;
- recognize that mutating a collection can also change the state tested by a loop;
- understand what `while True` means without using it as a safe runnable example yet;
- keep `break`, `continue`, and loop `else` separate until the next chapter;
- choose `while` only when its state-driven model communicates the task more clearly than `for`.

## 1. Why `while` exists

The previous two chapters focused on repetition driven by iterables:

```python
for item in iterable:
    statement
```

That model is excellent when the program already has something to iterate over, such as a list, string, dictionary, `range`, `enumerate` object, or `zip` object.

But some tasks are not naturally described as “for each item.”

Instead, they sound like:

```text
while work remains, keep going
while a value is below a limit, keep updating it
while a condition remains true, repeat the block
```

That is the role of `while`.

## 2. The basic syntax

The basic form is:

```python
while condition:
    statement
```

The colon ends the `while` header, and the indented block is the loop body.

For example:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

Output:

```text
3
2
1
```

The loop keeps running while `remaining > 0` is true.

## 3. A `while` loop tests before it runs the body

A `while` loop is a **pre-test loop**: Python evaluates the condition before entering the body each time.

The flow is:

```text
test condition
    ↓
true  -> execute body -> test condition again
false -> leave the loop
```

This detail explains several important behaviors in the rest of the chapter.

## 4. The body may execute zero times

Because the condition is tested first, the body is skipped when the condition is already false.

```python
remaining = 0

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Done")
```

Output:

```text
Done
```

The loop itself performed zero iterations.

## 5. `while` uses truth-value testing

The condition does not have to be a value literally written as `True` or `False`.

Python tests the truth value of the expression, just as it does for an `if` condition.

This means the Boolean ideas from Chapter 01 still apply:

```python
attempts = 2

while attempts:
    print(attempts)
    attempts = attempts - 1
```

Because nonzero integers are truthy and zero is falsy, this prints:

```text
2
1
```

For beginner code, an explicit comparison such as `while attempts > 0:` is often easier to read because it states the intended rule directly.

## 6. The core mental model: state changes over time

A useful way to reason about a finite `while` loop is:

```text
1. establish initial state
2. test the condition
3. execute the body if the condition is true
4. update relevant state
5. return to the condition
6. stop when the condition becomes false
```

The important new idea is **state**: information whose current value affects whether another iteration should happen.

## 7. State is whatever the condition depends on

In this loop:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

`remaining` is loop state because the condition depends on it.

The state starts at `3`, then becomes `2`, `1`, and finally `0`.

When Python tests `remaining > 0` with `remaining == 0`, the condition is false and the loop ends.

## 8. A finite loop needs a path toward termination

If a loop is intended to finish normally, something must eventually make its condition false.

For the countdown:

```text
initial state: 3
condition:     remaining > 0
update:        remaining = remaining - 1
```

The update moves the state toward the point where the condition fails.

A practical question to ask while reading a `while` loop is:

**What changes, and how can that change eventually make the condition false?**

## 9. Counting upward with `while`

State can move upward too:

```python
number = 1

while number <= 3:
    print(number)
    number = number + 1
```

Output:

```text
1
2
3
```

The condition becomes false after `number` changes from `3` to `4`.

## 10. Counting downward with `while`

A countdown uses the opposite direction:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

Output:

```text
3
2
1
Start
```

The final `print()` is outside the loop because it should run only after repetition has finished.

## 11. Indentation decides what repeats

Compare these two shapes:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

and:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
    print("Still inside the loop")
```

Only statements indented under the `while` header belong to the loop body.

Indentation is therefore part of both Python syntax and program meaning.

## 12. Initialization belongs before the first test

The condition usually depends on state that must already exist:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

The assignment `remaining = 3` happens before Python reaches the first condition test.

A useful reading order is:

```text
initialize -> test -> work -> update -> test again
```

## 13. The update does not have to be the last statement

There is no Python rule saying the state update must be the final line in the body.

However, placing the important update where it is easy to see often improves readability:

```python
progress = 0

while progress < 3:
    progress = progress + 1
    print(f"Progress: {progress}")
```

The key requirement is semantic: the loop's state changes in a way that matches the intended condition and behavior.

## 14. Threshold-controlled repetition

A `while` loop is useful when repetition depends on reaching a changing threshold.

```python
studied_minutes = 0
session_minutes = 20
target_minutes = 60

while studied_minutes < target_minutes:
    studied_minutes = studied_minutes + session_minutes
    print(f"Study total: {studied_minutes} min")
```

Output:

```text
Study total: 20 min
Study total: 40 min
Study total: 60 min
```

The number of iterations follows from the changing state and the condition.

## 15. An accumulator can also control the loop

An accumulator stores a running result.

In the previous example, `studied_minutes` is both:

- an accumulator that stores the running total;
- state used by the `while` condition.

A variable can play more than one role when those roles describe the same evolving value clearly.

## 16. The state does not need to land exactly on the boundary

Consider:

```python
value = 1
limit = 20

while value < limit:
    print(value)
    value = value * 2

print(value)
```

Output:

```text
1
2
4
8
16
32
```

The loop stops because `32 < 20` is false on the next test.

Nothing requires the state to become exactly `20`.

The stopping rule is the truth value of the condition, not whether a boundary value was visited exactly.

## 17. The condition is re-evaluated with the current state

Python does not calculate the condition once and reuse that result forever.

Each pass returns to the header and evaluates the expression again using the current values.

For:

```python
value = 1

while value < 5:
    value = value * 2
```

Python effectively observes:

```text
1 < 5 -> True
2 < 5 -> True
4 < 5 -> True
8 < 5 -> False
```

That repeated re-evaluation is the engine of a `while` loop.

## 18. `for` and `while` solve different shapes of repetition

A useful first distinction is:

```text
for   -> repeat for items from an iterable
while -> repeat while a condition remains truthy
```

For example, when the task is simply to print the numbers `1`, `2`, and `3`, a `for` loop is often clearer:

```python
for number in range(1, 4):
    print(number)
```

A `while` version can work:

```python
number = 1

while number <= 3:
    print(number)
    number = number + 1
```

But it introduces manual state that `range()` could provide directly.

## 19. Prefer `for` when the iterable already expresses the task

If you already have a collection:

```python
topics = ["conditions", "loops", "functions"]
```

this is direct:

```python
for topic in topics:
    print(topic)
```

Rebuilding the same traversal manually with indexes and `while` would add state management without improving the meaning.

Use `while` because the continuation condition is the natural model, not merely because it can imitate `for`.

## 20. Prefer `while` when the next repetition depends on current state

A state-driven task may not know its useful iteration count in advance.

For example:

```python
value = 1
limit = 100

while value < limit:
    value = value * 2
```

The important idea is not “repeat exactly seven times.”

The important idea is “keep doubling while the value remains below the limit.”

That intent fits `while` naturally.

## 21. Infinite loop: forgetting to update the state

This loop never changes the value used by its condition:

```python
remaining = 3

while remaining > 0:
    print(remaining)
```

`remaining > 0` stays true forever.

If executed, the loop keeps printing `3` unless something outside normal loop completion interrupts the program.

This example is shown to explain the bug. It is intentionally not included in the repository's executable-example manifest.

## 22. Infinite loop: updating in the wrong direction

An update can exist and still move away from termination:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining + 1
```

The values become `3`, `4`, `5`, and so on, so `remaining > 0` does not become false.

Do not merely ask whether state changes. Ask whether it changes **toward a state that can stop the loop**.

## 23. Infinite loop: resetting state inside the body

A less obvious bug is repeatedly restoring the same state:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = 2
```

After the first pass, `remaining` stays at `2` forever.

Progress requires more than assignment. The sequence of states must support termination.

## 24. Conditions can combine several pieces of state

A `while` condition can use Boolean operators learned earlier:

```python
remaining = 5
energy = 3

while remaining > 0 and energy > 0:
    print(remaining, energy)
    remaining = remaining - 1
    energy = energy - 1
```

Output:

```text
5 3
4 2
3 1
```

The next test fails because `energy > 0` becomes false.

When several variables participate, inspect how each one changes and which part of the condition can end the loop.

## 25. Collections can be part of loop state

State is not limited to numbers.

A mutable collection can change in a way that affects a `while` condition:

```python
tasks = ["review", "practice", "recap"]

while tasks:
    current = tasks.pop()
    print(current)
```

Output:

```text
recap
practice
review
```

The list becomes shorter after each `pop()`. When it becomes empty, it is falsy and the loop ends.

This is valid, but direct `for` iteration is usually clearer when the goal is only to read every item without consuming or mutating the collection.

## 26. Mutation can be the state update

In the previous example there is no numeric counter.

The relevant update is:

```python
current = tasks.pop()
```

`pop()` mutates `tasks`, and that mutation changes the truth value tested by `while tasks:`.

The broader rule is:

**Find the state used by the condition, then find what changes that state.**

## 27. Explicit conditions can make intent easier to audit

Python allows truthy and falsy values directly:

```python
while tasks:
    ...
```

Sometimes an explicit condition communicates the business rule more precisely:

```python
while remaining_attempts > 0:
    ...
```

Neither style is universally required. Choose the form that makes the stopping rule easiest to understand.

## 28. Preview: what `while True` means

This syntax is valid Python:

```python
while True:
    statement
```

Because the literal condition `True` never becomes false on its own, the condition itself does not provide a normal stopping point.

Real programs often combine `while True` with another control-flow mechanism that exits the loop when a condition is met.

That mechanism is deliberately deferred to the next chapter, where `break`, `continue`, and loop `else` are taught together.

## 29. Why this chapter does not use `while True` in safe examples

A standalone `while True` loop is intentionally unbounded unless another mechanism exits it.

The repository's safe executable examples must finish deterministically, so this chapter does not register an unbounded `while True` example.

For now, remember only the meaning:

```text
while True -> keep repeating because the loop condition itself never becomes false
```

The next chapter shows how explicit loop-control statements interact with that pattern.

## 30. `break`, `continue`, and loop `else` are next

Python's complete loop syntax includes control-flow features that can change or interpret normal completion.

They are not prerequisites for understanding ordinary condition-driven `while` loops.

This chapter therefore keeps the model intentionally simple:

```text
condition true  -> run body
update state    -> test again
condition false -> loop ends
```

Chapter 07 adds the extra control paths.

## 31. A practical termination audit

Before running a new `while` loop, answer four questions:

1. What is the initial state?
2. What exact condition controls repetition?
3. What changes the state used by that condition?
4. Why can that change eventually make the condition false?

If the fourth answer is unclear, inspect the loop carefully before executing it.

This small audit catches many accidental infinite loops.

## 32. Common mistakes

### Mistake 1: forgetting the colon

Incorrect:

```python
while remaining > 0
    print(remaining)
```

The `while` header must end with `:`.

### Mistake 2: incorrect indentation

The repeated statements must be indented under the `while` header.

### Mistake 3: forgetting the state update

If the condition remains true and nothing relevant changes, the loop may never finish.

### Mistake 4: updating in the wrong direction

An update that moves state away from the stopping condition can also create an infinite loop.

### Mistake 5: assuming the body always runs once

The condition is tested first, so zero iterations are possible.

### Mistake 6: using `while` for straightforward collection traversal

When the task is simply “for each item,” direct `for` iteration is usually clearer.

### Mistake 7: assuming a threshold must be reached exactly

A loop ends when its condition becomes false. The state may cross a numeric boundary without ever equaling it.

## 33. Worked example: `countdown_state.py`

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

Output:

```text
3
2
1
Start
```

Repository example: [`examples/countdown_state.py`](examples/countdown_state.py)

## 34. Worked example: `study_target.py`

```python
studied_minutes = 0
session_minutes = 20
target_minutes = 60

while studied_minutes < target_minutes:
    studied_minutes = studied_minutes + session_minutes
    print(f"Study total: {studied_minutes} min")
```

Output:

```text
Study total: 20 min
Study total: 40 min
Study total: 60 min
```

Repository example: [`examples/study_target.py`](examples/study_target.py)

## 35. Worked example: `doubling_until_limit.py`

```python
value = 1
limit = 20

while value < limit:
    print(value)
    value = value * 2

print(f"Stopped at {value}")
```

Output:

```text
1
2
4
8
16
Stopped at 32
```

Repository example: [`examples/doubling_until_limit.py`](examples/doubling_until_limit.py)

## 36. Exercise

Create a small progress tracker with this initial state:

```python
completed = 0
target = 4
```

Your program should:

1. use a `while` loop whose condition compares `completed` with `target`;
2. print the next completed step on each iteration;
3. update `completed` so the loop makes progress toward termination;
4. after the loop, print `Target reached`.

Expected output:

```text
Completed: 1
Completed: 2
Completed: 3
Completed: 4
Target reached
```

Then answer these questions without running the program:

- What is the initial state?
- Which expression is re-evaluated before each iteration?
- Which statement changes the loop state?
- What value makes the condition false?
- Would the body run at all if `completed` started at `4`?

Do not use `break`, `continue`, loop `else`, or `while True` in this exercise.

## 37. Review checklist

Before moving on, confirm that you can explain each statement without running the code:

- [ ] `while` repeats a block while its condition is truthy.
- [ ] the condition is tested before every iteration.
- [ ] the body may execute zero times.
- [ ] loop state is information that affects whether repetition continues.
- [ ] a finite condition-driven loop needs a path toward making its condition false.
- [ ] state may increase, decrease, multiply, accumulate, or mutate in other deliberate ways.
- [ ] a numeric state does not have to equal a boundary exactly for the loop to stop.
- [ ] forgetting an update can create an infinite loop.
- [ ] updating in the wrong direction can also prevent termination.
- [ ] `for` is usually clearer for direct iterable traversal.
- [ ] `while` is useful when continuation depends naturally on current state.
- [ ] several variables can participate in the condition.
- [ ] a mutable collection can itself be part of the changing state.
- [ ] `while True` has a condition that never becomes false on its own.
- [ ] `break`, `continue`, and loop `else` are intentionally deferred to Chapter 07.

## 38. Quick reference

| Need | Typical form |
|---|---|
| Repeat while a comparison is true | `while value < limit:` |
| Count upward until a boundary | initialize, test, increment |
| Count downward until a boundary | initialize, test, decrement |
| Accumulate until a target | update accumulator inside `while accumulator < target:` |
| Repeat while a collection is non-empty | `while collection:` when consuming/mutating it is intentional |
| Traverse each item from an iterable | usually `for item in iterable` |
| Audit termination | identify initial state, condition, update, and path to false |
| Unbounded condition preview | `while True:`; loop-control details come next chapter |

Remember the progression:

**initial state → condition → body → state update → condition again → termination**

## Next step

The next chapter is **`break`, `continue`, and Loop `else`**.

You now know the normal condition-driven life cycle of a `while` loop. Next, the guide adds statements that can leave a loop early, skip directly to its next iteration, and distinguish normal completion from termination by `break`.

## Official references

- [Python 3.13 reference: The `while` statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-while-statement)
- [Python 3.13 built-in types: Truth Value Testing](https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing)
- [Python 3.13 tutorial: First Steps Towards Programming](https://docs.python.org/3.13/tutorial/introduction.html#first-steps-towards-programming)

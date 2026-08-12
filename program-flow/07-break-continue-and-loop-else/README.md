<div align="center">

# `break`, `continue`, and Loop `else`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Program Flow](../README.md) · [← Previous: `while` Loops and State-Driven Repetition](../06-while-loops-and-state-driven-repetition/README.md)

Loops normally follow their natural repetition rule: a `for` loop consumes its iterable, and a `while` loop keeps running while its condition remains truthy. Sometimes a program needs to **stop early, skip the rest of one iteration, or distinguish normal completion from an early exit**.

This chapter introduces the three tools Python provides for those situations: `break`, `continue`, and the optional `else` clause on loops.

**Estimated study time:** 110–135 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain what normal loop completion means for both `for` and `while`;
- use `break` to terminate the nearest enclosing loop early;
- recognize that code after `break` in the same iteration does not run;
- use `continue` to skip the remaining statements of the current iteration;
- explain the different next step after `continue` in `for` and `while`;
- update `while` state safely when `continue` is possible;
- use `while True` deliberately when `break` expresses the real stopping rule more clearly;
- explain that loop `else` belongs to the loop, not to an inner `if`;
- predict when loop `else` runs and when a `break` suppresses it;
- use `for ... else` for searches where `break` means a match was found;
- use `while ... else` when normal condition failure has a meaningful completion path;
- recognize that an empty `for` loop and an initially false `while` condition can still reach loop `else`;
- explain that `break` affects only the nearest enclosing loop in nested loops;
- choose between `break`, `continue`, loop `else`, and ordinary conditions according to intent;
- avoid unnecessary control-flow jumps that make a loop harder to read.

## 1. Start from normal loop completion

Before changing a loop, define what would happen without any special control statement.

A `for` loop normally ends when its iterator is exhausted:

```python
for number in [1, 2, 3]:
    print(number)
```

A `while` loop normally ends when its condition becomes false:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

`break`, `continue`, and loop `else` only make sense when you understand that normal path first.

## 2. What `break` does

`break` terminates the nearest enclosing `for` or `while` loop immediately.

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

Output:

```text
1
2
```

When `number` becomes `3`, the loop stops before `print(number)` can run for that iteration.

## 3. `break` exits the loop, not just the `if`

Consider:

```python
for item in ["pen", "book", "mug"]:
    if item == "book":
        break
    print(item)

print("Done")
```

Output:

```text
pen
Done
```

The `if` decides whether `break` executes. The `break` itself transfers control outside the loop.

## 4. Code after `break` in the same loop body is skipped

This code never prints `"After break"`:

```python
for number in [1, 2, 3]:
    if number == 2:
        break
        print("After break")
```

Once `break` executes, control leaves the loop immediately.

Unreachable statements after an unconditional `break` should not be left in real code.

## 5. `break` is useful when the answer is already known

Suppose you are searching for one target:

```python
codes = ["PEN", "BOOK", "MUG", "CABLE"]
target = "MUG"

for code in codes:
    if code == target:
        print("Found")
        break
```

After the target is found, examining later items would not change the answer.

## 6. A search can stop at the first match

If duplicates are possible but only the first match matters, `break` communicates that policy directly:

```python
values = [4, 7, 7, 9]

for value in values:
    if value == 7:
        print("First match found")
        break
```

The second `7` is never examined by the loop body.

## 7. Do not use `break` when every item must be processed

This is a poor fit if the task must inspect all values:

```python
scores = [82, 47, 91, 58]
```

If you need to classify every score, ending the loop at the first failing value would lose information.

The control statement should match the real requirement, not merely shorten the code.

## 8. `break` also works in `while`

```python
count = 1

while count <= 10:
    print(count)
    if count == 3:
        break
    count += 1
```

Output:

```text
1
2
3
```

The original `while` condition could still be true, but `break` ends the loop anyway.

## 9. `while True` can express an open-ended loop

A loop whose natural stopping rule occurs inside the body can be written as:

```python
while True:
    command = input("Command: ")

    if command == "quit":
        break

    print(command)
```

`True` keeps the loop eligible to repeat. The meaningful termination rule is the `break` triggered by `"quit"`.

This is not automatically better than a condition in the `while` header. Use it when the internal stop condition is genuinely clearer.

## 10. `while True` requires a believable exit path

This loop has no visible path to termination:

```python
while True:
    print("Running")
```

That may be intentional in specialized programs, but for beginner application code it should make you ask:

**What event or state change will stop this loop?**

If there is no answer, you may have created an accidental infinite loop.

## 11. What `continue` does

`continue` skips the rest of the current loop-body execution and starts the next cycle of the nearest enclosing loop.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```text
1
2
4
5
```

The loop itself continues. Only the remainder of the iteration for `3` is skipped.

## 12. `continue` is not `break`

Compare the intent:

```text
break    -> stop this loop
continue -> skip the rest of this iteration and keep looping
```

Confusing the two changes the entire control-flow shape.

## 13. `continue` is useful for filtering inside a loop

```python
scores = [82, 47, 91, 58, 76]

for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

Output:

```text
Passing score: 82
Passing score: 91
Passing score: 76
```

Failing scores are skipped, while the remaining values still reach the main action.

## 14. `continue` can reduce nesting

Without `continue`:

```python
for score in scores:
    if score >= 60:
        print(f"Passing score: {score}")
```

With `continue`:

```python
for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

Both can be clear. The second form is often useful when several early checks reject an item before a longer main path.

This is a readability choice, not a rule that `continue` is always superior.

## 15. In a `for` loop, `continue` moves toward the next item

```python
for letter in "ABC":
    if letter == "B":
        continue
    print(letter)
```

Output:

```text
A
C
```

After skipping the rest of the `B` iteration, the `for` loop requests the next item from its iterator.

## 16. In a `while` loop, `continue` retests the condition

```python
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

After `continue`, Python returns to the `while` condition before another body execution.

## 17. Update `while` state before a possible `continue`

This pattern is dangerous:

```python
number = 0

while number < 5:
    if number == 2:
        continue
    number += 1
```

When `number` reaches `2`, `continue` runs before the update. The condition remains true and `number` stays `2`, so the loop repeats forever.

A useful review question is:

**Can every path through this `while` body still make progress toward termination?**

## 18. Conditions can sometimes be clearer than `continue`

Do not add a jump merely because Python provides one.

```python
for number in range(1, 6):
    if number != 3:
        print(number)
```

may be perfectly readable compared with:

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Choose the shape that communicates the loop's main path most clearly.

## 19. What loop `else` is

Both `for` and `while` may have an optional `else` clause.

For a `for` loop:

```python
for item in iterable:
    statement
else:
    normal_completion_statement
```

For a `while` loop:

```python
while condition:
    statement
else:
    normal_completion_statement
```

The key rule is not “the condition was false.” The general rule is:

**The loop `else` runs when that loop finishes without executing a `break`.**

## 20. `for ... else` after normal exhaustion

```python
for number in [1, 2, 3]:
    print(number)
else:
    print("Finished normally")
```

Output:

```text
1
2
3
Finished normally
```

The iterable was exhausted and no `break` occurred, so the `else` suite runs.

## 21. `break` suppresses the loop `else`

```python
for number in [1, 2, 3]:
    if number == 2:
        break
else:
    print("Finished normally")
```

There is no output from the `else` clause because `break` terminated that loop.

## 22. `continue` does not suppress loop `else`

```python
for number in [1, 2, 3]:
    if number == 2:
        continue
    print(number)
else:
    print("Finished without break")
```

Output:

```text
1
3
Finished without break
```

`continue` changes an iteration, not the loop's final completion category.

## 23. Loop `else` belongs to the loop

Look carefully at the indentation:

```python
for name in names:
    if name == target:
        print("Found")
        break
else:
    print("Not found")
```

The `else` aligns with `for`, not with `if`.

That visual relationship is essential to reading this syntax correctly.

## 24. Search is the classic `for ... else` use case

```python
names = ["Ari", "Mina", "Leo"]
target = "Nora"

for name in names:
    if name == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} was not found")
```

Output:

```text
Nora was not found
```

The meaning is compact:

```text
match found -> break -> skip else
no match     -> no break -> run else
```

## 25. Loop `else` can replace a manual flag

A flag-based search can work:

```python
found = False

for name in names:
    if name == target:
        found = True
        break

if not found:
    print("Not found")
```

The loop-`else` form represents the same control-flow fact directly:

```python
for name in names:
    if name == target:
        break
else:
    print("Not found")
```

Use the version that your readers can understand reliably. Loop `else` is a real Python feature, but it can be unfamiliar to some teams.

## 26. An empty `for` can still execute `else`

```python
for item in []:
    print(item)
else:
    print("No break occurred")
```

Output:

```text
No break occurred
```

The loop body ran zero times, but the loop still completed without `break`.

## 27. `while ... else` runs after the condition becomes false

```python
count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Condition became false")
```

Output:

```text
1
2
3
Condition became false
```

This is normal completion for that `while` loop.

## 28. `break` also suppresses `while ... else`

```python
count = 1

while count <= 5:
    if count == 3:
        break
    count += 1
else:
    print("Condition became false")
```

The `else` suite does not run because `break` ended the loop first.

## 29. An initially false `while` can still execute `else`

```python
count = 5

while count < 3:
    print(count)
else:
    print("Loop completed without break")
```

Output:

```text
Loop completed without break
```

The body executed zero times, but no `break` occurred.

## 30. Think “no break,” not “something failed”

Loop `else` is sometimes informally described as a “not found” block because searches are a common use case.

That description is too narrow.

The actual control-flow fact is:

```text
loop ended without break -> else runs
loop ended through break -> else is skipped
```

The meaning of “success,” “failure,” “found,” or “not found” comes from your program, not from Python itself.

## 31. `break` affects only the nearest enclosing loop

```python
rows = [[1, 2], [3, 4]]

for row in rows:
    for value in row:
        if value == 2:
            break
        print(value)
```

Output:

```text
1
3
4
```

The `break` exits the inner loop only. The outer loop continues with the next row.

## 32. `continue` also targets the nearest enclosing loop

In nested loops, `continue` advances the nearest loop that syntactically contains it.

That can become difficult to read if several nested levels contain control jumps.

When nesting grows, prefer making the control flow explicit rather than stacking many `break` and `continue` statements.

## 33. The `else` belongs to one specific loop

Nested loops may each have their own `else` clause, but indentation determines which loop owns which clause.

For beginners, avoid dense combinations until the simpler shape is completely clear.

One loop, one search goal, and one meaningful `else` is usually easier to study.

## 34. Common mistake: expecting `break` to leave multiple loops

This does not exit both loops:

```python
for row in rows:
    for value in row:
        if value == target:
            break
```

Only the inner loop ends.

Later phases introduce functions, which often provide cleaner ways to organize larger searches without complicated nested-loop control.

## 35. Common mistake: putting important state updates after `continue`

```python
while condition:
    if skip_this_cycle:
        continue
    update_state()
```

If `update_state()` is necessary for termination, the skipped path may never make progress.

When reviewing a `while` loop, trace every branch that can reach `continue`.

## 36. Common mistake: reading loop `else` as `if ... else`

This indentation:

```python
for item in items:
    if condition:
        break
else:
    statement
```

means the `else` belongs to `for`.

Moving the `else` under the `if` would create a different program with different behavior.

## 37. Common mistake: using loop `else` when a normal statement is enough

If code must always run after a loop regardless of whether `break` occurred, place it after the loop:

```python
for item in items:
    if should_stop:
        break

print("Cleanup message")
```

Do not use loop `else` for unconditional post-loop work, because `break` would skip it.

## 38. Common mistake: overusing `break` and `continue`

A loop with many control jumps can become a maze:

```text
condition -> continue
condition -> break
condition -> continue
condition -> nested break
```

These statements are useful because they are precise, not because more of them makes code better.

Prefer a small number of clearly motivated exits and skips.

## 39. Worked example: `break_search.py`

```python
codes = ["PEN", "BOOK", "MUG", "CABLE"]
target = "MUG"

for code in codes:
    print(f"Checking {code}")
    if code == target:
        print(f"Found {target}")
        break
```

Output:

```text
Checking PEN
Checking BOOK
Checking MUG
Found MUG
```

Repository example: [`examples/break_search.py`](examples/break_search.py)

## 40. Worked example: `continue_filtering.py`

```python
scores = [82, 47, 91, 58, 76]

for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

Output:

```text
Passing score: 82
Passing score: 91
Passing score: 76
```

Repository example: [`examples/continue_filtering.py`](examples/continue_filtering.py)

## 41. Worked example: `loop_else_search.py`

```python
names = ["Ari", "Mina", "Leo"]
target = "Nora"

for name in names:
    if name == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} was not found")
```

Output:

```text
Nora was not found
```

Repository example: [`examples/loop_else_search.py`](examples/loop_else_search.py)

## 42. Exercise

Create a list of fictional task codes:

```python
task_codes = ["A10", "B20", "SKIP", "C30", "STOP", "D40"]
```

Write one loop that:

1. uses `continue` when the value is `"SKIP"`;
2. uses `break` when the value is `"STOP"`;
3. prints every other task code that is reached;
4. adds a loop `else` that prints `"All tasks processed"` only if the loop finishes without `break`.

With the list above, the expected output is:

```text
A10
B20
C30
```

Then remove `"STOP"` from the list and predict what changes before running the program.

## 43. Review checklist

Before moving on, confirm that you can explain each statement without running the code:

- [ ] `break` terminates the nearest enclosing `for` or `while` loop.
- [ ] statements later in the same iteration are skipped after `break`.
- [ ] `continue` skips the rest of the current iteration without terminating the loop.
- [ ] in `for`, `continue` proceeds toward the next item.
- [ ] in `while`, `continue` returns to the condition test.
- [ ] a `while` loop must still update relevant state on paths that can reach `continue`.
- [ ] `while True` is appropriate when an internal `break` expresses the real stop rule clearly.
- [ ] loop `else` aligns with and belongs to the loop.
- [ ] loop `else` runs when that loop completes without `break`.
- [ ] `break` suppresses the associated loop `else`.
- [ ] `continue` does not by itself suppress loop `else`.
- [ ] an empty `for` can still execute its `else`.
- [ ] an initially false `while` can still execute its `else`.
- [ ] in nested loops, `break` and `continue` affect the nearest enclosing loop.
- [ ] loop-control statements should clarify intent rather than create unnecessary jumps.

## 44. Quick reference

| Need | Typical tool |
|---|---|
| Stop the current loop immediately | `break` |
| Skip the rest of one iteration | `continue` |
| Repeat indefinitely until an internal stop rule | `while True` + `break` |
| Run a block only when no `break` ended the loop | loop `else` |
| Search until a match is found | `for` + condition + `break` |
| Handle “not found” after a complete search | `for ... else` |
| Skip rejected items while keeping later items | `continue` |
| Always run code after a loop | ordinary statement after the loop |

Remember the progression:

**normal repetition → early exit → skip one cycle → distinguish normal completion from `break`**

## Next step

The next chapter is **Choosing and Combining Program Flow**.

You now have the main selection and repetition tools of Phase 4: conditions, `if`, `match`, `for`, iteration helpers, `while`, `break`, `continue`, and loop `else`. The final chapter of the phase will focus on choosing among them and combining them without turning control flow into a maze.

## Official references

- [Python 3.13 language reference: `break`](https://docs.python.org/3.13/reference/simple_stmts.html#the-break-statement)
- [Python 3.13 language reference: `continue`](https://docs.python.org/3.13/reference/simple_stmts.html#the-continue-statement)
- [Python 3.13 language reference: `while`](https://docs.python.org/3.13/reference/compound_stmts.html#the-while-statement)
- [Python 3.13 language reference: `for`](https://docs.python.org/3.13/reference/compound_stmts.html#the-for-statement)
- [Python 3.13 tutorial: `break`, `continue`, and loop `else`](https://docs.python.org/3.13/tutorial/controlflow.html#break-and-continue-statements)
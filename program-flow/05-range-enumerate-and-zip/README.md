<div align="center">

# `range()`, `enumerate()`, and `zip()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Program Flow](../README.md) · [← Previous: `for` Loops and Iteration](../04-for-loops-and-iteration/README.md)

A plain `for` loop is often enough when you only need each item. Sometimes, however, the loop also needs **numbers, positions, or items from more than one iterable**.

This chapter introduces three built-ins that make those intentions explicit: `range()`, `enumerate()`, and `zip()`.

**Estimated study time:** 105–130 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain when direct iteration is clearer than using an iteration helper;
- create numeric progressions with `range()`;
- explain why the `stop` value of `range()` is excluded;
- use `start`, `stop`, and `step` deliberately;
- create descending ranges with a negative step;
- recognize empty ranges and the invalid zero-step case;
- explain why a `range` object is not a materialized list;
- use `enumerate()` when both a position and an item are needed;
- choose an appropriate `start` value for `enumerate()`;
- unpack the pairs produced by `enumerate()` directly in a `for` loop;
- use `zip()` to iterate over multiple iterables in parallel;
- explain the default shortest-iterable behavior of `zip()`;
- use `strict=True` when equal lengths are part of the program's expectation;
- recognize that `zip(strict=True)` was added in Python 3.10;
- distinguish the reusable `range` sequence from the iterators returned by `enumerate()` and `zip()`;
- combine iteration helpers without hiding the intent of the loop;
- choose among direct iteration, `range()`, `enumerate()`, and `zip()` according to the information the loop actually needs.

## 1. Why iteration helpers exist

The previous chapter established the basic pattern:

```python
for item in iterable:
    statement
```

That is still the preferred shape when the body only needs each item.

But some loops need additional information:

```text
need a numeric progression -> range()
need position + item       -> enumerate()
need parallel items        -> zip()
```

These tools do not replace `for`. They provide a more suitable iterable for the `for` loop to consume.

## 2. Start with the simplest tool that matches the intent

Suppose you only need the topic names:

```python
topics = ["conditions", "loops", "helpers"]

for topic in topics:
    print(topic)
```

Do not add indexes merely because indexes exist.

A useful rule for this chapter is:

**Ask what information the loop body needs, then choose the iterable that provides exactly that information.**

## 3. What `range()` is

`range()` represents an immutable sequence of integers that follow a regular progression.

The simplest form is:

```python
range(stop)
```

For example:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

The progression starts at `0` by default.

## 4. The `stop` value is excluded

In:

```python
range(5)
```

`5` is the stopping boundary, not an included item.

The represented values are:

```text
0, 1, 2, 3, 4
```

This half-open design connects naturally with zero-based indexing. A sequence with five items has valid indexes `0` through `4`.

## 5. `range(start, stop)`

You can provide a different starting value:

```python
for number in range(2, 7):
    print(number)
```

Output:

```text
2
3
4
5
6
```

The start is included when it belongs to the progression. The stop boundary is still excluded.

## 6. `range(start, stop, step)`

The third argument controls the step between values:

```python
for number in range(0, 10, 3):
    print(number)
```

Output:

```text
0
3
6
9
```

The default step is `1`.

## 7. A negative step creates a descending progression

To move downward, the step must be negative:

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

Again, the stop boundary `0` is excluded.

## 8. Direction and step must agree

A positive step moves upward. A negative step moves downward.

With a positive step, the range is empty when `start >= stop`. With a negative step, the range is empty when `start <= stop`. The progression does not need to land exactly on `stop`; that boundary remains excluded.

```python
print(list(range(5, 0)))
print(list(range(0, 5, -1)))
```

Output:

```text
[]
[]
```

This is normal behavior, not an error.

## 9. A zero step is invalid

A step of zero could never advance toward a boundary, so Python rejects it:

```python
range(0, 5, 0)
```

This raises `ValueError`.

Exception handling is taught later in the guide. For now, remember the rule:

**`step` may be positive or negative, but not zero.**

## 10. `range()` expects integer-like arguments

For beginner code, treat the `start`, `stop`, and `step` values as integers.

This is valid:

```python
range(0, 10, 2)
```

This is not a floating-point progression tool:

```python
range(0, 1, 0.1)
```

Passing ordinary `float` values this way raises `TypeError`.

## 11. A `range` object is not a list

Printing a range directly makes this visible:

```python
numbers = range(5)

print(numbers)
print(type(numbers))
```

Output:

```text
range(0, 5)
<class 'range'>
```

`range()` does not build a list containing every integer in advance.

## 12. `range` is an immutable sequence and an iterable

A `range` object can be used directly in `for` because it is iterable:

```python
for number in range(3):
    print(number)
```

It also behaves like a sequence in useful ways:

```python
numbers = range(10, 20, 2)

print(len(numbers))
print(numbers[0])
print(numbers[-1])
print(14 in numbers)
```

Output:

```text
5
10
18
True
```

You do not need to convert a range to a list just to iterate over it.

## 13. Convert to a list when you actually need a list

Conversion can be useful for inspection or when later code truly needs a mutable list:

```python
numbers = list(range(1, 6))
print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

Do not materialize a list automatically when the `range` object already expresses the progression you need.

## 14. Use `range()` when the numbers themselves matter

A good use case is a fixed progression of attempt numbers:

```python
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
```

Output:

```text
Attempt 1
Attempt 2
Attempt 3
```

Here the numbers are meaningful output, so `range()` communicates the intent well.

## 15. Direct iteration is clearer when only values matter

Suppose you have:

```python
topics = ["conditions", "loops", "helpers"]
```

This is direct and clear:

```python
for topic in topics:
    print(topic)
```

This version adds an unnecessary indirection when the index is not used for anything else:

```python
for index in range(len(topics)):
    print(topics[index])
```

Both can work, but the first says what the program means more directly: process each topic.

## 16. `range(len(sequence))` still has legitimate uses

Sometimes the index itself is necessary, such as when assigning back to a specific position:

```python
scores = [70, 80, 90]

for index in range(len(scores)):
    scores[index] = scores[index] + 5

print(scores)
```

Output:

```text
[75, 85, 95]
```

The important question is not whether `range(len(...))` is forbidden. It is whether the index is genuinely part of the task.

## 17. What `enumerate()` is

When you need both the position and the item, `enumerate()` usually expresses that intent more directly.

```python
topics = ["conditions", "loops", "helpers"]

for index, topic in enumerate(topics):
    print(index, topic)
```

Output:

```text
0 conditions
1 loops
2 helpers
```

`enumerate()` produces pairs containing a count and an item.

## 18. `enumerate()` starts at zero by default

The default count follows the familiar zero-based convention:

```python
letters = ["A", "B", "C"]

for index, letter in enumerate(letters):
    print(index, letter)
```

Output:

```text
0 A
1 B
2 C
```

Use that default when the count represents normal Python indexes.

## 19. Use `start=` when the displayed numbering has a different meaning

Human-facing numbering often starts at one:

```python
topics = ["conditions", "loops", "helpers"]

for position, topic in enumerate(topics, start=1):
    print(f"{position}. {topic}")
```

Output:

```text
1. conditions
2. loops
3. helpers
```

The items did not move inside the list. Only the counter produced by `enumerate()` starts at `1`.

## 20. `enumerate()` works with iterables, not only lists

A string can be enumerated too:

```python
for position, letter in enumerate("loop", start=1):
    print(position, letter)
```

Output:

```text
1 l
2 o
3 o
4 p
```

The same idea applies to many other iterables.

## 21. The pairs from `enumerate()` are unpacked by the loop target

This loop:

```python
for index, topic in enumerate(["conditions", "loops"]):
    print(index, topic)
```

uses the unpacking behavior you already learned.

Each produced item has two components:

```text
(count, item)
```

The loop target assigns the first component to `index` and the second to `topic`.

## 22. Prefer `enumerate()` to a manual counter when it matches the task

A manual counter can work:

```python
position = 1

for topic in ["conditions", "loops", "helpers"]:
    print(position, topic)
    position = position + 1
```

But when the purpose is simply to pair each item with a count, this is more direct:

```python
for position, topic in enumerate(
    ["conditions", "loops", "helpers"],
    start=1,
):
    print(position, topic)
```

`enumerate()` keeps the counting responsibility with the iteration tool rather than scattering it through the loop body.

## 23. What `zip()` is

`zip()` combines items from multiple iterables in parallel.

```python
topics = ["conditions", "loops", "helpers"]
minutes = [25, 40, 30]

for topic, duration in zip(topics, minutes):
    print(topic, duration)
```

Output:

```text
conditions 25
loops 40
helpers 30
```

The first topic is paired with the first duration, the second with the second, and so on.

## 24. `zip()` produces tuples

You can inspect the paired items by converting the result to a list:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

print(list(zip(names, scores)))
```

Output:

```text
[('Ari', 82), ('Mina', 91)]
```

Each item produced by `zip()` is a tuple.

That is why a loop can unpack it naturally:

```python
for name, score in zip(names, scores):
    print(name, score)
```

## 25. `zip()` accepts more than two iterables

Parallel iteration is not limited to pairs:

```python
names = ["Ari", "Mina"]
scores = [82, 91]
levels = ["review", "advance"]

for name, score, level in zip(names, scores, levels):
    print(name, score, level)
```

Output:

```text
Ari 82 review
Mina 91 advance
```

Use as many parallel sources as the task genuinely needs, but remember that many parallel lists can become difficult to maintain. A dictionary or structured record may sometimes model the data more clearly.

## 26. By default, `zip()` stops at the shortest iterable

This behavior is important:

```python
names = ["Ari", "Mina", "Leo"]
scores = [82, 91]

print(list(zip(names, scores)))
```

Output:

```text
[('Ari', 82), ('Mina', 91)]
```

`"Leo"` is not included because the scores iterable ended first.

Default truncation can be intentional, but it can also hide a data-alignment bug.

## 27. Use `strict=True` when equal lengths are required

If the program expects all input iterables to have matching lengths, make that expectation explicit:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

for name, score in zip(names, scores, strict=True):
    print(name, score)
```

Output:

```text
Ari 82
Mina 91
```

If one iterable ends before another, `zip(..., strict=True)` raises `ValueError` instead of silently truncating.

The `strict` argument was added in Python 3.10.

## 28. This chapter does not require exception handling

You should understand what `strict=True` guarantees without needing to catch the error yet.

The current rule is enough:

```text
length mismatch is acceptable -> default zip() may be intentional
lengths must match            -> prefer zip(..., strict=True)
```

Later phases teach `try` and `except` for programs that need to recover from exceptions deliberately.

## 29. `zip()` works with general iterables

The arguments do not have to be lists:

```python
letters = "ABC"
numbers = range(1, 4)

for letter, number in zip(letters, numbers, strict=True):
    print(letter, number)
```

Output:

```text
A 1
B 2
C 3
```

This works because both `str` and `range` are iterable.

## 30. `range` is reusable; `enumerate()` and `zip()` return iterators

This is an important connection to the previous chapter.

A `range` object is a sequence, so iterating over it does not consume the object permanently:

```python
numbers = range(3)

print(list(numbers))
print(list(numbers))
```

Output:

```text
[0, 1, 2]
[0, 1, 2]
```

By contrast, the objects returned by `enumerate()` and `zip()` are iterators. Once exhausted, the same iterator does not restart automatically:

```python
pairs = zip(["A", "B"], [1, 2])

print(list(pairs))
print(list(pairs))
```

Output:

```text
[('A', 1), ('B', 2)]
[]
```

If you need another pass, create a new `enumerate()` or `zip()` object from the original iterables.

## 31. Combine helpers when the combined intent remains clear

Sometimes you need both a displayed position and aligned data from multiple iterables:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

for position, (name, score) in enumerate(
    zip(names, scores, strict=True),
    start=1,
):
    print(position, name, score)
```

Output:

```text
1 Ari 82
2 Mina 91
```

This works because:

1. `zip()` produces `(name, score)` tuples;
2. `enumerate()` pairs each tuple with a count;
3. the loop target unpacks both layers.

Use combinations like this only when they remain readable to the intended audience.

## 32. Choose the helper by intent

| Need | Prefer |
|---|---|
| Each value only | direct `for item in iterable` |
| Numeric progression | `range()` |
| Position and value | `enumerate()` |
| Parallel values | `zip()` |
| Parallel values that must align exactly | `zip(..., strict=True)` |

These are guidelines for clarity, not restrictions in the Python language.

## 33. Common mistakes

### Mistake 1: expecting `stop` to be included

```python
print(list(range(1, 5)))
```

Output:

```text
[1, 2, 3, 4]
```

### Mistake 2: using a step with the wrong direction

```python
print(list(range(5, 0, 1)))
```

Output:

```text
[]
```

### Mistake 3: using `range(len(...))` when the index is unnecessary

```python
for index in range(len(topics)):
    print(topics[index])
```

If the body only needs each topic, direct iteration is clearer.

### Mistake 4: confusing `enumerate(start=1)` with changing list indexes

The counter can start at `1`, but the underlying list still uses its normal zero-based indexes.

### Mistake 5: assuming default `zip()` validates equal lengths

It does not. Default `zip()` stops at the shortest iterable.

### Mistake 6: reusing an exhausted `zip()` or `enumerate()` iterator

Create a fresh helper object when another complete pass is needed.

## 34. Worked example: `range_progressions.py`

```python
print(list(range(5)))
print(list(range(2, 7)))
print(list(range(0, 10, 3)))
print(list(range(5, 0, -1)))
```

Output:

```text
[0, 1, 2, 3, 4]
[2, 3, 4, 5, 6]
[0, 3, 6, 9]
[5, 4, 3, 2, 1]
```

Repository example: [`examples/range_progressions.py`](examples/range_progressions.py)

## 35. Worked example: `enumerate_positions.py`

```python
topics = ["conditions", "loops", "helpers"]

for position, topic in enumerate(topics, start=1):
    print(f"{position}. {topic}")
```

Output:

```text
1. conditions
2. loops
3. helpers
```

Repository example: [`examples/enumerate_positions.py`](examples/enumerate_positions.py)

## 36. Worked example: `zip_parallel_iteration.py`

```python
topics = ["conditions", "loops", "helpers"]
minutes = [25, 40, 30]

for topic, duration in zip(topics, minutes, strict=True):
    print(f"{topic}: {duration} min")
```

Output:

```text
conditions: 25 min
loops: 40 min
helpers: 30 min
```

Repository example: [`examples/zip_parallel_iteration.py`](examples/zip_parallel_iteration.py)

## 37. Exercise

Create a small study schedule with these two aligned lists:

```python
topics = ["strings", "collections", "flow"]
minutes = [20, 35, 30]
```

Your program should:

1. use `zip(..., strict=True)` to keep each topic aligned with its duration;
2. use `enumerate(..., start=1)` to number the rows from one;
3. print one line for each study block in this shape:

```text
1. strings - 20 min
2. collections - 35 min
3. flow - 30 min
```

Then create a separate countdown with `range()` that prints:

```text
3
2
1
Start
```

Do not use `while`, `break`, `continue`, or a comprehension.

## 38. Review checklist

Before moving on, confirm that you can explain each statement without running the code:

- [ ] `range(stop)` starts at zero by default.
- [ ] the `stop` boundary is excluded.
- [ ] `range(start, stop, step)` supports positive and negative steps.
- [ ] a zero step raises `ValueError`.
- [ ] `range` represents an immutable sequence rather than a prebuilt list.
- [ ] direct iteration is clearer when only the item value is needed.
- [ ] `enumerate()` provides a count together with each item.
- [ ] `enumerate(..., start=1)` changes the counter, not the underlying collection indexes.
- [ ] `zip()` combines items from iterables in parallel.
- [ ] default `zip()` stops when the shortest iterable is exhausted.
- [ ] `zip(..., strict=True)` raises `ValueError` when lengths differ.
- [ ] the `strict` argument exists in Python 3.10 and later.
- [ ] `range` is reusable as a sequence.
- [ ] `enumerate()` and `zip()` return iterators that can be exhausted.
- [ ] iteration helpers can be combined when the result remains readable.

## 39. Quick reference

| Need | Typical form |
|---|---|
| Count from zero to before `stop` | `range(stop)` |
| Choose start and stop | `range(start, stop)` |
| Choose a step | `range(start, stop, step)` |
| Count downward | `range(start, stop, -1)` or another negative step |
| Position and item | `enumerate(iterable)` |
| Human-facing numbering | `enumerate(iterable, start=1)` |
| Parallel iteration | `zip(first, second)` |
| Require equal lengths | `zip(first, second, strict=True)` |
| Only each item | direct `for item in iterable` |

Remember the progression:

**item iteration → numeric progression → position + item → parallel items → explicit alignment rule**

## Next step

The next chapter is **`while` Loops and State-Driven Repetition**.

You now know how to repeat work for items and how to shape iteration when the loop needs numbers, positions, or aligned values. Next, the guide introduces repetition controlled by a **Boolean condition** rather than by exhaustion of an iterable.

## Official references

- [Python 3.13 tutorial: The `range()` Function](https://docs.python.org/3.13/tutorial/controlflow.html#the-range-function)
- [Python 3.13 tutorial: Looping Techniques](https://docs.python.org/3.13/tutorial/datastructures.html#looping-techniques)
- [Python 3.13 built-in functions: `enumerate()` and `zip()`](https://docs.python.org/3.13/library/functions.html)
- [Python 3.13 built-in types: Ranges](https://docs.python.org/3.13/library/stdtypes.html#typesseq-range)

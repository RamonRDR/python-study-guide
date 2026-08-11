<div align="center">

# `for` Loops and Iteration

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Program Flow](../README.md) · [← Previous: `match` and `case`](../03-match-and-case/README.md)

The previous chapters taught Python how to **choose** what should run. A `for` loop introduces a different kind of control flow: **repeat a block once for each item provided by an iterable**.

This is where collections stop being values you only inspect and start becoming streams of work your program can process one item at a time.

**Estimated study time:** 105–130 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain the difference between selection and repetition;
- explain what iteration means;
- write a basic `for` loop with correct syntax and indentation;
- identify the loop target and the iterable in a `for` statement;
- explain what an iterable is at a beginner-friendly level;
- recognize that Python creates and consumes an iterator for a `for` loop automatically;
- iterate over lists, tuples, strings, dictionaries, and sets;
- explain the ordering guarantees or lack of guarantees of those iterable types;
- iterate over dictionary keys, values, and key-value pairs;
- unpack multi-part items directly in a `for` target;
- combine `for` with an `if` statement;
- build a new collection from selected items without using a comprehension;
- use nested loops when one repeated task genuinely belongs inside another;
- explain what happens when an iterable is empty;
- avoid relying on the loop target as a result variable after the loop;
- avoid modifying the structure of the same collection while iterating over it;
- recognize when `for` is appropriate and when a later flow tool will express the intent better.

## 1. From selection to repetition

An `if` statement chooses whether a block runs. A `match` statement chooses a block according to a pattern.

A `for` loop answers a different question:

**What should Python do for each item?**

Suppose a list contains three topics:

```python
topics = ["conditions", "patterns", "loops"]
```

Without a loop, you could write:

```python
print(topics[0])
print(topics[1])
print(topics[2])
```

That works only because you already know the exact size and positions.

A `for` loop expresses the relationship directly:

```python
for topic in topics:
    print(topic)
```

Output:

```text
conditions
patterns
loops
```

The loop says: for every item supplied by `topics`, temporarily call that item `topic` and run the indented block.

## 2. Basic syntax

The beginner form is:

```python
for item in iterable:
    statement
```

It has four important parts:

1. `for` starts the loop;
2. `item` is the target that receives each value;
3. `in` connects the target to the source of items;
4. `iterable` is the object that can provide items one at a time.

The colon ends the loop header. The indented block is the loop body.

A real example:

```python
colors = ["blue", "green", "orange"]

for color in colors:
    print(f"Color: {color}")
```

Output:

```text
Color: blue
Color: green
Color: orange
```

## 3. One loop, step by step

Consider:

```python
levels = ["beginner", "intermediate", "advanced"]

for level in levels:
    print(level)
```

A useful mental trace is:

```text
first item  -> level = "beginner"     -> run the body
second item -> level = "intermediate" -> run the body
third item  -> level = "advanced"     -> run the body
no more items -> leave the loop
```

Python does not run the entire collection at once. Each iteration assigns one item to the target and then executes the body.

## 4. Python's `for` is item-driven

A Python `for` loop is fundamentally about **items from an iterable**.

That is different from the classic C-style idea of a loop header that manually contains:

- an initial counter;
- a condition;
- an increment expression.

In this chapter, do not think:

```text
repeat three times
```

Think:

```text
for each item supplied by this iterable
```

When the real goal is to produce a numeric progression or explicitly track positions, the next chapter introduces `range()` and `enumerate()`.

## 5. What an iterable is

An **iterable** is an object that can provide its members one at a time.

You already know several iterable types:

- `list`;
- `tuple`;
- `str`;
- `dict`;
- `set`.

That means all of these can appear after `in` in a `for` loop.

The word iterable does **not** mean "list". A list is one kind of iterable.

This distinction matters because the same `for` syntax works with many different kinds of objects.

## 6. Iterable versus iterator

Python's terminology distinguishes an **iterable** from an **iterator**.

For a beginner, the practical mental model is:

```text
iterable = source that can provide items
iterator = object Python uses to obtain the next item from that source
```

When a `for` loop starts, Python obtains an iterator for the iterable and keeps asking it for the next item until no items remain.

You normally do **not** need to call `iter()` or `next()` yourself to write a `for` loop. The statement handles that protocol for you.

Later topics can explore iterators directly. For now, understand why the word **iterable** is broader than collection or sequence.

## 7. The loop target is an assignment target

In this loop:

```python
scores = [72, 81, 90]

for score in scores:
    print(score)
```

`score` is assigned a new item on each iteration.

Conceptually:

```text
score = 72
run body
score = 81
run body
score = 90
run body
```

This connects loops to a concept you already know: assignment.

The loop target is not a magical read-only placeholder. It is a normal assignment target that Python updates as iteration advances.

## 8. Indentation defines the loop body

As with `if` and `match`, indentation is syntax.

```python
names = ["Ana", "Mina"]

for name in names:
    print(f"Hello, {name}")
    print("Inside the loop")

print("After the loop")
```

Output:

```text
Hello, Ana
Inside the loop
Hello, Mina
Inside the loop
After the loop
```

Both indented `print()` calls run for each name. The final `print()` runs once after iteration finishes.

The guide uses four spaces per indentation level, following PEP 8.

## 9. Iterating over a list

Lists are a natural first use case because they contain a sequence of items:

```python
topics = ["strings", "collections", "flow"]

for topic in topics:
    print(f"Review: {topic}")
```

Output:

```text
Review: strings
Review: collections
Review: flow
```

List iteration follows list order.

You do not need indexes when your goal is simply to process each value.

## 10. Iterating over a tuple

Tuples are iterable too:

```python
coordinates = (4, -2)

for coordinate in coordinates:
    print(coordinate)
```

Output:

```text
4
-2
```

Tuple immutability does not prevent iteration. Immutability means the tuple's structure cannot be changed through tuple item assignment; it does not mean its items cannot be read one at a time.

Tuple iteration follows tuple order.

## 11. Iterating over a string

A string is an iterable sequence of characters:

```python
word = "loop"

for letter in word:
    print(letter)
```

Output:

```text
l
o
o
p
```

The two `o` characters both appear because iteration processes positions from the string, not only distinct values.

String iteration follows the string's character order.

## 12. Repeated values are still repeated items

A loop does not automatically remove duplicates.

```python
scores = [80, 90, 80]

for score in scores:
    print(score)
```

Output:

```text
80
90
80
```

The first and third items have equal values, but they are still separate items in the list's sequence.

If uniqueness is the important relationship, a set may be a more appropriate collection. That is a data-model decision, not a special behavior of `for`.

## 13. An empty iterable runs the body zero times

A `for` loop does not require at least one iteration.

```python
topics = []

for topic in topics:
    print(topic)

print("Finished")
```

Output:

```text
Finished
```

There were no items to assign to `topic`, so the loop body never ran.

This is an important property: **zero iterations is normal**.

## 14. Iterating over a dictionary gives keys by default

A dictionary is iterable, but its default iteration produces keys:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic in lesson_minutes:
    print(topic)
```

Output:

```text
conditions
patterns
loops
```

This is equivalent in intent to iterating over `lesson_minutes.keys()`.

In Python 3.7 and later, dictionary insertion order is guaranteed by the language. The keys above therefore appear in the order in which those entries were inserted.

## 15. Iterating over dictionary values

If the keys are not needed, `.values()` provides the values:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for minutes in lesson_minutes.values():
    print(minutes)
```

Output:

```text
25
35
40
```

Choose the iterable according to what the body needs.

## 16. Iterating over dictionary key-value pairs

`.items()` provides key-value pairs:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic, minutes in lesson_minutes.items():
    print(f"{topic}: {minutes} min")
```

Output:

```text
conditions: 25 min
patterns: 35 min
loops: 40 min
```

The loop target has two names because each item from `.items()` is a two-item pair.

## 17. A `for` target can unpack items

The previous example connects directly to tuple and sequence unpacking from Phase 3.

```python
records = [
    ("conditions", 25),
    ("patterns", 35),
]

for topic, minutes in records:
    print(topic, minutes)
```

Output:

```text
conditions 25
patterns 35
```

For each pair, Python assigns the first component to `topic` and the second to `minutes`.

The number and structure of target names must be compatible with the items being unpacked.

## 18. Iterating over a set

Sets are iterable:

```python
topics = {"strings", "collections", "flow"}

for topic in topics:
    print(topic)
```

However, a set has no positional ordering contract for you to rely on.

Do not write beginner code that assumes a particular set iteration order.

This chapter therefore avoids documenting an exact output order for that example.

## 19. The iterable determines meaningful order

`for` itself does not promise one universal ordering rule.

The iterable supplies items according to its own semantics:

| Iterable | Order to rely on |
|---|---|
| `list` | list sequence order |
| `tuple` | tuple sequence order |
| `str` | character sequence order |
| `dict` | insertion order of keys in Python 3.7+ |
| `dict.values()` | corresponding insertion order |
| `dict.items()` | corresponding insertion order |
| `set` | no positional order contract |

A useful rule is:

**Ask what order the iterable defines, not what order `for` defines.**

## 20. Combining `for` with `if`

The flow tools from earlier chapters can work inside a loop:

```python
scores = [52, 81, 67, 90]

for score in scores:
    if score >= 70:
        print(f"Passing: {score}")
```

Output:

```text
Passing: 81
Passing: 90
```

The loop controls **which item is current**. The `if` controls **what happens for that item**.

That combination is one of the most common foundations for data processing.

## 21. Building a new list during iteration

You already know `list.append()`, so you can collect selected results explicitly:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)

print(passing_scores)
```

Output:

```text
[81, 90]
```

This pattern has three clear stages:

```text
create destination
    ↓
iterate over source
    ↓
append selected result
```

List comprehensions can express some transformations more compactly, but they are intentionally deferred until loops are fully understood.

## 22. Accumulating a result

A loop can also update a separate accumulator:

```python
minutes = [20, 35, 15]
total = 0

for value in minutes:
    total = total + value

print(total)
```

Output:

```text
70
```

The important distinction is:

- `value` is the current item;
- `total` is state that survives from one iteration to the next.

For a simple total of numeric values, `sum()` is usually clearer and you already learned it in Phase 2. This manual example exists to show how state can change across iterations, not to replace `sum()`.

## 23. Nested loops

A loop body can contain another loop:

```python
groups = [
    ["A", "B"],
    ["C", "D"],
]

for group in groups:
    for item in group:
        print(item)
```

Output:

```text
A
B
C
D
```

For each `group`, the inner loop completes its iteration over that group.

The indentation shows the relationship:

```text
outer item
    ↓
run the complete inner loop
    ↓
move to the next outer item
```

Nested loops are useful when the data itself has nested structure. Avoid nesting merely because it is possible; each level increases the amount of flow a reader must track.

## 24. Be careful when modifying the collection being iterated

Changing the structure of the same collection while iterating over it can produce confusing behavior or errors depending on the collection and change.

For beginner code, prefer one of these strategies:

- iterate over the original and build a new collection;
- when mutation is genuinely required, iterate over an appropriate copy.

A clear filtering pattern is:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)
```

Here the loop reads `scores` while mutations happen only to `passing_scores`.

This separation is easier to reason about than deleting or inserting items in `scores` while it is being traversed.

## 25. The loop target can still exist after a non-empty loop

Python does not automatically delete the target name after a `for` loop.

```python
values = [10, 20, 30]

for value in values:
    print(value)

print(f"Last assigned value: {value}")
```

Output:

```text
10
20
30
Last assigned value: 30
```

This is real language behavior, but relying on the loop target as the program's final result is often unclear.

There is also an important edge case: if the iterable is empty, the loop does not assign the target at all.

Prefer a separate, deliberately initialized result variable when code after the loop needs a result.

## 26. Reassigning the target inside the body does not control iteration

Because Python assigns the next item to the loop target on each iteration, changing that name inside the body does not tell the loop what the next item should be.

```python
values = [1, 2, 3]

for value in values:
    value = value * 10
    print(value)
```

Output:

```text
10
20
30
```

The body changes the current binding, but the next iteration assigns the next item from `values` to `value` again.

If you need a transformed value, a separate name can make intent clearer:

```python
values = [1, 2, 3]

for value in values:
    transformed = value * 10
    print(transformed)
```

## 27. When `for` is a good fit

Use `for` when the central idea is:

- process every item in a collection;
- inspect characters in text;
- process dictionary keys, values, or pairs;
- filter items with an `if` inside the loop;
- build a new result from existing items;
- traverse nested iterable structures.

The strongest signal is that you already have, or can naturally obtain, an iterable whose items define the repetition.

## 28. When another tool may express the intent better

Do not choose `for` merely because repetition is involved.

Later chapters provide tools for different intentions:

- `range()` for arithmetic progressions and count-oriented iteration;
- `enumerate()` when position and item are both needed;
- `zip()` when multiple iterables should advance together;
- `while` when repetition is controlled by a changing condition rather than by exhausting an iterable;
- `break` and `continue` when loop flow needs deliberate early exit or skipping.

This separation keeps the first mental model clean: **`for` consumes items from an iterable**.

## 29. Choose singular target names when possible

If a collection name is plural, a singular target often makes the relationship obvious:

```python
topics = ["strings", "collections", "flow"]

for topic in topics:
    print(topic)
```

Likewise:

```python
students = ["Ana", "Diego"]

for student in students:
    print(student)
```

Names such as `x` or `item` are valid, but a domain-specific singular name usually teaches the code's intent more clearly.

## 30. Common mistakes

### Mistake 1: forgetting the colon

Incorrect:

```python
for topic in topics
    print(topic)
```

Correct:

```python
for topic in topics:
    print(topic)
```

### Mistake 2: forgetting indentation

Incorrect:

```python
for topic in topics:
print(topic)
```

Correct:

```python
for topic in topics:
    print(topic)
```

### Mistake 3: iterating over the wrong part of a dictionary

This gives keys:

```python
for item in settings:
    print(item)
```

If the body needs both key and value, use `.items()`:

```python
for key, value in settings.items():
    print(key, value)
```

### Mistake 4: assuming set order

Do not depend on this producing a chosen positional order:

```python
for topic in {"strings", "collections", "flow"}:
    print(topic)
```

### Mistake 5: assuming the body runs at least once

An empty iterable produces zero body executions.

### Mistake 6: changing the source collection while traversing it

Prefer building a new collection or deliberately iterating over a suitable copy.

### Mistake 7: expecting reassignment of the target to control the loop

The next iteration assigns the next item from the iterator again.

### Mistake 8: reaching for indexes when only values are needed

If the body only needs each value, iterate over the values directly. Position-aware tools arrive in the next chapter.

## 31. Scope boundary for this chapter

This chapter focuses on direct item-by-item iteration.

It does not require:

- `range()`;
- `enumerate()`;
- `zip()`;
- `while` loops;
- `break`;
- `continue`;
- loop `else`;
- comprehensions;
- user-defined functions;
- exception handling;
- external libraries.

Python's `for` grammar supports an optional `else` clause, but this guide intentionally teaches loop `else` together with `break` later because its meaning is clearest when normal loop completion and early termination can be compared directly.

## 32. Worked example: iterating over collections

The file [`examples/collection_iteration.py`](examples/collection_iteration.py) contains:

```python
topics = ["conditions", "patterns", "loops"]

for topic in topics:
    print(f"Study: {topic}")

coordinates = (4, -2)

for coordinate in coordinates:
    print(f"Coordinate: {coordinate}")

word = "loop"
letters = []

for letter in word:
    letters.append(letter.upper())

print("Letters:", letters)
```

Output:

```text
Study: conditions
Study: patterns
Study: loops
Coordinate: 4
Coordinate: -2
Letters: ['L', 'O', 'O', 'P']
```

This example connects list, tuple, and string iteration to list mutation already learned in earlier phases.

## 33. Worked example: dictionary iteration

The file [`examples/dictionary_iteration.py`](examples/dictionary_iteration.py) contains:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic in lesson_minutes:
    print(f"Topic: {topic}")

for topic, minutes in lesson_minutes.items():
    print(f"{topic}: {minutes} min")
```

Output:

```text
Topic: conditions
Topic: patterns
Topic: loops
conditions: 25 min
patterns: 35 min
loops: 40 min
```

The first loop uses dictionary keys. The second uses `.items()` and target unpacking.

## 34. Worked example: filter and collect

The file [`examples/filter_and_collect.py`](examples/filter_and_collect.py) contains:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)

print("Passing scores:", passing_scores)
print("Passing count:", len(passing_scores))
```

Output:

```text
Passing scores: [81, 90]
Passing count: 2
```

This example combines the first four phases directly:

```text
list of values
    ↓
for each value
    ↓
if the condition is true
    ↓
append the value to a result list
```

## 35. Exercise

Create a list named `study_minutes` containing:

```python
[25, 40, 15, 50]
```

Then:

1. create an empty list named `long_sessions`;
2. iterate over `study_minutes` with `for`;
3. if a value is at least `30`, append it to `long_sessions`;
4. after the loop, print `long_sessions`;
5. print its length.

Expected final values:

```text
[40, 50]
2
```

Then explain in your own words:

- what the iterable is;
- what the loop target is;
- how many iterations occur;
- why the `if` block runs fewer times than the loop body is entered.

### Extra practice

Given:

```python
course = {
    "title": "Python",
    "phase": 4,
    "chapter": 4,
}
```

Write one loop that prints only the keys, then another that prints each key and its corresponding value using `.items()`.

Do not use `range()`, `enumerate()`, `zip()`, or a comprehension yet.

## 36. Review checklist

Before moving on, confirm that you can explain each statement without running the code:

- [ ] `for` repeats a block for items supplied by an iterable.
- [ ] an iterable can provide items one at a time.
- [ ] Python manages the iterator used by a normal `for` loop automatically.
- [ ] the loop target is assigned a new item on each iteration.
- [ ] an empty iterable causes zero body executions.
- [ ] lists, tuples, and strings iterate in sequence order.
- [ ] dictionary iteration produces keys by default.
- [ ] `.values()` provides dictionary values.
- [ ] `.items()` provides key-value pairs that can be unpacked.
- [ ] set iteration must not be treated as positional ordering.
- [ ] an `if` inside a loop can make a decision for each current item.
- [ ] a separate destination list can collect selected results safely.
- [ ] nested loops are appropriate when repeated work follows nested data structure.
- [ ] modifying the same collection while traversing it is usually a poor beginner strategy.
- [ ] the loop target may still exist after a non-empty loop, but should not be treated as a reliable result variable.
- [ ] `range()`, `enumerate()`, and `zip()` belong to the next chapter.

## 37. Quick reference

| Need | Typical form |
|---|---|
| Iterate over values | `for item in iterable:` |
| Iterate over a list | `for item in items:` |
| Iterate over text characters | `for character in text:` |
| Iterate over dictionary keys | `for key in mapping:` |
| Iterate over dictionary values | `for value in mapping.values():` |
| Iterate over key-value pairs | `for key, value in mapping.items():` |
| Decide per item | `for item in items:` with an inner `if` |
| Build a filtered list | initialize `result = []`, then `append()` selected items |
| Traverse nested collections | nested `for` loops |
| No items available | loop body runs zero times |

Remember the progression:

**iterable → next item → assign target → run body → repeat until exhausted**

## Next step

The next chapter is **`range()`, `enumerate()`, and `zip()`**.

You now know how to process items directly. Next, the guide adds tools for generating numeric progressions, keeping positions alongside items, and advancing through multiple iterables together.

## Official references

- [Python 3.13 tutorial: `for` Statements](https://docs.python.org/3.13/tutorial/controlflow.html#for-statements)
- [Python 3.13 language reference: The `for` statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-for-statement)
- [Python 3.13 glossary: iterable](https://docs.python.org/3.13/glossary.html#term-iterable)
- [Python 3.13 glossary: iterator](https://docs.python.org/3.13/glossary.html#term-iterator)
- [Python 3.13 tutorial: Looping Techniques](https://docs.python.org/3.13/tutorial/datastructures.html#looping-techniques)
- [PEP 8: Indentation](https://peps.python.org/pep-0008/#indentation)

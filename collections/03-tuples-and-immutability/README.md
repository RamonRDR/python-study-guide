<div align="center">

# Tuples and Immutability

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Previous chapter: Modifying lists and common list methods](../02-modifying-lists-and-methods/README.md) · [Back to the Collections index](../README.md) · [Next chapter: Dictionaries: keys and values](../04-dictionaries-keys-and-values/README.md)

Lists taught you what it means for a collection to be mutable. Tuples introduce the contrasting idea: an ordered sequence whose item positions cannot be replaced, added to, or removed from after the tuple is created.

That difference is useful because the shape of some data is meant to stay fixed. A tuple can communicate that intent directly.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Collections Chapters 01 and 02 |
| Estimated study time | 80 to 100 minutes |
| Main concepts | tuple literals, immutable sequences, indexing, slicing, singleton tuples, `tuple()`, `count()`, `index()`, packing, unpacking, nested mutable objects |

## Learning objectives

By the end of this chapter, you should be able to:

- explain what makes a tuple an immutable sequence;
- create empty, single-item, and multi-item tuples;
- recognize why the comma matters in tuple syntax;
- read tuple items with positive and negative indexes;
- slice tuples without changing the original;
- use `len()`, `in`, and `not in` with tuples;
- create tuples with `tuple()`;
- use `count()` and `index()`;
- explain why list mutation methods do not exist on tuples;
- recognize the error caused by assigning to a tuple position;
- pack several values into a tuple;
- unpack a fixed-size sequence into variables;
- explain why a tuple can still contain a mutable object;
- choose a tuple when a fixed sequence communicates the data's intent better than a list.

## 1. What is a tuple?

A tuple is an **ordered, immutable sequence**.

Ordered means each item has a position. Immutable means the tuple cannot have its item positions changed after creation.

```python
course_info = ("Python", "Beginner", 90)

print(course_info)
print(type(course_info))
```

```text
('Python', 'Beginner', 90)
<class 'tuple'>
```

The tuple contains three items in a defined order.

## 2. Tuple versus list

Lists and tuples share many sequence operations, but they differ in one central behavior.

```python
topics_list = ["strings", "numbers", "lists"]
topics_tuple = ("strings", "numbers", "lists")

print(type(topics_list))
print(type(topics_tuple))
print(topics_list[0])
print(topics_tuple[0])
```

```text
<class 'list'>
<class 'tuple'>
strings
strings
```

Both are ordered and indexable. The list can later change its positions and size. The tuple cannot.

Use that difference as a design signal, not as a contest over which type is "better."

## 3. Creating a tuple

A common tuple literal uses comma-separated values inside parentheses:

```python
dimensions = (1920, 1080)
languages = ("Python", "SQL", "JavaScript")
```

The parentheses make the tuple easy to recognize, but there is an important syntax detail coming next: the comma is what creates a non-empty tuple.

## 4. The comma matters

These two expressions are not the same:

```python
grouped_value = ("Python")
single_item_tuple = ("Python",)

print(type(grouped_value))
print(type(single_item_tuple))
```

```text
<class 'str'>
<class 'tuple'>
```

`("Python")` is just a parenthesized string expression.

`("Python",)` is a tuple containing one item.

This is one of the most important tuple syntax rules for beginners.

## 5. Empty tuples

An empty tuple is written with empty parentheses:

```python
empty_tuple = ()

print(empty_tuple)
print(len(empty_tuple))
print(type(empty_tuple))
```

```text
()
0
<class 'tuple'>
```

Unlike a one-item tuple, the empty tuple does not need a comma.

## 6. Parentheses are often optional

For a non-empty tuple, commas can create the tuple even without surrounding parentheses:

```python
coordinates = 10, 20

print(coordinates)
print(type(coordinates))
```

```text
(10, 20)
<class 'tuple'>
```

In beginner code, parentheses are usually clearer when you intend to write a tuple:

```python
coordinates = (10, 20)
```

There are contexts where parentheses are required by the surrounding syntax. The useful idea here is simply that commas, not parentheses alone, define a non-empty tuple.

## 7. Reading items by index

Tuple indexing follows the same zero-based model used by strings and lists:

```python
record = ("Ana", "Python", 3)

print(record[0])
print(record[1])
print(record[2])
```

```text
Ana
Python
3
```

The first item is at index `0`.

## 8. Negative indexes

Negative indexes work the same way they do with strings and lists:

```python
record = ("Ana", "Python", 3)

print(record[-1])
print(record[-2])
```

```text
3
Python
```

`-1` means the last item.

## 9. Slicing a tuple

Tuple slices create another tuple:

```python
steps = ("study", "understand", "practice", "review", "repeat")

print(steps[:2])
print(steps[1:4])
print(steps[-2:])
```

```text
('study', 'understand')
('understand', 'practice', 'review')
('review', 'repeat')
```

Slicing reads a range. It does not modify the original tuple.

## 10. Slice steps also work

The common sequence slicing model still applies:

```python
steps = ("study", "understand", "practice", "review", "repeat")

print(steps[::2])
print(steps[::-1])
```

```text
('study', 'practice', 'repeat')
('repeat', 'review', 'practice', 'understand', 'study')
```

The reversed slice creates a new tuple. The original remains unchanged.

## 11. Length and membership

`len()`, `in`, and `not in` work with tuples:

```python
topics = ("strings", "numbers", "lists", "tuples")

print(len(topics))
print("tuples" in topics)
print("sets" not in topics)
```

```text
4
True
True
```

These operations inspect the tuple without changing it.

## 12. Immutability in practice

A tuple position cannot be replaced:

```python
topics = ("strings", "numbers", "lists")

topics[1] = "numeric tools"
```

```text
TypeError: 'tuple' object does not support item assignment
```

This is different from a list, where the same style of indexed assignment is allowed.

Do not use the error as a normal program flow technique. Its purpose here is to make the rule visible.

## 13. Tuples do not have list mutation methods

A tuple has no `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `reverse()`, or `sort()` methods.

That absence is consistent with immutability: those methods would need to change the existing sequence.

If the data needs to grow, shrink, reorder itself in place, or replace positions over time, a list is usually the clearer choice.

## 14. Concatenation creates a new tuple

Two tuples can be concatenated with `+`:

```python
core_topics = ("strings", "numbers")
collection_topics = ("lists", "tuples")

all_topics = core_topics + collection_topics

print(all_topics)
print(core_topics)
```

```text
('strings', 'numbers', 'lists', 'tuples')
('strings', 'numbers')
```

The original tuples are unchanged. `+` produces a new tuple.

## 15. Repetition creates a new tuple

Sequence repetition also works:

```python
pattern = ("study", "practice")

repeated = pattern * 2

print(repeated)
print(pattern)
```

```text
('study', 'practice', 'study', 'practice')
('study', 'practice')
```

Again, the existing tuple is not modified.

## 16. Creating tuples with `tuple()`

The built-in `tuple()` can create a tuple from another iterable. A list is a familiar example:

```python
topics_list = ["strings", "numbers", "lists"]
topics_tuple = tuple(topics_list)

print(topics_tuple)
print(type(topics_tuple))
```

```text
('strings', 'numbers', 'lists')
<class 'tuple'>
```

The new tuple contains the items provided by the list in the same order.

You do not need to explore every kind of iterable yet. Phase 4 loops will make that general concept more concrete.

## 17. `count()` answers how many

Tuples support `count()`:

```python
scores = (8, 10, 9, 10, 8, 10)

print(scores.count(10))
print(scores.count(7))
```

```text
3
0
```

`count(value)` returns how many items compare equal to the requested value.

It does not change the tuple.

## 18. `index()` finds the first matching position

Tuples also support `index()`:

```python
topics = ("strings", "numbers", "lists", "numbers")

print(topics.index("numbers"))
```

```text
1
```

Only the first equal match is returned.

If the value is absent, `index()` raises `ValueError`, just as it does for lists.

## 19. Tuple packing

Python can pack comma-separated values into a tuple:

```python
study_record = "tuples", 45, True

print(study_record)
print(type(study_record))
```

```text
('tuples', 45, True)
<class 'tuple'>
```

This is called **tuple packing**.

The three values become one tuple value.

## 20. Sequence unpacking

A fixed-size sequence can be unpacked into separate variables:

```python
study_record = ("tuples", 45, True)

topic, minutes, completed = study_record

print(topic)
print(minutes)
print(completed)
```

```text
tuples
45
True
```

Each variable receives the item from the matching position.

Although tuples make this pattern especially common, unpacking works with other sequences too.

## 21. The number of targets must match

Basic unpacking needs the number of variables on the left to match the number of sequence items on the right:

```python
study_record = ("tuples", 45, True)

topic, minutes = study_record
```

```text
ValueError: too many values to unpack (expected 2)
```

Later material can explore extended unpacking. For now, keep the shapes equal.

## 22. Packing and unpacking explain multiple assignment

This familiar-looking assignment:

```python
left = "A"
right = "B"

left, right = right, left

print(left)
print(right)
```

```text
B
A
```

works through packing and unpacking.

The right side produces the values, and the left side receives them by position. Python does not need a temporary variable for this swap.

## 23. Immutability is about the tuple's positions

A subtle but important rule: a tuple can contain mutable objects.

```python
profile = ("Ana", ["Python"])

profile[1].append("SQL")

print(profile)
```

```text
('Ana', ['Python', 'SQL'])
```

The tuple still has the same two positions:

1. the string `"Ana"`;
2. the same list object.

The tuple did not replace its second item. The list stored in that position changed internally.

So "tuple is immutable" does **not** mean "every object reachable from a tuple is immutable."

## 24. What still fails with a mutable item inside?

Even when a tuple contains a list, you still cannot replace that tuple position:

```python
profile = ("Ana", ["Python"])

profile[1] = ["SQL"]
```

```text
TypeError: 'tuple' object does not support item assignment
```

This contrast separates two ideas:

- changing the tuple's item positions;
- changing a mutable object already stored in one of those positions.

The first is forbidden. The second can be possible depending on the contained object's own type.

## 25. When a tuple communicates intent well

A tuple is useful when a sequence represents a fixed shape.

Examples include:

- a width and height pair;
- an `(x, y)` coordinate;
- a fixed summary such as `(topic, minutes, completed)`;
- values that are naturally unpacked into a known number of variables.

This is a design recommendation, not a Python requirement. A list can technically hold many of the same values.

Choose the type that communicates how the data is meant to behave.

## 26. When a list is clearer

Prefer a list when the collection is expected to change as part of normal work:

- new items will be appended;
- items will be removed;
- positions will be replaced;
- the collection will be sorted or reversed in place;
- the number of items naturally grows or shrinks.

The previous chapter gave you the tools for those jobs.

## 27. Practical example: fixed display settings

```python
display_size = (1920, 1080)

width, height = display_size

print("Width:", width)
print("Height:", height)
print("Pixels:", width * height)
```

```text
Width: 1920
Height: 1080
Pixels: 2073600
```

The pair has a fixed meaning: first width, then height. Unpacking gives those positions descriptive names.

## 28. Practical example: study summary

```python
study_summary = ("tuples", 50, True)

topic, minutes, completed = study_summary

print("Topic:", topic)
print("Minutes:", minutes)
print("Completed:", completed)
print("Fields:", len(study_summary))
```

```text
Topic: tuples
Minutes: 50
Completed: True
Fields: 3
```

This is a compact example of a fixed-shape record without introducing dictionaries yet. The next chapter will show why keys are often clearer when records become more descriptive.

## 29. Common mistakes

### Forgetting the comma in a one-item tuple

`("Python")` is a string expression. `("Python",)` is a one-item tuple.

### Trying to modify a tuple like a list

Indexed assignment and list mutation methods are not available for tuples.

### Thinking parentheses alone create every tuple

For non-empty tuples, commas are the defining syntax. Parentheses often improve clarity and are required in some contexts.

### Assuming immutability is deep

A tuple can contain a mutable object such as a list, and that contained object can still change.

### Expecting `+` to modify an existing tuple

Tuple concatenation returns a new tuple.

### Unpacking into the wrong number of variables

Basic unpacking requires the target count to match the sequence length.

### Using a tuple for a collection that naturally grows and shrinks

Immutability can become friction when mutation is actually part of the data's normal lifecycle. A list may express that intent better.

## 30. Connections to earlier and later concepts

This chapter reuses earlier ideas:

- indexing and slicing work like the sequence operations learned with strings and lists;
- `len()`, membership tests, `count()`, and `index()` inspect collection contents;
- list mutation provides the contrast that makes tuple immutability concrete;
- type conversion provides the model for `tuple()`.

It prepares later material:

- dictionaries will replace position-based meaning with key-based meaning;
- sets will focus on uniqueness rather than positional access;
- the final Collections chapter will compare all four collection choices;
- Phase 4 loops will iterate through tuples just as they will other iterables;
- Phase 5 functions will make packing, unpacking, and immutable data shapes increasingly useful.

## 31. Exercise: unpack a fixed learning record

Create `tuple_practice.py`.

Start with:

```python
learning_record = ("collections", "tuples", 60, True)
```

Without using loops or conditionals:

1. print the tuple;
2. print its length;
3. print the first item;
4. print the last item;
5. print the slice containing `"tuples"` and `60`;
6. print whether `"tuples"` is in the tuple;
7. unpack the four items into `phase`, `topic`, `minutes`, and `completed`;
8. print each unpacked value with a label;
9. create a one-item tuple named `next_topic` containing `"dictionaries"`;
10. print `next_topic` and its type;
11. concatenate `learning_record` and `next_topic` into `extended_record`;
12. print both tuples to confirm that the original was not changed.

One possible final output shape is:

```text
Record: ('collections', 'tuples', 60, True)
Length: 4
First: collections
Last: True
Middle: ('tuples', 60)
Contains tuples: True
Phase: collections
Topic: tuples
Minutes: 60
Completed: True
Next: ('dictionaries',)
Next type: <class 'tuple'>
Extended: ('collections', 'tuples', 60, True, 'dictionaries')
Original: ('collections', 'tuples', 60, True)
```

Try to predict the value and type of each expression before running the file.

## 32. Self-check

Before moving on, make sure you can answer these questions:

1. What makes a tuple a sequence?
2. What does immutable mean for a tuple?
3. Why is `("Python")` not a one-item tuple?
4. How do you write an empty tuple?
5. Can tuples be indexed and sliced?
6. What do `count()` and `index()` return?
7. What happens when you assign to `items[0]` if `items` is a tuple?
8. What is tuple packing?
9. What is sequence unpacking?
10. Why can a list stored inside a tuple still change?
11. Does `tuple_a + tuple_b` modify either original tuple?
12. When would a list communicate intent more clearly than a tuple?

If any answer feels uncertain, change one of the examples and observe what stays fixed and what can change.

## 33. Quick reference

- Multi-item tuple: `items = ("a", "b", "c")`
- Empty tuple: `items = ()`
- One-item tuple: `items = ("a",)`
- Create from another iterable: `items = tuple(values)`
- Read one item: `items[index]`
- Read a slice: `items[start:stop]`
- Length: `len(items)`
- Membership: `value in items`
- Count equal values: `items.count(value)`
- First equal position: `items.index(value)`
- Concatenate into a new tuple: `combined = first + second`
- Repeat into a new tuple: `repeated = items * 2`
- Pack values: `record = value_a, value_b`
- Unpack values: `value_a, value_b = record`

Remember:

- tuples are ordered;
- tuples are immutable;
- tuple positions cannot be assigned to or deleted;
- tuple concatenation and repetition create new tuples;
- a comma is required for a one-item tuple;
- contained mutable objects can still have their own internal changes.

## 34. Where to go next

You can now compare the two positional collection types introduced so far:

1. **List:** ordered and mutable.
2. **Tuple:** ordered and immutable.

The next Collections chapter introduces **dictionaries**, where positions stop being the main lookup model. Instead of asking for item `0` or item `1`, you will retrieve values using meaningful keys.

---

Official references used for technical verification:

- [Python Tutorial: Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Built-in Types: Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Built-in Types: Tuples](https://docs.python.org/3/library/stdtypes.html#tuples)
- [Python Data Model: Tuples](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

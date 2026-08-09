<div align="center">

# List Creation, Indexing, and Slicing

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the Collections index](../README.md) · [Next chapter: Modifying lists and common list methods →](../02-modifying-lists-and-methods/README.md)

Phase 2 taught you how ordered strings expose positions and slices. Phase 3 begins by applying that familiar idea to a new kind of value: a **list**, which can keep several related values together under one name.

A Python list is a mutable sequence. For this chapter, focus first on the sequence part: lists preserve item order, support integer indexing, and support slicing. The next chapter will focus on mutability and list-changing methods.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Phases 1 and 2 |
| Estimated study time | 75 to 95 minutes |
| Main concepts | `list`, list literals, `len()`, indexing, negative indexes, slicing, membership, `IndexError`, mutability preview |

## Learning objectives

By the end of this chapter, you should be able to:

- explain why a list is useful when several related values belong together;
- create empty and populated lists with square brackets;
- recognize that list order is significant;
- measure a list with `len()`;
- read items with positive and negative indexes;
- read ranges with slicing;
- explain why a direct invalid index raises `IndexError`;
- explain why broad slice boundaries are allowed;
- test whether a value is present with `in` and `not in`;
- connect list indexing and slicing to the string behavior learned in Phase 2;
- explain, at a high level, what it means for a list to be mutable.

## 1. Why lists exist

Before collections, you may store related values in separate variables:

```python
first_topic = "strings"
second_topic = "numbers"
third_topic = "lists"
```

That works for a tiny fixed example, but the relationship between the values exists mostly in the variable names.

A list lets one value represent the collection:

```python
topics = ["strings", "numbers", "lists"]

print(topics)
```

```text
['strings', 'numbers', 'lists']
```

Now `topics` clearly represents one ordered collection of related items.

## 2. Creating a list literal

Square brackets create a list literal. Separate items with commas:

```python
languages = ["Python", "JavaScript", "SQL"]
scores = [8, 9, 10]
prices = [12.50, 8.75, 21.00]

print(languages)
print(scores)
print(prices)
```

```text
['Python', 'JavaScript', 'SQL']
[8, 9, 10]
[12.5, 8.75, 21.0]
```

The brackets and commas are syntax. The items inside are the values stored by the list.

## 3. Creating an empty list

A list may begin with no items:

```python
tasks = []

print(tasks)
print(len(tasks))
print(type(tasks))
```

```text
[]
0
<class 'list'>
```

An empty list is still a valid `list` value.

The next chapter will show how a list can gain, change, and lose items after creation.

## 4. Lists preserve order

Item order is part of a list's value:

```python
first_order = ["study", "practice", "review"]
second_order = ["review", "practice", "study"]

print(first_order == second_order)
```

```text
False
```

The two lists contain the same three strings, but the positions differ.

This ordered structure is what makes indexing and slicing meaningful.

## 5. Lists can contain different kinds of values

Python permits list items to have different types:

```python
mixed_values = ["Python", 3, True, 9.5]

print(mixed_values)
```

```text
['Python', 3, True, 9.5]
```

That does not mean mixing unrelated values is always a good design. Lists are easiest to understand when the items belong to one clear concept, even if their exact types are not always identical.

For example, a list of scores or a list of topic names communicates intent more clearly than a list of unrelated facts.

## 6. Measuring a list with `len()`

`len()` returns the number of items:

```python
topics = ["strings", "numbers", "lists"]

print(len(topics))
```

```text
3
```

The result is an `int`, just as it was when you measured a string.

For a non-empty list of length `n`, positive indexes run from `0` through `n - 1`.

## 7. Positive indexing starts at zero

Use square brackets after the list value or variable name to read one position:

```python
topics = ["strings", "numbers", "lists"]

print(topics[0])
print(topics[1])
print(topics[2])
```

```text
strings
numbers
lists
```

A useful position map is:

```text
Item:   strings  numbers  lists
Index:        0        1      2
```

This is the same zero-based indexing model you already used with strings.

## 8. Negative indexes count from the end

Negative indexes read relative to the end:

```python
topics = ["strings", "numbers", "lists"]

print(topics[-1])
print(topics[-2])
print(topics[-3])
```

```text
lists
numbers
strings
```

```text
Item:      strings  numbers  lists
Positive:        0        1      2
Negative:       -3       -2     -1
```

`-1` means the last item.

## 9. Indexing returns the stored item

String indexing always returned another `str` because a string stores text code points. A list can store values of many types, so list indexing returns the item at that position with its own type.

```python
values = ["Python", 42, True]

print(values[0])
print(type(values[0]))
print(values[1])
print(type(values[1]))
print(values[2])
print(type(values[2]))
```

```text
Python
<class 'str'>
42
<class 'int'>
True
<class 'bool'>
```

The list is the container. Indexing reads one contained value.

## 10. Invalid direct indexes raise `IndexError`

A direct index requests one exact position:

```python
topics = ["strings", "numbers", "lists"]

print(topics[3])
```

```text
IndexError: list index out of range
```

The list has length `3`, so its valid positive indexes are `0`, `1`, and `2`.

An empty list has no valid direct index.

## 11. Slicing reads a range

List slicing uses the same basic syntax as string slicing:

```text
items[start:stop]
```

The start boundary is included and the stop boundary is excluded.

```python
topics = ["strings", "numbers", "lists", "tuples", "dictionaries"]

print(topics[1:4])
```

```text
['numbers', 'lists', 'tuples']
```

Indexes `1`, `2`, and `3` are included. Index `4` marks where the slice stops.

## 12. A list slice produces a list

Slicing a list produces another list:

```python
topics = ["strings", "numbers", "lists", "tuples"]

selected_topics = topics[1:3]

print(selected_topics)
print(type(selected_topics))
```

```text
['numbers', 'lists']
<class 'list'>
```

This differs from direct indexing:

```text
topics[1]    -> one stored item
topics[1:3]  -> a new list containing a range of items
```

A slice creates a new list object. If the items themselves refer to mutable objects, those inner objects can still be shared; that deeper topic is outside this beginner chapter.

## 13. Omitting slice boundaries

Omit the start boundary to begin at the first item:

```python
steps = ["study", "understand", "practice", "review"]

print(steps[:2])
print(steps[2:])
print(steps[:])
```

```text
['study', 'understand']
['practice', 'review']
['study', 'understand', 'practice', 'review']
```

Omitting the stop boundary continues to the end. Omitting both selects the full range.

## 14. Negative indexes also work in slices

Negative boundaries are useful when the end of the list is the natural reference point:

```python
steps = ["study", "understand", "practice", "review", "repeat"]

print(steps[-2:])
print(steps[:-2])
```

```text
['review', 'repeat']
['study', 'understand', 'practice']
```

Prefer boundaries that make the intention easy to read.

## 15. Slices tolerate broad boundaries

Like string slices, list slices can extend beyond the available positions:

```python
topics = ["strings", "numbers", "lists"]

print(topics[:100])
print(topics[100:])
```

```text
['strings', 'numbers', 'lists']
[]
```

Compare the two ideas:

```text
topics[100]   -> one exact missing position -> IndexError
topics[:100]  -> available range            -> valid list
```

## 16. Slice steps

A slice can include a step:

```text
items[start:stop:step]
```

For a first example, omit start and stop and select every second item:

```python
steps = ["study", "understand", "practice", "review", "repeat"]

print(steps[::2])
```

```text
['study', 'practice', 'repeat']
```

Advanced slicing tricks are not the goal here. Use steps when they make the code clearer.

## 17. Checking membership with `in`

The `in` operator checks whether an equal item is present:

```python
topics = ["strings", "numbers", "lists"]

print("lists" in topics)
print("tuples" in topics)
print("tuples" not in topics)
```

```text
True
False
True
```

These expressions produce `bool` values, connecting collections directly to the Boolean concepts from Phase 2.

Membership checks answer whether a value is present. They do not tell you where it appears.

## 18. Lists are mutable, but this chapter reads them first

A key difference between strings and lists is **mutability**.

- a string does not allow one of its positions to be replaced in place;
- a list does allow its contents to be changed after creation.

This chapter intentionally focuses on creating and reading lists so the sequence model becomes familiar first.

The next chapter will teach item assignment, `append()`, `insert()`, `remove()`, `pop()`, `clear()`, and `del`, and will make the mutation rules explicit.

## 19. When a list is a good choice

A list is a strong beginner choice when:

- several values belong to one ordered collection;
- positions matter;
- the number of items may change later;
- duplicate values are acceptable;
- you expect to read values by index or slice them into ranges.

Examples include a sequence of lesson topics, a shopping list, ordered steps, or a set of scores recorded in order.

## 20. When a list may not be the best choice

A list may be a poor fit when the main relationship is not positional.

Later in this phase you will learn alternatives:

- tuples for sequence data where immutability communicates intent;
- dictionaries for key-to-value relationships;
- sets for unique values and set-style membership operations.

Do not choose a collection only because its syntax is familiar. Choose the structure that expresses the relationship between the values.

## 21. Practical example: inspect a study plan

```python
study_plan = ["strings", "numbers", "lists", "tuples", "dictionaries"]

print("Plan:", study_plan)
print("Length:", len(study_plan))
print("Current:", study_plan[2])
print("Next:", study_plan[3])
print("Last two:", study_plan[-2:])
print("Lists included:", "lists" in study_plan)
```

```text
Plan: ['strings', 'numbers', 'lists', 'tuples', 'dictionaries']
Length: 5
Current: lists
Next: tuples
Last two: ['tuples', 'dictionaries']
Lists included: True
```

This example uses the collection as an ordered plan without changing it yet.

## 22. Practical example: reuse numeric tools from Phase 2

Lists become especially useful when earlier tools can work with several related values:

```python
scores = [8, 9, 10]

print("Lowest:", min(scores))
print("Highest:", max(scores))
print("Total:", sum(scores))
```

```text
Lowest: 8
Highest: 10
Total: 27
```

You already learned these built-ins in Phase 2. The new idea is that one list can supply the related values as a collection.

## 23. Common mistakes

### Starting at index `1`

```python
topics = ["strings", "numbers", "lists"]
print(topics[1])
```

This prints `numbers`, not `strings`. The first index is `0`.

### Using `len(items)` as the last valid index

If a list has length `3`, index `3` is already outside it. The last valid positive index is `len(items) - 1`, and `items[-1]` is often clearer.

### Expecting a slice to return one item

`items[1]` reads one item. `items[1:2]` returns a list containing at most one item.

### Expecting the stop boundary to be included

`items[1:3]` includes indexes `1` and `2`, not index `3`.

### Confusing an empty list with a missing value

`[]` is a real list containing zero items. It is not the same value as `None`.

### Mixing unrelated values without a reason

Python allows mixed item types, but a collection is easier to understand when its items represent one clear idea.

## 24. Connections to earlier and later concepts

This chapter reuses several ideas you already know:

- variables name values;
- `type()` identifies the list and the types of indexed items;
- `len()` returns an integer count;
- indexes are integers;
- slicing follows the same include-start, exclude-stop model used by strings;
- `in` and `not in` produce Boolean results;
- `min()`, `max()`, and `sum()` can work with appropriate list values.

It also prepares the next steps:

- Chapter 02 changes list contents deliberately;
- Chapter 03 compares lists with tuples and introduces immutability as a collection design choice;
- Chapter 04 replaces positional lookup with dictionary keys;
- Chapter 05 introduces sets, where indexing is not the organizing model;
- Phase 4 later uses loops to visit collection items repeatedly.

## 25. Exercise: build a collection inspector

Create `collection_inspector.py` with this starting value:

```python
topics = ["variables", "strings", "numbers", "lists", "tuples"]
```

Print:

1. the complete list;
2. its length;
3. the first item;
4. the last item;
5. the middle three items with a slice;
6. the first three items with a slice;
7. the last two items with a slice;
8. every second item;
9. whether `"lists"` is present;
10. the type of the complete collection;
11. the type of the first indexed item.

A possible output shape is:

```text
Topics: ['variables', 'strings', 'numbers', 'lists', 'tuples']
Length: 5
First: variables
Last: tuples
Middle three: ['strings', 'numbers', 'lists']
First three: ['variables', 'strings', 'numbers']
Last two: ['lists', 'tuples']
Every second: ['variables', 'numbers', 'tuples']
Contains lists: True
Collection type: <class 'list'>
First item type: <class 'str'>
```

Try to solve it without loops. Phase 4 will introduce repeated iteration later.

### Stretch goal

Create a second list of five numeric scores. Print its first and last values, a slice containing the middle scores, its lowest value, its highest value, and its total.

Do not modify either list yet. That is the next chapter's job.

## 26. Self-check

Make sure you can answer:

1. What problem does a list solve compared with several separate variables?
2. Which symbols create a list literal?
3. What does `len()` count for a list?
4. What is the first positive index?
5. What does index `-1` mean?
6. What is the difference between `items[1]` and `items[1:2]`?
7. Is the slice stop boundary included?
8. What happens when a direct index is outside the list?
9. Why can `items[:100]` succeed when `items[100]` fails?
10. What type of result does a list slice produce?
11. What do `in` and `not in` return?
12. At a high level, what does it mean that a list is mutable?

## 27. Quick reference

| Goal | Syntax | Example |
|---|---|---|
| Empty list | `[]` | `items = []` |
| Create items | `[a, b, c]` | `topics = ["strings", "lists"]` |
| Number of items | `len(items)` | `len(topics)` |
| First item | `items[0]` | `topics[0]` |
| Last item | `items[-1]` | `topics[-1]` |
| Range | `items[start:stop]` | `topics[1:3]` |
| From start | `items[:stop]` | `topics[:2]` |
| To end | `items[start:]` | `topics[2:]` |
| Every second item | `items[::2]` | `topics[::2]` |
| Membership | `value in items` | `"lists" in topics` |
| Absence | `value not in items` | `"sets" not in topics` |
| Type | `type(items)` | `type(topics)` |

## 28. Official references

- [Python documentation: Lists](https://docs.python.org/3/library/stdtypes.html#lists)
- [Python documentation: Common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

## Next step

Continue with **Modifying Lists and Common List Methods** to learn how mutability works in practice.

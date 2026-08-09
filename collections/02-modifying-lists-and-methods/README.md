<div align="center">

# Modifying Lists and Common List Methods

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Previous chapter: List creation, indexing, and slicing](../01-list-creation-and-indexing/README.md) · [Back to the Collections index](../README.md) · [Next chapter: Tuples and immutability](../03-tuples-and-immutability/README.md)

The previous chapter taught you to create and read lists. Now the other half of the list model becomes important: a list is **mutable**, which means its contents can be changed after the list is created.

This chapter turns that idea into concrete operations. You will replace items, add items, remove items, reorder items, inspect positions and counts, and learn why some methods change a list but deliberately return `None`.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Collections Chapter 01 |
| Estimated study time | 100 to 125 minutes |
| Main concepts | mutability, item assignment, slice assignment, `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `del`, `index()`, `count()`, `reverse()`, `sort()`, `copy()` |

## Learning objectives

By the end of this chapter, you should be able to:

- explain list mutability in terms of observable changes;
- replace an existing item by index;
- replace a slice with other values;
- add one item with `append()`;
- add several items with `extend()`;
- insert an item at a chosen position with `insert()`;
- remove by value with `remove()`;
- remove and retrieve by position with `pop()`;
- remove items with `del` and empty a list with `clear()`;
- locate the first matching value with `index()`;
- count matching values with `count()`;
- reverse or sort a list in place;
- recognize which common list methods return `None`;
- distinguish assigning another name to the same list from creating a shallow copy with `copy()`;
- choose a modification operation according to intent rather than habit.

## 1. What mutability means

A mutable object can change while remaining the value referenced by the same variable.

```python
topics = ["strings", "numbers", "lists"]

topics[1] = "numeric tools"

print(topics)
```

```text
['strings', 'numeric tools', 'lists']
```

The variable is still named `topics`, and it still refers to a list. The contents of that list changed.

That is the central difference from strings. String positions can be read, but they cannot be replaced in place. List positions can be both read and replaced.

## 2. Replacing one item by index

Use an assignment target with square brackets to replace one existing position:

```python
languages = ["Python", "Java", "SQL"]

languages[1] = "JavaScript"

print(languages)
```

```text
['Python', 'JavaScript', 'SQL']
```

The right side provides the new value. The indexed position on the left side identifies where that value should go.

Negative indexes work too:

```python
steps = ["study", "practice", "draft"]

steps[-1] = "review"

print(steps)
```

```text
['study', 'practice', 'review']
```

Use the same index model you learned in the previous chapter.

## 3. Assignment does not create a missing position

Item assignment replaces a position that must already exist.

```python
topics = ["strings", "numbers", "lists"]

topics[3] = "tuples"
```

```text
IndexError: list assignment index out of range
```

The list has three items, so its valid positive indexes are `0`, `1`, and `2`.

If your intention is to add a new item rather than replace an existing one, use an adding operation such as `append()` or `insert()`.

## 4. Replacing a range with slice assignment

A slice can appear on the left side of an assignment:

```python
steps = ["study", "practice", "review", "repeat"]

steps[1:3] = ["understand", "practice"]

print(steps)
```

```text
['study', 'understand', 'practice', 'repeat']
```

The selected slice is replaced by the values on the right.

Unlike assigning one direct index, ordinary slice assignment can also change the number of items:

```python
steps = ["study", "review", "repeat"]

steps[1:2] = ["understand", "practice", "review"]

print(steps)
```

```text
['study', 'understand', 'practice', 'review', 'repeat']
```

You do not need advanced slice-assignment patterns yet. The useful beginner idea is that a slice target can replace a range, not just one position.

## 5. Adding one item with `append()`

`append()` adds one value to the end of the existing list:

```python
topics = ["strings", "numbers"]

topics.append("lists")

print(topics)
```

```text
['strings', 'numbers', 'lists']
```

The list is modified in place.

Use `append()` when the entire value you pass should become one new item.

## 6. `append()` adds exactly one item

If the value passed to `append()` is itself a list, that whole list becomes one nested item:

```python
topics = ["strings", "numbers"]

topics.append(["lists", "tuples"])

print(topics)
print(len(topics))
```

```text
['strings', 'numbers', ['lists', 'tuples']]
3
```

This is valid Python. Whether it is the structure you intended is a separate question.

If you want the values from another list to become separate items, use `extend()` instead.

## 7. Adding several items with `extend()`

`extend()` adds the items from another iterable to the end of the list. In this beginner chapter, another list is the clearest example:

```python
topics = ["strings", "numbers"]

topics.extend(["lists", "tuples"])

print(topics)
```

```text
['strings', 'numbers', 'lists', 'tuples']
```

Compare the intent:

- `append(value)` adds `value` as one item.
- `extend(values)` adds the items provided by `values`.

The general Python term *iterable* covers objects that can provide items one after another. Loops will make that concept more concrete in Phase 4. For now, using another list with `extend()` is enough.

## 8. Inserting at a position with `insert()`

`insert(index, value)` places a value before the item currently at that index:

```python
steps = ["study", "review", "repeat"]

steps.insert(1, "practice")

print(steps)
```

```text
['study', 'practice', 'review', 'repeat']
```

Use `insert()` when the position itself carries meaning.

Unlike direct item assignment, `insert()` does not require the index to name an existing item. Python adjusts an out-of-range insertion index to a boundary: `items.insert(len(items), value)` and larger positive indexes insert at the end, while sufficiently negative indexes insert at the beginning. An out-of-range insertion index therefore does not raise `IndexError` by itself.

If the new item simply belongs at the end, `append()` communicates that intent more directly.

## 9. Removing by value with `remove()`

`remove(value)` deletes the first equal value it finds:

```python
topics = ["lists", "strings", "lists", "tuples"]

topics.remove("lists")

print(topics)
```

```text
['strings', 'lists', 'tuples']
```

Only the first matching `"lists"` item was removed.

Use `remove()` when you know the value you want to remove and do not need the removed value returned to you.

## 10. Missing values make `remove()` raise `ValueError`

`remove()` expects a matching value to exist:

```python
topics = ["strings", "numbers", "lists"]

topics.remove("tuples")
```

```text
ValueError: list.remove(x): x not in list
```

Later, program flow will let you decide what to do conditionally when a value may or may not be present. In this chapter, the important rule is simply that a missing value causes `ValueError`.

## 11. Removing and retrieving with `pop()`

`pop()` removes an item and returns the removed value.

With no argument, it uses the last position:

```python
topics = ["strings", "numbers", "lists"]

removed_topic = topics.pop()

print("Removed:", removed_topic)
print("Remaining:", topics)
```

```text
Removed: lists
Remaining: ['strings', 'numbers']
```

You can also provide an index:

```python
topics = ["strings", "numbers", "lists"]

removed_topic = topics.pop(0)

print("Removed:", removed_topic)
print("Remaining:", topics)
```

```text
Removed: strings
Remaining: ['numbers', 'lists']
```

Use `pop()` when both actions matter: changing the list and keeping the removed value for later use.

## 12. Invalid `pop()` positions raise `IndexError`

An invalid index cannot be popped. Calling `pop()` on an empty list also has no item to remove.

```python
topics = []

topics.pop()
```

```text
IndexError: pop from empty list
```

This is different from `remove()`: a missing value leads to `ValueError`, while an invalid or unavailable position for `pop()` leads to `IndexError`.

## 13. Removing with `del`

`del` is a statement that can remove an item by index:

```python
topics = ["strings", "numbers", "lists", "tuples"]

del topics[1]

print(topics)
```

```text
['strings', 'lists', 'tuples']
```

It can also remove a slice:

```python
topics = ["variables", "strings", "numbers", "lists", "tuples"]

del topics[1:3]

print(topics)
```

```text
['variables', 'lists', 'tuples']
```

Unlike `pop()`, `del` does not give the removed item back as a method result.

## 14. Emptying a list with `clear()`

`clear()` removes all items while leaving the list itself available:

```python
topics = ["strings", "numbers", "lists"]

topics.clear()

print(topics)
print(len(topics))
```

```text
[]
0
```

The variable still refers to a list, but that list now contains zero items.

## 15. Finding the first matching position with `index()`

`index(value)` searches for the first equal value and returns its zero-based index:

```python
topics = ["lists", "strings", "lists", "tuples"]

print(topics.index("lists"))
print(topics.index("tuples"))
```

```text
0
3
```

`index()` does not modify the list.

If the value is absent, `index()` raises `ValueError`.

## 16. Counting matching values with `count()`

`count(value)` returns how many equal items appear:

```python
topics = ["lists", "strings", "lists", "tuples"]

print(topics.count("lists"))
print(topics.count("numbers"))
```

```text
2
0
```

A missing value is not an error for `count()`. Its count is simply `0`.

This makes `count()` different from both `index()` and `remove()`.

## 17. Reversing the current order with `reverse()`

`reverse()` flips the existing order in place:

```python
steps = ["study", "practice", "review"]

steps.reverse()

print(steps)
```

```text
['review', 'practice', 'study']
```

`reverse()` does not sort by value. It only reverses whatever order the list currently has.

## 18. Sorting in place with `sort()`

`sort()` rearranges a list in place when its items support the required comparisons:

```python
scores = [9, 7, 10, 8]

scores.sort()

print(scores)
```

```text
[7, 8, 9, 10]
```

A simple list of strings can also be sorted according to Python's ordering rules:

```python
topics = ["tuples", "lists", "dictionaries"]

topics.sort()

print(topics)
```

```text
['dictionaries', 'lists', 'tuples']
```

Advanced sort customization with `key=` belongs outside this chapter. First learn the important distinction: `sort()` changes the existing list.

## 19. Not every mixture can be sorted

A list may legally contain different types, but that does not guarantee that those values have a meaningful ordering relationship.

```python
values = ["Python", 3, None]

values.sort()
```

```text
TypeError: '<' not supported between instances of 'int' and 'str'
```

Do not interpret this as a rule that mixed-type lists are invalid. The issue is narrower: `sort()` needs comparisons that the contained values support.

## 20. In-place mutating methods usually return `None`

This is one of the most important list habits to learn early.

Methods whose main purpose is to modify a list in place, such as `append()`, `extend()`, `insert()`, `remove()`, `clear()`, `reverse()`, and `sort()`, return `None` rather than the changed list.

```python
topics = ["strings", "numbers"]

result = topics.append("lists")

print("Topics:", topics)
print("Result:", result)
```

```text
Topics: ['strings', 'numbers', 'lists']
Result: None
```

The useful result of `append()` is the changed `topics` list itself. The method return value is `None`.

`pop()` is intentionally different because retrieving the removed item is part of its purpose.

## 21. The common `items = items.append(...)` mistake

Because `append()` returns `None`, this pattern destroys the variable's useful list reference:

```python
items = ["strings", "numbers"]

items = items.append("lists")

print(items)
```

```text
None
```

Use the mutating method as its own statement:

```python
items = ["strings", "numbers"]

items.append("lists")

print(items)
```

```text
['strings', 'numbers', 'lists']
```

The same caution applies to other in-place methods such as `sort()` and `reverse()`.

## 22. Assignment can create another name for the same list

This line does not copy a list:

```python
original = ["strings", "numbers"]
alias = original

alias.append("lists")

print("Original:", original)
print("Alias:", alias)
```

```text
Original: ['strings', 'numbers', 'lists']
Alias: ['strings', 'numbers', 'lists']
```

Both variable names refer to the same mutable list, so a mutation observed through one name is visible through the other.

This is why mutability matters beyond a single line of code.

## 23. Creating a separate list with `copy()`

`copy()` creates a new list containing references to the same current items:

```python
original = ["strings", "numbers"]
independent = original.copy()

independent.append("lists")

print("Original:", original)
print("Copy:", independent)
```

```text
Original: ['strings', 'numbers']
Copy: ['strings', 'numbers', 'lists']
```

Changing the outer copied list no longer changes the outer original list.

The official term is **shallow copy**. If a list contains mutable objects inside it, those inner objects can still be shared between the two outer lists. Nested-object copying is a deeper topic; for now, remember that `copy()` gives you a separate outer list.

## 24. One comparison: alias versus copy

```python
original = ["strings", "numbers"]
alias = original
independent = original.copy()

alias.append("lists")
independent.append("tuples")

print("Original:", original)
print("Alias:", alias)
print("Copy:", independent)
```

```text
Original: ['strings', 'numbers', 'lists']
Alias: ['strings', 'numbers', 'lists']
Copy: ['strings', 'numbers', 'tuples']
```

This example is worth running and changing. It makes reference sharing visible without requiring advanced memory-model terminology.

## 25. Choosing the operation by intent

Several operations can change a list, but they communicate different intentions.

| Intent | Operation |
|---|---|
| Replace one existing position | `items[index] = value` |
| Replace a range | `items[start:stop] = values` |
| Add one item at the end | `append()` |
| Add several items at the end | `extend()` |
| Add one item at a specific position | `insert()` |
| Remove the first matching value | `remove()` |
| Remove and retrieve an item by position | `pop()` |
| Remove by index or slice without retrieving | `del` |
| Remove all items | `clear()` |
| Find the first matching position | `index()` |
| Count matching values | `count()` |
| Reverse the existing order | `reverse()` |
| Sort the existing list | `sort()` |
| Create a separate shallow outer list | `copy()` |

Prefer the operation whose name or syntax best matches the job you are performing.

## 26. Practical example: update a study queue

```python
study_queue = ["strings", "numbers"]

study_queue.append("lists")
study_queue.insert(1, "variables")
study_queue.remove("numbers")
completed_topic = study_queue.pop(0)

print("Completed:", completed_topic)
print("Queue:", study_queue)
```

```text
Completed: strings
Queue: ['variables', 'lists']
```

The example uses different operations because the intentions differ: add at the end, insert at a position, remove by value, then remove and retrieve by position.

## 27. Practical example: repair and summarize scores

```python
scores = [8, 10, 7, 9, 10]

scores[2] = 8
scores.append(9)

print("Tens:", scores.count(10))
print("First ten index:", scores.index(10))

scores.sort()

print("Sorted:", scores)
print("Lowest:", min(scores))
print("Highest:", max(scores))
print("Total:", sum(scores))
```

```text
Tens: 2
First ten index: 1
Sorted: [8, 8, 9, 9, 10, 10]
Lowest: 8
Highest: 10
Total: 54
```

This combines Phase 2 numeric tools with the new ability to change and reorganize a list.

## 28. Common mistakes

### Assigning the result of a mutating method

`items.append(value)`, `items.sort()`, and similar in-place methods return `None`. Do not replace your list variable with that return value.

### Using `append()` when you meant `extend()`

`append(["lists", "tuples"])` adds one nested list item. `extend(["lists", "tuples"])` adds two separate items.

### Confusing value removal with position removal

`remove(value)` searches by equality. `pop(index)` and `del items[index]` work by position.

### Expecting `remove()` to delete every duplicate

`remove(value)` deletes only the first equal match.

### Expecting `pop()` to return the changed list

`pop()` returns the item that was removed, not the list.

### Assuming assignment copies a list

`second = first` creates another reference to the same list. Use `copy()` when you need a separate outer list.

### Treating `reverse()` as sorting

`reverse()` flips current order. It does not decide which value should come first according to size or alphabetic ordering.

### Sorting values that do not support ordering with one another

A list can hold mixed types even when `sort()` cannot compare those particular values.

## 29. Mutation and readable code

Mutation is useful, but a program becomes harder to reason about when a list changes in many unrelated places.

For beginner code, prefer a simple habit:

- use descriptive variable names;
- make one change for one clear reason;
- choose an operation that states the intention;
- inspect the list after experimenting with a mutation;
- avoid clever chains of operations when separate statements are easier to understand.

Later phases will give you functions, loops, and tests that make larger mutation workflows easier to organize.

## 30. Connections to earlier and later concepts

This chapter builds directly on earlier material:

- indexes and slices came from string and list reading;
- assignment already connected names to values;
- `None` was introduced as a built-in value;
- `IndexError` already appeared when reading an invalid list position;
- Boolean and numeric tools still work with appropriate list contents.

It also prepares later ideas:

- Chapter 03 will contrast mutable lists with immutable tuples;
- dictionaries and sets have their own mutation operations and rules;
- Phase 4 will use conditionals and loops to decide when and how repeated collection changes happen;
- Phase 5 functions will make it important to understand when a mutable object can be changed through a reference passed elsewhere.

## 31. Exercise: manage a learning backlog

Create `learning_backlog.py` with this starting list:

```python
backlog = ["strings", "numbers", "lists"]
```

Without using loops or conditionals:

1. replace `"numbers"` with `"numeric tools"` by index;
2. append `"tuples"`;
3. extend the list with `"dictionaries"` and `"sets"`;
4. insert `"variables"` at index `0`;
5. print how many times `"lists"` appears;
6. print the index of `"tuples"`;
7. remove `"numeric tools"` by value;
8. pop the last item and store it in `removed_topic`;
9. print the removed topic;
10. print the resulting backlog;
11. create a shallow copy named `backlog_copy`;
12. reverse only `backlog_copy`;
13. print both lists to confirm that reversing the copy did not reverse the original.

One possible final output shape is:

```text
Lists count: 1
Tuples index: 4
Removed: sets
Backlog: ['variables', 'strings', 'lists', 'tuples', 'dictionaries']
Copy: ['dictionaries', 'tuples', 'lists', 'strings', 'variables']
```

Try to predict each intermediate list before running the file.

## 32. Self-check

Before moving on, make sure you can answer these questions without guessing:

1. Why can a list item be replaced while a string character cannot?
2. What is the difference between `append()` and `extend()`?
3. What is the difference between `remove()` and `pop()`?
4. What does `pop()` return?
5. Why does `items = items.append(value)` usually break beginner code?
6. What does `clear()` change?
7. Does `reverse()` sort values?
8. What do `index()` and `count()` return?
9. Why can `second = first` make mutations visible through both names?
10. What does `copy()` separate, and what does the word *shallow* warn about?

If any answer feels fuzzy, return to the matching section and change one of the examples yourself.

## 33. Quick reference

- Replace one item: `items[index] = value`
- Replace a range: `items[start:stop] = values`
- Add one item at the end: `items.append(value)`
- Add several items: `items.extend(values)`
- Insert before a position: `items.insert(index, value)`
- Remove the first equal value: `items.remove(value)`
- Remove and return an item: `removed = items.pop()` or `removed = items.pop(index)`
- Delete by position or range: `del items[index]` or `del items[start:stop]`
- Remove every item: `items.clear()`
- Find the first equal value: `position = items.index(value)`
- Count equal values: `quantity = items.count(value)`
- Reverse in place: `items.reverse()`
- Sort in place: `items.sort()`
- Create a shallow outer copy: `other = items.copy()`

Remember the return-value pattern:

- `append()`, `extend()`, `insert()`, `remove()`, `clear()`, `reverse()`, and `sort()` change the list and return `None`.
- `pop()` changes the list and returns the removed item.
- `index()` and `count()` do not change the list and return information.
- `copy()` does not change the original list and returns a new shallow list.

## 34. Where to go next

You now know both halves of the beginner list model:

1. Create and read a list.
2. Change a list deliberately.
3. Compare mutable lists with immutable tuples.

The next Collections chapter introduces **tuples and immutability**. That comparison will make the design choice behind list mutability much clearer.

---

Official references used for technical verification:

- [Python Tutorial: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Built-in Types: Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
- [Python Built-in Types: Lists](https://docs.python.org/3/library/stdtypes.html#lists)

<div align="center">

# Sets and Unique Values

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Previous chapter: Dictionaries: keys and values](../04-dictionaries-keys-and-values/README.md) · [Back to the Collections index](../README.md) · Next chapter: Choosing the right collection

Lists and tuples organize values by position. Dictionaries organize values by keys. Sets introduce another model: a value is either **a member of the collection or it is not**.

That model is especially useful when uniqueness matters, when you want to test membership, or when you want to compare groups of values.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Collections Chapters 01 through 04 |
| Estimated study time | 120 to 150 minutes |
| Main concepts | `set`, unique elements, membership, hashable elements, `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`, union, intersection, difference, symmetric difference, subset, superset, disjoint sets, copying |

## Learning objectives

By the end of this chapter, you should be able to:

- explain what makes a set different from lists, tuples, and dictionaries;
- create empty and populated sets;
- explain why duplicate values collapse into one set element;
- convert another iterable into a set with `set()`;
- explain why sets do not support positional indexing or slicing;
- count elements with `len()`;
- test membership with `in` and `not in`;
- add one element with `add()`;
- add several elements with `update()`;
- distinguish `remove()` from `discard()`;
- explain why `pop()` does not mean "remove the last item" for a set;
- clear a set;
- recognize which values can be set elements;
- compute union, intersection, difference, and symmetric difference;
- test subset, superset, and disjoint relationships;
- distinguish another reference to the same set from a shallow copy;
- choose a set when uniqueness or membership is more important than position.

## 1. From keys to membership

The previous chapter used meaningful dictionary keys:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("track" in profile)
```

```text
True
```

For a dictionary, membership tests keys by default.

A set removes the key-value relationship entirely:

```python
topics = {"strings", "lists", "dictionaries"}

print("lists" in topics)
print("files" in topics)
```

```text
True
False
```

There is no value stored "under" `"lists"`. The value `"lists"` is itself an element of the set.

That is the central set idea:

**value → member or not a member**

## 2. What a set is

Python's built-in mutable set type is `set`.

A set is an unordered collection of **distinct hashable elements**.

```python
skills = {"python", "sql", "git"}

print(type(skills))
print(len(skills))
```

```text
<class 'set'>
3
```

Three ideas matter immediately:

- **distinct:** equal elements do not appear as separate duplicates;
- **unordered:** a set does not provide positional ordering for lookup;
- **hashable elements:** each element must be suitable for set membership lookup.

The dictionary chapter already introduced the practical meaning of *hashable*. Sets reuse the same requirement for their elements.

## 3. Set literal syntax

A non-empty set literal uses braces with comma-separated elements:

```python
languages = {"Python", "JavaScript", "SQL"}
```

This resembles dictionary braces, but there are no `key: value` pairs.

Compare the shapes:

```python
mapping = {"language": "Python"}
collection = {"Python"}

print(type(mapping))
print(type(collection))
```

```text
<class 'dict'>
<class 'set'>
```

The colon is the visual clue that the first object is a dictionary entry.

## 4. An empty set uses `set()`

Empty braces create an empty dictionary, not an empty set:

```python
empty_braces = {}
empty_set = set()

print(type(empty_braces))
print(type(empty_set))
```

```text
<class 'dict'>
<class 'set'>
```

This is one of the most important syntax differences to remember in this chapter.

Use:

```python
items = set()
```

when you need an empty set.

## 5. Duplicate values collapse

A set stores distinct elements. Repeating an equal value does not create another separate element:

```python
topics = {"lists", "sets", "lists", "sets", "tuples"}

print(len(topics))
print("lists" in topics)
print("tuples" in topics)
```

```text
3
True
True
```

The set has three distinct elements, even though five values were written in the literal.

This makes sets useful when the question is "which unique values are present?" rather than "how many times was each value entered?"

## 6. Equality is about members, not written order

Two sets are equal when they contain the same elements:

```python
first = {"python", "sql", "git"}
second = {"git", "python", "sql"}

print(first == second)
```

```text
True
```

Do not interpret this as sets "remembering a different order and ignoring it later". A set does not provide sequence-style positional order in the first place.

## 7. Sets do not support indexing

Lists and tuples support position-based lookup:

```python
items = ["python", "sql", "git"]
print(items[0])
```

```text
python
```

A set does not:

```python
items = {"python", "sql", "git"}
print(items[0])
```

The second example raises `TypeError` because sets are not subscriptable sequences.

If your program needs a stable "first", "second", or "third" item, a set is usually the wrong collection model.

## 8. Sets do not support slicing

Slicing describes a positional range, so it also does not apply to sets:

```python
items = {"python", "sql", "git"}
print(items[0:2])
```

Python raises `TypeError` because a set has no positional slice to retrieve.

This is an important contrast with strings, lists, and tuples.

## 9. Do not rely on printed set order

Because sets do not define positional or insertion order, code should not depend on the order in which multiple set elements appear when displayed.

For example, this creates a valid set:

```python
skills = {"python", "sql", "git"}
```

But this guide will not attach a fixed expected multi-element `print(skills)` output to that example.

When examples need deterministic verification, they will use membership, length, equality, or another result whose meaning does not depend on display order.

## 10. Creating a set from another iterable

The `set()` constructor can collect distinct elements from another iterable.

From a list:

```python
languages = ["Python", "SQL", "Python", "Git"]
unique_languages = set(languages)

print(len(unique_languages))
print(unique_languages == {"Python", "SQL", "Git"})
```

```text
3
True
```

The original list still contains its original values. `set(languages)` creates a new set.

## 11. Converting a string to a set

A string is iterable, so `set()` can read its characters:

```python
letters = set("banana")

print(len(letters))
print("b" in letters)
print("n" in letters)
print("z" in letters)
```

```text
3
True
True
False
```

The distinct characters are `"b"`, `"a"`, and `"n"`, but the set should not be treated as a character sequence with positions.

## 12. Using `len()` with a set

`len()` returns the number of distinct elements currently stored:

```python
permissions = {"read", "write", "export"}

print(len(permissions))
```

```text
3
```

Adding a duplicate does not increase that count.

## 13. Membership is a natural set operation

Use `in` and `not in` to test membership:

```python
completed = {"strings", "lists", "tuples"}

print("lists" in completed)
print("sets" not in completed)
```

```text
True
True
```

Membership testing is one of the main reasons sets are useful.

## 14. Adding one element with `add()`

Sets are mutable. Use `add()` to add one element:

```python
skills = {"python", "sql"}

skills.add("git")

print("git" in skills)
print(len(skills))
```

```text
True
3
```

Calling `add()` with an element that is already present leaves the membership unchanged:

```python
skills.add("python")
print(len(skills))
```

```text
3
```

`add()` mutates the set in place and returns `None`.

## 15. Adding several elements with `update()`

Use `update()` when another iterable contains several values you want to add:

```python
skills = {"python"}

skills.update(["sql", "git", "python"])

print(len(skills))
print(skills == {"python", "sql", "git"})
```

```text
3
True
```

`update()` adds the elements from the iterable. It does not add the list itself as one element.

Like `dict.update()`, set `update()` mutates the existing object and returns `None`.

## 16. `add()` and `update()` mean different things

Compare these intentions:

```python
skills = {"python"}
skills.add("sql")
```

`add()` receives one element.

```python
skills = {"python"}
skills.update(["sql", "git"])
```

`update()` reads elements from an iterable and adds them individually.

For strings, that distinction matters:

```python
letters = set()
letters.add("ab")

print("ab" in letters)
print(len(letters))
```

```text
True
1
```

But:

```python
letters = set()
letters.update("ab")

print("a" in letters)
print("b" in letters)
print(len(letters))
```

```text
True
True
2
```

The first set contains one string element, `"ab"`. The second receives the two characters from the iterable string.

## 17. Removing an element with `remove()`

`remove(element)` deletes an element that must already be present:

```python
skills = {"python", "sql", "git"}

skills.remove("git")

print("git" in skills)
print(len(skills))
```

```text
False
2
```

If the requested element is missing, `remove()` raises `KeyError`.

Use `remove()` when absence should be treated as an error rather than silently ignored.

## 18. Removing conditionally with `discard()`

`discard(element)` removes the element if it is present, but does not raise `KeyError` when it is missing:

```python
skills = {"python", "sql"}

skills.discard("git")
skills.discard("sql")

print(skills == {"python"})
```

```text
True
```

That makes `discard()` useful when "already absent" is an acceptable state.

## 19. `remove()` versus `discard()`

Both methods can remove a present element. Their missing-element behavior is the important difference:

| Method | Present element | Missing element |
|---|---|---|
| `remove(value)` | removes it | raises `KeyError` |
| `discard(value)` | removes it | leaves the set unchanged |

Both methods mutate the set in place and return `None`; neither returns the removed element.

Choose based on whether a missing value should be considered exceptional for that operation.

## 20. `pop()` removes an arbitrary element

Set `pop()` removes and returns an **arbitrary** element.

Do not transfer the list meaning of `pop()` to sets. A set has no "last element" position.

A one-element set gives us a deterministic beginner example:

```python
status = {"ready"}
removed = status.pop()

print(removed)
print(len(status))
```

```text
ready
0
```

On a set with several elements, your program should not depend on which element `pop()` chooses.

Calling `pop()` on an empty set raises `KeyError`.

## 21. Clearing a set

`clear()` removes every element while keeping the set object:

```python
skills = {"python", "sql", "git"}

skills.clear()

print(skills)
print(len(skills))
```

```text
set()
0
```

Notice how Python displays an empty set as `set()`, which also reinforces why `{}` cannot represent an empty set.

`clear()` mutates the set in place and returns `None`.

## 22. Set elements must be hashable

The same practical rule from dictionary keys applies to set elements.

Common beginner-safe set elements include:

- strings;
- integers;
- floating-point numbers;
- Booleans;
- tuples whose contents are hashable.

Lists, dictionaries, and ordinary sets are mutable and unhashable, so they cannot be elements of a set.

This works:

```python
points = {(10, 20), (30, 40)}

print((10, 20) in points)
```

```text
True
```

This does not work:

```python
invalid = {[10, 20]}
```

Python raises `TypeError` while trying to use the list as a set element.

## 23. A set cannot normally contain another set

An ordinary `set` is mutable and therefore unhashable:

```python
outer = set()
inner = {"python", "sql"}

outer.add(inner)
```

Python raises `TypeError` because `inner` is itself an ordinary set.

Python also provides `frozenset`, an immutable and hashable set type. It can be used when an immutable set-like value must itself become a dictionary key or set element:

```python
frozen_skills = frozenset({"python", "sql"})
groups = {frozen_skills}

print(frozen_skills in groups)
```

```text
True
```

This chapter focuses on ordinary mutable `set`. For now, recognize `frozenset` as the immutable counterpart rather than a new collection you must master in depth.

## 24. Union combines members

The union of two sets contains every element that appears in either set.

Use `union()`:

```python
backend = {"python", "sql"}
data = {"python", "pandas"}

combined = backend.union(data)

print(combined == {"python", "sql", "pandas"})
print(backend == {"python", "sql"})
```

```text
True
True
```

`union()` creates a new set. It does not mutate `backend` in this example.

The `|` operator expresses the same set union when both operands are sets:

```python
combined = backend | data
```

## 25. Intersection keeps shared members

The intersection contains elements present in both sets:

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

shared = backend.intersection(data)

print(shared == {"python", "sql"})
```

```text
True
```

The `&` operator is the set-operator form:

```python
shared = backend & data
```

Think of intersection as answering: **what do these groups have in common?**

## 26. Difference keeps members from one side only

Set difference is directional.

`A - B` means "elements in A that are not in B":

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

backend_only = backend.difference(data)
data_only = data.difference(backend)

print(backend_only == {"git"})
print(data_only == {"pandas"})
```

```text
True
True
```

The operator form is:

```python
backend_only = backend - data
```

Reversing the operands can change the result.

## 27. Symmetric difference keeps non-shared members

Symmetric difference contains elements that appear in either set, but not in both:

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

exclusive = backend.symmetric_difference(data)

print(exclusive == {"git", "pandas"})
```

```text
True
```

The operator form uses `^`:

```python
exclusive = backend ^ data
```

Think of this as: **which members belong to exactly one of the two groups?**

## 28. A compact operation map

For two sets `a` and `b`:

| Question | Method | Operator |
|---|---|---|
| Everything from either set | `a.union(b)` | `a | b` |
| Shared by both | `a.intersection(b)` | `a & b` |
| In `a`, not in `b` | `a.difference(b)` | `a - b` |
| In exactly one set | `a.symmetric_difference(b)` | `a ^ b` |

The method forms are often easier to read while first learning the concepts. The operators are compact once the relationships are familiar.

## 29. Subsets

A set is a subset of another when every one of its elements is contained in the other set.

```python
core = {"python", "sql"}
all_skills = {"python", "sql", "git", "testing"}

print(core.issubset(all_skills))
print(core <= all_skills)
```

```text
True
True
```

`<=` allows equality as well. `<` means a **proper subset**, so the sets must not be equal.

## 30. Supersets

A set is a superset when it contains every element of another set:

```python
core = {"python", "sql"}
all_skills = {"python", "sql", "git", "testing"}

print(all_skills.issuperset(core))
print(all_skills >= core)
```

```text
True
True
```

`>` means a proper superset, requiring the sets to be different.

Subset and superset relationships describe containment, not numeric size alone.

## 31. Disjoint sets

Two sets are disjoint when they have no elements in common:

```python
frontend = {"html", "css"}
backend = {"python", "sql"}

print(frontend.isdisjoint(backend))
```

```text
True
```

If their intersection is empty, the sets are disjoint.

This is useful when you need to ask whether two groups overlap at all.

## 32. Set methods versus operators

The method forms of union, intersection, difference, and symmetric difference accept appropriate iterables as arguments.

The operator forms such as `|`, `&`, `-`, and `^` require set-like operands.

For beginner code, using two actual sets on both sides keeps the intent clear:

```python
first = {"python", "sql"}
second = {"sql", "git"}
shared = first & second

print(shared == {"sql"})
```

```text
True
```

Do not memorize every accepted input variation now. The important idea is the set relationship each operation represents.

## 33. Another name is not a copy

Sets are mutable, so reference sharing works the same way you saw with lists and dictionaries:

```python
original = {"python", "sql"}
alias = original

alias.add("git")

print("git" in original)
print(original is alias)
```

```text
True
True
```

Both variables refer to the same set object.

## 34. Creating a shallow copy

Use `copy()` when you need a separate outer set object:

```python
original = {"python", "sql"}
copied = original.copy()

copied.add("git")

print("git" in original)
print("git" in copied)
print(original is copied)
```

```text
False
True
False
```

`set.copy()` is a shallow copy. In ordinary beginner sets, elements themselves must already be hashable, so the main lesson here is that the outer set object is separate.

## 35. Removing duplicates from another collection

Converting to a set is a compact way to obtain unique values:

```python
entries = ["python", "sql", "python", "git", "sql"]
unique_entries = set(entries)

print(len(unique_entries))
print(unique_entries == {"python", "sql", "git"})
```

```text
3
True
```

But converting to a set also abandons sequence positions and does not preserve a list-style ordering contract.

If the original order or duplicate counts matter, do not replace the original collection with a set just because duplicates exist.

## 36. When a set is a good fit

A set is often a good choice when:

- each element should appear at most once;
- membership is a central question;
- you need to compare groups through union or intersection;
- you need to find values present in one group but not another;
- positional lookup is not part of the problem.

For example, a set can represent completed topic names:

```python
completed_topics = {"strings", "lists", "tuples"}
```

The meaning is "these topics are members of the completed group", not "strings is item 0".

## 37. When a set is not a good fit

Avoid choosing a set when:

- position or slicing matters;
- duplicate occurrences carry information;
- you need key-value relationships;
- your required elements are unhashable mutable objects such as lists;
- your program depends on a stable sequence order.

A collection should reflect the relationship between the values, not simply use the shortest syntax.

## 38. Practical example: compare learning topics

Suppose two fictional study tracks share some topics and differ on others:

```python
python_track = {"python", "sql", "git", "testing"}
data_track = {"python", "sql", "pandas", "statistics"}

shared = python_track & data_track
python_only = python_track - data_track
data_only = data_track - python_track
all_topics = python_track | data_track

print("Shared is correct:", shared == {"python", "sql"})
print("Python-only is correct:", python_only == {"git", "testing"})
print("Data-only is correct:", data_only == {"pandas", "statistics"})
print("Total unique topics:", len(all_topics))
print("Python is shared:", "python" in shared)
```

```text
Shared is correct: True
Python-only is correct: True
Data-only is correct: True
Total unique topics: 6
Python is shared: True
```

The example deliberately checks membership and equality instead of depending on printed set order.

## 39. Common mistakes

### Using `{}` for an empty set

`{}` creates an empty dictionary. Use `set()` for an empty set.

### Expecting duplicates to remain

A set stores distinct elements. Equal duplicates collapse into one membership entry.

### Trying to read `set[0]`

Sets do not support positional indexing.

### Trying to slice a set

Slicing requires sequence positions. Sets do not have them.

### Relying on display order

Set display order is not a positional or insertion-order contract. Do not write logic that depends on it.

### Using `add()` when you mean `update()`

`add()` adds one element. `update()` reads elements from an iterable.

### Assuming `remove()` silently ignores missing values

`remove()` raises `KeyError` when the element is absent. `discard()` does not.

### Treating `pop()` like list `pop()`

Set `pop()` removes an arbitrary element, not the "last" one.

### Adding a list or set as an element

Set elements must be hashable. Ordinary lists and sets are not.

### Assuming conversion to `set` only removes duplicates

It also changes the collection model. You lose positional sequence behavior.

### Confusing difference direction

`a - b` means "members of `a` that are not in `b`". Reversing the operands can change the result.

### Forgetting that assignment shares the same set

`alias = original` does not copy a mutable set.

## 40. Connections to earlier and later concepts

This chapter reuses ideas you already know:

- membership operators from strings, lists, tuples, and dictionaries;
- mutability from lists and dictionaries;
- hashability from dictionary keys;
- `len()` for collection size;
- aliasing and shallow copies;
- equality comparisons.

It also prepares the next chapter:

- lists will represent ordered mutable sequences;
- tuples will represent ordered immutable sequence shapes;
- dictionaries will represent key-value mappings;
- sets will represent distinct membership-oriented groups.

The final Collections chapter will compare those four models directly and help you choose by intent.

## 41. Exercise: compare two skill groups

Create `skill_groups.py` with these starting sets:

```python
backend = {"python", "sql", "git"}
automation = {"python", "testing", "git"}
```

Without using loops or conditionals:

1. print the number of distinct elements in each set;
2. print whether `"python"` belongs to both sets by checking each membership expression;
3. create `shared` using intersection;
4. create `backend_only` using difference;
5. create `automation_only` using difference in the opposite direction;
6. create `combined` using union;
7. create `exclusive` using symmetric difference;
8. verify `shared == {"python", "git"}`;
9. verify `backend_only == {"sql"}`;
10. verify `automation_only == {"testing"}`;
11. verify `exclusive == {"sql", "testing"}`;
12. add `"apis"` to `backend`;
13. discard `"testing"` from `automation`;
14. print whether `"apis"` is now in `backend`;
15. print whether `"testing"` is still in `automation`;
16. create `backend_copy = backend.copy()`;
17. add `"linux"` only to the copy;
18. verify that `"linux"` is not in the original but is in the copy.

A possible deterministic output shape is:

```text
Backend count: 3
Automation count: 3
Python in backend: True
Python in automation: True
Shared correct: True
Backend-only correct: True
Automation-only correct: True
Exclusive correct: True
APIs in backend: True
Testing in automation: False
Linux in original: False
Linux in copy: True
```

Predict each Boolean result before running the program.

## 42. Self-check

Before moving on, make sure you can answer these questions:

1. Why is a set different from a list even when both contain several values?
2. Why does `{}` not create an empty set?
3. What happens to equal duplicate elements in a set?
4. Why can you not use `set[0]` or set slicing?
5. What do `in` and `not in` test?
6. What is the difference between `add()` and `update()`?
7. What is the difference between `remove()` and `discard()`?
8. Why should set `pop()` not be described as removing the last item?
9. What requirement must every set element satisfy?
10. Why can a tuple sometimes be a set element while a list cannot?
11. What does union contain?
12. What does intersection contain?
13. Why is set difference directional?
14. What does symmetric difference contain?
15. What does it mean for one set to be a subset of another?
16. What does `isdisjoint()` tell you?
17. Why can converting a list to a set change more than duplicate handling?
18. Why can mutations through an alias affect the original set?

If any answer feels uncertain, return to the corresponding section and change one example yourself.

## 43. Quick reference

- Empty set: `values = set()`
- Non-empty set: `values = {"a", "b"}`
- Convert an iterable: `values = set(source)`
- Count distinct elements: `len(values)`
- Membership: `item in values`
- Non-membership: `item not in values`
- Add one element: `values.add(item)`
- Add several elements: `values.update(iterable)`
- Remove, error if missing: `values.remove(item)`
- Remove if present: `values.discard(item)`
- Remove and return an arbitrary element: `item = values.pop()`
- Remove all elements: `values.clear()`
- Union: `a.union(b)` or `a | b`
- Intersection: `a.intersection(b)` or `a & b`
- Difference: `a.difference(b)` or `a - b`
- Symmetric difference: `a.symmetric_difference(b)` or `a ^ b`
- Subset: `a.issubset(b)` or `a <= b`
- Superset: `a.issuperset(b)` or `a >= b`
- Disjoint: `a.isdisjoint(b)`
- Shallow copy: `other = values.copy()`

Remember the model:

- set elements are distinct;
- set elements must be hashable;
- ordinary sets are mutable;
- sets do not provide positional indexing or slicing;
- do not rely on multi-element set display order;
- membership and group relationships are the main strengths of sets.

## 44. Where to go next

You now know all four primary collection models used in this phase:

1. **List:** ordered, mutable sequence.
2. **Tuple:** ordered, immutable sequence structure.
3. **Dictionary:** key-value mapping.
4. **Set:** unordered collection of distinct hashable members.

The final Collections chapter will bring them together in **Choosing the right collection**. Instead of learning another syntax family, you will practice deciding which model best represents the relationship between your values.

---

Official references used for technical verification:

- [Python Tutorial: Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Built-in Types: Set Types — `set`, `frozenset`](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Python Glossary: hashable](https://docs.python.org/3/glossary.html#term-hashable)

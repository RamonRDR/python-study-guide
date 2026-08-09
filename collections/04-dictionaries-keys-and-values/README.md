<div align="center">

# Dictionaries: Keys and Values

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Previous chapter: Tuples and immutability](../03-tuples-and-immutability/README.md) · [Back to the Collections index](../README.md) · Next chapter: Sets and unique values

Lists and tuples organize values by **position**. Dictionaries introduce a different model: each stored value is associated with a **key**.

That change is powerful because a key can describe what a value means. Instead of remembering that a name is at position `0`, you can ask for the value stored under the key `"name"`.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Collections Chapters 01 through 03 |
| Estimated study time | 120 to 150 minutes |
| Main concepts | mappings, keys, values, dictionary literals, lookup, `get()`, mutation, `update()`, removal, membership, insertion order, hashable keys, dictionary views, `copy()` |

## Learning objectives

By the end of this chapter, you should be able to:

- explain how a dictionary differs from a positional sequence;
- create empty and populated dictionaries;
- identify keys and their associated values;
- read a value with `dictionary[key]`;
- explain why a missing direct lookup raises `KeyError`;
- use `get()` when a missing key should return a fallback instead of raising `KeyError`;
- add a new key-value pair by assignment;
- update the value associated with an existing key;
- combine entries with `update()`;
- remove entries with `del`, `pop()`, and `clear()`;
- test key membership with `in` and `not in`;
- explain that dictionary keys are unique;
- recognize common beginner-safe key types and understand the practical meaning of *hashable*;
- inspect `keys()`, `values()`, and `items()`;
- explain insertion order without treating a dictionary like a positional sequence;
- distinguish another reference to the same dictionary from a shallow copy;
- choose a dictionary when values are naturally identified by meaningful keys.

## 1. From positions to keys

Consider a tuple that represents a fictional learner:

```python
learner = ("Ana", "Python", "beginner")

print(learner[0])
print(learner[1])
```

```text
Ana
Python
```

This works, but the meaning of positions `0` and `1` must be remembered separately.

A dictionary makes those relationships explicit:

```python
learner = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

print(learner["name"])
print(learner["track"])
```

```text
Ana
Python
```

The keys `"name"` and `"track"` describe the values they identify.

That is the central dictionary idea:

**key → value**

## 2. What a dictionary is

Python's built-in dictionary type is `dict`.

A dictionary is a **mapping**. A mapping associates keys with values instead of assigning values to numbered positions.

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
    "available": True,
}

print(type(course))
```

```text
<class 'dict'>
```

The dictionary contains three entries. Each entry has one key and one associated value.

## 3. Dictionary literal syntax

A dictionary literal uses braces with `key: value` pairs separated by commas:

```python
profile = {
    "name": "Mina",
    "city": "Lisbon",
    "active": True,
}
```

Read each pair from left to right:

- `"name"` maps to `"Mina"`;
- `"city"` maps to `"Lisbon"`;
- `"active"` maps to `True`.

For multi-line dictionaries, a trailing comma after the final entry is a common readable style.

## 4. Creating an empty dictionary

Use empty braces to create an empty dictionary:

```python
settings = {}

print(settings)
print(type(settings))
print(len(settings))
```

```text
{}
<class 'dict'>
0
```

This will matter again in the next chapter: `{}` creates an empty **dictionary**, not an empty set.

## 5. Keys and values are different roles

A key identifies an entry. A value is the information associated with that key.

```python
book = {
    "title": "A Small Python Book",
    "pages": 180,
    "finished": False,
}
```

Here:

- the keys are `"title"`, `"pages"`, and `"finished"`;
- the values are `"A Small Python Book"`, `180`, and `False`.

Values do not need to have the same type.

## 6. Reading a value with square brackets

Use a key inside square brackets to retrieve its value:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

print(profile["name"])
print(profile["level"])
```

```text
Ana
beginner
```

The square brackets may look familiar from lists and tuples, but the lookup model is different.

For a list, the expression inside the brackets is usually an integer position. For a dictionary, it is a key.

## 7. A dictionary is not positionally indexed

Insertion order does not turn a dictionary into a list.

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

print(profile[0])
```

The dictionary above has no key `0`, so this lookup raises `KeyError`.

If a dictionary actually has an integer key, that integer works because it is a key, not because it is a position:

```python
labels = {
    0: "zero",
    10: "ten",
}

print(labels[10])
```

```text
ten
```

Keep the two models separate:

- sequence: **position → value**;
- dictionary: **key → value**.

## 8. Missing keys and `KeyError`

Direct lookup requires the key to exist:

```python
profile = {
    "name": "Ana",
}

print(profile["city"])
```

Because `"city"` is missing, Python raises `KeyError`.

This is useful when a missing key represents a programming mistake or invalid assumption. Later, error-handling chapters will show how exceptions can be handled deliberately.

## 9. Reading safely with `get()`

`get()` reads a key without raising `KeyError` when the key is absent:

```python
profile = {
    "name": "Ana",
}

print(profile.get("name"))
print(profile.get("city"))
```

```text
Ana
None
```

With no explicit fallback, `get()` returns `None` for a missing key.

## 10. Providing a fallback to `get()`

Pass a second argument when another fallback value communicates the situation more clearly:

```python
profile = {
    "name": "Ana",
}

print(profile.get("city", "not provided"))
print(profile.get("level", "unknown"))
```

```text
not provided
unknown
```

The fallback is returned only when the requested key is absent. `get()` does not add that key to the dictionary.

## 11. A stored `None` and a missing key can look the same

This distinction matters:

```python
profile = {
    "nickname": None,
}

print(profile.get("nickname"))
print(profile.get("city"))
```

```text
None
None
```

The first `None` is stored in the dictionary. The second `None` is the default result for a missing key.

When your program must distinguish those cases, key membership becomes important.

## 12. Counting entries with `len()`

`len()` returns the number of key-value entries:

```python
profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

print(len(profile))
```

```text
3
```

One key and its associated value count together as one dictionary entry.

## 13. Membership checks keys by default

The `in` and `not in` operators test dictionary **keys**:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("name" in profile)
print("Python" in profile)
print("city" not in profile)
```

```text
True
False
True
```

`"Python"` is a value, not a key, so `"Python" in profile` is `False`.

To test the current values explicitly, use the values view:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("Python" in profile.values())
```

```text
True
```

## 14. Adding a new entry by assignment

Assign to a key that does not yet exist:

```python
profile = {
    "name": "Ana",
}

profile["track"] = "Python"
profile["active"] = True

print(profile)
```

```text
{'name': 'Ana', 'track': 'Python', 'active': True}
```

Unlike direct list item assignment, dictionary assignment does not require a numeric position to exist first. A new key creates a new entry.

## 15. Updating an existing value

Assign to a key that already exists to replace its associated value:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

profile["level"] = "intermediate"

print(profile)
```

```text
{'name': 'Ana', 'level': 'intermediate'}
```

The key stays the same. Its value changes.

This is dictionary mutation: dictionaries are mutable objects.

## 16. Dictionary keys are unique

A dictionary cannot contain two separate entries with equal keys at the same time.

If the same key appears more than once while constructing a dictionary, the later value becomes the value associated with that key:

```python
profile = {
    "name": "Ana",
    "name": "Mina",
}

print(profile)
```

```text
{'name': 'Mina'}
```

Although Python defines this behavior, repeating a literal key usually harms readability. Prefer one clear entry per key.

Values, by contrast, may repeat:

```python
scores = {
    "first": 10,
    "second": 10,
}

print(scores)
```

```text
{'first': 10, 'second': 10}
```

## 17. Updating several entries with `update()`

`update()` applies entries from another mapping or compatible source to the existing dictionary:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

profile.update({
    "level": "intermediate",
    "active": True,
})

print(profile)
```

```text
{'name': 'Ana', 'level': 'intermediate', 'active': True}
```

The existing `"level"` value was replaced, while `"active"` was added.

Like many in-place mutating methods you saw with lists, `dict.update()` returns `None`.

## 18. Removing an entry with `del`

Use `del` when you know the key and do not need the removed value:

```python
profile = {
    "name": "Ana",
    "temporary": True,
}

del profile["temporary"]

print(profile)
```

```text
{'name': 'Ana'}
```

If the key is missing, `del dictionary[key]` raises `KeyError`.

## 19. Removing and returning with `pop()`

`pop(key)` removes an entry and returns its value:

```python
settings = {
    "theme": "dark",
    "language": "en",
}

removed_language = settings.pop("language")

print("Removed:", removed_language)
print("Settings:", settings)
```

```text
Removed: en
Settings: {'theme': 'dark'}
```

This mirrors the useful idea from lists: `pop()` both changes the collection and gives you the removed value.

You can also supply a fallback for a missing key:

```python
settings = {
    "theme": "dark",
}

removed = settings.pop("language", "not set")

print(removed)
print(settings)
```

```text
not set
{'theme': 'dark'}
```

With a fallback, the missing key does not raise `KeyError`.

## 20. Removing every entry with `clear()`

`clear()` keeps the dictionary object but removes all of its entries:

```python
settings = {
    "theme": "dark",
    "language": "en",
}

settings.clear()

print(settings)
print(len(settings))
```

```text
{}
0
```

`clear()` mutates the dictionary in place and returns `None`.

## 21. Dictionaries preserve insertion order

Starting with Python 3.7, preserving dictionary insertion order is a guarantee of the Python language specification. CPython 3.6 also preserved insertion order, but only as an implementation detail, so Python 3.6 code should not treat that behavior as a language-wide guarantee.

That means that in Python 3.7 and later, entries are observed in the order their keys were inserted:

```python
profile = {}

profile["name"] = "Ana"
profile["track"] = "Python"
profile["level"] = "beginner"

print(profile)
```

```text
{'name': 'Ana', 'track': 'Python', 'level': 'beginner'}
```

Updating the value of an existing key does not move that key to a new position:

```python
profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

profile["track"] = "Data"

print(profile)
```

```text
{'name': 'Ana', 'track': 'Data', 'level': 'beginner'}
```

Order is useful for predictable observation, but dictionary lookup is still based on keys, not numbered positions.

## 22. What kinds of values can be keys?

Dictionary keys must be **hashable**.

For a beginner, the practical model is:

- strings are commonly used as keys;
- integers can be keys;
- Booleans can be keys, although descriptive string keys are often clearer for records;
- tuples can be keys when all of their contents are hashable;
- lists, dictionaries, and sets cannot be dictionary keys.

A hashable key has a stable hash value suitable for dictionary lookup and obeys Python's equality/hash rules. You do not need to implement hashing yourself to use ordinary dictionaries.

This works:

```python
coordinates = {
    (10, 20): "checkpoint",
}

print(coordinates[(10, 20)])
```

```text
checkpoint
```

This does not work because a list is mutable and unhashable:

```python
invalid = {
    [10, 20]: "checkpoint",
}
```

Python raises `TypeError` while trying to use the list as a key.

## 23. Dictionary values are flexible

Values do not have the same restriction as keys. A value can be a string, number, Boolean, list, tuple, another dictionary, or many other Python objects.

```python
profile = {
    "name": "Ana",
    "topics": ["strings", "lists"],
    "progress": (3, 6),
}

print(profile["topics"])
print(profile["progress"])
```

```text
['strings', 'lists']
(3, 6)
```

A mutable value inside a dictionary can still be mutated:

```python
profile = {
    "name": "Ana",
    "topics": ["strings"],
}

profile["topics"].append("lists")

print(profile)
```

```text
{'name': 'Ana', 'topics': ['strings', 'lists']}
```

The dictionary maps `"topics"` to a list, and that list has its own mutability behavior.

## 24. Inspecting keys with `keys()`

`keys()` returns a dictionary view containing the current keys:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.keys())
print(list(course.keys()))
```

```text
dict_keys(['title', 'phase', 'chapter'])
['title', 'phase', 'chapter']
```

Converting the view with `list()` is useful when you specifically need a separate list of the current keys.

## 25. Inspecting values with `values()`

`values()` returns a view of the current values:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.values())
print(list(course.values()))
```

```text
dict_values(['Python', 3, 4])
['Python', 3, 4]
```

Remember that values do not need to be unique.

## 26. Inspecting pairs with `items()`

`items()` returns a view of key-value pairs:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.items())
print(list(course.items()))
```

```text
dict_items([('title', 'Python'), ('phase', 3), ('chapter', 4)])
[('title', 'Python'), ('phase', 3), ('chapter', 4)]
```

Each pair behaves like a two-item tuple containing the key and its value.

In Phase 4, loops will make `items()` especially useful because you will be able to process those pairs one at a time.

## 27. Dictionary views reflect later changes

The objects returned by `keys()`, `values()`, and `items()` are **views**, not frozen snapshots.

```python
profile = {
    "name": "Ana",
}

keys_view = profile.keys()
profile["level"] = "beginner"

print(list(keys_view))
```

```text
['name', 'level']
```

The view reflects the current dictionary.

If you need a separate snapshot for beginner code, converting the view to a list creates a separate list at that moment.

## 28. Creating dictionaries with `dict()`

The `dict()` constructor can also create dictionaries.

Keyword-style construction is concise when the desired string keys are valid Python identifiers and are not reserved keywords:

```python
profile = dict(name="Ana", level="beginner")

print(profile)
```

```text
{'name': 'Ana', 'level': 'beginner'}
```

Because you already know tuples and lists, you can also understand a sequence of key-value pairs:

```python
pairs = [
    ("name", "Ana"),
    ("level", "beginner"),
]

profile = dict(pairs)

print(profile)
```

```text
{'name': 'Ana', 'level': 'beginner'}
```

Dictionary literals are often the clearest choice for fixed records written directly in code, but `dict()` is useful when your data already exists in another compatible form.

## 29. Another name is not a copy

Dictionaries are mutable, so the reference-sharing lesson from lists applies again:

```python
original = {
    "theme": "light",
}

alias = original
alias["theme"] = "dark"

print("Original:", original)
print("Alias:", alias)
```

```text
Original: {'theme': 'dark'}
Alias: {'theme': 'dark'}
```

Both variables refer to the same dictionary.

## 30. Creating a shallow copy with `copy()`

`copy()` creates a separate outer dictionary:

```python
original = {
    "theme": "light",
    "language": "en",
}

copied = original.copy()
copied["theme"] = "dark"

print("Original:", original)
print("Copied:", copied)
```

```text
Original: {'theme': 'light', 'language': 'en'}
Copied: {'theme': 'dark', 'language': 'en'}
```

Like list `copy()`, dictionary `copy()` is **shallow**. Nested mutable objects are still shared unless they are copied separately.

That deeper copying topic belongs later. For now, remember that `copy()` separates the outer dictionary itself.

## 31. When a dictionary is a good fit

A dictionary is often a good choice when:

- each value has a meaningful label or identifier;
- you want to retrieve information by that label;
- the relationship between fields matters more than numbered positions;
- you need to add or update fields by key.

For example:

```python
student = {
    "name": "Mina",
    "track": "Python",
    "completed_chapters": 3,
}
```

The keys make the record self-describing.

A list is usually clearer when the main idea is an ordered series of similar items. A tuple is useful when the ordered shape is intentionally fixed. The final Collections chapter will compare all four collection types directly.

## 32. Practical example: update a study profile

```python
study_profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

study_profile["level"] = "intermediate"
study_profile["active"] = True
study_profile["topics"] = ["lists", "tuples", "dictionaries"]
removed_active = study_profile.pop("active")

print("Name:", study_profile["name"])
print("Level:", study_profile.get("level"))
print("Removed active:", removed_active)
print("Keys:", list(study_profile.keys()))
print("Profile:", study_profile)
```

```text
Name: Ana
Level: intermediate
Removed active: True
Keys: ['name', 'track', 'level', 'topics']
Profile: {'name': 'Ana', 'track': 'Python', 'level': 'intermediate', 'topics': ['lists', 'tuples', 'dictionaries']}
```

This example combines lookup, update, addition, removal, and key inspection without needing loops or conditionals.

## 33. Common mistakes

### Treating a dictionary like a list

`dictionary[0]` does not mean “the first entry” unless `0` is literally a key.

### Assuming `in` searches values

`value in dictionary` tests keys. Use `value in dictionary.values()` when you intentionally need value membership.

### Using direct lookup for an optional key

`dictionary[key]` raises `KeyError` when the key is absent. `get()` can return a fallback when absence is expected.

### Forgetting that `get()` does not add the key

Reading `dictionary.get("city", "unknown")` returns the fallback but leaves the dictionary unchanged.

### Assuming every `None` from `get()` means “missing”

A key can legitimately store `None`. Use membership information when your program must distinguish those cases.

### Expecting duplicate keys to create duplicate entries

Keys are unique within one dictionary. Assigning or constructing the same key again replaces the associated value.

### Using a list as a dictionary key

Lists are unhashable and cannot be keys. Use a suitable hashable value instead.

### Forgetting that dictionaries are mutable

Another variable may refer to the same dictionary. Assignment alone does not copy it.

### Assuming `copy()` duplicates nested mutable values

`dict.copy()` is shallow. It separates the outer dictionary, not every object stored inside it.

### Confusing insertion order with positional lookup

Dictionary order is preserved, but lookup remains key-based.

## 34. Readability and key design

Good dictionary keys make data easier to understand.

Prefer keys that clearly describe the meaning of their values:

```python
profile = {
    "name": "Ana",
    "completed_chapters": 4,
    "is_active": True,
}
```

Compare that with vague keys such as `"a"`, `"b"`, and `"c"`. The shorter version may save characters but forces the reader to memorize hidden meanings.

The same naming principle from variables applies to dictionary keys: choose names that make the relationship visible.

## 35. Connections to earlier and later concepts

This chapter reuses ideas you already know:

- square brackets were introduced with sequences, but now contain keys rather than positions;
- dictionaries are mutable like lists;
- dictionary `copy()` repeats the shallow-copy idea from lists;
- tuples can serve as dictionary keys when their contents are hashable;
- lists can appear as dictionary values and keep their own mutability behavior;
- `len()` and membership operators work with a new collection model.

It also prepares later concepts:

- sets will reuse the idea of hashable values and make uniqueness central;
- Phase 4 loops will process dictionary keys, values, and key-value pairs repeatedly;
- functions will often receive or return dictionaries representing structured data;
- JSON work later in the guide will feel familiar because JSON objects resemble string-keyed mappings, although JSON and Python dictionaries are not identical concepts.

## 36. Exercise: build and maintain a learning record

Create `learning_record.py` with this starting dictionary:

```python
record = {
    "name": "Mina",
    "track": "Python",
    "level": "beginner",
}
```

Without using loops or conditionals:

1. print the value associated with `"name"` using square-bracket lookup;
2. print `"city"` with `get()` and the fallback `"not provided"`;
3. change `"level"` to `"intermediate"`;
4. add the key `"active"` with value `True`;
5. add `"topics"` with the list `["lists", "tuples"]`;
6. append `"dictionaries"` to the list stored under `"topics"`;
7. print the number of entries with `len()`;
8. print whether `"track"` is a key;
9. remove `"active"` with `pop()` and store its value in `removed_active`;
10. print `removed_active`;
11. print the keys as a list;
12. print the values as a list;
13. create a shallow copy named `record_copy`;
14. change only `record_copy["level"]` to `"advanced"`;
15. print both dictionaries and confirm that the outer `"level"` entry changed only in the copy.

One possible final output shape is:

```text
Name: Mina
City: not provided
Entries: 5
Has track: True
Removed active: True
Keys: ['name', 'track', 'level', 'topics']
Values: ['Mina', 'Python', 'intermediate', ['lists', 'tuples', 'dictionaries']]
Original: {'name': 'Mina', 'track': 'Python', 'level': 'intermediate', 'topics': ['lists', 'tuples', 'dictionaries']}
Copy: {'name': 'Mina', 'track': 'Python', 'level': 'advanced', 'topics': ['lists', 'tuples', 'dictionaries']}
```

Predict the dictionary after each mutation before running the program.

## 37. Self-check

Before moving on, make sure you can answer these questions:

1. What is the main lookup difference between a sequence and a dictionary?
2. What does `dictionary[key]` do when the key is missing?
3. What does `get()` return for a missing key when no fallback is supplied?
4. Does `get()` add a missing key?
5. What does `in` test for a dictionary by default?
6. What happens when you assign to a new key?
7. What happens when you assign to an existing key?
8. Can one dictionary contain two separate equal keys at the same time?
9. Why can a string usually be a key while a list cannot?
10. What do `keys()`, `values()`, and `items()` expose?
11. Does insertion order make integer positions valid dictionary indexes?
12. What does `pop(key)` return?
13. Why can mutations through an alias affect the original dictionary?
14. What does `copy()` separate, and what does *shallow* warn about?

If any answer feels uncertain, return to the matching section and change one example yourself.

## 38. Quick reference

- Create an empty dictionary: `data = {}`
- Create entries: `data = {"key": "value"}`
- Read an existing key: `value = data["key"]`
- Read with a fallback: `value = data.get("key", fallback)`
- Count entries: `len(data)`
- Test a key: `"key" in data`
- Test a value explicitly: `value in data.values()`
- Add or replace: `data["key"] = value`
- Apply several entries: `data.update(other)`
- Delete by key: `del data["key"]`
- Remove and return: `removed = data.pop("key")`
- Empty the dictionary: `data.clear()`
- Inspect keys: `data.keys()`
- Inspect values: `data.values()`
- Inspect key-value pairs: `data.items()`
- Create a shallow outer copy: `other = data.copy()`

Remember the model:

- keys identify entries;
- keys are unique and must be hashable;
- values may repeat and may be mutable;
- dictionaries are mutable;
- dictionaries preserve insertion order;
- preserved order does not create positional indexing.

## 39. Where to go next

You now know three different collection models:

1. **List:** ordered positions that can be changed.
2. **Tuple:** ordered positions whose tuple structure cannot be changed.
3. **Dictionary:** meaningful keys mapped to values.

The next Collections chapter introduces **sets and unique values**. Sets will remove key-value pairing and positional lookup entirely, placing uniqueness and membership at the center of the model.

---

Official references used for technical verification:

- [Python Tutorial: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Built-in Types: Mapping Types — `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Python Glossary: hashable](https://docs.python.org/3/glossary.html#term-hashable)

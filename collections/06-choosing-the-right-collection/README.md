<div align="center">

# Choosing the Right Collection

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Previous chapter: Sets and unique values](../05-sets-and-unique-values/README.md) · [Back to the Collections index](../README.md) · [View the roadmap](../../docs/roadmap.en.md)

You now know four important built-in collection models: lists, tuples, dictionaries, and sets.

The final skill in this phase is not memorizing another method. It is learning to look at a problem and ask:

**What relationship exists between these values?**

That question is more useful than choosing a collection because its syntax looks familiar.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Collections Chapters 01 through 05 |
| Estimated study time | 90 to 120 minutes |
| Main concepts | collection choice, positional data, mutability, key-value mappings, uniqueness, membership, semantic tradeoffs, nested collections |

## Learning objectives

By the end of this chapter, you should be able to:

- compare lists, tuples, dictionaries, and sets by purpose;
- identify when position is part of the meaning of the data;
- decide whether the collection itself needs to change;
- recognize when meaningful keys are clearer than numeric positions;
- recognize when uniqueness and membership are central;
- explain why dictionary insertion order does not make dictionaries positional sequences;
- explain why converting between collection types can change the data model;
- combine different collection types when different relationships exist at different levels;
- justify a collection choice in plain language;
- enter Phase 4 ready to use program flow with collections you already understand.

## 1. Start with the relationship, not the brackets

These values could be written in several collection types:

```python
values = ["python", "sql", "git"]
```

```python
values = ("python", "sql", "git")
```

```python
values = {"python", "sql", "git"}
```

The values look similar, but the collection models are not equivalent.

Before choosing, ask what the values mean together.

Do they form an ordered series? A fixed positional structure? Named fields? A group of unique members?

The answer should guide the collection choice.

## 2. The four collection models

A useful beginner summary is:

| Collection | Main model |
|---|---|
| `list` | ordered positions that can change |
| `tuple` | ordered positions whose tuple structure cannot change |
| `dict` | keys mapped to values |
| `set` | distinct members with no positional lookup |

This table describes the main relationship each collection communicates.

## 3. A first decision map

Use these questions in order:

```text
Do meaningful keys identify the values?
    yes -> dict
    no
     |
     v
Is uniqueness or membership the central idea?
    yes -> set
    no
     |
     v
Do positions and order matter?
    yes
     |
     v
Should the sequence structure change later?
    yes -> list
    no  -> tuple
```

This is a learning aid, not a complete law for every Python program. Real software can have additional constraints.

For beginner problems, however, these questions provide a strong starting point.

One edge case is worth making explicit: if meaningful keys, distinct membership, and positional order all answer no, none of these four models represents "unordered duplicate occurrences" exactly. If repeated occurrences must be preserved, a list is a practical beginner container even when its order is incidental; make clear that the order is not part of the data's meaning. If repeated occurrences do not matter, reconsider whether a set matches the problem.

## 4. Question one: do meaningful keys identify values?

Suppose you want to represent a learner's name, track, and level.

A list can store the values:

```python
learner = ["Mina", "Python", "beginner"]
```

But the meaning of each position must be remembered separately.

A dictionary makes the labels part of the model:

```python
learner = {
    "name": "Mina",
    "track": "Python",
    "level": "beginner",
}
```

If the natural question is "what is the value for this field?", a dictionary is often the clearest choice.

## 5. Dictionary order is not positional lookup

Starting with Python 3.7, preserving dictionary insertion order is a language guarantee, but that does not make dictionaries lists.

```python
profile = {
    "name": "Mina",
    "track": "Python",
}

print(profile["track"])
```

```text
Python
```

The lookup works because `"track"` is a key.

`profile[0]` does not mean "the first entry" unless `0` is literally a key in that dictionary.

Choose a dictionary for the **key-value relationship**, not because you want numbered positions.

## 6. Question two: is uniqueness the central idea?

Suppose you want to represent completed topic names and each topic should appear at most once.

A set communicates that relationship directly:

```python
completed = {"strings", "lists", "tuples"}

print("lists" in completed)
```

```text
True
```

The important question is membership: is a topic in the completed group?

If duplicate occurrences or positions matter, a set is not the right model.

## 7. Question three: do positions matter?

A list and a tuple are both positional sequences.

```python
steps = ["read", "practice", "review"]
checkpoint = (3, 4)

print(steps[0])
print(checkpoint[1])
```

```text
read
4
```

Here, position has meaning.

For `steps`, position describes the order of activities. For `checkpoint`, the two positions form a small fixed coordinate-like structure.

## 8. Question four: should the sequence structure change?

When position matters, mutability helps distinguish lists from tuples.

Use a list when adding, removing, or replacing sequence elements is part of the normal job:

```python
steps = ["read", "practice"]
steps.append("review")

print(steps)
```

```text
['read', 'practice', 'review']
```

Use a tuple when the sequence structure itself should remain fixed:

```python
checkpoint = (3, 4)

print(checkpoint)
```

```text
(3, 4)
```

Tuple immutability applies to the tuple structure. A tuple can still contain a mutable object, as you learned in Chapter 03.

## 9. List versus tuple

Use this comparison when both choices seem reasonable:

| Question | `list` | `tuple` |
|---|---|---|
| Positional sequence? | yes | yes |
| Supports indexing and slicing? | yes | yes |
| Can the sequence structure be changed? | yes | no |
| Duplicate values allowed? | yes | yes |
| Typical beginner intent | changing ordered series | fixed ordered shape |

The important distinction is not square brackets versus parentheses. It is whether mutating the sequence structure belongs to the model.

## 10. List versus set

These two often appear when several similar values must be stored.

Choose a list when:

- sequence order matters;
- duplicates may carry information;
- positional lookup matters;
- the sequence may change.

Choose a set when:

- each member should be distinct;
- membership is central;
- set relationships such as intersection or difference are useful;
- positions are not part of the meaning.

Do not replace a list with a set merely because the list happens to contain duplicates.

## 11. Tuple versus dictionary

Both can represent a small structured group, but they communicate different meanings.

A tuple emphasizes positions:

```python
version = (3, 13)

print(version[0])
```

```text
3
```

A dictionary emphasizes labels:

```python
version = {
    "major": 3,
    "minor": 13,
}

print(version["major"])
```

```text
3
```

If readers need to remember what position `0` means, meaningful keys may make a dictionary clearer.

If the positional shape itself is meaningful and compact, a tuple may be appropriate.

## 12. Dictionary versus set

Both use braces in common literal forms, but their models are very different.

A dictionary stores key-value relationships:

```python
permissions = {
    "read": True,
    "write": False,
}
```

A set stores members:

```python
permissions = {"read", "export"}
```

Ask whether each item needs an associated value.

If yes, a dictionary may fit. If the item itself is simply a member or non-member, a set may fit.

## 13. Duplicate behavior matters

Lists and tuples preserve duplicate positions:

```python
items = ["python", "python", "sql"]

print(len(items))
```

```text
3
```

Sets collapse equal duplicate members:

```python
items = {"python", "python", "sql"}

print(len(items))
```

```text
2
```

Dictionaries cannot contain two separate equal keys at the same time, although their values may repeat.

If repeated occurrences carry information, model that deliberately instead of choosing a set automatically.

## 14. Hashability matters for dictionaries and sets

Dictionary keys and set elements must be hashable.

Common beginner-safe examples include strings, integers, and tuples whose contents are hashable.

Lists cannot be dictionary keys or ordinary set elements because lists are mutable and unhashable.

This requirement can affect a collection design, but do not make hashing the first decision question. Start with the relationship between values, then check whether the chosen model accepts the values you need.

## 15. Mutability is about the collection object

Lists, dictionaries, and ordinary sets are mutable.

Tuples are immutable sequences.

But nested objects keep their own behavior.

For example:

```python
record = (
    "Mina",
    ["strings", "lists"],
)

record[1].append("tuples")

print(record)
```

```text
('Mina', ['strings', 'lists', 'tuples'])
```

The tuple structure did not change. The list stored inside it did.

This is why "tuple means nothing inside can ever change" is an inaccurate mental model.

## 16. One program can need all four collections

Different relationships can exist at different levels of the same problem.

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
}
planned_topics = ["lists", "tuples", "dictionaries", "sets"]
checkpoint = (3, 4)
completed_topics = {"lists", "tuples"}
```

Each collection communicates something different:

- `course` uses named fields;
- `planned_topics` is an ordered series that may grow;
- `checkpoint` is a fixed positional pair;
- `completed_topics` is a group of distinct members.

Using several collection types together is normal when the data relationships are different.

## 17. Nested collections are not automatically advanced

A collection can contain another collection when that reflects the data.

```python
student = {
    "name": "Mina",
    "topics": ["strings", "lists"],
}
```

The outer dictionary answers "which field?".

The inner list answers "which ordered topic items?".

Choose each layer separately. Do not force one collection type to represent every relationship in a larger structure.

## 18. The same values can justify different models

Consider the values `"python"`, `"sql"`, and `"git"`.

If they represent a study sequence:

```python
skills = ["python", "sql", "git"]
```

If they represent a fixed three-part positional snapshot:

```python
skills = ("python", "sql", "git")
```

If they represent unique completed skills:

```python
skills = {"python", "sql", "git"}
```

The values alone do not determine the collection. The **relationship and intended operations** do.

## 19. Converting types changes the model

Python lets you convert between compatible collection forms, but conversion is not merely cosmetic.

```python
entries = ["python", "sql", "python"]
unique_entries = set(entries)

print(len(entries))
print(len(unique_entries))
```

```text
3
2
```

The set no longer represents duplicate positions from the list.

Converting back to a list does not recreate information that was discarded.

Do not convert collection types only to obtain different brackets in the output.

## 20. Do not choose by syntax familiarity

A common beginner habit is to use lists for everything because lists are learned first.

Another is to use whichever collection has the shortest literal.

Both habits hide the meaning of the data.

Prefer this reasoning:

- "I need ordered positions that will change, so I chose a list."
- "I need a fixed positional structure, so I chose a tuple."
- "I need values identified by names, so I chose a dictionary."
- "I need distinct membership, so I chose a set."

A short explanation like that is a strong design habit.

## 21. Do not choose only for a method you remember

Suppose you remember `append()` well. That does not mean a list is automatically appropriate.

Suppose you remember that sets remove duplicates. That does not mean every duplicate-containing input should become a set.

Methods are operations available **after** a data model has been chosen.

Choose the relationship first, then use the operations that belong to that collection.

## 22. A practical comparison table

| Need | Strong first candidate |
|---|---|
| Ordered series that will change | `list` |
| Fixed positional sequence | `tuple` |
| Named fields or identifiers | `dict` |
| Distinct members and membership tests | `set` |
| Duplicate occurrences must remain | `list` or `tuple` |
| Key associated with a value | `dict` |
| Union/intersection/difference between groups | `set` |
| Numeric position is part of the meaning | `list` or `tuple` |

"Strong first candidate" is deliberate wording. Software design can involve more context than one table can capture.

## 23. Scenario: shopping steps

Imagine these steps:

1. choose items;
2. review cart;
3. pay.

If the program needs to preserve this order and may insert another step later, a list is a natural model:

```python
steps = ["choose items", "review cart", "pay"]
```

The position and ability to change the sequence both matter.

## 24. Scenario: a coordinate

A two-part coordinate has a small fixed positional shape:

```python
point = (10, 20)
```

The first and second positions have established roles, and changing the number of coordinate parts is not the normal operation.

A tuple communicates that fixed sequence shape well.

## 25. Scenario: a profile

A profile has named fields:

```python
profile = {
    "name": "Mina",
    "level": "beginner",
}
```

The labels are more meaningful than saying that the name must always be remembered as item `0`.

A dictionary makes the field relationship explicit.

## 26. Scenario: supported features

Suppose the important question is whether a feature belongs to a supported group:

```python
supported = {"export", "search", "sync"}

print("search" in supported)
```

```text
True
```

A set communicates distinct membership directly.

## 27. Practical example: four models together

The approved example `collection_models.py` uses one collection for each relationship:

```python
tasks = ["read", "practice", "review"]
checkpoint = (3, 4)
profile = {"name": "Mina", "track": "Python"}
completed = {"strings", "lists", "tuples"}

print(tasks[0])
print(checkpoint[1])
print(profile["track"])
print("lists" in completed)
```

```text
read
4
Python
True
```

The syntax differs because the questions differ.

## 28. Practical example: mutability tradeoffs

`collection_tradeoffs.py` reinforces which outer collection structures can change:

```python
planned_topics = ["strings", "lists", "tuples"]
fixed_version = (3, 13)
student = {"name": "Mina", "active": False}
skills = {"python", "git"}

planned_topics.append("dictionaries")
student["active"] = True
skills.add("sql")

print(len(planned_topics))
print(fixed_version[0])
print(student["active"])
print("sql" in skills)
```

```text
4
3
True
True
```

The tuple is read positionally but not structurally mutated.

## 29. Practical example: a small study workspace

`study_workspace.py` combines the collection models in one fictional program:

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
}
planned_topics = ["lists", "tuples", "dictionaries", "sets"]
checkpoint = (3, 4)
completed_topics = {"lists", "tuples"}

planned_topics.append("collection choices")
course["status"] = "in progress"
completed_topics.add("dictionaries")

print(course["title"])
print(planned_topics[0])
print(checkpoint)
print("dictionaries" in completed_topics)
print(len(completed_topics))
```

```text
Python Study Guide
lists
(3, 4)
True
3
```

No collection is competing with the others. Each one handles a different relationship.

## 30. Common mistakes

### Using a list for every problem

Lists are flexible, but flexibility does not make them the clearest model for named fields or unique membership.

### Using a tuple only because the data is short

Length alone does not determine tuple suitability. The important question is whether a fixed positional sequence is meaningful.

### Treating dictionary insertion order as list indexing

Dictionaries preserve insertion order, but direct lookup is by key.

### Using a set when duplicate occurrences matter

A set removes equal duplicate membership. That can discard information.

### Choosing a set because its membership tests are attractive

First confirm that distinct, non-positional membership matches the problem itself.

### Assuming tuple immutability freezes nested objects

The tuple structure is immutable. Mutable objects stored inside it retain their own behavior.

### Converting collections without considering lost meaning

Changing the type can change duplicate handling, positional behavior, mutability, or lookup style.

### Forcing one collection type at every nesting level

Choose each layer according to the relationship at that layer.

## 31. A collection-choice checklist

Before writing the collection literal, ask:

1. Are values identified by meaningful names or keys?
2. Is distinct membership the main relationship?
3. Do numeric positions matter?
4. Does sequence order matter?
5. Should the outer collection change later?
6. Must duplicate occurrences be preserved?
7. Do the desired dictionary keys or set elements satisfy hashability requirements?
8. Would another reader understand the relationship from the chosen type?

You will not always need all eight questions, but they make hidden assumptions visible.

## 32. Exercise: choose before you code

For each scenario, choose `list`, `tuple`, `dict`, or `set` and write one sentence explaining why.

1. An ordered reading queue that will receive new books.
2. A fixed `(width, height)` pair.
3. A user interface theme with named settings such as `"font_size"` and `"dark_mode"`.
4. A group of unique enabled feature names.
5. The ordered results of three attempts where repeated scores must remain.
6. A fixed RGB triplet such as `(255, 128, 0)`.
7. A product record identified by fields such as `"name"`, `"price"`, and `"available"`.
8. Two groups whose shared members must be compared with intersection.
9. A sequence of lesson titles that may be reordered later.
10. A small fixed pair representing a start and end position.

Then create `collection_choice_practice.py` containing one original example of each collection type. Do not use loops or conditionals.

For each variable, add a short written explanation below your code describing why that collection matches the relationship.

## 33. Exercise extension: combine the models

Create a fictional study planner with:

- a dictionary for named course information;
- a list for ordered planned topics;
- a tuple for a fixed two-number checkpoint;
- a set for unique completed topics.

Perform at least one beginner-safe operation appropriate to each collection.

Examples of appropriate operations include:

- reading a dictionary value by key;
- appending to the list;
- reading a tuple position;
- checking membership in the set.

The goal is not to use every method. The goal is to make each collection's role obvious.

## 34. Self-check

Before completing Phase 3, make sure you can answer these questions:

1. What relationship does a list communicate best?
2. What important structural difference separates a tuple from a list?
3. When are dictionary keys clearer than numeric positions?
4. What relationship is central to a set?
5. Do dictionaries preserve insertion order?
6. Does that make dictionaries positionally indexed sequences?
7. Which collection types preserve duplicate occurrences naturally?
8. Why can converting a list to a set discard information?
9. What must dictionary keys and set elements satisfy?
10. Can a tuple contain a mutable object?
11. Why might one program use all four collection types?
12. What should you ask before choosing based on syntax?

If any answer is uncertain, return to the chapter that introduced that collection and change one example yourself.

## 35. Quick reference

- Changing ordered sequence: `list`
- Fixed positional sequence structure: `tuple`
- Meaningful key-value relationships: `dict`
- Distinct membership-oriented group: `set`
- Lists, tuples, and strings support positional sequence operations.
- Dictionaries use keys for direct lookup.
- Sets do not provide positional indexing or slicing.
- Lists, dictionaries, and ordinary sets are mutable.
- Tuple structure is immutable.
- Dictionary keys and set elements must be hashable.
- Duplicate occurrences remain meaningful in lists and tuples.
- Set members are distinct.
- Dictionary keys are unique, while dictionary values may repeat.
- Conversion between collection types can change the data model.
- Nested structures can use different collection types at different levels.

## 36. Phase 3 mental model

The entire Collections phase can now be summarized as:

```text
list  -> ordered positions that can change
tuple -> ordered positions with an immutable tuple structure
dict  -> key -> value relationships
set   -> distinct membership without positional lookup
```

And the final design rule is:

**Choose the collection that makes the relationship between the values easiest to understand.**

## 37. Where to go next

You have completed the core collection models for Phase 3.

Phase 4 introduces **program flow**: `if`, `elif`, `else`, `for`, `while`, and related tools.

That next phase will become much easier because loops and conditions will operate on collection structures whose meaning you already understand.

Instead of learning "how to loop over mysterious brackets", you will know what the collection represents before controlling how the program moves through it.

---

Official references used for technical verification:

- [Python Tutorial: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)

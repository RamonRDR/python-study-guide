<div align="center">

# Specialized Containers and Collection Contracts

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Standard Library](../README.md) · [← Previous chapter: Logging](../05-logging/README.md)

Phase 3 introduced the four general-purpose collection models: `list`, `tuple`, `dict`, and `set`. This chapter does not replace those built-ins. It studies the `collections` module as a set of specialized containers for cases where the **operations you need** are more specific than the general container model.

The central question is:

```text
What behavior is the data structure promising,
and does that behavior match the operations my program performs most often?
```

A specialized container is useful when its semantics make intent clearer, reduce custom bookkeeping, or provide a better performance contract for a particular access pattern.

**Estimated study time:** 150–190 minutes.

**Python requirement:** Python 3.10 or newer for the core material and executable examples. Version-sensitive notes identify later changes when they matter.

**Documentation baseline:** behavior and version notes were checked against the official Python 3.14 `collections`, `collections.abc`, and `typing` documentation.

## Learning objectives

By the end of this chapter, you should be able to:

- explain why `collections` complements rather than replaces built-in containers;
- use `Counter` as a tally and multiset abstraction;
- reason about zero, negative, and missing counts in a `Counter`;
- use `defaultdict` without accidentally creating keys during reads;
- choose `deque` for efficient operations at both ends and bounded history windows;
- explain the difference between deque endpoint access and middle indexing;
- use `namedtuple()` when tuple compatibility and named fields are both useful;
- distinguish `namedtuple()` from `typing.NamedTuple` and `dataclass` use cases;
- use `ChainMap` for layered mappings without eagerly copying them;
- understand why `ChainMap` reads across the chain but writes only to the first mapping;
- explain when `OrderedDict` still has behavior that a regular `dict` does not express as directly;
- recognize `UserDict`, `UserList`, and `UserString` as wrapper-oriented extension bases;
- use `collections.abc` to reason about collection interfaces rather than concrete implementations;
- choose specialized containers by semantics and access patterns instead of novelty.

## 1. What this chapter adds after Phase 3

Phase 3 taught the core shapes:

```python
items = ["alpha", "beta"]
point = (10, 20)
settings = {"mode": "safe"}
tags = {"python", "study"}
```

Those remain the default choices for most programs.

The `collections` module becomes useful when a program needs a stronger contract:

```text
count repeated values                -> Counter
create missing values from a factory -> defaultdict
append and pop efficiently at both ends -> deque
layer mappings without copying       -> ChainMap
keep tuple behavior with named fields -> namedtuple
reorder mapping keys deliberately    -> OrderedDict
extend container behavior via wrappers -> UserDict/UserList/UserString
reason about interfaces              -> collections.abc
```

The goal is not to memorize exotic names. The goal is to recognize the operation pattern that makes one structure a better fit than another.

## 2. Start with the operation contract

A data structure choice should answer questions such as:

- Is lookup by key or by position?
- Does missing data mean error, zero, or create-a-default?
- Are writes concentrated at one end, both ends, or random positions?
- Is the structure a snapshot or a live view over other mappings?
- Does order affect equality or only iteration?
- Must the object remain tuple-compatible?

If a regular built-in already communicates the intended contract clearly, prefer the built-in.

Specialization is useful when it removes ambiguity.

## 3. Import only what makes the design clearer

A common style is to import the specific container names used by the module:

```python
from collections import ChainMap, Counter, defaultdict, deque, namedtuple
```

For abstract interfaces, import from the dedicated submodule:

```python
from collections.abc import Iterable, Mapping, Sequence
```

`collections.abc` is related to `collections`, but it serves a different purpose: interfaces and protocols rather than concrete specialized storage.

# Part I: `Counter`

## 4. `Counter` models tallies

`Counter` is a `dict` subclass designed around counts of hashable objects.

```python
from collections import Counter

counts = Counter(["ok", "ok", "retry", "ok", "failed"])
print(counts)
```

A typical representation is:

```text
Counter({'ok': 3, 'retry': 1, 'failed': 1})
```

The keys are the counted elements and the values are their counts.

## 5. Construct a `Counter` from elements, mappings, or keywords

```python
from collections import Counter

from_elements = Counter("banana")
from_mapping = Counter({"red": 3, "blue": 1})
from_keywords = Counter(red=3, blue=1)
```

The first form counts occurrences. The mapping and keyword forms treat the supplied values as counts.

## 6. A missing key has count zero

Unlike a regular dictionary lookup, a missing `Counter` key returns `0`:

```python
from collections import Counter

counts = Counter({"ready": 4})
print(counts["missing"])
```

Output:

```text
0
```

This makes incremental counting convenient because callers do not need to initialize every possible key first.

## 7. A zero count is not the same as a missing entry

Assigning zero does not delete a key:

```python
from collections import Counter

counts = Counter(a=2)
counts["a"] = 0

print("a" in counts)
del counts["a"]
print("a" in counts)
```

Output:

```text
True
False
```

This distinction matters when inspecting keys or serializing the counter.

## 8. `total()` sums all counts

Python 3.10 added `Counter.total()`:

```python
from collections import Counter

counts = Counter(success=8, retry=2, failed=1)
print(counts.total())
```

Output:

```text
11
```

The total includes the numeric counts as stored, including negative values if present.

## 9. `most_common()` preserves first-seen order for ties

```python
from collections import Counter

counts = Counter(["b", "a", "b", "a", "c"])
print(counts.most_common())
```

Elements with equal counts keep their first-encounter order.

Do not silently treat ties as alphabetically sorted unless your program explicitly sorts them afterward.

## 10. `Counter.update()` adds counts

`Counter.update()` does not behave like `dict.update()`.

```python
from collections import Counter

counts = Counter(a=2)
counts.update(a=3, b=1)
print(counts)
```

The result contains `a=5`, not `a=3`.

This is a tally operation, not replacement semantics.

## 11. `subtract()` keeps signed results

```python
from collections import Counter

balance = Counter(apples=5, pears=1)
balance.subtract(apples=2, pears=3)
print(balance)
```

`Counter` allows zero and negative counts. That is useful for deltas, balances, and intermediate calculations.

## 12. Multiset arithmetic filters non-positive results

The arithmetic operators have a different output contract from `subtract()`:

```python
from collections import Counter

required = Counter(a=4, b=2)
actual = Counter(a=1, b=5)

print(required - actual)
print(required + actual)
print(required & actual)
print(required | actual)
```

For these multiset operations, the result excludes counts that are zero or negative.

That makes subtraction convenient for questions such as "what is still missing?".

## 13. Unary `+` and `-` normalize signed counters

```python
from collections import Counter

counts = Counter(a=3, b=0, c=-2)
print(+counts)
print(-counts)
```

Unary `+` keeps positive counts. Unary `-` keeps the positive magnitudes of negative counts.

This can be clearer than manually filtering a signed counter.

## 14. Counter comparisons treat missing counts as zero

Since Python 3.10, rich comparisons support equality and multiset inclusion relationships.

```python
from collections import Counter

left = Counter(a=1)
right = Counter(a=1, b=0)

print(left == right)
```

Output:

```text
True
```

A missing element is treated as if its count were zero for these comparisons.

## 15. Counter values are not restricted to positive integers

The class itself does not enforce only positive integer counts. Many operations accept other numeric values.

However, methods have their own contracts. For example, `elements()` requires counts that can be interpreted as repetition counts and ignores counts below one.

Do not assume every `Counter` method supports arbitrary numeric types equally.

## 16. Use a regular `dict` when you are not counting

If the value associated with a key is a state, object, timestamp, configuration, or arbitrary record rather than a tally, a regular dictionary usually communicates intent better.

`Counter` should answer a counting or multiset question.

# Part II: `defaultdict`

## 17. `defaultdict` models missing-value creation

`defaultdict` is a `dict` subclass with a `default_factory`.

```python
from collections import defaultdict

groups = defaultdict(list)
groups["blue"].append("item-1")
print(groups)
```

When `groups["blue"]` is missing, `list()` is called, the new list is inserted, and that list is returned.

## 18. The factory is a callable, not a pre-created value

Correct:

```python
from collections import defaultdict

rows = defaultdict(list)
counts = defaultdict(int)
```

The factory is called when needed.

Passing `list()` instead of `list` would pass an already-created list, which is not the required factory callable.

## 19. `__missing__()` is triggered by `__getitem__()`

The missing-value behavior is tied to bracket lookup:

```python
from collections import defaultdict

values = defaultdict(list)
values["new"].append(1)
```

The `dict.__getitem__()` path invokes the subclass's `__missing__()` method, which calls the factory when appropriate.

## 20. `get()` does not call the default factory

This is one of the most important `defaultdict` contracts:

```python
from collections import defaultdict

values = defaultdict(list)

print(values.get("missing"))
print("missing" in values)
```

Output:

```text
None
False
```

`get()` behaves like normal `dict.get()` and does not create the key.

## 21. Membership tests do not create keys

```python
from collections import defaultdict

values = defaultdict(int)
print("x" in values)
print(values)
```

A membership test is observational. It does not invoke the factory.

## 22. Bracket reads can mutate the mapping

This line looks like a read:

```python
value = values["missing"]
```

With a `defaultdict`, it may also insert `"missing"`.

That is a semantic difference from a normal dictionary and a common source of accidental keys.

If you want to inspect without creating, use membership tests or `get()` as appropriate.

## 23. `defaultdict(list)` is a natural grouping tool

```python
from collections import defaultdict

by_category = defaultdict(list)

for category, value in [("a", 1), ("b", 2), ("a", 3)]:
    by_category[category].append(value)

print(dict(by_category))
```

This avoids a repeated initialize-if-missing branch.

## 24. `defaultdict(int)` is useful for simple counting

```python
from collections import defaultdict

counts = defaultdict(int)

for word in ["red", "blue", "red"]:
    counts[word] += 1
```

For pure frequency counting, `Counter` usually expresses the goal more directly. `defaultdict(int)` remains useful when counting is only one part of a larger mapping workflow.

## 25. Factories can encode richer defaults

```python
from collections import defaultdict


def new_state() -> dict[str, int]:
    return {"attempts": 0, "successes": 0}


state = defaultdict(new_state)
state["worker-a"]["attempts"] += 1
```

Use a named factory when the initialization policy deserves a name or is more complex than a built-in constructor.

## 26. Merge operators do not mean "run the factory"

`defaultdict` supports the mapping merge operators introduced for dictionaries.

Merging combines mapping contents. Missing-key creation still happens only through the normal `default_factory` / `__missing__()` path.

Do not confuse merge behavior with missing-value behavior.

# Part III: `deque`

## 27. `deque` is a double-ended queue

A `deque` supports efficient appends and pops from both ends.

```python
from collections import deque

queue = deque(["a", "b"])
queue.append("c")
print(queue.popleft())
```

This is the standard-library structure to reach for when both ends are active parts of the algorithm.

## 28. Endpoint operations are approximately O(1)

The official documentation describes appends and pops on either side as approximately O(1).

By contrast, removing the first element of a list with `pop(0)` requires shifting the remaining elements and is O(n).

For FIFO queues, prefer:

```python
from collections import deque

queue = deque()
queue.append("job-1")
job = queue.popleft()
```

rather than repeatedly using `list.pop(0)`.

## 29. `maxlen` creates a bounded history window

```python
from collections import deque

recent = deque(maxlen=3)

for value in [10, 20, 30, 40, 50]:
    recent.append(value)

print(list(recent))
```

Output:

```text
[30, 40, 50]
```

Once full, adding at one end discards items from the opposite end.

## 30. Bounded `append()` eviction differs from bounded `insert()`

A full bounded deque accepts endpoint appends by discarding from the opposite side.

An `insert()` that would grow a bounded deque beyond `maxlen` raises `IndexError` instead.

The two operations intentionally have different contracts.

## 31. `extendleft()` reverses input order

```python
from collections import deque

values = deque([4])
values.extendleft([1, 2, 3])
print(list(values))
```

Output:

```text
[3, 2, 1, 4]
```

Each element is appended to the left in sequence, so the iterable appears reversed.

## 32. `rotate()` moves the logical endpoints

```python
from collections import deque

values = deque([1, 2, 3, 4])
values.rotate(1)
print(list(values))
values.rotate(-2)
print(list(values))
```

Positive values rotate right; negative values rotate left.

This is useful for cyclic scheduling and algorithms where the current front changes repeatedly.

## 33. Deque indexing is not a list replacement

Deque indexed access is O(1) near both ends but slows to O(n) toward the middle.

If the dominant operation is random positional access, a list is usually a better fit.

Use a deque because of endpoint behavior, not because it happens to support `d[index]`.

## 34. Thread-safe endpoint operations are not a whole transaction model

The official documentation describes deque appends and pops as thread-safe.

That does not mean a multi-step sequence of operations automatically becomes one atomic business transaction.

For example, a "check then pop then update another structure" workflow can still require explicit synchronization if multiple threads must observe the entire sequence consistently.

Use the narrow guarantee for what it says, not as a substitute for concurrency design.

## 35. Empty pops raise `IndexError`

```python
from collections import deque

queue = deque()

try:
    queue.popleft()
except IndexError:
    print("queue is empty")
```

Choose whether emptiness is an expected branch or an exceptional condition in your own application contract.

# Part IV: `namedtuple()`

## 36. `namedtuple()` gives tuple positions names

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
point = Point(10, 20)

print(point.x)
print(point[0])
```

The object remains tuple-like: indexable, iterable, unpackable, and immutable in the tuple sense.

The named fields improve readability when positions have stable meanings.

## 37. The factory creates a new tuple subclass

`namedtuple()` is not creating a single record. It creates a class.

```python
from collections import namedtuple

Coordinate = namedtuple("Coordinate", "latitude longitude")
a = Coordinate(10.0, 20.0)
b = Coordinate(30.0, 40.0)
```

`Coordinate` is the generated tuple subclass; `a` and `b` are instances.

## 38. Defaults apply to the rightmost fields

```python
from collections import namedtuple

Account = namedtuple("Account", ["name", "active"], defaults=[True])
print(Account("demo"))
```

A field with a default cannot precede a required field in the generated call signature.

## 39. `rename=True` repairs invalid or duplicate field names

```python
from collections import namedtuple

Row = namedtuple("Row", ["name", "class", "name"], rename=True)
print(Row._fields)
```

Use this when field names come from an external schema you do not fully control.

When you control the schema, explicit valid names are usually clearer than relying on automatic renaming.

## 40. Named tuples are immutable records

You cannot assign to a field:

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
point = Point(1, 2)

updated = point._replace(x=10)
print(updated)
```

`_replace()` returns a new instance.

Starting in Python 3.13, invalid keyword arguments passed to `_replace()` raise `TypeError` rather than `ValueError`.

## 41. `_asdict()` returns a regular dictionary

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
point = Point(1, 2)
print(point._asdict())
```

Since Python 3.8, `_asdict()` returns a normal `dict`, not an `OrderedDict`.

## 42. `_fields` and `_field_defaults` support introspection

```python
from collections import namedtuple

Record = namedtuple("Record", "key enabled", defaults=[False])
print(Record._fields)
print(Record._field_defaults)
```

The leading underscores are part of the named-tuple API and exist to reduce collisions with user field names.

## 43. Bind the generated class to its type name for pickling

The official documentation recommends assigning the generated named-tuple class to a variable that matches `typename` when pickling support matters:

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
```

Dynamic class generation can interact with serialization and importability. Prefer module-level definitions for reusable record types.

## 44. `typing.NamedTuple` is the typed sibling

When static field annotations are a central part of the design, class-based `typing.NamedTuple` is often clearer:

```python
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int
```

It preserves tuple semantics while expressing field types directly.

## 45. A dataclass is not just a newer named tuple

Choose by semantics:

```text
need tuple compatibility, indexing, unpacking -> namedtuple / NamedTuple
need a record-oriented class with generated methods and flexible class semantics -> dataclass
```

Do not migrate automatically just because both tools create compact record-like objects.

# Part V: `ChainMap`

## 46. `ChainMap` creates a live view over mappings

```python
from collections import ChainMap

defaults = {"mode": "safe", "retries": 2}
overrides = {"mode": "fast"}

config = ChainMap(overrides, defaults)
print(config["mode"])
print(config["retries"])
```

Lookups search the mappings from first to last until a key is found.

## 47. ChainMap stores mappings by reference

```python
from collections import ChainMap

base = {"region": "global"}
config = ChainMap({}, base)

base["region"] = "test"
print(config["region"])
```

Output:

```text
test
```

A `ChainMap` is not an eager flattened copy. Changes to underlying mappings remain visible.

## 48. Writes and deletions target only the first mapping

```python
from collections import ChainMap

local = {}
defaults = {"retries": 3}
config = ChainMap(local, defaults)

config["retries"] = 1
print(local)
print(defaults)
```

Output:

```text
{'retries': 1}
{'retries': 3}
```

Lookup precedence and write destination are intentionally asymmetric.

## 49. `new_child()` creates a new writable front layer

```python
from collections import ChainMap

base = ChainMap({"mode": "safe"})
child = base.new_child({"mode": "fast"})

print(child["mode"])
print(base["mode"])
```

This models nested scopes and temporary override layers naturally.

## 50. `parents` skips the first mapping

`chain.parents` returns a new `ChainMap` over all mappings except the first.

This is useful when the first layer represents the current local scope and you need the enclosing view.

## 51. Iteration order is not lookup order

Lookups search first to last.

Iteration order is determined by scanning mappings from last to first while applying mapping-style overwrite semantics.

This can surprise code that assumes "first searched" also means "first iterated".

Test the contract you actually depend on.

## 52. Flatten explicitly when you need a snapshot

```python
from collections import ChainMap

config = ChainMap({"mode": "fast"}, {"mode": "safe", "retries": 2})
snapshot = dict(config)
```

The regular dictionary is independent as a mapping snapshot of the resolved values at that moment.

Use `ChainMap` when live layering is the feature. Use a merged dictionary when a standalone resolved snapshot is the feature.

# Part VI: `OrderedDict`

## 53. Regular dictionaries already preserve insertion order

Insertion order has been guaranteed for regular dictionaries since Python 3.7.

Therefore, "I need keys to stay in insertion order" is usually **not** enough reason to choose `OrderedDict` today.

## 54. `OrderedDict` specializes in reordering

It still provides behavior designed around deliberate order manipulation:

```python
from collections import OrderedDict

items = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
items.move_to_end("a")
items.move_to_end("c", last=False)
print(list(items))
```

Frequent endpoint reordering is one of the remaining reasons to consider it.

## 55. `OrderedDict` equality can be order-sensitive

Two `OrderedDict` objects compare equal only when their key-value pairs and their order match.

Regular dictionary equality ignores insertion order.

This semantic difference matters when order is part of the value contract rather than only a presentation detail.

## 56. `popitem(last=False)` expresses FIFO removal directly

`OrderedDict.popitem()` accepts `last=True` or `last=False`.

A regular dict's `popitem()` removes the most recently inserted item. `OrderedDict` has a direct API for choosing either end.

If you do not need these specialized reordering semantics, prefer a regular dictionary.

# Part VII: Extension wrappers and collection interfaces

## 57. `UserDict`, `UserList`, and `UserString` wrap built-ins

These classes provide wrapper-oriented bases whose underlying data is available through `.data`.

```python
from collections import UserDict


class NormalizedKeys(UserDict):
    def __setitem__(self, key: str, value: object) -> None:
        super().__setitem__(key.strip().lower(), value)
```

They can be easier to extend consistently than subclassing a built-in directly when you want to intercept many operations through a controlled wrapper abstraction.

## 58. Wrapper bases are a design choice, not a requirement

Modern Python allows direct subclassing of `dict`, `list`, and `str` in many situations.

The `User*` classes remain useful when access to the wrapped `.data` container and their extension model make customization simpler.

Prefer composition or a purpose-built class when your object is not conceptually a general-purpose collection.

## 59. `collections.abc` models interfaces

```python
from collections.abc import Mapping, Sequence

print(isinstance({"a": 1}, Mapping))
print(isinstance([1, 2, 3], Sequence))
```

ABCs let code ask "does this object satisfy a mapping/sequence-like interface?" rather than "is this exactly a dict/list?".

This supports more flexible APIs.

## 60. `Iterable` checks have an important limitation

`isinstance(obj, Iterable)` recognizes registered iterables and objects with `__iter__()`.

It does not reliably detect every legacy object that can iterate through `__getitem__()`.

The official documentation states that the only reliable way to determine whether an object is iterable is to call `iter(obj)` and handle failure.

## 61. ABC mixins can have performance consequences

Some `Sequence` mixin methods repeatedly call `__getitem__()`.

If a custom sequence implements `__getitem__()` in O(n), inherited mixins such as iteration can become O(n²).

An interface can provide correct behavior while still having the wrong performance contract for a particular implementation.

# Choosing and combining the tools

## 62. Decision table

| Need | Prefer | Main reason |
|---|---|---|
| Count hashable values | `Counter` | Tally and multiset semantics |
| Group/create missing values | `defaultdict` | Factory-backed missing-key policy |
| FIFO queue or both-end operations | `deque` | Efficient endpoint operations |
| Keep only recent N values | `deque(maxlen=N)` | Automatic opposite-end eviction |
| Tuple-compatible record with field names | `namedtuple` / `NamedTuple` | Named fields plus tuple semantics |
| Layer mappings with live precedence | `ChainMap` | View instead of eager merge |
| Frequent mapping reordering | `OrderedDict` | Reordering-focused API |
| Extend collection through wrapper behavior | `UserDict` / `UserList` / `UserString` | Controlled underlying `.data` |
| Accept an interface, not one concrete type | `collections.abc` | Protocol-oriented design |

## 63. Use specialized structures together only when each has a job

A program might legitimately use:

```text
Counter      -> summarize frequencies
deque        -> retain recent events
ChainMap     -> resolve layered configuration
```

That does not mean every data structure in the program should come from `collections`.

Specialization should make the model simpler, not decorate it with unfamiliar types.

## 64. Common mistakes

### Using `Counter` as a generic dictionary

If values are not counts, use a mapping designed for arbitrary values.

### Assuming `Counter.update()` replaces values

It adds counts.

### Assuming a zero `Counter` value removes the key

Use `del` if the key must disappear.

### Reading `defaultdict[key]` only to check whether a key exists

That can create the key.

### Expecting `defaultdict.get()` to invoke the factory

It does not.

### Using `list.pop(0)` for a long-lived FIFO queue

Use `deque.popleft()` when the queue grows and shrinks from the front.

### Treating deque middle indexing as O(1)

Use lists for fast random positional access.

### Assuming `extendleft()` preserves the iterable order

It reverses the visible order.

### Expecting `ChainMap` writes to update the mapping where a key was found

Writes go to the first mapping only.

### Using `OrderedDict` only because dictionaries must preserve insertion order

Regular dictionaries already do.

## 65. Practical example: capacity reconciliation with `Counter`

```python
from collections import Counter

required = Counter({"sensor": 4, "cable": 3, "case": 2})
packed = Counter({"sensor": 4, "cable": 1, "case": 3})

missing = required - packed
surplus = packed - required

print(f"required units: {required.total()}")
print(f"missing: {dict(missing)}")
print(f"surplus: {dict(surplus)}")
```

Expected output:

```text
required units: 9
missing: {'cable': 2}
surplus: {'case': 1}
```

The data model communicates that these mappings are quantities, not arbitrary key-value state.

## 66. Practical example: grouping with `defaultdict`

```python
from collections import defaultdict

records = [
    ("billing", "INV-101"),
    ("support", "REQ-203"),
    ("billing", "INV-102"),
]

by_team = defaultdict(list)

for team, reference in records:
    by_team[team].append(reference)
```

The factory removes initialization boilerplate while keeping grouping intent visible.

## 67. Practical example: recent history with a bounded deque

```python
from collections import deque

recent = deque(maxlen=3)

for event in ["boot", "load-config", "connect", "ready"]:
    recent.append(event)

print(list(recent))
```

Expected output:

```text
['load-config', 'connect', 'ready']
```

No explicit "if full, remove oldest" branch is required.

## 68. Practical example: configuration precedence with `ChainMap`

```python
from collections import ChainMap

defaults = {"mode": "safe", "retries": 2}
environment = {"retries": 4}
command_line = {"mode": "fast"}

config = ChainMap(command_line, environment, defaults)

print(config["mode"])
print(config["retries"])
```

Expected output:

```text
fast
4
```

The chain preserves the original layers while providing one lookup view.

## 69. Exercise

Build a small task-processing simulation with these requirements:

1. Incoming task categories must be counted.
2. Tasks awaiting execution must support FIFO removal from the left.
3. Only the five most recent completed task IDs should be retained.
4. Configuration should resolve from `runtime`, then `environment`, then `defaults` mappings without copying them into one dictionary.
5. Your program must print:
   - total tasks received;
   - counts by category;
   - the order tasks are processed;
   - the retained completion history;
   - the resolved retry limit.

Suggested tools:

```text
Counter
deque
ChainMap
```

Do not use a specialized container merely because it is listed. Explain in comments or notes why each selected structure matches the required operations.

## 70. Quick reference

```python
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple

Counter(iterable)
Counter(mapping)
counter.total()
counter.most_common(n)
counter.update(...)
counter.subtract(...)
+counter
-counter

defaultdict(list)
defaultdict(int)
mapping.default_factory

deque(iterable)
deque(iterable, maxlen=n)
d.append(value)
d.appendleft(value)
d.pop()
d.popleft()
d.extend(values)
d.extendleft(values)
d.rotate(n)

Record = namedtuple("Record", "field_a field_b")
record._asdict()
record._replace(field_a=value)
Record._fields
Record._field_defaults

ChainMap(front, fallback)
chain.maps
chain.new_child()
chain.parents

ordered.move_to_end(key, last=True)
ordered.popitem(last=False)
```

## 71. Design checklist

Before choosing a specialized collection, ask:

- What operation dominates this workflow?
- What should a missing value mean?
- Does the structure mutate during a read?
- Is endpoint performance important?
- Is order part of equality or only iteration?
- Do I need a live view or a copied snapshot?
- Does tuple compatibility matter?
- Would a built-in structure be simpler?
- Am I depending on a version-specific behavior?
- Have I tested the semantics that matter, not only the happy-path output?

## 72. Connections to other Python concepts

`collections` connects directly to topics already studied:

- **Phase 3 collections:** specialized containers build on the mental models of lists, tuples, dictionaries, and sets.
- **Loops:** `Counter`, grouping, queues, and bounded histories usually process iterables incrementally.
- **Functions:** factories passed to `defaultdict` are callable policies.
- **Type hints:** `typing.NamedTuple` and generic collection interfaces make data contracts explicit.
- **Object-oriented programming:** `User*` wrappers and ABCs show different extension models.
- **Algorithms:** the choice between list front operations and deque endpoints changes complexity.
- **Configuration design:** `ChainMap` models precedence without flattening source layers.
- **Testing:** semantics such as missing-key creation, order-sensitive equality, and bounded eviction deserve behavioral tests.

## References

Primary references used for this chapter:

- [Python 3.14 documentation: `collections` — Container datatypes](https://docs.python.org/3.14/library/collections.html)
- [Python 3.14 documentation: `collections.abc` — Abstract Base Classes for Containers](https://docs.python.org/3.14/library/collections.abc.html)
- [Python 3.14 documentation: `typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple)
- [Python 3.14 tutorial: Data Structures, including deque guidance for queues](https://docs.python.org/3.14/tutorial/datastructures.html#using-lists-as-queues)

## Next chapter

Continue to [Chapter 07: `itertools`](../07-itertools/README.md).

The next chapter shifts from specialized **containers** to specialized **iterator pipelines**: composing lazy transformations, repetition, slicing, grouping, and combinatoric iteration without building unnecessary intermediate collections.

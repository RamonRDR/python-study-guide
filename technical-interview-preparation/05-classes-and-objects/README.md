# Classes and Objects

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../04-data-structures-and-algorithms-review/README.md) · [Module index](../README.md) · [Next →](../06-attributes-methods-and-object-behavior/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [functions/01-defining-and-calling-functions](../../functions/01-defining-and-calling-functions/README.md)
- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.md)
- [comments-and-documentation/02-docstrings](../../comments-and-documentation/02-docstrings/README.md)

## What and why

A class defines a type and groups related behavior; an instance is an object of that type with its own state. Prefer a class when state and operations share a lifecycle or invariant. A pure function can be simpler for a stateless calculation.

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

first = Counter()
second = Counter()
first.increment()
print(first.value, second.value)  # 1 0
```

The class call normally creates and initializes an instance. `__init__` initializes an already created instance; it is not the object-creation hook (`__new__`). Do not return a value other than None from `__init__`. `self` is the conventional name for the instance parameter; a call like `first.increment()` binds that instance automatically. Each assignment to `self.value` stores state on the instance.

## Practical example and mistakes

The shared example models a reading session. Its read method validates the amount before updating state. Two sessions keep independent totals. Do not use a shared mutable class attribute for per-instance state; do not add classes just to wrap a single independent function.

## Practice

Implement a session that tracks completed tasks instead of pages. Create two instances, test independent state and ensure invalid amounts leave the total unchanged. Explain class, instance, attribute and method in your own words.

**Quick reference:** class defines type; instance holds state; method operates on the instance; initialize and validate deliberately.

[Shared executable example](examples/reading_session.py)

`python technical-interview-preparation/05-classes-and-objects/examples/reading_session.py`

## Official references (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Previous](../04-data-structures-and-algorithms-review/README.md) · [Module index](../README.md) · [Next →](../06-attributes-methods-and-object-behavior/README.md)
<!-- /chapter-navigation:bottom -->

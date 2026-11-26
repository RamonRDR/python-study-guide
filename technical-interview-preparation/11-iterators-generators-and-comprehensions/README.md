# Iterators, Generators and Comprehensions

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../10-python-memory-management/README.md) · [Module index](../README.md) · [Next →](../12-closures-and-decorators/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [program-flow/04-for-loops-and-iteration](../../program-flow/04-for-loops-and-iteration/README.md)
- [standard-library/07-itertools](../../standard-library/07-itertools/README.md)

## Iteration protocol

An iterable can supply an iterator through `iter()`. An iterator returns itself from `iter()`, produces values with `next()` and signals exhaustion with `StopIteration`. A list can provide fresh iterators; a single iterator is consumed. A generator function contains `yield`; calling it creates a generator without running its body. Each advance resumes execution until a yield or completion. It retains execution state between advances. Do not explicitly raise StopIteration from a generator body to finish; use return or reach the end.

```python
values = [1, 2, 3]
squares = [value ** 2 for value in values]
stream = (value ** 2 for value in values)
print(squares, next(stream), list(stream), list(stream))
```

Output: `[1, 4, 9] 1 [4, 9] []`. List, set and dictionary comprehensions construct containers eagerly: `[x for x in values if x > 1]`, `{x for x in values}`, `{x: x ** 2 for x in values}`. A generator expression defers result computation (the leftmost iterable expression is evaluated immediately). Comprehensions can have filters and nested loops, but complex logic is clearer in named functions or ordinary loops.

## When to stream

The shared example filters rows without materializing the full input. It uses constant extra state excluding input, output and caller storage; a caller using list materializes results. Laziness can reduce peak storage and permit early stopping, but does not guarantee lower total time or memory for every pipeline. Avoid repeated consumption when you need a reusable collection; do not silently consume an iterator just to inspect it.

## Practice

Use a generator source recording each item consumed, call next once, then consume the remainder. Test empty input and exhaustion. Compare an eager comprehension with the generator for a large stream; explain when materialization is justified.

**Quick reference:** iterable supplies; iterator advances; generator suspends; comprehension builds; generator expression streams.

## Shared executable example

[eligible_rows.py](examples/eligible_rows.py)

`python technical-interview-preparation/11-iterators-generators-and-comprehensions/examples/eligible_rows.py`

## Official references (Python 3.13)

- [Python 3.13: tutorial/classes.html#iterators](https://docs.python.org/3.13/tutorial/classes.html#iterators)
- [Python 3.13: tutorial/classes.html#generators](https://docs.python.org/3.13/tutorial/classes.html#generators)
- [Python 3.13: tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions)
- [Python 3.13: reference/expressions.html#generator-expressions](https://docs.python.org/3.13/reference/expressions.html#generator-expressions)

<!-- chapter-navigation:bottom -->
[← Previous](../10-python-memory-management/README.md) · [Module index](../README.md) · [Next →](../12-closures-and-decorators/README.md)
<!-- /chapter-navigation:bottom -->

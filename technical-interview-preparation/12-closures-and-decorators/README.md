# Closures and Decorators

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../11-iterators-generators-and-comprehensions/README.md) · [Module index](../README.md) · [Next →](../13-context-managers/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [functions/04-scope](../../functions/04-scope/README.md)
- [functions/06-default-values](../../functions/06-default-values/README.md)
- [technical-interview-preparation/06-attributes-methods-and-object-behavior](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.md)

## Closures and scope

A closure is a function retaining access to bindings from an enclosing function. LEGB lookup explains how it finds them. `nonlocal` permits rebinding an existing enclosing function variable, not a module global. Each call to the outer factory can create independent state.

```python
def make_multiplier(factor):
    def multiply(value):
        return factor * value
    return multiply

double = make_multiplier(2)
print(double(5))
```

Output: 10. Closures capture bindings, not automatic value snapshots. A loop creating lambdas referring to its changing index can make every lambda read the final index. For a snapshot, bind a default argument (for immutable values) or use a separate factory call. Closures can keep referenced objects alive.

## Decorators

A decorator transforms a function or class at definition time. For a single function decorator, `@decorate` above a definition is approximately rebinding `function = decorate(function)` after creation. A decorator factory accepts configuration and returns a decorator; stacked decorators apply from the nearest definition upward. In the shared example, `record_calls(records)` returns a decorator whose wrapper forwards positional and keyword arguments, records each attempt and returns the original result or propagates its exception. `functools.wraps` preserves useful metadata and exposes `__wrapped__`; it does not automatically preserve every behavior or make a synchronous wrapper suitable for async functions.

## Practice

Create two counters and confirm independent state. Decorate a calculation and test positional and keyword calls, return value, metadata and a raised exception. Explain why the wrapper should not swallow errors by default. Use decorators for consistent cross-cutting behavior; avoid obscuring control flow or introducing hidden side effects when explicit calls are clearer.

**Quick reference:** closure retains enclosing bindings; nonlocal rebinds; decorator transforms; wrapper forwards.

## Shared executable example

[call_counter.py](examples/call_counter.py)

`python technical-interview-preparation/12-closures-and-decorators/examples/call_counter.py`

## Official references (Python 3.13)

- [Python 3.13: tutorial/classes.html#python-scopes-and-namespaces](https://docs.python.org/3.13/tutorial/classes.html#python-scopes-and-namespaces)
- [Python 3.13: reference/compound_stmts.html#function-definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13: library/functools.html#functools.wraps](https://docs.python.org/3.13/library/functools.html#functools.wraps)

<!-- chapter-navigation:bottom -->
[← Previous](../11-iterators-generators-and-comprehensions/README.md) · [Module index](../README.md) · [Next →](../13-context-managers/README.md)
<!-- /chapter-navigation:bottom -->

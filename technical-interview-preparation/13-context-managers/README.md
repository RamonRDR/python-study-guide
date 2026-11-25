# Context Managers

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../12-closures-and-decorators/README.md) · [Module index](../README.md) · [Next →](../14-concurrency-parallelism-and-the-gil/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [errors-files-and-modules/03-open-and-with](../../errors-files-and-modules/03-open-and-with/README.md)
- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.md)
- [technical-interview-preparation/11-iterators-generators-and-comprehensions](../../technical-interview-preparation/11-iterators-generators-and-comprehensions/README.md)
- [technical-interview-preparation/12-closures-and-decorators](../../technical-interview-preparation/12-closures-and-decorators/README.md)

## The with protocol

A context manager packages acquisition and release around a block. The `with manager as value:` statement calls `__enter__()`; its return becomes value. After successful entry, `__exit__(exc_type, exc_value, traceback)` receives exception details or three None values. A truthy return suppresses a body exception; false or None lets it propagate. If entry itself fails, that manager's exit is not called. Cleanup failure can also raise. Do not treat `with` as an automatic exception suppressor.

```python
class Marker:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("close")
        return False

with Marker():
    print("work")
```

Output is open, work, close on separate lines. A class can manage a resource through those special methods. Alternatively `contextlib.contextmanager` converts a generator function yielding exactly once into a context-manager factory. Place cleanup in finally around yield. A body exception is injected at the yield point; if caught only to log, re-raise it unless suppression is the intended contract.

## Practical decisions

The shared example records open/work/close in a list rather than accessing an external resource. Test both normal completion and body failure. A manager produced by contextmanager is normally single-use; call the factory again. Use `ExitStack` when a variable number of context managers must be managed. Avoid a custom manager when built-in file or lock managers already express the contract.

## Practice

Raise RuntimeError inside the example and verify cleanup happens exactly once while the exception propagates. Explain what changes if entry fails before acquisition completes. Compare explicit try/finally with the reusable manager.

**Quick reference:** enter returns binding; exit handles cleanup; truthy exit suppresses body exception; successful entry is the boundary.

## Shared executable example

[managed_session.py](examples/managed_session.py)

`python technical-interview-preparation/13-context-managers/examples/managed_session.py`

## Official references (Python 3.13)

- [Python 3.13: reference/compound_stmts.html#the-with-statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-with-statement)
- [Python 3.13: library/contextlib.html](https://docs.python.org/3.13/library/contextlib.html)

<!-- chapter-navigation:bottom -->
[← Previous](../12-closures-and-decorators/README.md) · [Module index](../README.md) · [Next →](../14-concurrency-parallelism-and-the-gil/README.md)
<!-- /chapter-navigation:bottom -->

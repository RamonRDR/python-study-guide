# Python Memory Management

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../09-object-identity-references-and-copying/README.md) · [Module index](../README.md) · [Next →](../11-iterators-generators-and-comprehensions/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [technical-interview-preparation/09-object-identity-references-and-copying](../../technical-interview-preparation/09-object-identity-references-and-copying/README.md)

## Object lifetime and reachability

Memory management is how an implementation allocates and reclaims storage. A live object may be reachable through names, containers, closures or other objects. `del name` removes a binding; it does not necessarily destroy the object. Python does not promise immediate finalization. In conventional CPython 3.13, reference counting reclaims many objects when strong references disappear, supplemented by a cyclic garbage collector. A cycle can keep counts above zero even after it becomes unreachable. Other implementations and free-threaded builds may differ; do not rely on exact collection timing.

```python
first = []
second = first
del first
second.append("still alive")
print(second)
```

A weak reference does not itself keep its referent alive; `weakref.ref(obj)()` may return the object or None after destruction. Not all objects support weak references (ordinary lists do not). Use weak references only when ownership should be non-owning. Use `with` for files and similar resources; do not depend on collection for timely cleanup.

## Retention and measurement

A reachable cache, global collection or closure can retain objects indefinitely without a collector bug. Bound caches by entry count or an appropriate resource budget; remove references when no longer needed. The shared example evicts the least recently inserted or updated key using dictionary insertion order. Reads of a snapshot do not refresh order: this is not a full LRU cache. A count limit does not bound byte size, and its shallow snapshot does not isolate mutable values.

`tracemalloc` can compare Python allocation snapshots; it is not a complete measure of process memory or native allocations. `gc.collect()` requests collection; it does not free reachable objects or promise that process RSS falls. Avoid forcing collection as a default fix.

## Practice

Run the cache example, update an older key, insert another key and check eviction. Clear the cache and explain why external aliases could still retain values. Sketch a cycle between two containers and distinguish unreachable cycles from reachable retention.

**Quick reference:** reachability and ownership first; collection timing is not a resource contract; measure before optimizing.

## Shared executable example

[bounded_cache.py](examples/bounded_cache.py)

`python technical-interview-preparation/10-python-memory-management/examples/bounded_cache.py`

## Official references (Python 3.13)

- [Python 3.13: reference/datamodel.html](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13: library/gc.html](https://docs.python.org/3.13/library/gc.html)
- [Python 3.13: library/weakref.html](https://docs.python.org/3.13/library/weakref.html)
- [Python 3.13: library/tracemalloc.html](https://docs.python.org/3.13/library/tracemalloc.html)

<!-- chapter-navigation:bottom -->
[← Previous](../09-object-identity-references-and-copying/README.md) · [Module index](../README.md) · [Next →](../11-iterators-generators-and-comprehensions/README.md)
<!-- /chapter-navigation:bottom -->

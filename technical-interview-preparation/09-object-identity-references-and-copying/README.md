# Object Identity, References and Copying

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../08-encapsulation-abstraction-and-solid/README.md) · [Module index](../README.md) · [Next →](../10-python-memory-management/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.md)
- [collections/02-modifying-lists-and-methods](../../collections/02-modifying-lists-and-methods/README.md)
- [program-flow/01-conditions-comparisons-and-boolean-logic](../../program-flow/01-conditions-comparisons-and-boolean-logic/README.md)

## Identity, equality and binding

Every object has identity, type and value. `is` compares identity; `==` uses equality semantics, which a class may customize. Use `is None` for the singleton, not `is` to compare strings or integers. `id(obj)` identifies a live object, but IDs may be reused after its lifetime; only CPython specifically uses the memory address.

Assignment binds a name, not a copy. Function parameters also bind to objects: rebinding a parameter does not rebind the caller's name, while mutation of a shared mutable object may be visible through both names.

```python
from copy import copy, deepcopy

original = {"steps": ["draft"]}
alias = original
shallow = copy(original)
deep = deepcopy(original)
shallow["steps"].append("review")
print(original == shallow, original is shallow)
print(alias is original, deep["steps"])
```

The output is `True False`, then `True ['draft']`. A shallow copy has a new outer dictionary but shares its inner list. A deep copy recursively copies supported components; its memo tracks already copied objects, including cycles and repeated references. It does not guarantee a new object for every component (immutable objects may be shared), nor does it clone external resources. Custom classes can control copying.

## Equality and hashing

Hashable objects must have a stable hash and equal objects must have equal hashes. Unequal objects may collide. Lists and dictionaries are unhashable; a tuple is hashable only if its elements are hashable. If you implement value equality on a mutable class, making it a hash key can break lookup if its hash changes. Python normally makes a class unhashable when it defines `__eq__` without `__hash__`.

## Practice

Run the shared example. Make two keys reference the same list and check that the deep copy preserves that internal relationship while separating it from the original. Try a shallow copy first. Prefer no copy for intentional sharing, shallow copy for independent outer structure, and deep copy only when the nested ownership contract requires it; copying large graphs costs time and memory.

**Quick reference:** alias shares; shallow copies the container; deep copies the supported graph; equality is not identity.

## Shared executable example

[copy_plan.py](examples/copy_plan.py)

`python technical-interview-preparation/09-object-identity-references-and-copying/examples/copy_plan.py`

## Official references (Python 3.13)

- [Python 3.13: reference/datamodel.html](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13: library/copy.html](https://docs.python.org/3.13/library/copy.html)

<!-- chapter-navigation:bottom -->
[← Previous](../08-encapsulation-abstraction-and-solid/README.md) · [Module index](../README.md) · [Next →](../10-python-memory-management/README.md)
<!-- /chapter-navigation:bottom -->

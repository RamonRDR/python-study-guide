# Attributes, Methods and Object Behavior

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../05-classes-and-objects/README.md) · [Module index](../README.md) · [Next →](../07-inheritance-polymorphism-and-composition/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [Classes and objects](../05-classes-and-objects/README.md)
- [functions/06-default-values](../../functions/06-default-values/README.md)
- [collections/02-modifying-lists-and-methods](../../collections/02-modifying-lists-and-methods/README.md)

## Attributes and binding

An instance attribute stores per-object data; a class attribute normally provides shared data accessible through instances. Assigning an instance attribute of the same name usually shadows the class attribute. A mutable class attribute such as a list is a common accidental-sharing bug; initialize independent lists in `__init__`.

| Method kind | Receives implicitly | Purpose |
| --- | --- | --- |
| Instance | self | Read or update instance state |
| Class | cls | Alternative constructors or class-specific behavior |
| Static | Neither | Related utility without implicit state |

The built-in markers `@classmethod` and `@staticmethod` change binding; the general decorator mechanism is taught later. In the example, `from_label` calls cls so a subclass can be constructed; `valid_label` needs no instance. A static method is not automatically pure. Both construction paths reject a non-string or blank label with `ValueError`; `from_label` additionally strips surrounding whitespace. A subclass using the inherited constructor can create its own instance through the class method.

## Special methods

Names such as `__len__`, `__str__` and `__repr__` integrate objects with Python operations. `len(group)` uses the length protocol; `str(group)` is user-oriented; repr is useful for debugging and need not be executable Python. Follow documented contracts (length must be a nonnegative integer). Equality and hashing require compatible semantics; their deeper contracts are addressed in the identity lesson. Avoid inventing new dunder names.

## Practice

Run the shared study-group example. Create two groups, add a member to only one and check both lengths. Explain why the members list is per instance and category is shared. Add a validation test for an empty label. Compare str and repr.

**Quick reference:** self = instance; cls = class; static = no implicit argument; special methods implement language protocols.

[Shared executable example](examples/study_group.py)

`python technical-interview-preparation/06-attributes-methods-and-object-behavior/examples/study_group.py`

## Official references (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Previous](../05-classes-and-objects/README.md) · [Module index](../README.md) · [Next →](../07-inheritance-polymorphism-and-composition/README.md)
<!-- /chapter-navigation:bottom -->

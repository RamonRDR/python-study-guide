# Inheritance, Polymorphism and Composition

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../06-attributes-methods-and-object-behavior/README.md) · [Module index](../README.md) · [Next →](../08-encapsulation-abstraction-and-solid/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [Previous OOP instruction](../06-attributes-methods-and-object-behavior/README.md)
- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.md)

## Inheritance and substitution

Inheritance creates a subclass, written `class Child(Parent):`. It can reuse or override inherited behavior. Use it when the subtype can honor the base contract, not merely because two implementations contain similar lines. In a single-inheritance example, `super().__init__(...)` can initialize the base part; more generally super follows the method resolution order, not simply a hardcoded parent.

## Polymorphism and composition

Polymorphism lets the caller use a common operation with different implementations. Python often supports duck typing: an object can meet a behavioral contract without sharing a base class. Composition stores or receives a collaborator instead of inheriting its implementation. In the shared example, Notifier delegates to a channel's send method. The channel returns a text result, not an actual network message. It can be replaced by another compatible channel or a fake in a test. TextChannel and EmailChannel both override Channel.send, while the base contract states that subclasses must provide the operation. An independent class with the same contract can also work.

Avoid deep hierarchies chosen only to reuse code; avoid assuming that matching method names guarantee matching semantics. Composition adds an explicit dependency, which can be easier to replace but may add indirection.

## Practice

Add a fictional log channel returning `"log: Ready"` for message `"Ready"` without modifying Notifier. Test a fake and explain what contract all channels must honor. Explain a case where inheritance is appropriate and one where composition is simpler.

**Quick reference:** inheritance = subtype relationship; polymorphism = interchangeable behavior; composition = collaboration.

[Shared executable example](examples/notifications.py)

`python technical-interview-preparation/07-inheritance-polymorphism-and-composition/examples/notifications.py`

## Official references (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Previous](../06-attributes-methods-and-object-behavior/README.md) · [Module index](../README.md) · [Next →](../08-encapsulation-abstraction-and-solid/README.md)
<!-- /chapter-navigation:bottom -->

# Encapsulation, Abstraction and SOLID

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../07-inheritance-polymorphism-and-composition/README.md) · [Module index](../README.md) · [Next →](../09-object-identity-references-and-copying/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [Inheritance and composition](../07-inheritance-polymorphism-and-composition/README.md)
- [manual-programming-practices/02-specification-driven-development](../../manual-programming-practices/02-specification-driven-development/README.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.md)
- [practical-projects/03-user-registration](../../practical-projects/03-user-registration/README.md)

## Encapsulation and abstraction

Encapsulation exposes operations that preserve valid state. In the stock example, remove validates before changing quantity. A leading underscore signals a nonpublic implementation detail by convention; double leading underscores trigger name mangling, not security. A property can expose read access without a normal setter; callers can still bypass conventions, so this is not an access-control boundary.

Abstraction defines what a collaborator promises without forcing callers to know how it works. `ABC` and `@abstractmethod` from the standard library express an explicit abstract contract: a concrete subclass must implement the abstract methods before normal instantiation. `StockReader` defines available; a reader that obtains data from memory or another source can honor the same contract. A type hint alone does not enforce runtime behavior.

## SOLID as design questions

| Principle | Practical question |
| --- | --- |
| Single responsibility (SRP) | Does this component have a coherent reason to change? |
| Open/closed (OCP) | Can a planned variation be supported through a stable extension point instead of modifying all callers? |
| Liskov substitution (LSP) | Can a subtype replace its base without breaking the promised behavior? |
| Interface segregation (ISP) | Does the caller depend only on the operations it needs? |
| Dependency inversion (DIP) | Can high-level policy depend on a useful abstraction instead of a concrete infrastructure detail? |

The stock example separates state rules from reading; the reader exposes only available; remaining depends on that contract. A fake reader supports testing. SOLID is a set of design heuristics, not Python syntax or a requirement for five classes. A one-off calculation may need only a function. Introduce abstractions when they reduce meaningful coupling or support a real variation.

## Practice

Add a fake reader returning 7 and verify remaining without modifying it. Attempt to remove more than the stock holds; test that quantity remains unchanged. Explain which two SOLID principles apply and one cost of introducing an extra abstraction.

**Quick reference:** protect invariants, expose small contracts, favor useful substitutability, justify complexity.

[Shared executable example](examples/stock.py)

`python technical-interview-preparation/08-encapsulation-abstraction-and-solid/examples/stock.py`

## Official references (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)
- [abc](https://docs.python.org/3.13/library/abc.html)

<!-- chapter-navigation:bottom -->
[← Previous](../07-inheritance-polymorphism-and-composition/README.md) · [Module index](../README.md) · [Next →](../09-object-identity-references-and-copying/README.md)
<!-- /chapter-navigation:bottom -->

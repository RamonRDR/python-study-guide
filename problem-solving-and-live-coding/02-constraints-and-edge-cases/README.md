# Constraints and Edge Cases

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../01-problem-solving-fundamentals/README.md) · [Module index](../README.md) · [Next →](../03-algorithmic-complexity/README.md)
<!-- /chapter-navigation:top -->

**Prerequisites:** [Parameters](../../functions/02-parameters-and-arguments/README.md) · [Return values](../../functions/03-return-values/README.md) · [pytest](../../external-libraries/04-pytest/README.md) · [TDD](../../manual-programming-practices/03-test-driven-development/README.md)

## Goal

Turn input constraints into explicit behavior and useful tests (25–35 minutes).

## 1. Domain and boundaries

A fictional workshop accepts a group if its size is between 1 and the room capacity, inclusive. Both arguments must be exact integers (not booleans); capacity must be at least 1 and group size nonnegative. Return a Boolean for valid arguments, raise TypeError for wrong types before checking values, and ValueError for invalid values. The caller does not need arbitrary limits unrelated to this contract.

| Group | Capacity | Expected |
| --- | --- | --- |
| 0 | 5 | False |
| 1 | 5 | True |
| 5 | 5 | True |
| 6 | 5 | False |
| -1 | 5 | ValueError |
| 2 | 0 | ValueError |
| True | 5 | TypeError |

An edge case is a boundary or unusual valid condition; an invalid input violates the contract. Test below, at and above each meaningful boundary. A type error differs from a valid but rejected booking.

## 2. Turn examples into tests

Write the expected output independently of the implementation. Use exact equality for these Boolean outputs and check exception types for invalid inputs. In Python, `isinstance(True, int)` is true, so the exact-integer requirement needs `type(value) is int`. Use an inclusive comparison only after validating arguments. See the [example](examples/capacity.py). A solution that uses a strict upper bound would fail the group-size-equals-capacity test; this is a useful discrimination check. Avoid testing exception message text unless the contract requires it.

## Practice

Write a boundary table for a fictional locker that accepts item weights from 1 to 10 whole units, inclusive. Specify which inputs raise errors and which return False before writing code. Add a case that detects replacing `<=` with `<`. Explain why testing only typical values is insufficient.

**Quick reference:** define valid domain, expected result, invalid-input policy and boundary tests before coding.

Run from the chapter directory (Python 3.13 baseline):

```bash
python examples/capacity.py
```

<!-- chapter-navigation:bottom -->
[← Previous](../01-problem-solving-fundamentals/README.md) · [Module index](../README.md) · [Next →](../03-algorithmic-complexity/README.md)
<!-- /chapter-navigation:bottom -->

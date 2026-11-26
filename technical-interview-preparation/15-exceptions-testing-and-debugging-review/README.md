# Exceptions, Testing and Debugging Review

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../14-concurrency-parallelism-and-the-gil/README.md) · [Module index](../README.md) · [Next →](../16-http-rest-and-backend-fundamentals/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.md)
- [external-libraries/04-pytest](../../external-libraries/04-pytest/README.md)
- [manual-programming-practices/01-manual-coding-and-debugging](../../manual-programming-practices/01-manual-coding-and-debugging/README.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.md)

## Exception boundaries

Exceptions communicate failures across call boundaries. Catch a specific expected exception where you can recover or translate it; unexpected errors should normally propagate to an appropriate outer boundary. `raise` inside a handler re-raises the active exception; `raise NewError(...) from error` preserves an explicit cause. `else` runs after successful protected work; `finally` handles exit work, not success. Do not return from finally to hide an error. Context managers often make resource cleanup clearer.

```python
try:
    value = int("unknown")
except ValueError as error:
    raise ValueError("invalid quantity") from error
```

This intentionally raises an exception with its cause; it is not a successful conversion. The shared example accepts strings supported by int, including surrounding whitespace, then requires a nonnegative result. It does not silently turn a bad value into zero.

## Test and debug by evidence

Unit tests check a small behavior with controlled dependencies; integration tests cross real component boundaries; end-to-end tests exercise a complete supported workflow. Use Arrange/Act/Assert, meaningful equality or exception assertions, boundary inputs and deterministic setup/teardown. A fake can replace a network dependency, but test the real boundary separately. Parametrization varies input; fixtures provide and release dependencies. A test passing on intentionally incorrect code is evidence of a weak oracle, not proof the implementation is correct. Coverage measures execution, not correctness.

Debugging sequence: reproduce with a minimal input, read traceback from the failing frame and its callers, form a hypothesis, inspect relevant state with a debugger (`breakpoint()`) or structured logs, change one cause, then add a regression test. Redact secrets and sensitive payloads. Avoid broad exception catches or adding retries without understanding the failure.

## Practice

Predict valid and invalid outputs of parse_quantity, verify zero and negative boundaries, and assert the exception cause. Temporarily return zero for invalid text in your own copy; the negative test must fail. Explain which test would detect each defect.

**Quick reference:** specific catch; preserve cause; reproduce; test behavior; verify regression.

## Shared executable example

[parse_quantity.py](examples/parse_quantity.py)

`python technical-interview-preparation/15-exceptions-testing-and-debugging-review/examples/parse_quantity.py`

## Official references

- [docs.python.org/3.13/tutorial/errors.html](https://docs.python.org/3.13/tutorial/errors.html)
- [docs.python.org/3.13/library/unittest.html](https://docs.python.org/3.13/library/unittest.html)
- [docs.python.org/3.13/library/pdb.html](https://docs.python.org/3.13/library/pdb.html)

<!-- chapter-navigation:bottom -->
[← Previous](../14-concurrency-parallelism-and-the-gil/README.md) · [Module index](../README.md) · [Next →](../16-http-rest-and-backend-fundamentals/README.md)
<!-- /chapter-navigation:bottom -->

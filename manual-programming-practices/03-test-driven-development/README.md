# Test-Driven Development

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../02-specification-driven-development/README.md) · [Module index](../README.md) · [Next →](../04-professional-workflow/README.md)
<!-- /chapter-navigation:top -->

## Goal

**Estimated time:** 45–60 minutes. Follow the requirements in [the specification lesson](../02-specification-driven-development/README.md). TDD means writing a failing test for a small behavior, implementing enough to pass, then improving the code without changing behavior. It is a feedback loop, not a substitute for requirements. This lesson uses standard-library unittest; see [pytest](../../external-libraries/04-pytest/README.md) for the existing alternative.

## 1. Red: write a test first

In a new practice folder, create reading_progress.py with a deliberate placeholder:

```python
def remaining_pages(total_pages, pages_read):
    raise NotImplementedError
```

Create test_reading_progress.py beside it:

```python
import unittest
from reading_progress import remaining_pages


class ReadingProgressTests(unittest.TestCase):
    def test_remaining_pages(self):
        self.assertEqual(remaining_pages(20, 7), 13)
```

From that folder run:

```shell
python -m unittest discover -s . -p 'test_*.py' -v
```

On a supported shell this discovers the test; use double quotes around the pattern if needed. Use your verified environment Python. Expect one test to report an error (NotImplementedError): the behavior is missing. A test that cannot import the module for unrelated reasons is not evidence of the intended red state; fix the setup first.

## 2. Green: implement only the first behavior

Replace the placeholder with `return total_pages - pages_read`. Rerun the test. Expect it to pass. Add tests for AC2, then AC3 and AC4 in small increments. Use `self.assertRaises(ValueError)` or `self.assertRaises(TypeError)` as context managers. Run each new test before implementing its missing behavior; the subtraction alone will fail invalid-range tests. Check types before ranges, including bool, because bool is a subclass of int. Add the no-output test (AC5) using redirected stdout/stderr, then verify type-error precedence and the accepted int subclass case. Do not weaken a failing test to make it green.

## 3. Refactor and verify

Improve names or remove repetition only while tests remain green. For instance, group equivalent boundary cases with subTest. Refactoring changes structure, not the specified behavior. Run the full suite after each change.

Try independently before opening the [reference implementation](examples/reading_progress.py) and [reference tests](examples/test_reading_progress.py). The final code is shared across languages. The reference has seven test methods, including boundary groups; one method may check several cases. From the repository root run:

```shell
python -m unittest discover -s manual-programming-practices/03-test-driven-development/examples -p 'test_*.py' -v
python manual-programming-practices/03-test-driven-development/examples/reading_progress.py
```

Expected demo output: 13. The final reference suite should be green; the intentionally red placeholder is only in the lesson, not committed as executable code. The repository CI runs the dedicated test suite and approved demo.

## 4. Independent practice

Without reading the reference, implement the contract, write tests and record red/green/refactor observations. Temporarily replace subtraction with addition or remove a validation check in your practice copy. Verify that a relevant test fails; restore the correct implementation and rerun. Explain why test success does not prove all possible cases or code quality. For a new feature, update the specification first when behavior changes.

**Quick reference:** define behavior → failing test → smallest correct implementation → passing test → refactor → rerun. Consult [unittest](https://docs.python.org/3.13/library/unittest.html) for assertions and discovery.

<!-- chapter-navigation:bottom -->
[← Previous](../02-specification-driven-development/README.md) · [Module index](../README.md) · [Next →](../04-professional-workflow/README.md)
<!-- /chapter-navigation:bottom -->

<div align="center">

# Engineering Automated Tests with `pytest`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to External Libraries](../README.md) · [← Previous: `requests`](../03-requests/README.md)

Software becomes easier to change when expected behavior can be checked repeatedly and automatically. `pytest` provides a concise testing model built around normal Python functions, plain `assert` statements, reusable fixtures, parametrization, rich failure reports, and an extensible plugin system.

This chapter targets **pytest 9.1.x** and was researched against the current stable **pytest 9.1.1** documentation and release metadata. pytest 9.1.1 requires Python 3.10 or newer; this repository validates examples on Python 3.13.

**Estimated study time:** 300–390 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain what an automated test proves and what it does not prove;
- organize tests so pytest can discover them predictably;
- write readable assertions and interpret assertion introspection;
- test floating-point values, exceptions, and warnings deliberately;
- reduce duplication with parametrization;
- model setup, teardown, and dependencies with fixtures;
- isolate filesystem and environment state with `tmp_path` and `monkeypatch`;
- capture standard output and logs with `capsys` and `caplog`;
- use marks, skips, expected failures, and test selection intentionally;
- configure pytest without hiding warnings or accidental test omissions;
- distinguish unit, integration, and end-to-end boundaries;
- avoid flaky tests caused by time, randomness, network access, shared state, or ordering assumptions;
- integrate pytest into CI as an executable quality contract.

## 1. Why automated tests exist

A manual check answers a question once. An automated test turns that question into executable code that can be repeated after future changes.

A useful test describes a behavior, provides controlled inputs, observes an output or side effect, and fails when the observed behavior violates the expected contract.

Tests reduce uncertainty. They do not prove that software has no bugs.

## 2. What `pytest` adds

Python includes `unittest` in the standard library. `pytest` is an external test framework that can run plain test functions while adding features such as:

- assertion introspection;
- fixtures;
- parametrization;
- marks and test selection;
- temporary paths;
- environment monkeypatching;
- output, warning, and log capture;
- plugins and hooks.

The goal is not to make tests clever. The goal is to make intent visible and repetition cheap.

## 3. External libraries need a version contract

This repository declares Phase 9 dependencies in `requirements-external.txt`.

For this chapter the contract is:

```text
pytest >= 9.1 and < 9.2
```

The upper bound matters because the pytest changelog already contains an unreleased 9.2 draft with backward-incompatible changes. A published curriculum should describe released behavior rather than silently following a future version.

## 4. Install the repository dependency set

Create and activate a virtual environment, then install:

```bash
python -m pip install -r requirements-external.txt
```

For isolated experimentation:

```bash
python -m pip install pytest
```

A project should still record which pytest range it supports.

## 5. Prefer `python -m pytest` when interpreter identity matters

A common invocation is:

```bash
python -m pytest
```

Using `python -m` makes the interpreter explicit. This is especially useful when several Python installations or virtual environments exist on the same machine.

The `pytest` console command is also valid when the environment is unambiguous.

## 6. A test is executable specification, not production code

Consider a small function:

```python
def calculate_total(unit_price: int, quantity: int) -> int:
    return unit_price * quantity
```

A test can state one expected behavior:

```python
def test_calculate_total_multiplies_price_by_quantity() -> None:
    assert calculate_total(12, 3) == 36
```

The test name communicates the contract before the assertion is even read.

## 7. pytest discovers tests by convention

By default, pytest discovers test modules and test functions according to naming conventions.

A common layout is:

```text
project/
├── src/
│   └── calculator.py
└── tests/
    └── test_calculator.py
```

Inside `test_calculator.py`, functions named `test_*` are collected as tests.

## 8. Collection is a phase of the test run

Before executing tests, pytest first discovers and collects them.

You can inspect collection without executing tests:

```bash
python -m pytest --collect-only
```

This is useful when a test you expected to run is missing.

A green suite that accidentally collected the wrong tests is not a reliable signal.

## 9. Keep test names behavioral

Prefer names that explain an observable rule:

```python
def test_discount_is_zero_for_empty_cart() -> None:
    ...
```

Avoid names that only mirror implementation details:

```python
def test_function_2() -> None:
    ...
```

Good names make failures easier to triage in CI.

## 10. Plain `assert` is the normal pytest assertion style

```python
def test_status_is_ready() -> None:
    status = "ready"
    assert status == "ready"
```

pytest rewrites assertions during collection so failing expressions can produce richer diagnostics than a bare Python `AssertionError` normally provides.

## 11. Assertion introspection helps explain failures

A comparison such as:

```python
def test_summary() -> None:
    actual = {"count": 2, "status": "ready"}
    expected = {"count": 3, "status": "ready"}
    assert actual == expected
```

can show the differing values when it fails.

This is one reason to prefer direct expressions over manually constructing vague failure messages everywhere.

## 12. Add a message only when it adds domain context

```python
def test_inventory_never_becomes_negative() -> None:
    remaining = 4
    assert remaining >= 0, "inventory contract requires a non-negative balance"
```

The message should explain why the condition matters, not merely restate `remaining >= 0`.

## 13. Use Arrange, Act, Assert when it clarifies the test

A readable test often has three conceptual stages:

```python
def test_normalize_name_removes_outer_whitespace() -> None:
    raw_name = "  Nova  "

    normalized = raw_name.strip()

    assert normalized == "Nova"
```

Not every tiny test needs comments naming the stages. The structure itself can make them obvious.

## 14. Test one coherent behavior

A test may contain several assertions when they describe one result, but avoid turning a single test into a tour of unrelated behaviors.

Smaller behavioral tests make failures more local and easier to diagnose.

## 15. Deterministic tests are repeatable

A deterministic test gives the same result when the relevant code and inputs have not changed.

Common threats include:

- current time;
- random values without control;
- network services;
- shared files or databases;
- environment variables;
- locale and timezone;
- dependency on test execution order.

Isolation is a design skill, not just a test-framework feature.

## 16. Compare floating-point results with an explicit tolerance

Binary floating-point values are often unsuitable for exact equality after calculations.

pytest provides `approx()`:

```python
import pytest


def test_ratio() -> None:
    result = 1 / 3
    assert result == pytest.approx(0.333333, rel=1e-5)
```

Choose tolerances according to the domain rather than copying arbitrary values.

## 17. Exact values should still use exact assertions

Do not reach for `pytest.approx()` when the contract is exact.

```python
def test_item_count() -> None:
    assert len(["a", "b", "c"]) == 3
```

Testing tools should make contracts clearer, not blur them.

## 18. Test expected exceptions with `pytest.raises`

```python
import pytest


def parse_positive(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise ValueError("value must be positive")
    return number


def test_zero_is_rejected() -> None:
    with pytest.raises(ValueError):
        parse_positive("0")
```

The test passes only if the expected exception type is raised inside the context manager.

## 19. Match exception messages when the message is part of the contract

```python
def test_zero_has_clear_message() -> None:
    with pytest.raises(ValueError, match="must be positive"):
        parse_positive("0")
```

`match` is interpreted as a regular expression. Escape special characters when you intend a literal match.

## 20. Inspect captured exception information when necessary

```python
def test_invalid_value_context() -> None:
    with pytest.raises(ValueError) as exc_info:
        parse_positive("-4")

    assert "positive" in str(exc_info.value)
```

Do this when the extra detail matters. Do not inspect internals merely because pytest exposes them.

## 21. Test warnings explicitly with `pytest.warns`

```python
import warnings

import pytest


def old_api() -> None:
    warnings.warn("old API", DeprecationWarning, stacklevel=2)


def test_old_api_warns() -> None:
    with pytest.warns(DeprecationWarning, match="old API"):
        old_api()
```

Warnings can represent migration contracts that deserve tests of their own.

## 22. pytest 9.1 can enforce a warning budget

pytest 9.1 added `--max-warnings`.

For example:

```bash
python -m pytest --max-warnings=10
```

If all tests pass but the unfiltered warning count exceeds the threshold, pytest reports a dedicated non-zero exit status.

A warning budget can help a project reduce warning debt gradually instead of suppressing everything.

## 23. Parametrization turns data variation into test cases

When the same behavior should hold for many inputs, use `@pytest.mark.parametrize`:

```python
import pytest


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(-5, 0), (40, 40), (130, 100)],
)
def test_normalize_score(raw: int, expected: int) -> None:
    result = max(0, min(raw, 100))
    assert result == expected
```

pytest creates a separate collected case for each parameter set.

## 24. Separate test logic from test data

Parametrization works best when the test body expresses one rule and the data describes interesting cases.

Include meaningful boundaries, not just many random examples.

A ten-row parameter table is not automatically better than three carefully chosen boundary cases.

## 25. Give parameter cases useful IDs when reports need them

```python
@pytest.mark.parametrize(
    ("value", "expected"),
    [(0, "empty"), (1, "single"), (2, "many")],
    ids=["zero", "one", "multiple"],
)
def test_classification(value: int, expected: str) -> None:
    result = "empty" if value == 0 else "single" if value == 1 else "many"
    assert result == expected
```

Readable IDs improve failure reports for complex parameter values.

## 26. Use `pytest.param` for per-case metadata

```python
@pytest.mark.parametrize(
    "value",
    [
        1,
        pytest.param(-1, marks=pytest.mark.xfail(reason="known limitation")),
    ],
)
def test_positive_only(value: int) -> None:
    assert value > 0
```

Per-case marks can keep exceptional cases visible without duplicating the whole test.

## 27. pytest 9.1 deprecates non-collection iterables for parametrization

Current pytest documentation deprecates passing a non-`Collection` iterable such as a generator directly as `argvalues`.

Prefer a concrete list or tuple for published tests:

```python
cases = [(1, 2), (2, 4), (3, 6)]
```

This also makes the test data easier to inspect and review.

## 28. Fixtures model test dependencies

A fixture is a value or resource that pytest provides to a test by name.

```python
import pytest


@pytest.fixture
def sample_user() -> dict[str, str]:
    return {"name": "Nova", "role": "reader"}


def test_user_role(sample_user: dict[str, str]) -> None:
    assert sample_user["role"] == "reader"
```

The test requests the fixture by declaring a parameter with the fixture name.

## 29. Fixtures can return objects

Fixtures can return plain values, data structures, configured clients, temporary repositories, database connections, or other resources.

Keep fixtures focused. A giant fixture that prepares the entire application can hide dependencies instead of clarifying them.

## 30. Fixtures can perform teardown with `yield`

```python
import pytest


@pytest.fixture
def opened_resource():
    resource = {"open": True}
    yield resource
    resource["open"] = False
```

Code before `yield` performs setup. Code after `yield` performs teardown when pytest finalizes the fixture.

Use actual context managers when the production resource already provides one.

## 31. Fixture scope controls lifetime

Common fixture scopes are:

```text
function -> one test invocation
class    -> one test class
module   -> one test module
package  -> one test package
session  -> the whole pytest session
```

The default is `function` scope.

## 32. Wider fixture scope trades isolation for reuse

A session-scoped resource may be faster to create once, but it also lives longer and can carry shared mutable state between tests.

Do not increase fixture scope only to make a suite faster. First understand whether the shared lifetime preserves test independence.

## 33. Fixtures can depend on other fixtures

```python
import pytest


@pytest.fixture
def base_url() -> str:
    return "https://example.invalid"


@pytest.fixture
def endpoint(base_url: str) -> str:
    return f"{base_url}/items"
```

Dependency composition is often cleaner than one fixture that knows every setup detail.

## 34. Avoid hidden dependencies with excessive `autouse`

An `autouse=True` fixture runs without appearing in every test signature.

This can be useful for a true suite-wide invariant, but widespread autouse fixtures make behavior harder to trace.

Prefer explicit fixture parameters unless automatic application is genuinely part of the test environment contract.

## 35. `conftest.py` shares local pytest configuration and fixtures

A common structure is:

```text
tests/
├── conftest.py
├── test_api.py
└── test_reports.py
```

Fixtures defined in `tests/conftest.py` can be discovered by tests below that directory without importing `conftest` directly.

## 36. `conftest.py` follows directory visibility rules

For a given test, pytest searches relevant `conftest.py` files in that test's directory and parent directories.

This makes fixture visibility hierarchical.

Place shared fixtures at the narrowest directory level that needs them rather than automatically putting everything at the test root.

## 37. Do not import from `conftest.py`

Treat `conftest.py` as pytest configuration, not as an application module.

If helpers need normal Python imports, put them in a regular module or package and import that module from tests and fixtures.

## 38. `tmp_path` gives each test a temporary `Path`

```python
from pathlib import Path


def test_export(tmp_path: Path) -> None:
    report = tmp_path / "report.txt"
    report.write_text("ready\n", encoding="utf-8")

    assert report.read_text(encoding="utf-8") == "ready\n"
```

`tmp_path` is a `pathlib.Path` unique to the test invocation.

This avoids polluting the repository with test artifacts.

## 39. `tmp_path_factory` is useful for wider fixture scopes

A session- or module-scoped fixture cannot depend on a function-scoped `tmp_path`.

For broader temporary-resource lifetimes, pytest provides `tmp_path_factory`.

Choose broader lifetime only when it is part of the test design.

## 40. `monkeypatch` changes state and restores it automatically

The `monkeypatch` fixture can temporarily modify:

- object attributes;
- dictionary items;
- environment variables;
- `sys.path`;
- current working directory.

Its changes are undone after the requesting test or fixture finishes.

## 41. Patch environment variables with `setenv` and `delenv`

```python
import os


def read_mode() -> str:
    return os.getenv("STUDY_MODE", "default")


def test_configured_mode(monkeypatch) -> None:
    monkeypatch.setenv("STUDY_MODE", "focused")
    assert read_mode() == "focused"
```

Environment-dependent code becomes deterministic when the test controls the environment explicitly.

## 42. Patch where the code looks up the dependency

Suppose `service.py` contains:

```python
from client import fetch_status


def is_ready() -> bool:
    return fetch_status() == "ready"
```

A test usually needs to patch `service.fetch_status`, because that is the name `is_ready()` resolves at runtime.

Patching the original definition in `client` may not replace an already imported reference in `service`.

## 43. `monkeypatch.context()` can limit patch lifetime further

When a test needs a patch only for a small block, `monkeypatch.context()` provides a nested context whose changes are undone when that block exits.

Smaller patch lifetimes reduce surprising interactions inside complex tests.

## 44. Use test doubles to replace boundaries, not everything

A test double may stand in for a slow, nondeterministic, destructive, or unavailable collaborator.

Common informal categories include:

```text
stub  -> returns controlled values
fake  -> lightweight working implementation
spy   -> records how it was used
mock  -> verifies expected interactions
```

The vocabulary is less important than making the replacement's purpose clear.

## 45. The standard library `unittest.mock` works with pytest

pytest does not require a separate mocking style.

You can combine pytest assertions and fixtures with `unittest.mock.Mock`, `MagicMock`, or `patch` when those tools fit the test.

Do not mock pure calculations just because mocking is available.

## 46. `capsys` captures Python-level stdout and stderr

```python
def announce(topic: str) -> None:
    print(f"Studying: {topic}")


def test_announce(capsys) -> None:
    announce("pytest")
    captured = capsys.readouterr()
    assert captured.out == "Studying: pytest\n"
    assert captured.err == ""
```

This is useful for command-line interfaces and functions whose output stream is part of the contract.

## 47. `capfd` captures at the file-descriptor level

`capsys` focuses on Python's `sys.stdout` and `sys.stderr` objects.

`capfd` captures file descriptors 1 and 2, which can be useful when output comes from lower-level code or subprocess-adjacent components that bypass normal Python stream objects.

Use the narrowest capture mechanism that matches the behavior being tested.

## 48. `caplog` captures logging records

```python
import logging


def test_log_message(caplog) -> None:
    logger = logging.getLogger("study")

    with caplog.at_level(logging.INFO, logger="study"):
        logger.info("session ready")

    assert "session ready" in caplog.text
```

Tests can also inspect structured log records instead of only matching rendered text.

## 49. Be careful when reconfiguring the root logger during `caplog`

pytest documentation warns that changing root logger handlers during a test can interfere with log capture.

Prefer targeted logger configuration and avoid replacing the whole root-handler set unless the test specifically validates logging configuration.

## 50. Marks attach metadata to tests

Marks can classify or alter test behavior.

```python
import pytest


@pytest.mark.slow
def test_large_report() -> None:
    assert True
```

Custom marks should describe useful test categories, not become a substitute for clear test organization.

## 51. Register custom marks

Unregistered custom marks can produce warnings and spelling mistakes can silently create unintended categories.

A `pyproject.toml` can register them:

```toml
[tool.pytest.ini_options]
markers = [
    "slow: tests that intentionally take longer",
    "integration: tests that cross component boundaries",
]
```

Registration turns mark names into a documented project contract.

## 52. `strict_markers` can turn unknown marks into errors

```toml
[tool.pytest.ini_options]
strict_markers = true
```

This is useful when a misspelled marker should fail immediately instead of being treated as a new marker.

## 53. pytest 9 introduced broader strict mode

pytest 9 provides a `strict` configuration option that enables several strictness checks together, currently including strict configuration, markers, xfail behavior, and parametrization IDs.

The documentation cautions that future pytest versions may add more strictness options. Use global strict mode with a controlled pytest version or when the project deliberately wants to adopt new strict checks.

## 54. Skip tests only for a real environmental reason

```python
import sys

import pytest


@pytest.mark.skipif(sys.platform == "win32", reason="POSIX-only contract")
def test_posix_behavior() -> None:
    assert True
```

A skipped test does not verify the behavior. Too many skips can create blind spots.

## 55. `xfail` records a known expected failure

```python
import pytest


@pytest.mark.xfail(reason="known parser limitation", strict=True)
def test_future_case() -> None:
    assert False
```

With `strict=True`, an unexpected pass fails the suite, forcing the team to notice that the known limitation may have been fixed.

Do not use `xfail` as a permanent parking lot for broken tests.

## 56. Select tests with `-k`

`-k` filters collected tests by name expression:

```bash
python -m pytest -k "report and not slow"
```

This is convenient during local development, but CI should still run the intended complete suite or explicitly documented partitions.

## 57. Select marked groups with `-m`

```bash
python -m pytest -m "integration"
```

or:

```bash
python -m pytest -m "not slow"
```

Marks make suite partitions explicit when they are registered and maintained consistently.

## 58. Stop early with `-x` or `--maxfail`

```bash
python -m pytest -x
```

stops after the first failure.

```bash
python -m pytest --maxfail=3
```

stops after three failures.

These options are useful for feedback speed. They do not replace running the full suite before release.

## 59. Re-run previous failures with `--lf`

```bash
python -m pytest --lf
```

pytest can use its cache to select tests that failed in the previous run.

Treat this as a local development accelerator. A clean CI job must not depend on state from a developer's previous run.

## 60. Verbosity changes reporting, not correctness

Common options include:

```bash
python -m pytest -q
python -m pytest -v
```

Quiet output can be useful in automated logs; verbose output can help identify individual parameter cases.

The test contract should not depend on terminal decoration.

## 61. Configuration belongs in version control

pytest supports project configuration through supported config files such as `pyproject.toml`, `pytest.ini`, and others documented by the project.

A minimal `pyproject.toml` configuration might be:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
strict_markers = true
```

Configuration should make the suite more predictable, not hide failing behavior.

## 62. `testpaths` narrows default discovery

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

When pytest is invoked without explicit test paths, this tells it where the project expects tests to live.

If tests also live elsewhere, configure or invoke them intentionally.

## 63. Be cautious with global `addopts`

A project may configure default command-line options, for example:

```toml
[tool.pytest.ini_options]
addopts = "-ra"
```

Avoid defaults that quietly skip important test categories or suppress diagnostics developers need to see.

## 64. Understand the project root pytest selects

pytest determines a root directory and configuration context for collection.

Running pytest from an unexpected directory can change which configuration and `conftest.py` files are visible.

When debugging discovery problems, inspect the reported rootdir and configuration file.

## 65. Keep imports predictable

Tests are still Python modules, so import rules matter.

A project should use a deliberate package layout and test against the code it intends to ship, rather than relying on accidental working-directory imports.

The common `src/` layout can help distinguish installed application code from repository-local paths.

## 66. Do not give pytest test classes a custom `__init__`

pytest test classes are collected by convention and should not behave like application objects requiring constructor arguments.

Use fixtures for test dependencies instead of custom test-class construction.

Plain test functions are often the simplest starting point.

## 67. Fixture values should match their declared meaning

If a fixture is named `authenticated_client`, it should reliably provide that state.

Avoid fixtures whose result changes unexpectedly according to unrelated global settings. Ambiguous fixtures make tests read like riddles.

## 68. Avoid fixture forests

Fixture composition is powerful, but a test that depends on one fixture that depends on six more fixtures can become difficult to understand.

If setup feels like a dependency maze, consider simpler builders, helper functions, or smaller integration boundaries.

## 69. Unit tests isolate a small behavioral unit

A unit test usually exercises a function, class, or small component with controlled collaborators.

Unit tests are valuable for fast feedback, but the exact definition of “unit” depends on architecture.

Do not turn the label into a doctrinal rule.

## 70. Integration tests cross real component boundaries

An integration test may exercise combinations such as:

```text
application code + database adapter
application code + local HTTP server
parser + real file format
repository + temporary filesystem
```

Integration tests intentionally validate contracts that mocks cannot fully prove.

## 71. End-to-end tests validate larger workflows

End-to-end tests exercise a broad path through the system and can detect integration problems that smaller tests miss.

They are also usually slower, more expensive to diagnose, and more sensitive to environment state.

A healthy suite commonly uses several layers rather than one test type for everything.

## 72. Test observable behavior before implementation details

If a refactor preserves the public behavior, good tests should usually keep passing.

Tests that assert every private helper call often make internal cleanup unnecessarily expensive.

Interaction assertions are appropriate when the interaction itself is part of the contract, such as “do not send the request twice.”

## 73. Mock external services at the correct boundary

A unit test should not make a live request to a public API.

For HTTP code, useful strategies include:

- patching your own client abstraction;
- using a local test server;
- using a purpose-built HTTP test plugin when the project adopts one.

Tests should not depend on public network availability unless they are deliberately external-system tests.

## 74. Keep secrets out of test data

Never place real tokens, passwords, cookies, private URLs, or personal data in tests.

Use fictional values such as:

```python
fake_token = "test-token-not-a-secret"
```

Test fixtures often end up copied into logs and failure reports, so they deserve the same privacy discipline as production code.

## 75. Control time instead of racing the clock

Avoid tests like:

```python
import time


def test_waits() -> None:
    time.sleep(2)
    assert True
```

If behavior depends on time, inject a clock or patch the narrow time source the code uses.

Sleeping makes suites slow and does not guarantee that asynchronous state is ready.

## 76. Control randomness

For code that uses randomness, options include:

- injecting a random-number generator;
- using a known seed when that contract is appropriate;
- testing invariants over controlled inputs.

A test that fails only on some random runs is difficult to reproduce and diagnose.

## 77. Tests should not depend on execution order

A test should not require another test to run first.

Shared mutable module or session state is a common cause of order dependence.

If tests fail only when the suite order changes, the suite has exposed a real isolation problem.

## 78. A flaky test is a reliability defect

A flaky test alternates between pass and fail without a relevant code change.

Common causes include:

- timing races;
- external services;
- shared state;
- nondeterministic ordering;
- insufficient cleanup;
- resource exhaustion.

Repeatedly rerunning until green hides the signal rather than repairing it.

## 79. Coverage and correctness are different metrics

Code coverage can reveal code that tests never execute.

It cannot prove that assertions are meaningful, boundary cases are represented, or requirements are correct.

Treat coverage as evidence about execution, not as a substitute for test design.

## 80. Plugins extend pytest

pytest has a large plugin ecosystem for domains such as coverage, asynchronous code, frameworks, parallel execution, and HTTP testing.

Plugins are dependencies too. Pin or bound important plugin versions, review their compatibility, and avoid adding a plugin when core pytest already solves the problem clearly.

## 81. Core pytest does not automatically make every `async def` test work

Asynchronous test functions generally require an appropriate async testing plugin or framework integration.

Do not assume that installing pytest alone defines the event-loop policy your application needs.

The plugin becomes part of the test dependency contract.

## 82. `required_plugins` can enforce plugin presence

pytest configuration can declare required plugins so a run fails early when a necessary plugin is missing.

This is useful when the suite would otherwise collect incorrectly or fail later with confusing missing-fixture errors.

Use exact project requirements rather than copying plugin lists from unrelated repositories.

## 83. pytest can run many `unittest`-style tests

Adopting pytest does not necessarily require rewriting an existing `unittest` suite immediately.

pytest supports running many tests written with `unittest.TestCase` while allowing gradual use of pytest features around the broader suite.

Migration should improve maintainability, not create churn for its own sake.

## 84. Treat test exit codes as CI contracts

A CI system should fail when the test runner reports failure.

Do not write shell wrappers that discard pytest's exit status.

The repository's executable examples later in this chapter convert pytest's programmatic exit code to an integer only so the demonstration can report it deterministically.

## 85. Executable example: assertions and parametrization

[`examples/assertions_and_parametrize.py`](examples/assertions_and_parametrize.py) creates a temporary pytest module, runs it with the real pytest runner, and reports only deterministic summary data.

Expected output:

```text
exit code: 0
passed: 4
```

The temporary suite demonstrates one normal assertion plus three parametrized boundary cases.

## 86. Executable example: fixtures and `tmp_path`

[`examples/fixtures_and_tmp_path.py`](examples/fixtures_and_tmp_path.py) demonstrates a fixture that depends on pytest's built-in `tmp_path` fixture.

Expected output:

```text
exit code: 0
passed: 2
```

Each test receives its own fixture invocation and temporary filesystem boundary.

## 87. Executable example: `monkeypatch`

[`examples/monkeypatch_environment.py`](examples/monkeypatch_environment.py) controls an environment variable without leaving process-global test state behind.

Expected output:

```text
exit code: 0
passed: 2
```

The example verifies both the fallback state and an explicitly configured state.

## 88. Executable example: exceptions and warnings

[`examples/exceptions_and_warnings.py`](examples/exceptions_and_warnings.py) uses `pytest.raises` and `pytest.warns` to make failure and migration behavior explicit.

Expected output:

```text
exit code: 0
passed: 2
```

Both exception type/message behavior and warning category/message behavior are verified.

## 89. Executable example: output and log capture

[`examples/capture_output_and_logs.py`](examples/capture_output_and_logs.py) demonstrates `capsys` and `caplog`.

Expected output:

```text
exit code: 0
passed: 2
```

The test suite validates both command-line output and a targeted logger message.

## 90. Common mistakes

### Mistake 1: treating a green suite as proof of no bugs

Tests only cover the behaviors and inputs they actually exercise.

### Mistake 2: testing implementation trivia

Overly coupled tests make harmless refactoring expensive.

### Mistake 3: sharing mutable state between tests

This creates order dependence and flakes.

### Mistake 4: calling public services from unit tests

Network availability and remote data changes make the suite nondeterministic.

### Mistake 5: hiding all warnings

Warnings often reveal migrations the project needs to make.

### Mistake 6: overusing mocks

A suite of mocks can prove that mocks behave exactly as configured while missing real integration errors.

### Mistake 7: creating giant fixtures

Large setup graphs hide what each test actually needs.

### Mistake 8: accepting flaky reruns as normal

A flaky test is a defect in the feedback system.

## 91. Decision table

| Need | Useful pytest tool | Main caution |
| --- | --- | --- |
| Compare normal values | `assert` | keep the expected contract explicit |
| Compare floats | `pytest.approx()` | choose domain-appropriate tolerance |
| Expect an exception | `pytest.raises()` | do not catch unrelated failures |
| Expect a warning | `pytest.warns()` | test warning category/message deliberately |
| Repeat one rule over cases | `@pytest.mark.parametrize` | choose meaningful boundary data |
| Reuse setup | fixture | avoid hidden, oversized dependency graphs |
| Temporary files | `tmp_path` | do not depend on repository artifacts |
| Temporary environment changes | `monkeypatch` | patch where the code looks up the name |
| Capture stdout/stderr | `capsys` | assert only output that is part of the contract |
| Capture logs | `caplog` | avoid disrupting root logger handlers |
| Classify tests | registered marks | avoid silent spelling mistakes |
| Known expected failure | `xfail` | prefer strict handling and remove when fixed |

## 92. Quick reference

```bash
python -m pytest
python -m pytest -q
python -m pytest -v
python -m pytest --collect-only
python -m pytest -k "name_expression"
python -m pytest -m "marker_expression"
python -m pytest -x
python -m pytest --maxfail=3
python -m pytest --lf
python -m pytest --max-warnings=10
```

Core Python patterns:

```python
assert actual == expected

with pytest.raises(ValueError, match="message"):
    operation()

with pytest.warns(DeprecationWarning):
    old_operation()
```

## 93. Review checklist

Before calling a test suite reliable, ask:

- Are the intended tests actually collected?
- Do test names explain behaviors?
- Are assertions specific enough to fail for the right reason?
- Are boundary and error cases represented?
- Are files written under temporary paths?
- Are environment changes restored automatically?
- Are network, clock, and randomness boundaries controlled?
- Can tests run independently and in any order?
- Are warnings visible and intentional?
- Are custom marks registered?
- Are expected failures reviewed and temporary?
- Does CI preserve pytest's failing exit status?
- Are test data and logs free of secrets and personal data?

## 94. Practice exercise

Create a small fictional package that validates study-session records.

Requirements:

1. Create a function that receives a topic and a duration in minutes.
2. Reject an empty topic with `ValueError`.
3. Reject zero or negative duration with `ValueError`.
4. Return a normalized dictionary for valid input.
5. Write normal success tests using plain `assert`.
6. Parametrize at least three invalid duration cases.
7. Use `pytest.raises(..., match=...)` for one validation error.
8. Write a fixture that returns valid sample data.
9. Add a function that saves a session as text or JSON and test it with `tmp_path`.
10. Add a function that reads one configuration value from an environment variable and test it with `monkeypatch`.
11. Add one CLI-style function and validate output with `capsys`.
12. Add one logger call and validate it with `caplog`.
13. Register one custom marker for integration tests.
14. Run `python -m pytest --collect-only` and confirm the expected cases appear.
15. Run the complete suite from a clean process.

Extension challenges:

- move shared fixtures into a carefully scoped `conftest.py`;
- add a warning for a deprecated input form and test it with `pytest.warns`;
- use `pytest.approx` for a calculated ratio with a documented tolerance;
- build a local HTTP integration test using concepts from the previous `requests` chapter;
- add CI that installs the declared dependencies and runs the suite from scratch.

## 95. Connections to earlier concepts

`pytest` connects almost every earlier phase:

- **functions:** test behavior through explicit inputs and outputs;
- **collections:** build parameter tables and structured expected values;
- **program flow:** exercise branches and boundary conditions;
- **exceptions:** validate deliberate failure contracts;
- **files:** isolate filesystem behavior with temporary paths;
- **modules and packages:** organize application code and test imports predictably;
- **`pathlib`:** work naturally with `tmp_path`;
- **`datetime`:** inject or patch time boundaries instead of racing real time;
- **logging:** validate operational signals with `caplog`;
- **`decimal`:** test exact monetary rules without inappropriate float tolerance;
- **pandas/openpyxl/requests:** turn external-library behavior into repeatable regression tests.

## 96. Primary references

- [pytest documentation](https://docs.pytest.org/)
- [Get Started](https://docs.pytest.org/en/stable/getting-started.html)
- [How to invoke pytest](https://docs.pytest.org/en/stable/how-to/usage.html)
- [Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
- [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Temporary directories](https://docs.pytest.org/en/stable/how-to/tmp_path.html)
- [Monkeypatching](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [Logging](https://docs.pytest.org/en/stable/how-to/logging.html)
- [Warnings](https://docs.pytest.org/en/stable/how-to/capture-warnings.html)
- [Skip and xfail](https://docs.pytest.org/en/stable/how-to/skipping.html)
- [API reference](https://docs.pytest.org/en/stable/reference/reference.html)
- [pytest changelog](https://docs.pytest.org/en/stable/changelog.html)
- [pytest on PyPI](https://pypi.org/project/pytest/)

At the time this chapter was prepared, PyPI listed pytest 9.1.1 as the latest stable release. The curriculum targets the 9.1.x series rather than the unreleased 9.2 draft or an unbounded future version.

## 97. Phase 9 complete

Phase 9 now connects four important third-party boundaries:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
requests -> communicate with HTTP services
pytest   -> verify behavior repeatedly and automatically
```

That closes **Phase 9: External Libraries**.

The next phase moves from isolated library skills to integrated portfolio work: **Phase 10: Practical Projects**.

Before moving on, practice writing tests that make failures informative. A test suite is most valuable when it gives you confidence to change the code, not when it merely produces a green number.

<div align="center">

# Raising and Custom Exceptions

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Errors, Files, and Modules](../README.md) · [← Previous chapter: Handling Exceptions](../01-try-except-else-finally/README.md)

Chapter 01 focused on **handling exceptions that already occur**. This chapter adds the other side of the contract: deciding when your own code should deliberately report that an operation cannot continue normally.

Python uses the `raise` statement for that purpose. A function can validate its inputs or state, raise an appropriate exception when its contract cannot be honored, and let a caller decide where recovery or explanation belongs.

The chapter also introduces **custom exception classes**. This is a narrow introduction to class inheritance specifically for exceptions, not a full object-oriented-programming chapter.

**Estimated study time:** 90–120 minutes.

**Python requirement:** Python 3.10 or newer. The examples reuse modern annotations such as `list[str]` and the exception-handling concepts from Chapter 01.

## Learning goals

By the end of this chapter, you should be able to:

- explain the difference between handling an exception and raising one;
- use `raise` to signal an invalid value or state deliberately;
- choose a suitable built-in exception for common validation failures;
- write useful exception messages without treating message text as a programmatic API;
- explain why raising an exception interrupts the current normal path;
- let exceptions propagate to a layer that can handle them meaningfully;
- re-raise the currently handled exception with a bare `raise`;
- translate one exception into another with `raise ... from ...`;
- explain the purpose of explicit exception chaining;
- define a simple custom exception class;
- choose when a custom exception adds useful domain meaning;
- catch a custom exception without hiding unrelated failures;
- distinguish `raise` from `assert`;
- avoid broad, vague, or unnecessary exception designs.

## 1. Handling and raising are different responsibilities

Chapter 01 used `except` to respond to a failure:

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

This chapter focuses on code that **creates the failure signal deliberately**:

```python
if score < 0:
    raise ValueError("score cannot be negative")
```

The two responsibilities connect like this:

```text
callee detects a condition it cannot accept
        ↓
callee raises an exception
        ↓
normal execution in that call is interrupted
        ↓
exception propagates outward
        ↓
a suitable caller may handle it
```

A function does not need to know how every caller will recover. It needs to report failure accurately enough that callers can make that decision.

## 2. The basic `raise` syntax

The most common beginner form is:

```python
raise ValueError("score must be between 0 and 100")
```

`ValueError` is the exception class. The text passed to it becomes useful diagnostic information carried by the exception instance.

The general syntax also supports re-raising and exception chaining, which appear later in this chapter.

## 3. Raising an exception interrupts the current normal path

Consider:

```python
def validate_score(score: int) -> int:
    if score > 100:
        raise ValueError("score cannot exceed 100")
    print("Validation finished")
    return score
```

If `score` is `120`, execution reaches `raise`. The later `print()` and `return` are not executed in that call unless the exception is somehow handled inside a surrounding structure before control leaves it.

Conceptually:

```text
score = 120
    ↓
condition is true
    ↓
raise ValueError(...)
    ↓
normal path stops here
    ↓
search outward for a matching handler
```

This is the same propagation model learned in Chapter 01, but now your own code deliberately starts the exceptional path.

## 4. Raise when a function cannot honor its contract

A useful way to think about validation is through a function contract.

Suppose this function promises to accept only percentages from 0 through 100:

```python
def normalize_percentage(value: int) -> int:
    if not 0 <= value <= 100:
        raise ValueError("value must be between 0 and 100")
    return value
```

For `75`, the function can honor its contract and returns normally.

For `130`, returning the value as if everything were valid would violate the contract. Raising `ValueError` makes the invalid state explicit.

## 5. Guard clauses keep invalid paths near the top

Validation often reads clearly when invalid cases are rejected first:

```python
def calculate_average(total: float, count: int) -> float:
    if count <= 0:
        raise ValueError("count must be greater than zero")
    return total / count
```

The first `if` is a **guard clause**. It protects the valid path from a known invalid precondition.

This pattern often makes the main operation easier to read:

```text
invalid precondition? → raise
otherwise             → continue with normal work
```

A guard clause is a design pattern, not special Python syntax.

## 6. `ValueError` is appropriate for many invalid values

`ValueError` is useful when an argument has an acceptable general kind of value but its specific value is invalid for the operation.

Examples include:

```python
def set_progress(progress: int) -> int:
    if not 0 <= progress <= 100:
        raise ValueError("progress must be between 0 and 100")
    return progress
```

and:

```python
def choose_level(level: str) -> str:
    if level not in {"beginner", "intermediate", "advanced"}:
        raise ValueError("unsupported level")
    return level
```

The important question is not merely "Can Python store this value?" It is "Is this value valid for this function's contract?"

## 7. `TypeError` can describe an unsupported type

A public API may sometimes deliberately reject an argument because its runtime type is unsupported:

```python
def repeat_label(label: str, times: int) -> str:
    if not isinstance(label, str):
        raise TypeError("label must be a string")
    if not isinstance(times, int):
        raise TypeError("times must be an integer")
    return label * times
```

However, do not add runtime type checks everywhere merely because type hints exist.

Type hints communicate expected types to readers and tooling, but they do not automatically enforce those types at runtime. Add explicit checks only when the API genuinely needs runtime validation.

## 8. Choose the exception that best describes the failed contract

Useful beginner-level choices include:

| Situation | Common exception |
|---|---|
| value outside an accepted range | `ValueError` |
| unsupported runtime argument type | `TypeError` |
| required mapping key is missing in an API that naturally exposes that lookup | `KeyError` |
| requested sequence position is outside the available range | `IndexError` |
| requested file does not exist | `FileNotFoundError` |
| operation is not implemented for the requested case | `NotImplementedError` |

This table is guidance, not a rule that every function must manually raise each of these exceptions.

Often a built-in operation already raises the most appropriate exception naturally. Do not duplicate checks only to recreate the same signal unless your function needs a clearer contract or message.

## 9. Do not use `Exception` when a more specific built-in fits

This is legal:

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise Exception("invalid age")
    return age
```

But it gives callers little information about what category of failure occurred.

Prefer:

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

Specific exception types make selective handling possible.

## 10. Exception messages should explain the violated expectation

Compare:

```python
raise ValueError("invalid")
```

with:

```python
raise ValueError("score must be between 0 and 100")
```

The second message is more useful to a person reading a traceback or log.

A practical message often states:

- what was invalid;
- what the accepted condition was;
- enough context to diagnose the problem without exposing secrets or sensitive data.

Avoid placing passwords, access tokens, private paths, or confidential payloads in exception messages.

## 11. Do not make program logic depend on exact exception-message text

Messages are primarily diagnostic text for people.

Avoid logic like:

```python
try:
    validate_score(score)
except ValueError as error:
    if str(error) == "score must be between 0 and 100":
        print("Range problem")
```

If callers need to distinguish failure categories programmatically, use distinct exception **types**, structured return values, or another explicit API contract.

## 12. `raise` can receive an exception instance or class

Python permits:

```python
raise ValueError("invalid score")
```

and also:

```python
raise ValueError
```

When given an exception class, Python instantiates it as needed with no arguments.

For teaching and application code, raising an instance with a useful message is usually clearer:

```python
raise ValueError("score must be between 0 and 100")
```

## 13. Exceptions can propagate through several function calls

A helper can raise an exception without handling it:

```python
def validate_quantity(quantity: int) -> int:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return quantity


def build_order(quantity: int) -> str:
    valid_quantity = validate_quantity(quantity)
    return f"Order quantity: {valid_quantity}"
```

If `validate_quantity()` raises `ValueError`, `build_order()` stops its normal path too unless it handles that exception.

The exception continues outward through the call stack.

## 14. Handle the exception at a layer that can respond meaningfully

A low-level validation helper may know **what is wrong** but not **what the program should do next**.

For example:

```python
def validate_quantity(quantity: int) -> int:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return quantity


try:
    quantity = validate_quantity(0)
except ValueError as error:
    print(f"Could not continue: {error}")
```

The validator reports the contract violation. The caller chooses the user-facing response.

A useful design question is:

```text
Does this layer know how to recover or explain the failure?
    yes → handling may belong here
    no  → let the exception propagate
```

## 15. Do not raise and immediately catch without a reason

This often adds ceremony without improving the design:

```python
def validate_score(score: int) -> int:
    try:
        if not 0 <= score <= 100:
            raise ValueError("invalid score")
    except ValueError:
        return 0
    return score
```

The function turns a clear contract violation into an unrelated fallback value.

If `0` is genuinely the documented fallback, returning it directly may be clearer. If invalid input should be reported, let the `ValueError` propagate.

Raise and handle at the same layer only when that layer truly has a meaningful recovery action.

## 16. A bare `raise` re-raises the active exception

Inside an `except` block, a bare `raise` sends the currently handled exception outward again:

```python
def parse_quantity(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        print("Could not parse quantity")
        raise
```

The handler performs some local work, then preserves the failure instead of pretending the operation succeeded.

Conceptually:

```text
ValueError occurs
    ↓
except ValueError runs
    ↓
local logging or cleanup
    ↓
bare raise
    ↓
same active exception continues outward
```

## 17. Prefer bare `raise` when your goal is simply to re-raise

Inside an active handler, this is the direct re-raise form:

```python
except ValueError:
    raise
```

Writing `raise error` raises that exception object again as an explicit raise operation and can alter the traceback presentation by adding the current raise location.

When your intent is "continue propagating the exception I am currently handling," bare `raise` communicates that intent more precisely.

## 18. Translating exceptions can improve an abstraction boundary

Sometimes a lower-level exception exposes an implementation detail that callers should not need to understand.

Suppose configuration text must contain an integer:

```python
class ConfigurationError(Exception):
    pass


def parse_attempt_limit(text: str) -> int:
    try:
        return int(text)
    except ValueError as error:
        raise ConfigurationError("attempt limit must be an integer") from error
```

The caller can now handle `ConfigurationError` as part of the configuration API instead of depending directly on the internal conversion detail.

## 19. `raise ... from ...` creates an explicit exception chain

In:

```python
raise ConfigurationError("attempt limit must be an integer") from error
```

`ConfigurationError` is the new exception and `error` is recorded as its explicit cause.

If the new exception remains unhandled, Python's traceback display shows the relationship between the original failure and the translated failure.

This preserves diagnostic history while allowing the higher-level API to expose a more meaningful exception type.

## 20. Explicit chaining is especially useful when changing abstraction levels

A common shape is:

```text
low-level operation fails
        ↓
low-level exception is caught
        ↓
higher-level exception is raised from the original
        ↓
caller sees the higher-level contract
        ↓
diagnostics still retain the original cause
```

Examples include translating parsing errors into configuration errors or storage-library errors into an application-specific persistence error.

Do not translate every exception automatically. Translate when doing so makes the public boundary clearer.

## 21. `from None` suppresses displayed context and should be deliberate

Python also allows:

```python
raise ValueError("invalid identifier") from None
```

This suppresses automatic display of the previous exception context in the resulting traceback.

It can be useful when the lower-level failure is irrelevant or confusing to users, but it also removes diagnostic context from the displayed traceback. Use it sparingly and deliberately.

## 22. Custom exceptions are exception classes you define

A custom exception lets an application give a failure a domain-specific type.

The smallest useful form is:

```python
class EmptyStudyPlanError(Exception):
    pass
```

This creates a new exception class named `EmptyStudyPlanError` that inherits normal application-exception behavior from `Exception`.

The `pass` statement means the class does not add any extra behavior yet.

## 23. This is a narrow introduction to class inheritance

The syntax:

```python
class EmptyStudyPlanError(Exception):
    pass
```

means, conceptually:

```text
Exception
    ↓
EmptyStudyPlanError
```

`EmptyStudyPlanError` is a more specific kind of `Exception`.

That relationship matters because:

```python
except EmptyStudyPlanError:
```

can catch only that custom category, while:

```python
except Exception:
```

can also catch it because the custom class inherits from `Exception`.

You do not need a complete object-oriented-programming model to use this simple pattern safely.

## 24. Application-level custom exceptions normally inherit from `Exception`

For ordinary application failures, define custom exceptions under `Exception`, directly or through another appropriate application exception.

Prefer:

```python
class StudyPlanError(Exception):
    pass
```

over deriving directly from `BaseException`.

`BaseException` also sits above control-flow exceptions such as `KeyboardInterrupt` and `SystemExit`, which ordinary application handlers typically should not accidentally group together with domain failures.

## 25. Custom exception names conventionally end in `Error`

Examples:

```python
class EmptyStudyPlanError(Exception):
    pass
```

```python
class ConfigurationError(Exception):
    pass
```

The `Error` suffix is a strong Python convention for exception-class names and makes their purpose immediately visible.

## 26. Raise a custom exception just like a built-in one

```python
class EmptyStudyPlanError(Exception):
    pass


def summarize_plan(topics: list[str]) -> str:
    if not topics:
        raise EmptyStudyPlanError("study plan must contain at least one topic")
    return ", ".join(topics)
```

The custom type carries domain meaning. The message carries human-readable detail.

## 27. Catch the custom type when you know how to respond

```python
try:
    summary = summarize_plan([])
except EmptyStudyPlanError as error:
    print(f"Plan error: {error}")
```

This handler does not accidentally catch unrelated exceptions such as a programming `TypeError` elsewhere in the same operation.

Specific custom types can therefore make an API easier to handle correctly.

## 28. Do not create a custom exception for every tiny validation rule

This can become noisy:

```text
NegativeScoreError
ScoreTooLargeError
EmptyScoreTextError
UnsupportedScoreFormatError
...
```

If all those situations mean the same thing to callers, a built-in `ValueError` may be sufficient.

Create a custom exception when the **category itself** is meaningful to callers, logging, tests, or an abstraction boundary.

## 29. A custom exception can inherit from a meaningful built-in category

If a domain-specific error is also clearly a kind of built-in error, inheritance can preserve both meanings:

```python
class ScoreRangeError(ValueError):
    pass
```

Now callers may choose either:

```python
except ScoreRangeError:
```

for the specific domain case, or:

```python
except ValueError:
```

for a broader value-error policy.

Use this only when the built-in parent accurately describes the custom failure.

## 30. Custom exceptions can carry structured attributes

A simple custom class often needs only `pass`, but an exception can also store structured details:

```python
class ScoreRangeError(ValueError):
    def __init__(self, score: int) -> None:
        self.score = score
        super().__init__(f"score must be between 0 and 100: {score}")
```

A caller can then inspect `error.score` without parsing message text.

This is a slightly more advanced class pattern. Prefer the simpler `pass` form until structured exception data provides a real benefit.

## 31. Practical example: validate scores explicitly

```python
def validate_score(score: int) -> int:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score


scores = [85, 120]

for score in scores:
    try:
        valid_score = validate_score(score)
    except ValueError as error:
        print(f"Rejected {score}: {error}")
    else:
        print(f"Accepted {valid_score}")
```

Output:

```text
Accepted 85
Rejected 120: score must be between 0 and 100
```

Each item is validated independently. The validator raises; the loop decides how to continue after an invalid item.

Runnable version: [`examples/validate_score.py`](examples/validate_score.py).

## 32. Practical example: a custom domain exception

```python
class EmptyStudyPlanError(Exception):
    pass


def summarize_plan(topics: list[str]) -> str:
    if not topics:
        raise EmptyStudyPlanError("study plan must contain at least one topic")
    return ", ".join(topics)


plans = [["Functions", "Exceptions"], []]

for topics in plans:
    try:
        print(summarize_plan(topics))
    except EmptyStudyPlanError as error:
        print(f"Plan error: {error}")
```

Output:

```text
Functions, Exceptions
Plan error: study plan must contain at least one topic
```

Runnable version: [`examples/custom_exception.py`](examples/custom_exception.py).

## 33. Practical example: translate and chain an exception

```python
class ConfigurationError(Exception):
    pass


def parse_attempt_limit(text: str) -> int:
    try:
        limit = int(text)
    except ValueError as error:
        raise ConfigurationError("attempt limit must be an integer") from error

    if limit <= 0:
        raise ConfigurationError("attempt limit must be greater than zero")

    return limit


try:
    parse_attempt_limit("three")
except ConfigurationError as error:
    cause_name = type(error.__cause__).__name__ if error.__cause__ else "None"
    print(f"{type(error).__name__}: {error}")
    print(f"Cause: {cause_name}")
```

Output:

```text
ConfigurationError: attempt limit must be an integer
Cause: ValueError
```

The explicit cause remains available through `__cause__` even though the higher-level code handles `ConfigurationError`.

Runnable version: [`examples/exception_chaining.py`](examples/exception_chaining.py).

## 34. `raise` and `assert` are not interchangeable

An assertion expresses a condition that the programmer expects to be true while debugging or checking an internal invariant:

```python
assert total >= 0
```

Assertions can be disabled when Python runs with optimization enabled.

Therefore, do not use `assert` for validation that must always happen, such as checking user input, file contents, API data, or a public function contract.

Use an explicit exception instead:

```python
if total < 0:
    raise ValueError("total cannot be negative")
```

## 35. Raise before mutating shared state when possible

Suppose invalid data should not enter a list:

```python
def add_score(scores: list[int], score: int) -> None:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    scores.append(score)
```

Validation happens before mutation.

That order reduces the chance of leaving partially updated state after failure.

A useful flow is:

```text
validate preconditions
        ↓
raise if invalid
        ↓
perform state-changing work only after validation succeeds
```

## 36. Common mistake: raising the wrong category

This is misleading:

```python
def validate_name(name: str) -> str:
    if not name:
        raise TypeError("name is empty")
    return name
```

An empty string still has the expected type `str`; the problem is its value.

`ValueError` communicates the failure more accurately:

```python
def validate_name(name: str) -> str:
    if not name:
        raise ValueError("name cannot be empty")
    return name
```

## 37. Common mistake: catching your custom base too broadly

Imagine:

```python
class ApplicationError(Exception):
    pass
```

It may be tempting to wrap large sections with:

```python
except ApplicationError:
    print("Something failed")
```

But a broad application base class can still collapse several distinct failure categories into one vague response.

Catch the narrowest type that the current layer can actually handle meaningfully.

## 38. Common mistake: converting every exception into a custom one

This is not automatically better:

```python
try:
    value = int(text)
except ValueError as error:
    raise ApplicationError("operation failed") from error
```

If callers already understand `ValueError` and the conversion is part of the public contract, the translation may add no useful abstraction.

Custom exceptions should clarify boundaries, not merely rename built-in failures.

## 39. Common mistake: hiding diagnostic history unnecessarily

Using:

```python
raise ConfigurationError("invalid configuration") from None
```

may produce a cleaner user-facing traceback, but it suppresses display of the previous exception context.

If the lower-level cause would help developers diagnose the failure, explicit chaining with `from error` is usually more informative.

## 40. Exercise

Build a small study-session validator that deliberately reports invalid input.

Requirements:

1. Create a custom exception named `StudySessionError` that inherits from `Exception`.
2. Create `validate_session(minutes: int, topic: str) -> tuple[int, str]`.
3. Raise `ValueError` when `minutes` is less than or equal to zero.
4. Raise `StudySessionError` when `topic` is empty after `strip()`.
5. Return the validated `(minutes, topic)` tuple when both values are valid.
6. Create at least three test cases containing one valid session and both failure categories.
7. Handle `ValueError` and `StudySessionError` separately at the caller.
8. Print deterministic messages for every case.
9. Add a helper that receives a text version of minutes, converts it with `int()`, and raises `StudySessionError("minutes must be an integer") from error` when conversion fails.
10. Before running the code, draw the normal and exceptional paths for each input.

Extra challenge: decide whether the conversion helper should expose `ValueError` directly or translate it to `StudySessionError`, and explain which API boundary your choice creates.

## 41. Review checklist

You should now be able to answer:

- What does `raise` do to the current normal execution path?
- When is `ValueError` a better fit than `TypeError`?
- Why should exception messages not become a string-matching API?
- What happens when a raised exception has no local handler?
- When should a low-level helper let an exception propagate?
- What does a bare `raise` do inside an `except` block?
- Why is bare `raise` usually preferable when simply re-raising the active exception?
- What relationship does `raise NewError(...) from error` record?
- Why can exception chaining improve an abstraction boundary?
- Why should `from None` be used deliberately?
- What does `class CustomError(Exception): pass` mean at a beginner level?
- Why do application custom exceptions normally inherit from `Exception` rather than directly from `BaseException`?
- When is a custom exception more useful than a built-in exception?
- Why should `assert` not validate required external input?
- Why is validation often safer before mutating shared state?

## 42. Quick reference

| Need | Useful approach |
|---|---|
| reject an invalid value | `raise ValueError("...")` |
| reject an unsupported runtime type | `raise TypeError("...")` when runtime checking is truly part of the API |
| preserve the current handled exception | bare `raise` |
| translate an exception while preserving its cause | `raise NewError("...") from error` |
| suppress displayed previous context deliberately | `raise NewError("...") from None` |
| introduce a domain-specific failure category | `class DomainError(Exception): pass` |
| preserve both domain and built-in value semantics | subclass an appropriate built-in exception, such as `ValueError` |
| distinguish failures programmatically | use exception types or structured data, not message-string parsing |
| validate external/user data reliably | explicit checks + `raise`, not `assert` |
| reduce partial state changes | validate before mutation when practical |

## 43. Scope boundary

This chapter deliberately does **not** teach in depth yet:

- full object-oriented programming and general class design;
- multiple inheritance for exception classes;
- `ExceptionGroup` and `except*`;
- advanced traceback manipulation;
- retry policies;
- logging frameworks;
- context managers and file cleanup;
- testing exception contracts with `pytest`.

Those topics are easier once the basic raise/propagate/handle model is stable.

## 44. Where Phase 7 goes next

The progression is now:

```text
handle exceptions that already occur
        ↓
raise exceptions deliberately
        ↓
choose built-in or custom exception types
        ↓
propagate, re-raise, or chain deliberately
        ↓
next: open and manage files safely
        ↓
structured text data
        ↓
modules and packages
```

Next planned chapter: **`open()` and `with`**.

## Official references

- [Python 3.14 Language Reference: The `raise` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-raise-statement)
- [Python 3.14 Tutorial: Raising Exceptions](https://docs.python.org/3.14/tutorial/errors.html#raising-exceptions)
- [Python 3.14 Tutorial: User-defined Exceptions](https://docs.python.org/3.14/tutorial/errors.html#user-defined-exceptions)
- [Python 3.14 Built-in Exceptions](https://docs.python.org/3.14/library/exceptions.html)
- [Python 3.14 Language Reference: The `assert` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-assert-statement)

<div align="center">

# Handling Exceptions with `try`, `except`, `else`, and `finally`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Errors, Files, and Modules](../README.md) · [← Previous phase: Comments and Documentation](../../comments-and-documentation/README.md)

Programs do not always follow the happy path. A conversion can receive invalid text, a division can use zero, a dictionary lookup can miss a key, or a later file operation can fail.

Python represents many of these runtime failures with **exceptions**. A `try` statement lets a program define what should happen when a specific exception interrupts normal execution.

This chapter focuses on **handling exceptions that already occur**. Chapter 02 will cover creating exceptions deliberately with `raise` and defining simple custom exception classes.

**Estimated study time:** 90–120 minutes.

**Python requirement:** Python 3.10 or newer. The examples reuse modern type-hint syntax such as `int | None` from the Functions phase.

## Learning goals

By the end of this chapter, you should be able to:

- explain the difference between a syntax error and a runtime exception;
- describe how an exception interrupts normal control flow;
- use `try` and a specific `except` clause;
- catch different exception types with separate handlers;
- access a caught exception with `as` when its details are useful;
- explain why handler order matters;
- use `else` for code that should run only when the `try` block completes normally;
- use `finally` for cleanup work that should happen on every exit path;
- explain what happens when no `except` clause matches;
- keep `try` blocks narrow enough to show which operation may fail;
- avoid hiding unrelated failures with overly broad handlers;
- distinguish handling an exception from preventing every possible invalid state;
- trace the execution path through `try`, `except`, `else`, and `finally`.

## 1. Normal flow and exceptional flow

Most code follows a normal sequence:

```text
statement 1
    ↓
statement 2
    ↓
statement 3
```

An exception changes that path:

```text
statement 1
    ↓
failing operation
    ↓ exception raised
search for a matching handler
```

If a matching handler exists, execution can continue from the handling structure. If no matching handler exists, the exception continues outward through surrounding code and function calls.

This is a different control-flow mechanism from `if`, loops, and ordinary `return` values.

## 2. Syntax errors and exceptions are not the same thing

A **syntax error** means Python cannot parse the source code according to the language grammar.

For example, this source is invalid:

```python
if score > 70
    print("Ready")
```

The missing colon prevents the file from being parsed normally.

A **runtime exception** happens after Python has valid code to execute but an operation cannot complete normally.

```python
number = int("seven")
```

The syntax is valid. The conversion fails at runtime and raises `ValueError`.

This chapter is mainly about handling runtime exceptions.

## 3. What an unhandled exception looks like conceptually

Consider:

```python
number = int("seven")
print(number)
```

`int("seven")` cannot produce the requested integer. Python raises `ValueError` before `print(number)` can run.

When an exception remains unhandled in a normal script, execution stops and Python reports a traceback describing where the failure propagated.

The important beginner model is:

```text
operation cannot complete
        ↓
exception object is raised
        ↓
normal path is interrupted
        ↓
Python searches for a matching handler
```

## 4. The smallest useful `try` and `except`

```python
try:
    number = int("seven")
except ValueError:
    print("Invalid integer")
```

Output:

```text
Invalid integer
```

The `try` block contains code that may raise an exception.

The `except ValueError` block describes what to do if a `ValueError` reaches this `try` statement.

## 5. Read the structure as two possible paths

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

A useful trace is:

```text
try int(text)
    ├─ succeeds → continue after try statement
    └─ ValueError → run except ValueError
```

The `except` block does not run when the protected operation succeeds.

## 6. Catch the exception you expect

Prefer naming the failure the code is prepared to handle:

```python
try:
    score = int("ninety")
except ValueError:
    print("Score must be an integer")
```

This tells readers that invalid numeric text is an expected failure case here.

Specific handlers also let unrelated programming mistakes continue to surface instead of being silently converted into the same fallback behavior.

## 7. A successful `try` skips its `except` handlers

```python
try:
    score = int("90")
except ValueError:
    print("Invalid score")

print(score)
```

Output:

```text
90
```

No `ValueError` occurred, so the handler was skipped.

## 8. The rest of a `try` block is skipped after an exception

```python
try:
    number = int("seven")
    print("Conversion succeeded")
except ValueError:
    print("Conversion failed")
```

Output:

```text
Conversion failed
```

Once `int("seven")` raises `ValueError`, Python does not continue with the next statement inside that same `try` block.

Control moves to the matching handler.

## 9. Access the exception object with `as`

A handler can bind the caught exception to a local name:

```python
try:
    number = int("seven")
except ValueError as error:
    print(type(error).__name__)
```

Output:

```text
ValueError
```

The name after `as` refers to the exception object while the handler is running.

Use it when the exception type or details genuinely help with logging, diagnostics, or a user-facing explanation.

## 10. Do not build logic around exact exception messages

Exception text is useful for people, but exact message wording can change between Python versions or implementation details.

Prefer branching on the exception **type**:

```python
try:
    number = int("seven")
except ValueError:
    print("Invalid integer")
```

rather than checking whether an exception message contains a particular sentence.

## 11. Different failures can need different handlers

A calculation may fail while converting text or while dividing:

```python
try:
    numerator = float("12")
    denominator = float("0")
    result = numerator / denominator
except ValueError:
    print("Invalid numeric text")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

Python searches the handlers in order and runs the first one that matches the raised exception.

## 12. Handler order matters

Exception classes form a hierarchy. A handler for a more general base class can also match subclasses.

When both a specific and a broader handler are present, place the specific handler first:

```python
try:
    value = int(text)
except ValueError:
    print("Invalid integer")
except Exception:
    print("Unexpected application error")
```

Putting `except Exception` first would make the later `except ValueError` unreachable for a `ValueError`, because the broader handler already matches it.

## 13. One handler can match a tuple of exception types

If several failures genuinely need the same response, an `except` clause can name a tuple:

```python
try:
    result = int(text) / divisor
except (ValueError, ZeroDivisionError):
    print("Could not calculate the result")
```

This is useful only when the same recovery behavior makes sense for every listed exception.

Separate handlers are clearer when different failures need different explanations or recovery paths.

## 14. `else` describes the success-only path

A `try` statement can include `else`:

```python
try:
    score = int("90")
except ValueError:
    print("Invalid score")
else:
    print(f"Parsed score: {score}")
```

Output:

```text
Parsed score: 90
```

The `else` block runs when the `try` block completes normally without an exception and without an early control-flow exit such as `return`, `break`, or `continue`.

## 15. Why not put all success code inside `try`?

This works:

```python
try:
    score = int(text)
    print(f"Parsed score: {score}")
except ValueError:
    print("Invalid score")
```

But the `print()` call is not the operation we expect to raise `ValueError`.

Using `else` can keep the protected region smaller:

```python
try:
    score = int(text)
except ValueError:
    print("Invalid score")
else:
    print(f"Parsed score: {score}")
```

Now the structure communicates more precisely which operation belongs to the expected failure boundary.

## 16. Keep the `try` block narrow

A large `try` block can make it unclear which statement produced the exception.

Prefer:

```python
try:
    quantity = int(text)
except ValueError:
    print("Invalid quantity")
else:
    total = quantity * unit_price
    print(total)
```

when only the conversion is expected to fail with `ValueError`.

Narrow `try` blocks make exception boundaries easier to inspect and reduce the chance of handling an unrelated failure accidentally.

## 17. `finally` describes cleanup that must happen

A `finally` block runs as the `try` statement is being left, whether the protected work succeeded, a matching handler ran, or an unhandled exception is continuing outward.

```python
try:
    number = int("12")
except ValueError:
    print("Invalid integer")
finally:
    print("Finished conversion attempt")
```

Output:

```text
Finished conversion attempt
```

The `finally` block is about cleanup and guaranteed finalization, not about deciding whether the original operation succeeded.

## 18. `finally` also runs after a handled exception

```python
try:
    number = int("twelve")
except ValueError:
    print("Invalid integer")
finally:
    print("Finished conversion attempt")
```

Output:

```text
Invalid integer
Finished conversion attempt
```

The handler responds to the `ValueError`. The `finally` block still runs afterward.

## 19. `finally` also runs when an exception remains unhandled

Conceptually:

```python
try:
    result = 10 / 0
finally:
    print("Cleanup runs")
```

`ZeroDivisionError` is not handled here, so it still propagates after `finally` finishes.

The cleanup runs, but the exception is not magically converted into success.

## 20. Combine `try`, `except`, `else`, and `finally`

```python
try:
    score = int("90")
except ValueError:
    print("except: invalid score")
else:
    print(f"else: parsed {score}")
finally:
    print("finally: attempt finished")
```

Output:

```text
else: parsed 90
finally: attempt finished
```

The structure separates four responsibilities:

| Clause | Responsibility |
|---|---|
| `try` | perform work that may raise an expected exception |
| `except` | handle a matching failure |
| `else` | continue the success-only path |
| `finally` | perform cleanup on every exit path |

## 21. Trace a handled failure through all clauses

```python
try:
    score = int("ninety")
except ValueError:
    print("except: invalid score")
else:
    print(f"else: parsed {score}")
finally:
    print("finally: attempt finished")
```

Output:

```text
except: invalid score
finally: attempt finished
```

Trace:

```text
enter try
    ↓
int("ninety") raises ValueError
    ↓
matching except runs
    ↓
else is skipped
    ↓
finally runs
    ↓
continue after try statement
```

## 22. If no handler matches, the exception propagates

```python
try:
    result = "12" + 3
except ValueError:
    print("Invalid value")
```

The operation raises `TypeError`, not `ValueError`.

Because the handler does not match, the `TypeError` keeps moving outward to surrounding exception handlers or, if none exists, to the interpreter.

This is useful behavior. A handler should not pretend it recovered from a failure it does not understand.

## 23. Exceptions can cross function boundaries

```python
def parse_score(text: str) -> int:
    return int(text)


try:
    score = parse_score("ninety")
except ValueError:
    print("Invalid score")
```

Output:

```text
Invalid score
```

`parse_score()` does not handle the exception. The `ValueError` propagates back to its caller, where the caller chooses to handle it.

This connects exception flow directly to the function call stack studied in Phase 5.

## 24. Decide where an exception can be handled meaningfully

Not every function should catch every exception it can possibly encounter.

A useful design question is:

```text
Does this layer know what recovery or explanation makes sense?
    yes → handling may belong here
    no  → let the exception propagate
```

A low-level parsing helper may simply let `ValueError` propagate. A user-facing coordinator may know how to turn that failure into a helpful message.

This is a design guideline, not a Python syntax rule.

## 25. Avoid bare `except:` for ordinary application handling

A bare handler looks like this:

```python
try:
    value = int(text)
except:
    print("Something failed")
```

It catches exceptions derived from `BaseException`, directly or indirectly, including control-flow exceptions such as `KeyboardInterrupt` and `SystemExit` that applications usually should not swallow accidentally.

For ordinary application failures, catch the specific exception types you expect.

## 26. `except Exception` is broad too

This is narrower than bare `except:`:

```python
try:
    value = int(text)
except Exception:
    print("Operation failed")
```

`Exception` is the common base class for most application-level built-in exceptions, so it can still hide many unrelated bugs if used casually.

A broad handler can be appropriate at a deliberate boundary, such as a top-level logging layer, but beginner code should usually start with specific expected exceptions.

## 27. Common built-in exception types you will meet

| Exception | Typical beginner situation |
|---|---|
| `ValueError` | a value has the right general type but an invalid value, such as `int("seven")` |
| `TypeError` | an operation receives an inappropriate type, such as adding a string and an integer |
| `ZeroDivisionError` | division or modulo uses zero as the divisor |
| `KeyError` | a dictionary lookup requests a missing key with `mapping[key]` |
| `IndexError` | a sequence index is outside the available range |
| `FileNotFoundError` | a requested file path does not exist when opening a file |

The goal is not to memorize every built-in exception now. Learn to read the exception type and understand what operation produced it.

## 28. Exceptions and validation are different tools

Sometimes a simple condition can prevent an invalid operation:

```python
if denominator == 0:
    print("Cannot divide by zero")
else:
    print(numerator / denominator)
```

Other times an API naturally signals failure by raising an exception:

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

Do not turn this into a rigid rule that exceptions are always better or always worse than validation.

Choose the clearest boundary for the operation and the API you are using.

## 29. A handler should define a real recovery path

This code catches an error but gives the caller no usable information:

```python
try:
    number = int(text)
except ValueError:
    pass
```

The exception disappears silently.

Silent handling is dangerous when the program then continues with incomplete or incorrect state.

Prefer a handler that intentionally returns a fallback, asks for new input in an interactive program, records the failure, or communicates what went wrong.

## 30. Returning a fallback can be an explicit contract

```python
def parse_integer(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None
```

Here `None` explicitly means that parsing did not produce an integer.

The caller must then handle both possible results:

```python
result = parse_integer("seven")

if result is None:
    print("Invalid integer")
else:
    print(result)
```

This combines exception handling with the `None` data-flow model from Phase 5.

## 31. Practical example: safe text-based division

```python
def safe_divide(numerator_text: str, denominator_text: str) -> str:
    try:
        numerator = float(numerator_text)
        denominator = float(denominator_text)
        result = numerator / denominator
    except ValueError:
        return "invalid number"
    except ZeroDivisionError:
        return "division by zero"
    else:
        return f"result: {result:.2f}"
```

Example calls:

```python
print(safe_divide("12", "4"))
print(safe_divide("twelve", "4"))
print(safe_divide("12", "0"))
```

Output:

```text
result: 3.00
invalid number
division by zero
```

The function distinguishes conversion failure from arithmetic failure and returns a deterministic result for each expected path.

## 32. Loops can handle one bad item without discarding all good items

```python
values = ["10", "twenty", "30"]
parsed_values = []

for text in values:
    try:
        parsed_values.append(int(text))
    except ValueError:
        print(f"Skipped invalid value: {text}")

print(parsed_values)
```

Output:

```text
Skipped invalid value: twenty
[10, 30]
```

The handler belongs inside the loop because each item is an independent conversion attempt.

That is different from wrapping the entire loop in one large `try` block, where the first invalid item could interrupt the remaining iterations.

## 33. Keep side effects after successful risky work when possible

Suppose an operation may fail during parsing. It is often clearer to parse first and update shared state only after success:

```python
try:
    quantity = int(text)
except ValueError:
    print("Invalid quantity")
else:
    quantities.append(quantity)
```

This reduces the chance of leaving partially updated state after a failure.

## 34. `finally` is not a good place for `return`

A `return` inside `finally` can override an earlier return value and can even suppress an exception that was propagating.

Avoid this pattern:

```python
def calculate() -> int:
    try:
        return 10 // 0
    finally:
        return 0
```

The `finally` return hides the `ZeroDivisionError`.

Use `finally` for cleanup. Keep ordinary return-value decisions in the normal, handled, or success paths.

## 35. Future file handling will often prefer `with`

`finally` is a general cleanup tool. In the file chapter, you will learn that Python's `with` statement packages common resource-management patterns into a clearer interface.

For example, files are normally managed with a context manager rather than manually reproducing every cleanup path.

That later chapter builds directly on the cleanup idea introduced here.

## 36. Common mistake: catching the wrong exception type

```python
try:
    result = 10 / 0
except ValueError:
    print("Invalid value")
```

This does not handle the failure because division by zero raises `ZeroDivisionError`.

Read the traceback and match the handler to the actual failure you intend to recover from.

## 37. Common mistake: making the `try` block enormous

```python
try:
    quantity = int(text)
    total = quantity * unit_price
    report = build_report(total)
    save_result(report)
except ValueError:
    print("Invalid quantity")
```

If a later operation can also raise `ValueError`, the handler may accidentally treat a different bug as invalid user input.

Protect the smallest practical region whose expected failures you understand.

## 38. Common mistake: swallowing every exception

```python
try:
    process_data()
except Exception:
    pass
```

This can hide programming errors, invalid assumptions, and important diagnostic information.

Handling is useful only when the program has a deliberate response to the failure.

## 39. Common mistake: using exceptions as invisible branching

Exception handling should make failure boundaries clearer, not turn ordinary decisions into a maze.

If a condition is already known and simple to test, a normal `if` may communicate the decision better.

If an operation naturally reports failure through an exception, handling that exception may be the clearer design.

## 40. Common mistake: assuming `finally` means the operation succeeded

`finally` means the cleanup path runs. It says nothing about success.

```text
success            → finally runs
handled exception  → finally runs
unhandled exception→ finally runs, then exception continues
```

Keep success-only work in `else` or after a successfully completed operation.

## 41. Exercise

Build a small score parser that handles invalid text safely.

Requirements:

1. Create `parse_score(text: str) -> int | None`.
2. Inside the function, try to convert `text` with `int()`.
3. Catch `ValueError` and return `None`.
4. Use an `else` clause to return the successfully parsed integer.
5. Create a list containing at least three strings, including one invalid integer.
6. Loop over the list and call `parse_score()` for each item.
7. Print a clear message for invalid values and print the integer for valid values.
8. Add a `finally` block inside `parse_score()` that prints a short deterministic cleanup message for each attempt.
9. Before running the code, draw the possible paths through `try`, `except`, `else`, and `finally`.

Extension challenge: decide whether printing from `finally` belongs in the final design or whether it should be removed after you finish tracing the exercise.

## 42. Review checklist

You should now be able to answer these questions:

- What is the difference between invalid Python syntax and a runtime exception?
- What happens to the remaining statements in a `try` block after an exception is raised?
- Why should `except ValueError` usually be preferred over a bare `except:` when `ValueError` is the expected failure?
- When does an `else` clause run?
- When does a `finally` clause run?
- What happens when no `except` clause matches?
- Why can a large `try` block hide the real source of a failure?
- Why does handler order matter?
- What does `except Exception` catch broadly, and why should it be used deliberately?
- Why should code avoid depending on exact exception-message wording?
- How can a function let an exception propagate to a caller that knows how to handle it?
- How does exception flow connect to the function call stack?

## 43. Quick reference

| Situation | Useful approach |
|---|---|
| Operation may raise one expected exception | narrow `try` + specific `except` |
| Different failures need different responses | separate `except` clauses |
| Several exception types share one response | tuple in one `except` clause |
| Need the caught exception object | `except SomeError as error` |
| Work should run only after successful `try` | `else` |
| Cleanup must happen on every exit path | `finally` |
| No handler understands the failure | let the exception propagate |
| Handler catches too much | narrow the exception type or the `try` block |
| Need exact branching by error text | avoid it; branch on exception type instead |
| Need to create an exception deliberately | Chapter 02: `raise` and custom exceptions |

## 44. Scope boundary for this chapter

This chapter deliberately does **not** teach these topics in depth yet:

- `raise` and explicit exception creation;
- custom exception classes;
- exception chaining with `raise ... from ...`;
- exception groups and `except*`;
- file opening and context managers;
- logging exception tracebacks;
- advanced retry strategies.

Those ideas become easier after the basic handler model is stable.

## 45. Where Phase 7 goes next

The sequence now begins like this:

```text
runtime operation
        ↓
exception may occur
        ↓
try / except / else / finally
        ↓
next: raise exceptions deliberately
        ↓
files and structured data
        ↓
modules and packages
```

Next planned chapter: **Raising and Custom Exceptions**.

## Official references

- [Python 3.13 Tutorial: Errors and Exceptions](https://docs.python.org/3.13/tutorial/errors.html)
- [Python 3.13 Language Reference: The `try` statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-try-statement)
- [Python 3.13 Execution Model: Exceptions](https://docs.python.org/3.13/reference/executionmodel.html#exceptions)
- [Python 3.13 Built-in Exceptions](https://docs.python.org/3.13/library/exceptions.html)
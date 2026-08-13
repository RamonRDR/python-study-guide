<div align="center">

# Type Hints

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous: Scope](../04-scope/README.md)

Chapter 01 named behavior. Chapter 02 moved data into functions. Chapter 03 returned results. Chapter 04 explained where names live. This chapter adds another layer:

> How can a function describe the kinds of values it expects and returns?

```text
function interface
├── parameter names
├── parameter type hints
└── return type hint
        ↓
function body still runs as ordinary Python
```

**Estimated study time:** 75–100 minutes.

**Python version:** This chapter requires **Python 3.10 or newer**.

## Learning objectives

By the end of this chapter, you should be able to:

- explain what a type hint communicates;
- annotate parameters with `name: type`;
- annotate returns with `-> type`;
- explain that Python does not enforce type hints at runtime by itself;
- distinguish hints from runtime validation and conversion;
- use `str`, `int`, `float`, `bool`, and `None` in simple signatures;
- annotate `list`, `dict`, and tuple contents;
- use `str | None` for a simple value-or-`None` result;
- read a typed signature as a compact interface;
- keep hints aligned with the function's real behavior.

## 1. Type hints describe expected types

A **type hint** is information attached to code that describes the type a value is expected to have.

A basic typed function looks like this:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


message = greet("Avery")
print(message)
```

Output:

```text
Hello, Avery
```

Read the signature as:

```text
name: str → parameter is expected to receive a string
-> str    → function is expected to return a string
```

The hints make the intended data flow visible before you read the body.

## 2. Parameter annotations use a colon

A parameter hint comes after the parameter name:

```text
parameter_name: type
```

The colon annotates the parameter that already exists. It does not create a second parameter.

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


print(calculate_total(12.5, 4))
```

Output:

```text
50.0
```

The signature communicates `price → float`, `quantity → int`, and `return → float`.

## 3. Return annotations use an arrow

A return hint appears after the parameter list:

```text
def function_name(...) -> return_type:
```

The arrow describes the expected result. It does not perform a conversion.

```python
def is_passing(score: int) -> bool:
    return score >= 60


print(is_passing(72))
print(is_passing(45))
```

Output:

```text
True
False
```

## 4. Type hints do not enforce types at runtime by themselves

This is the most important rule in the chapter.

Python does not automatically reject a call just because an argument disagrees with a type hint:

```python
def echo_text(value: str) -> str:
    return value


result = echo_text(42)

print(result)
print(type(result).__name__)
```

Output:

```text
42
int
```

The function says `value: str`, but ordinary Python runtime execution still accepts `42` because the body merely returns the object.

An IDE or static type checker may warn about the call. The annotation itself is not a runtime guard.

## 5. Type hints do not convert values

A hint describes an expected type. It does not silently run `int()`, `float()`, `str()`, or another converter.

```python
def add_tax(amount: float) -> float:
    return amount * 1.1


print(add_tax(100.0))
```

Keep the concepts separate:

```text
type hint  → describes
conversion → transforms a compatible value explicitly
validation → checks an actual value or rule
```

## 6. Type hints and runtime validation solve different problems

Static typing tools reason about declared types before or while you write code. Runtime validation checks actual values while the program runs.

This example contains both ideas:

```python
def set_username(username: str) -> str:
    if not isinstance(username, str):
        raise TypeError("username must be a str")

    return username


print(set_username("Avery"))
```

`username: str` documents the intended type. `isinstance(username, str)` participates in runtime checking.

Using `str` here keeps the example focused. A check such as `isinstance(value, int)` has an extra beginner-visible detail because `bool` is a subclass of `int` in Python.

Do not add validation everywhere merely because a function has annotations. Validate where real program boundaries or rules require it.

## 7. Built-in types are often enough

Many beginner signatures need only types you already know: `str`, `int`, `float`, and `bool`.

You do not need an import from `typing` for these basic annotations.

```python
def build_label(topic: str, chapter: int) -> str:
    return f"Chapter {chapter}: {topic}"


label = build_label("Type Hints", 5)
print(label)
```

Output:

```text
Chapter 5: Type Hints
```

## 8. `-> None` describes no useful return value

Use `-> None` when a function is not designed to send a useful result back to the caller:

```python
def show_status(status: str) -> None:
    print(f"Status: {status}")


show_status("ready")
```

This connects directly to Chapter 03: reaching the end of a function without another returned value produces `None`.

## 9. Collections can describe element types

A bare `list` says only that a list is expected. Modern Python can also describe the expected element type:

```python
def first_topic(topics: list[str]) -> str:
    return topics[0]


print(first_topic(["scope", "type hints", "defaults"]))
```

Read `list[str]` as “a list whose elements are expected to be strings.”

## 10. Dictionaries describe key and value types

```python
def total_scores(scores: dict[str, int]) -> int:
    return sum(scores.values())


print(total_scores({"Avery": 8, "Jordan": 9}))
```

`dict[str, int]` communicates:

```text
keys   → expected str
values → expected int
```

The hint does not make Python automatically inspect every item at runtime.

## 11. Tuple hints can describe multiple results

```python
def min_and_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


print(min_and_max([4, 8, 2, 9]))
```

`tuple[int, int]` describes a tuple with two expected integer items. This fits naturally with comma-separated return values from Chapter 03.

## 12. `str | None` describes a value-or-`None` result

```python
def find_topic(topics: list[str], target: str) -> str | None:
    for topic in topics:
        if topic == target:
            return topic

    return None


print(find_topic(["scope", "type hints"], "type hints"))
print(find_topic(["scope", "type hints"], "files"))
```

Output:

```text
type hints
None
```

`str | None` means the expected result may be a string or `None`. The vertical bar expresses a union of allowed types.

Older code may spell the same idea as `typing.Optional[str]`. This guide targets modern Python, so `str | None` is the preferred spelling here. For now, you only need to recognize the older form when you encounter it.

## 13. Typed signatures label data flow you already know

```python
def summarize_scores(scores: list[int]) -> tuple[int, int]:
    lowest = min(scores)
    highest = max(scores)
    return lowest, highest


result = summarize_scores([72, 88, 91])
print(result)
```

Trace the interface:

```text
caller
↓
list[int]
↓
parameter
↓
function-local work
↓
tuple[int, int]
↓
caller
```

Hints do not replace parameters, scope, or `return`. They describe those boundaries.

## 14. Hints must match real behavior

```python
def format_score(score: int) -> str:
    return f"Score: {score}"


print(format_score(95))
```

The function accepts an integer and formats a string, so `score: int -> str` matches the implementation. A stale hint can be worse than no hint because it creates false confidence.

## 15. Variable annotations exist too

```python
course: str = "Python"
chapter: int = 5

print(course)
print(chapter)
```

Function interfaces remain the main focus here. You do not need to annotate every local variable. Add a local annotation when it genuinely improves clarity or tooling.

## 16. Annotations are function metadata

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


print(greet.__annotations__)
```

In Python 3.13, function annotations are available through the function object's `__annotations__` mapping.

The exact printed representation matters less than the idea that tools can inspect annotation metadata. Beginner code usually reads hints in source code rather than using `__annotations__` directly.

## 17. Static analysis and runtime are separate

A type checker can flag this call before execution:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


greet(42)
```

Python may still execute it if the operations in the body happen to support the object.

```text
static analysis → reasons about declared types
runtime         → executes Python objects and operations
```

## 18. Editors and tools can use hints

Type-aware tools can use hints for warnings, autocomplete, hover information, navigation, and refactoring support.

The exact features depend on the tool and configuration. The language feature remains the same: annotations describe the intended interface.

## 19. Function boundaries are a high-value place for hints

Compare:

```python
def summarize(scores):
    ...
```

with:

```python
def summarize(scores: list[int]) -> str:
    ...
```

The second signature immediately answers “what should I pass?” and “what should I expect back?”

## 20. Do not annotate everything just because you can

This is valid:

```python
def double(number: int) -> int:
    result: int = number * 2
    return result
```

But the local annotation may add little because the expression already makes `result` obvious.

Prefer hints that clarify interfaces and non-obvious values. Avoid turning a small function into a hedge maze of redundant labels.

## 21. A type hint is not a business rule

`value: int` can communicate that an integer is expected. It cannot by itself communicate or enforce a range such as:

```text
0 <= value <= 100
```

Type constraints and domain rules are different dimensions. Implement runtime checks when runtime rules matter.

## 22. Common mistakes

### Mistake 1: expecting automatic runtime enforcement

```python
def echo(value: str) -> str:
    return value


echo(10)
```

The annotation alone is not a runtime guard.

### Mistake 2: expecting automatic conversion

```python
def parse_count(count: int) -> int:
    return count
```

Passing `"5"` does not automatically create the integer `5`.

### Mistake 3: annotating the wrong return type

```python
def label(score: int) -> int:
    return f"Score: {score}"
```

The implementation returns a string, so `-> int` is misleading.

### Mistake 4: assuming type hints prove the algorithm is correct

A perfectly annotated function can still contain incorrect logic.

## 23. A practical example

```python
def progress_message(completed: int, total: int) -> str:
    percentage = completed / total * 100
    return f"{percentage:.0f}% complete"


print(progress_message(4, 5))
```

Output:

```text
80% complete
```

The signature makes the boundary clear: `completed → int`, `total → int`, `return → str`. The body still owns the calculation.

## Executable examples

The chapter includes three approved unattended examples:

### `annotated_greeting.py`

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


message = greet("Avery")

print(message)
```

```text
Hello, Avery
```

### `collection_summary.py`

```python
def summarize_topics(topics: list[str]) -> str:
    return f"{len(topics)} topics: {', '.join(topics)}"


print(summarize_topics(["scope", "type hints", "defaults"]))
```

```text
3 topics: scope, type hints, defaults
```

### `runtime_does_not_enforce.py`

```python
def echo_text(value: str) -> str:
    return value


result = echo_text(42)

print(result)
print(type(result).__name__)
```

```text
42
int
```

The last example deliberately passes an `int` to a parameter annotated as `str`. Python executes the call because annotations do not enforce the type by themselves.

## 24. Exercise

Create `build_summary`.

Requirements:

1. Receive `topic` as a string.
2. Receive `scores` as a list of integers.
3. Return a string.
4. Add hints to both parameters and the return.
5. Produce this result for the example call:

```python
print(build_summary("Python", [8, 9, 10]))
```

```text
Python: 3 scores
```

Before running it, explain what `topic: str`, `scores: list[int]`, and `-> str` communicate. Also answer whether Python would automatically reject every incompatible argument at runtime.

## 25. One possible solution

```python
def build_summary(topic: str, scores: list[int]) -> str:
    return f"{topic}: {len(scores)} scores"


print(build_summary("Python", [8, 9, 10]))
```

Output:

```text
Python: 3 scores
```

## 26. Review checklist

Before moving on, make sure you can explain:

- [ ] what a type hint communicates;
- [ ] parameter syntax with `:`;
- [ ] return syntax with `->`;
- [ ] why hints do not enforce types at runtime by themselves;
- [ ] why hints do not convert values;
- [ ] hints versus runtime validation;
- [ ] `-> None`;
- [ ] `list[str]`;
- [ ] `dict[str, int]`;
- [ ] `tuple[int, int]`;
- [ ] `str | None`;
- [ ] why hints must match real behavior;
- [ ] why not every local variable needs an annotation.

## 27. Quick reference

| Goal | Syntax | Meaning |
|---|---|---|
| Hint a parameter | `name: str` | expected string argument |
| Hint a return | `-> int` | expected integer result |
| No useful result | `-> None` | caller should not expect a useful result |
| List of strings | `list[str]` | expected string elements |
| Dictionary | `dict[str, int]` | string keys, integer values |
| Two-int tuple | `tuple[int, int]` | two expected integer items |
| String or `None` | `str | None` | either result is expected |
| Runtime validation | explicit code | checks actual runtime values |
| Conversion | `int(value)`, etc. | explicitly creates a converted value |

## Scope boundary

This chapter intentionally postpones:

- `TypeVar` and generic type parameters;
- `Protocol` and structural subtyping;
- overloads;
- `Literal` and `TypedDict`;
- advanced type aliases;
- callable and higher-order-function typing;
- type narrowing tools such as `TypeGuard` and `TypeIs`;
- configuration of specific static type checkers;
- runtime validation libraries.

These topics are valuable, but they require more context than a first chapter on function annotations.

## 28. What comes next

You now have this function model:

```text
define behavior
↓
receive arguments through parameters
↓
work inside local scope
↓
return results
↓
describe the interface with type hints
```

The next chapter adds **Default Values**, allowing some parameters to become optional at call time while keeping the interface explicit.

[← Previous: Scope](../04-scope/README.md) · [Back to Functions](../README.md)

## References

Primary Python documentation:

- [Python 3.13 `typing` — Support for type hints](https://docs.python.org/3.13/library/typing.html)
- [Python 3.13 Data model — function annotations and `__annotations__`](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13 Standard type hierarchy — `bool` and `int`](https://docs.python.org/3.13/library/stdtypes.html)

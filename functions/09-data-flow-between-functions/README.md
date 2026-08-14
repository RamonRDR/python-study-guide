<div align="center">

# Data Flow Between Functions

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous: Functions Working Together](../08-functions-working-together/README.md) · [Next phase: Comments and Documentation →](../../comments-and-documentation/README.md)

When functions work together, values move through a program. An argument enters a function, a parameter receives it, local names may transform it, and a return value can carry a result back to the caller or forward to another function.

This chapter makes that movement explicit. It also introduces an important distinction: **rebinding a parameter name is not the same as mutating a shared mutable object**.

**Estimated study time:** 90–120 minutes.

**Python requirement:** Python 3.10 or newer. This chapter uses modern annotation syntax such as `int | None` and built-in collection annotations such as `list[int]`.

## Learning goals

By the end of this chapter, you should be able to:

- trace a value from a caller into a parameter and back through `return`;
- explain that parameters are local names created for each function call;
- distinguish the caller's variable name from a function's parameter name;
- explain why rebinding a parameter does not rebind the caller's variable;
- recognize when mutation of a shared list or dictionary is visible outside a function;
- choose between returning a transformed value and deliberately mutating an object;
- use intermediate variables as checkpoints in a data pipeline;
- follow data through conditions, loops, and several function calls;
- use tuple returns when a function naturally produces several related results;
- handle `None` deliberately when a function may have no useful result;
- use type hints to describe expected data flow without treating them as runtime enforcement;
- avoid hidden data flow through unnecessary global state;
- distinguish a call graph from a data-flow trace;
- finish Phase 5 with a complete mental model of function inputs, local work, and outputs.

## 1. The basic data-flow cycle

A function call often follows this pattern:

```text
caller value
    ↓
argument expression
    ↓
parameter
    ↓
local work
    ↓
return value
    ↓
caller receives result
```

For example:

```python
def double(number: int) -> int:
    result = number * 2
    return result


original = 6
doubled = double(original)
print(original)
print(doubled)
```

Output:

```text
6
12
```

`original` and `number` are different names. During the call, `number` is a local parameter name bound to the value supplied by the caller.

## 2. Argument names and parameter names do not need to match

The caller may use any suitable variable name:

```python
def format_name(name: str) -> str:
    return name.strip().title()


raw_text = "  ava stone  "
clean_text = format_name(raw_text)
print(clean_text)
```

Output:

```text
Ava Stone
```

The relationship is created by the function call, not by matching variable names:

```text
raw_text ──argument──> name
```

Inside `format_name()`, the function works with its local parameter `name`.

## 3. Each function call gets its own local parameter bindings

Calling the same function twice does not make both calls share one local parameter.

```python
def add_one(number: int) -> int:
    number = number + 1
    return number


first = add_one(4)
second = add_one(10)
print(first, second)
```

Output:

```text
5 11
```

Each call has its own local `number` binding.

This connects directly to the earlier chapter on scope: local names belong to a particular function call.

## 4. Rebinding a parameter does not rebind the caller's variable

Consider an integer:

```python
def add_five(number: int) -> int:
    number += 5
    return number


score = 70
updated_score = add_five(score)
print(score)
print(updated_score)
```

Output:

```text
70
75
```

Inside the function, `number += 5` makes the local name `number` refer to the result `75`.

It does **not** make the caller's name `score` start referring to `75`.

The caller changes only if it explicitly assigns the returned value:

```python
score = add_five(score)
```

## 5. A returned value does not automatically replace the original value

This call computes and returns a result:

```python
updated_score = add_five(score)
```

The result is stored in `updated_score` because the caller chose that assignment target.

This call discards the return value:

```python
add_five(score)
```

Python still runs the function, but no caller name keeps the returned integer.

A useful mental model is:

```text
return provides a value
assignment decides where the caller stores it
```

## 6. Immutable values make rebinding easier to see

Integers, strings, and tuples are immutable. A function cannot change an existing integer or string object in place.

For example:

```python
def add_prefix(text: str) -> str:
    text = "INFO: " + text
    return text


message = "Ready"
formatted = add_prefix(message)
print(message)
print(formatted)
```

Output:

```text
Ready
INFO: Ready
```

The local parameter is rebound to a new string result. The caller's original name still refers to the original string.

## 7. Mutable objects add an important second possibility

Lists and dictionaries are mutable. If the caller and the function both refer to the same mutable object, the function can mutate that object.

```python
def add_topic(topics: list[str], topic: str) -> None:
    topics.append(topic)


topics = ["Functions"]
add_topic(topics, "Data flow")
print(topics)
```

Output:

```text
['Functions', 'Data flow']
```

The function did not rebind the caller's variable. It mutated the list object that both names referred to during the call.

## 8. Rebinding a list parameter is different from mutating the list

Compare these functions:

```python
def replace_topics(topics: list[str]) -> None:
    topics = ["New topic"]


def append_topic(topics: list[str]) -> None:
    topics.append("New topic")


first = ["Functions"]
second = ["Functions"]

replace_topics(first)
append_topic(second)

print(first)
print(second)
```

Output:

```text
['Functions']
['Functions', 'New topic']
```

`replace_topics()` only rebinds its local parameter name.

`append_topic()` changes the shared list object itself.

This distinction is central to reasoning about data flow in Python.

## 9. Mutation is not automatically wrong

A function that deliberately updates a list can have a clear interface:

```python
def record_score(scores: list[int], score: int) -> None:
    scores.append(score)
```

The important question is whether the mutation is expected and understandable.

Mutation becomes difficult when callers assume a function only reads data but it silently changes the object instead.

Make side effects deliberate and easy to discover through naming, documentation, and small focused behavior.

## 10. Returning a new result can make transformations easier to trace

Instead of mutating an input collection, a function can build and return a new collection.

```python
def clamp_scores(scores: list[int]) -> list[int]:
    result = []

    for score in scores:
        if score < 0:
            result.append(0)
        elif score > 100:
            result.append(100)
        else:
            result.append(score)

    return result


raw_scores = [105, 80, -4]
clean_scores = clamp_scores(raw_scores)
print(raw_scores)
print(clean_scores)
```

Output:

```text
[105, 80, -4]
[100, 80, 0]
```

This design preserves the original input and makes the transformation explicit through the returned value.

## 11. Choose mutation or returned transformation by intent

There is no Python rule saying every function must avoid mutation.

A useful decision question is:

```text
Should this function update this existing object?
    yes → deliberate mutation may fit
    no  → return a new result instead
```

Whichever design you choose, make it predictable for the caller.

## 12. Intermediate variables are data-flow checkpoints

Chapter 08 showed that several functions can form a pipeline. Intermediate names make each stage visible.

```python
def clamp_score(score: int) -> int:
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score


def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


raw_score = 108
clean_score = clamp_score(raw_score)
status = classify_score(clean_score)

print(raw_score, clean_score, status)
```

Output:

```text
108 100 excellent
```

The names `raw_score`, `clean_score`, and `status` act like labeled checkpoints.

## 13. Trace the pipeline one transformation at a time

The previous example can be drawn as:

```text
108
 ↓ clamp_score()
100
 ↓ classify_score()
"excellent"
```

This is a **data-flow trace**. It emphasizes the values moving between stages.

That is different from a call graph:

```text
main code
├── clamp_score()
└── classify_score()
```

A call graph emphasizes who calls whom. A data-flow trace emphasizes what data moves and changes.

## 14. A coordinating function can make the flow explicit

The same pipeline can live inside a coordinator:

```python
def clamp_score(score: int) -> int:
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score


def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def build_score_summary(score: int) -> str:
    clean_score = clamp_score(score)
    status = classify_score(clean_score)
    return f"{clean_score}: {status}"


print(build_score_summary(108))
```

Output:

```text
100: excellent
```

The coordinator owns the sequence. The helpers own individual transformations.

## 15. Data can branch through conditions

A function does not need to return the same value shape from every internal step, but its public behavior should remain understandable.

```python
def find_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

The input `score` reaches one of two return statements.

A simple trace is:

```text
score
  ↓ condition
  ├─ true  → "ready"
  └─ false → "review"
```

## 16. Early returns can stop data flow deliberately

Sometimes a function detects that it has no useful result to continue with.

```python
def find_first_positive(values: list[int]) -> int | None:
    for value in values:
        if value > 0:
            return value
    return None


result = find_first_positive([-4, -2, 7, 9])
print(result)
```

Output:

```text
7
```

The function returns as soon as the first suitable value is found.

## 17. `None` can represent the absence of a useful result

When `None` is part of the interface, the caller should handle it intentionally.

```python
def find_first_positive(values: list[int]) -> int | None:
    for value in values:
        if value > 0:
            return value
    return None


result = find_first_positive([-4, -2])

if result is None:
    print("No positive value")
else:
    print(result)
```

Output:

```text
No positive value
```

The caller checks the result before sending it into another calculation.

## 18. Do not accidentally continue a pipeline with `None`

Suppose another function expects an integer:

```python
def double(number: int) -> int:
    return number * 2
```

Passing a possible `None` value without checking first creates an unsafe flow.

The type hint `int | None` is useful because it tells readers and type-checking tools that the absence case exists.

Type hints describe the intended interface. Python does not automatically enforce them at runtime.

## 19. Several related outputs can travel in a tuple

A function may naturally produce more than one related result.

```python
def summarize(values: list[int]) -> tuple[int, int]:
    total = sum(values)
    count = len(values)
    return total, count


total, count = summarize([10, 20, 30])
print(total)
print(count)
```

Output:

```text
60
3
```

Python creates a tuple for the returned values, and the caller unpacks that tuple into two names.

## 20. Tuple returns make downstream dependencies visible

A later calculation can use one or both returned values:

```python
def summarize(values: list[int]) -> tuple[int, int]:
    return sum(values), len(values)


def calculate_average(total: int, count: int) -> float:
    if count == 0:
        return 0.0
    return total / count


total, count = summarize([10, 20, 30])
average = calculate_average(total, count)
print(average)
```

Output:

```text
20.0
```

The dependency is explicit: `calculate_average()` requires both `total` and `count`.

## 21. Loops can move many values through the same helper

A loop can send one item at a time into a function:

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


names = [" ava ", "LEO", " mia"]
clean_names = []

for name in names:
    clean_names.append(normalize_name(name))

print(clean_names)
```

Output:

```text
['Ava', 'Leo', 'Mia']
```

Each iteration creates another call and another local parameter binding.

## 22. Collections can move through several stages

A collection can be transformed, summarized, and formatted by different functions.

```python
def keep_positive(values: list[int]) -> list[int]:
    result = []

    for value in values:
        if value > 0:
            result.append(value)

    return result


def calculate_total(values: list[int]) -> int:
    return sum(values)


def format_total(total: int) -> str:
    return f"Total: {total}"


raw_values = [-3, 5, 8, -1]
positive_values = keep_positive(raw_values)
total = calculate_total(positive_values)
message = format_total(total)
print(message)
```

Output:

```text
Total: 13
```

The type of data changes along the route:

```text
list[int] → list[int] → int → str
```

## 23. Type hints can document the shape of each stage

The previous pipeline exposes its expected transitions directly in function signatures:

```text
keep_positive(list[int]) -> list[int]
calculate_total(list[int]) -> int
format_total(int) -> str
```

This can make a multi-function design easier to inspect.

Remember: type hints communicate intent and support tooling. They do not automatically validate or convert runtime values.

## 24. Hidden globals make data flow harder to see

Compare this hidden dependency:

```python
tax_rate = 0.10


def add_tax(amount: float) -> float:
    return amount * (1 + tax_rate)
```

with an explicit dependency:

```python
def add_tax(amount: float, tax_rate: float) -> float:
    return amount * (1 + tax_rate)
```

The second signature shows exactly what data the function needs.

A module-level constant can be appropriate in some designs. The problem is using global state to hide ordinary changing inputs that should be visible in the interface.

## 25. Avoid making one function read another function's local variables

A local name inside one function is not directly available inside another unrelated function.

```python
def first() -> int:
    value = 10
    return value


def second() -> int:
    value = first()
    return value * 2
```

`second()` receives the data through `first()`'s return value. It does not reach into `first()`'s local namespace.

That explicit handoff is a healthy boundary.

## 26. Practical example: build a learning report

This example combines several ideas from the entire Functions phase:

```python
def summarize_sessions(sessions: list[int]) -> tuple[int, float]:
    total = sum(sessions)
    if not sessions:
        return total, 0.0
    return total, total / len(sessions)


def classify_total(total: int) -> str:
    if total >= 120:
        return "deep"
    if total >= 60:
        return "steady"
    return "light"


def build_learning_report(subject: str, sessions: list[int]) -> str:
    total, average = summarize_sessions(sessions)
    workload = classify_total(total)
    return (
        f"{subject}: {total} minutes, "
        f"average {average:.1f}, workload {workload}"
    )


print(build_learning_report("Python", [30, 45, 60]))
```

Output:

```text
Python: 135 minutes, average 45.0, workload deep
```

Trace it:

```text
subject = "Python"
sessions = [30, 45, 60]
        ↓ summarize_sessions()
total = 135, average = 45.0
        ↓ classify_total(total)
workload = "deep"
        ↓ formatting
final str returned to caller
```

## 27. Empty-input behavior should be part of the data-flow design

`summarize_sessions()` explicitly handles an empty list:

```python
if not sessions:
    return total, 0.0
```

Without that branch, dividing by `len(sessions)` would fail when the list is empty.

Thinking about data flow includes asking:

- What values can enter this function?
- What values can leave it?
- What happens at boundary cases?
- Can the next function safely consume every possible result?

## 28. Common mistake: assuming parameter reassignment changes the caller

Incorrect expectation:

```python
def reset_score(score: int) -> None:
    score = 0


score = 80
reset_score(score)
print(score)
```

Output:

```text
80
```

If the caller should receive `0`, return it and assign the result:

```python
def reset_score(score: int) -> int:
    return 0


score = reset_score(score)
```

## 29. Common mistake: mutating input accidentally

This function changes the caller's list:

```python
def prepare_names(names: list[str]) -> None:
    names.sort()
```

That may be correct if mutation is the intended contract.

If the caller expects the original order to remain untouched, build and return a separate result instead.

The important lesson is not "never mutate." It is "do not hide mutation."

## 30. Common mistake: mixing returned data with printed output

A function may print a useful message and still return `None`:

```python
def show_total(values: list[int]) -> None:
    print(sum(values))
```

If the next function needs the numeric total, printing is not enough. Return the number.

This distinction has appeared throughout Phase 5 because it is one of the most important boundaries in function data flow.

## 31. Common mistake: passing the wrong stage into the next function

Consider this pipeline:

```text
raw score → clamp → classify
```

If the classification rule is supposed to use the clamped score, this is wrong:

```python
clean_score = clamp_score(raw_score)
status = classify_score(raw_score)
```

The code runs, but the data path is not the intended one.

Intermediate variable names make this kind of mistake easier to notice.

## 32. Common mistake: hiding too much in a deeply nested expression

This may be technically valid:

```python
message = format_total(calculate_total(keep_positive(raw_values)))
```

But when learning, debugging, or inspecting several stages, explicit checkpoints are often clearer:

```python
positive_values = keep_positive(raw_values)
total = calculate_total(positive_values)
message = format_total(total)
```

Choose readability over line-count competitions.

## 33. Exercise

Build a small pipeline for temperatures.

Requirements:

1. Create `clamp_temperature(temperature: int) -> int` that limits values below `-50` to `-50` and values above `50` to `50`.
2. Create `classify_temperature(temperature: int) -> str` that returns `"hot"` for values at least `30`, `"cold"` for values below `10`, and `"mild"` otherwise.
3. Create `build_temperature_report(city: str, temperature: int) -> str`.
4. Inside the coordinator, pass the original temperature through the clamp function first.
5. Pass the clamped result into the classification function.
6. Return a final string containing the city, clamped temperature, and category.
7. Test the coordinator with at least one temperature outside the accepted range.

Before coding, draw the data flow with arrows.

## 34. Review checklist

You should now be able to answer these questions:

- What is the difference between a caller variable and a parameter name?
- Does rebinding a parameter automatically rebind the caller's variable?
- Why can list mutation still be visible to the caller?
- When is returning a new value clearer than mutating an input?
- What does `return` provide to the caller?
- What role does assignment play after a function returns?
- How can `None` interrupt a pipeline?
- How can type hints make stage-to-stage data movement easier to understand?
- What is the difference between a call graph and a data-flow trace?
- Why are hidden global dependencies harder to reason about?

## 35. Quick reference

| Situation | Useful model |
|---|---|
| Caller sends a value | argument expression binds to a parameter for that call |
| Function reassigns a parameter | caller's variable binding is unchanged |
| Function mutates a shared list/dict | mutation can be visible to the caller |
| Function produces a transformed value | return it and let the caller assign it |
| Function may produce no useful result | return and handle `None` deliberately |
| Function produces related results | return a tuple and unpack it |
| Several stages cooperate | use intermediate names to expose the pipeline |
| Dependencies are hidden in globals | prefer explicit parameters/returns when appropriate |
| Need structural view | draw a call graph |
| Need value-movement view | draw a data-flow trace |

## 36. Phase 5 complete

You can now connect the full Functions sequence:

```text
define and call
    ↓
parameters and arguments
    ↓
return values
    ↓
scope
    ↓
type hints
    ↓
default values
    ↓
*args and **kwargs
    ↓
functions working together
    ↓
data flow between functions
```

The phase began with a single `def` and ends with a model for composing functions while tracking exactly how data enters, changes, and leaves each call.

Next in the recommended learning sequence: [Comments, Documentation, and Clean Code](../../comments-and-documentation/README.md).

## Official references

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Tutorial: More on Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Python 3.13 Language Reference: `return` statement](https://docs.python.org/3.13/reference/simple_stmts.html#the-return-statement)
- [Python 3.13 Data Model](https://docs.python.org/3.13/reference/datamodel.html)

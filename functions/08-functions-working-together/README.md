<div align="center">

# Functions Working Together

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous: `*args` and `**kwargs`](../07-args-and-kwargs/README.md)

A useful program rarely depends on one giant function. More often, several small functions **divide the work, call one another, and connect their results**.

This chapter turns the function features from the previous chapters into a composition model. The goal is not to create as many functions as possible. The goal is to give each meaningful piece of work a clear role and then connect those roles deliberately.

**Estimated study time:** 90–120 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- call one user-defined function from another;
- use a returned value as input to the next function;
- explain what happens to the caller while another ordinary function is running;
- distinguish a focused helper from a coordinating function;
- separate calculation from presentation when that improves reuse;
- keep dependencies visible through parameters and return values;
- recognize when a global variable is being used to hide data flow;
- use intermediate variables to make a chain of calls easier to trace;
- read a simple call graph;
- combine functions with conditions and loops;
- recognize duplicated logic that should become a reusable helper;
- avoid splitting a simple operation into unnecessary tiny functions;
- identify hidden side effects that make collaboration harder to reason about;
- prepare for the next chapter's deeper treatment of data flow between calls.

## 1. Why functions need to collaborate

Earlier chapters isolated individual function skills:

```text
define behavior
receive inputs
return outputs
control scope
describe types
provide defaults
collect flexible arguments
```

Real programs connect those skills.

A larger task such as preparing a study summary may naturally contain smaller tasks:

```text
session durations
      ↓
calculate total minutes
      ↓
classify workload
      ↓
build readable summary
```

Each step can become a function when separating it makes the program easier to understand, test, reuse, or change.

## 2. One function can call another

A function call can appear inside another function just like other expressions and statements.

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


def build_greeting(name: str) -> str:
    clean_name = normalize_name(name)
    return f"Welcome, {clean_name}!"


print(build_greeting("  ava stone  "))
```

Output:

```text
Welcome, Ava Stone!
```

The important relationship is:

```text
build_greeting()
      ↓ calls
normalize_name()
      ↓ returns
clean_name
```

`build_greeting()` does not need to repeat the normalization logic. It delegates that part to `normalize_name()`.

## 3. The caller waits for the called function to finish

For an ordinary function call in this chapter, execution moves into the called function. When that call finishes, execution continues in the caller.

Trace this example:

```python
def double(number: int) -> int:
    return number * 2


def add_one_after_doubling(number: int) -> int:
    doubled = double(number)
    return doubled + 1


print(add_one_after_doubling(5))
```

The order is:

```text
1. call add_one_after_doubling(5)
2. enter add_one_after_doubling()
3. call double(5)
4. enter double()
5. return 10
6. continue inside add_one_after_doubling()
7. return 11
8. print 11
```

The outer function does not continue past `double(number)` until that call has produced its result.

## 4. Return values are natural connection points

A return value lets one function finish its responsibility and hand a result to another part of the program.

```python
def calculate_area(width: int, height: int) -> int:
    return width * height


def format_area(area: int) -> str:
    return f"Area: {area}"


area = calculate_area(6, 4)
message = format_area(area)
print(message)
```

Output:

```text
Area: 24
```

The two functions have different jobs:

```text
calculate_area() → produce a number
format_area()    → turn a number into text
```

That separation makes each result easier to reuse.

## 5. Use intermediate names when they improve the story

Python allows nested calls:

```python
def calculate_area(width: int, height: int) -> int:
    return width * height


def format_area(area: int) -> str:
    return f"Area: {area}"


print(format_area(calculate_area(6, 4)))
```

This is valid. Before `format_area()` can run, Python evaluates `calculate_area(6, 4)` to obtain the argument value.

For beginners, this version may be easier to trace:

```python
area = calculate_area(6, 4)
message = format_area(area)
print(message)
```

Prefer the version that makes the data movement easiest to understand. Fewer lines do not automatically mean clearer code.

## 6. Think in responsibilities

Suppose one function receives a score, decides its category, formats a sentence, and prints it.

That may be acceptable for a tiny one-use script. But if the category logic or formatting will be reused, separate responsibilities can help.

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"
```

Now each function answers one clear question:

```text
classify_score()      → What category does this score belong to?
format_score_report() → How should these already-known values be displayed?
```

## 7. A coordinating function can connect helpers

A larger function can coordinate smaller functions without duplicating their work.

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"


def build_score_report(student: str, score: int) -> str:
    status = classify_score(score)
    return format_score_report(student, score, status)


print(build_score_report("Ava", 84))
```

Output:

```text
Ava: 84 points - ready
```

In this guide, we may call `classify_score()` and `format_score_report()` **helpers**, while `build_score_report()` acts as a **coordinator** or **orchestrator**.

Those words describe design roles. They are not special Python syntax.

## 8. One responsibility is a design guideline, not a Python rule

Python does not require every function to perform exactly one tiny action.

This function is not invalid:

```python
def build_label(name: str, quantity: int) -> str:
    clean_name = name.strip().title()
    return f"{clean_name} x{quantity}"
```

The useful question is not:

> Does this function contain more than one line?

Ask instead:

> Does this function represent one understandable responsibility at the level this program needs?

Splitting code should improve clarity, reuse, testing, or maintenance. Splitting only to create more function names can make a program harder to follow.

## 9. Separate calculation from presentation when reuse matters

Printing is useful, but a value that is only printed cannot be directly reused by the caller.

Less reusable:

```python
def show_total(values: list[int]) -> None:
    total = sum(values)
    print(f"Total: {total}")
```

More reusable when callers need the number:

```python
def calculate_total(values: list[int]) -> int:
    return sum(values)


def format_total(total: int) -> str:
    return f"Total: {total}"
```

Now one caller can print the formatted result while another caller can use the numeric total in another calculation.

This is a design recommendation, not a rule that printing inside functions is always wrong.

## 10. Make dependencies visible through parameters

If one function needs data from another part of the program, parameters make that dependency visible.

```python
def calculate_bonus(points: int) -> int:
    return points // 10


def build_result(name: str, points: int) -> str:
    bonus = calculate_bonus(points)
    return f"{name}: {points} points + {bonus} bonus"
```

Someone reading `build_result(name, points)` can immediately see the values it requires.

Visible inputs make functions easier to understand in isolation.

## 11. Avoid using global variables as hidden coordination

This works, but the dependency is hidden:

```python
points = 80


def calculate_bonus() -> int:
    return points // 10
```

A clearer interface is:

```python
def calculate_bonus(points: int) -> int:
    return points // 10
```

The second version states its requirement directly.

Global variables can be appropriate for some program-level constants and other deliberate designs. The warning here is specifically about using shared global state as an invisible replacement for ordinary parameters and return values.

## 12. Reuse helpers instead of copying logic

Suppose several reports need the same score classification.

Duplicating the conditions creates several places that can drift apart.

Prefer one reusable helper:

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"
```

Then different coordinating functions can call the same helper.

```text
student report ─┐
                ├─→ classify_score()
team summary ───┘
```

Reuse is most valuable when the extracted function represents a real shared concept, not merely a repeated line of trivial syntax.

## 13. Call order matters when results depend on earlier work

If one function needs another function's result, the required result must exist first.

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


sessions = [30, 45, 60]
total_minutes = calculate_total_minutes(sessions)
workload = classify_workload(total_minutes)
print(total_minutes, workload)
```

Output:

```text
135 deep
```

The classification depends on the total, so the total is calculated first.

## 14. Build simple pipelines one step at a time

A pipeline is a useful mental model when one result becomes the next step's input.

```text
raw value
   ↓
normalize
   ↓
classify
   ↓
format
   ↓
final result
```

For example:

```python
def normalize_code(code: str) -> str:
    return code.strip().upper()


def classify_code(code: str) -> str:
    if code.startswith("A"):
        return "priority"
    return "standard"


def build_code_summary(code: str) -> str:
    clean_code = normalize_code(code)
    category = classify_code(clean_code)
    return f"{clean_code}: {category}"


print(build_code_summary(" a-17 "))
```

Output:

```text
A-17: priority
```

The coordinating function makes the sequence visible without containing the details of every step.

## 15. Conditions can live inside focused helpers

Composition does not replace program flow. It gives program-flow logic a meaningful home.

```python
def is_passing(score: int) -> bool:
    return score >= 70


def build_result(score: int) -> str:
    if is_passing(score):
        return "Pass"
    return "Review"


print(build_result(78))
```

Output:

```text
Pass
```

`is_passing()` answers one Boolean question. `build_result()` decides what result to produce using that answer.

## 16. Loops can call helpers for each item

A loop can delegate item-specific work to a function.

```python
def format_name(name: str) -> str:
    return name.strip().title()


names = [" ava ", "LEO", " mia"]

for name in names:
    print(format_name(name))
```

Output:

```text
Ava
Leo
Mia
```

This often keeps the loop focused on repetition while the helper focuses on transforming one item.

## 17. Coordinators should describe the larger story

A useful coordinating function often reads like a short outline of the task.

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


def build_study_summary(subject: str, sessions: list[int]) -> str:
    total_minutes = calculate_total_minutes(sessions)
    workload = classify_workload(total_minutes)
    return f"{subject}: {total_minutes} minutes ({workload})"
```

Without reading helper internals, you can already describe `build_study_summary()`:

```text
calculate total → classify workload → build summary
```

That is a strong sign that the collaboration is communicating intent well.

## 18. A simple call graph shows who calls whom

A **call graph** is a diagram of calling relationships.

For the previous example:

```text
build_study_summary()
├── calculate_total_minutes()
└── classify_workload()
```

A call graph does not show every variable or every runtime detail. It answers a simpler structural question:

> Which function calls which other function?

The next chapter will go deeper into exactly how data moves through those calls.

## 19. Deep nesting can hide the sequence

This is valid:

```python
result = format_total(calculate_total(values))
```

But a longer chain can become difficult to inspect:

```python
result = finalize(format_total(calculate_total(normalize_values(values))))
```

Intermediate names can expose the stages:

```python
clean_values = normalize_values(values)
total = calculate_total(clean_values)
message = format_total(total)
result = finalize(message)
```

The second form is longer but often easier to debug, explain, and change.

## 20. Common mistake: printing when another function needs the value

Consider:

```python
def calculate_total(values: list[int]) -> None:
    print(sum(values))
```

This prints a number but returns `None`.

So this does not pass the printed number forward:

```python
total = calculate_total([10, 20, 30])
print(total)
```

Output:

```text
60
None
```

When another function needs the result, return the value:

```python
def calculate_total(values: list[int]) -> int:
    return sum(values)
```

Printing and returning solve different problems.

## 21. Common mistake: duplicating the same rule in several functions

Repeated business or classification rules can drift apart.

Instead of copying:

```python
def student_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"


def course_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

Extract the shared concept when the rule is genuinely the same:

```python
def classify_readiness(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

Do not extract merely because two unrelated pieces of code happen to look similar today. Shared functions should represent shared meaning.

## 22. Common mistake: creating functions that are too tiny to clarify anything

This is technically valid:

```python
def add_one(number: int) -> int:
    return number + 1


def add_two(number: int) -> int:
    return add_one(add_one(number))
```

But not every expression needs a separate function.

A helper earns its place when its name or reuse makes the program easier to understand or maintain.

Ask:

1. Does this function name explain a meaningful concept?
2. Is the behavior reused?
3. Does extraction remove distracting detail from a larger function?
4. Can the function be understood and tested independently?

If the answer is no to all four, the split may be unnecessary.

## 23. Common mistake: hiding side effects inside helpers

A **side effect** is an observable action beyond simply returning a value, such as printing or changing an object that exists outside the function.

This helper both transforms and prints:

```python
def normalize_name(name: str) -> str:
    clean_name = name.strip().title()
    print("Normalized")
    return clean_name
```

That may be intentional, but callers now receive extra output whenever they reuse the helper.

For a reusable transformation, a quieter helper may be easier to combine:

```python
def normalize_name(name: str) -> str:
    return name.strip().title()
```

Side effects are not forbidden. The important part is to make them deliberate and unsurprising.

## 24. Executable examples

### Prepare a greeting through a helper

File: [`examples/prepare_greeting.py`](examples/prepare_greeting.py)

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


def build_greeting(name: str) -> str:
    clean_name = normalize_name(name)
    return f"Welcome, {clean_name}!"


print(build_greeting("  ava stone  "))
```

Expected output:

```text
Welcome, Ava Stone!
```

`build_greeting()` delegates normalization and uses the returned text.

### Build a score report with two helpers

File: [`examples/build_score_report.py`](examples/build_score_report.py)

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"


def build_score_report(student: str, score: int) -> str:
    status = classify_score(score)
    return format_score_report(student, score, status)


print(build_score_report("Ava", 84))
```

Expected output:

```text
Ava: 84 points - ready
```

The coordinating function connects classification and formatting without duplicating either responsibility.

### Build a study summary as a small pipeline

File: [`examples/build_study_summary.py`](examples/build_study_summary.py)

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


def build_study_summary(subject: str, sessions: list[int]) -> str:
    total_minutes = calculate_total_minutes(sessions)
    workload = classify_workload(total_minutes)
    return f"{subject}: {total_minutes} minutes ({workload})"


print(build_study_summary("Python", [30, 45, 60]))
```

Expected output:

```text
Python: 135 minutes (deep)
```

The larger function reads like a short outline: calculate, classify, summarize.

## 25. Exercise: compose a reading summary

Create these functions:

```python
def calculate_total_pages(chapters: list[int]) -> int:
    pass


def classify_reading(total_pages: int) -> str:
    pass


def build_reading_summary(book: str, chapters: list[int]) -> str:
    pass
```

Requirements:

1. `calculate_total_pages()` returns the sum of the chapter page counts;
2. `classify_reading()` returns `"long"` for 100 pages or more and `"short"` otherwise;
3. `build_reading_summary()` calls both helpers;
4. the final string uses the form `Book: 120 pages (long)`;
5. test with `"Python Notes"` and `[35, 40, 45]`;
6. keep printing outside the calculation helpers.

Expected output:

```text
Python Notes: 120 pages (long)
```

Try tracing the calls on paper before running the program.

## 26. Review checklist

Before continuing, confirm that you can:

- [ ] call one user-defined function from another;
- [ ] explain where execution returns after a helper finishes;
- [ ] store one function's return value and pass it to another step;
- [ ] explain why intermediate variables can improve traceability;
- [ ] distinguish helper and coordinating roles without treating them as Python keywords;
- [ ] separate calculation from formatting when reuse benefits from it;
- [ ] expose dependencies through parameters rather than hidden globals;
- [ ] reuse one helper from more than one caller;
- [ ] explain why dependent calls must occur in the required order;
- [ ] combine helpers with `if` and loops;
- [ ] draw a simple call graph;
- [ ] recognize when printing prevents a value from being reused;
- [ ] recognize duplicated logic that represents one shared concept;
- [ ] avoid unnecessary fragmentation into tiny functions;
- [ ] identify a surprising side effect inside a helper.

## 27. Quick reference

| Need | Useful pattern |
|---|---|
| reuse one piece of behavior | call a helper function |
| pass a result forward | `result = helper(...)` |
| make a multi-step sequence visible | use intermediate variables |
| coordinate several helpers | use a larger coordinating function |
| reuse a calculation separately from output | return the calculation, format or print later |
| show required data clearly | use parameters |
| avoid hidden coordination | prefer explicit parameters and returns over temporary global state |
| show calling relationships | draw a simple call graph |
| keep repeated rules consistent | extract a genuinely shared helper |
| avoid over-fragmentation | split only when the function adds meaning, reuse, or clarity |

## 28. Scope boundary

This chapter intentionally does not go deeply into:

- aliasing and object identity across several function calls;
- mutation ownership between callers and helpers;
- defensive copying between function boundaries;
- exceptions propagating through call chains;
- recursion;
- functions passed as arguments;
- closures;
- decorators;
- modules and imports as an organization strategy;
- asynchronous functions and concurrency;
- advanced call-stack inspection.

Those topics need separate treatment. The next chapter focuses specifically on tracing **data flow between functions**, including where values come from, where they go, and which function is responsible for changing them.

## 29. What comes next

You can now divide a larger task into cooperating functions and read the basic calling relationships between them.

The next question is more precise:

> When several functions exchange values, how can we trace exactly where the data came from, what changed it, and who owns each change?

That leads to **Chapter 09: Data Flow Between Functions**.

Return to the [Functions learning path](../README.md) or the [full learning path](../../docs/learning-path.en.md).

## References

Primary Python documentation:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Tutorial: More on Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Python 3.13 Language Reference: The `return` statement](https://docs.python.org/3.13/reference/simple_stmts.html#the-return-statement)

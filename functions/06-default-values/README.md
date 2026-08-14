<div align="center">

# Default Values

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous: Type Hints](../05-type-hints/README.md)

Earlier chapters showed how functions receive arguments, return values, resolve names, and describe expected types. This chapter adds one more interface decision:

> Which inputs must every caller provide, and which ones can have a sensible fallback?

```text
required input
    +
defaulted input
        ↓
caller supplies only what needs to differ
```

**Estimated study time:** 75–100 minutes.

**Python version:** The examples target **Python 3.10 or newer**, matching the Type Hints chapter.

## Learning objectives

By the end of this chapter, you should be able to:

- define a default with `name=value`;
- combine type hints and defaults with `name: type = value`;
- distinguish required parameters from defaulted parameters;
- override defaults with positional or keyword arguments;
- explain the ordering rule for ordinary required and defaulted parameters;
- explain when default expressions are evaluated;
- recognize the mutable-default trap;
- use `None` before creating a fresh mutable object;
- choose defaults that clarify rather than hide required input.

## 1. A default lets an argument be omitted

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


print(greet("Avery"))
print(greet("Avery", "Welcome"))
```

Output:

```text
Hello, Avery
Welcome, Avery
```

`name` has no default, so the caller must provide it.

`greeting` has the default `"Hello"`, so its argument may be omitted.

```text
greet("Avery")
       ↓
name = "Avery"
greeting = "Hello"  ← default fills the missing slot
```

## 2. Definition syntax and call syntax have different jobs

The basic definition form is:

```text
def function_name(required, optional=default_value):
    ...
```

Example:

```python
def build_label(topic, prefix="Topic"):
    return f"{prefix}: {topic}"


print(build_label("Functions"))
print(build_label("Functions", prefix="Chapter"))
```

Output:

```text
Topic: Functions
Chapter: Functions
```

Keep the two uses of `=` separate:

```text
definition → prefix="Topic"     establishes a default
call       → prefix="Chapter"   supplies a keyword argument
```

## 3. Required and defaulted parameters express design decisions

```python
def create_message(name, language="English"):
    return f"{name}: {language}"
```

`name` is required because the function should not invent it.

`language` is defaulted because `"English"` is a deliberate fallback.

Ask:

> If the caller says nothing about this option, what behavior is reasonable and unsurprising?

Do not add defaults merely to make every argument optional.

## 4. A supplied argument overrides the default for that call

```python
def format_score(score, suffix=" points"):
    return f"{score}{suffix}"


print(format_score(80))
print(format_score(80, " pts"))
```

Output:

```text
80 points
80 pts
```

Python uses the default only when the corresponding parameter remains unfilled.

Supplying another value for one call does not change the stored default.

## 5. Multiple defaults work well with keyword overrides

```python
def create_badge(name, color="blue", size="medium"):
    return f"{name}: {color}, {size}"


print(create_badge("Python"))
print(create_badge("Python", size="large"))
print(create_badge("Python", color="green"))
```

Output:

```text
Python: blue, medium
Python: blue, large
Python: green, medium
```

Keyword arguments let a caller change one option without repeating the others.

## 6. Required parameters normally come first

This is valid:

```python
def register(name, active=True):
    return f"{name}: {active}"
```

This is not:

```python
# SyntaxError: non-default argument follows default argument
def register(active=True, name):
    return f"{name}: {active}"
```

For ordinary parameters, use this beginner rule:

```text
required parameters first
defaulted parameters after them
```

Special parameter categories refine the rule later.

## 7. Type hints and defaults can appear together

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(greet("Avery"))
```

Read the signature as:

```text
name: str
├── expected type: str
└── no default → argument required

greeting: str = "Hello"
├── expected type: str
└── default: "Hello" → argument may be omitted

-> str
└── expected return type
```

Type hints describe expected types. Defaults describe omitted-argument behavior.

Neither concept replaces runtime validation.

## 8. Keep four concepts separate

```text
default    → fallback when an argument is omitted
type hint  → expected type information
validation → checks actual values or rules
conversion → explicitly transforms compatible data
```

For example:

```python
def repeat_text(text: str, times: int = 2) -> str:
    return text * times
```

`times=2` is a fallback. It does not validate every later value.

## 9. A default is part of public behavior

```python
def create_heading(title: str, level: int = 2) -> str:
    return f"h{level}: {title}"
```

The interface communicates:

> If the caller does not choose a level, use 2.

Changing the default later changes every call that omits `level`.

Defaults are small interface decisions, not merely shorter syntax.

## 10. Do not hide truly required input

This design can hide missing information:

```python
def create_student(name="", course=""):
    ...
```

If both pieces are necessary, require them:

```python
def create_student(name: str, course: str, active: bool = True):
    ...
```

Now only `active` has a deliberate fallback.

A shorter call is not automatically a clearer interface.

## 11. Default expressions are evaluated when the function is defined

```python
level = "beginner"


def describe(topic, course_level=level):
    return f"{topic}: {course_level}"


level = "advanced"

print(describe("Functions"))
print(describe("Functions", level))
```

Output:

```text
Functions: beginner
Functions: advanced
```

When the `def` statement ran, `level` was `"beginner"`.

That value became the stored default for `course_level`.

Changing the external variable later does not recalculate the default.

## 12. Defaults are evaluated once, not once per call

Use this mental model:

```text
execute def statement
    ↓
evaluate default expressions
    ↓
store their resulting values
    ↓
future calls reuse stored defaults when needed
```

This matters most when the stored object can change.

## 13. Immutable defaults are usually straightforward

Strings, numbers, booleans, and `None` are common defaults:

```python
def describe_course(
    name: str,
    level: str = "beginner",
    lessons: int = 10,
    published: bool = False,
) -> str:
    return f"{name} | {level} | {lessons} | {published}"
```

These values are immutable, so they do not create the shared-mutation problem shown next.

You should still ask whether each fallback is sensible.

## 14. Mutable defaults can retain changes between calls

```python
def add_topic(topic, topics=[]):
    topics.append(topic)
    return topics


print(add_topic("functions"))
print(add_topic("defaults"))
```

Output:

```text
['functions']
['functions', 'defaults']
```

The same list is reused because it was created when the function definition executed.

This is the **mutable default argument trap**.

## 15. The problem is reuse of the default object

Lists are fine inside function bodies:

```python
def create_topics():
    topics = []
    topics.append("functions")
    return topics
```

A new list is created each time the body runs.

The risky form is specifically:

```python
def add_topic(topic, topics=[]):
    ...
```

because that list belongs to the stored defaults and can survive across calls.

## 16. Use `None` when omission should create a fresh object

```python
def add_topic(topic: str, topics: list[str] | None = None) -> list[str]:
    if topics is None:
        topics = []

    topics.append(topic)
    return topics


print(add_topic("functions"))
print(add_topic("defaults"))
```

Output:

```text
['functions']
['defaults']
```

Each omitted `topics` argument first produces `None`, then the body creates a fresh list.

## 17. `None` acts as a sentinel in this pattern

Here, `None` means:

> No list was supplied, so create one now.

```text
topics supplied?
├── yes → use that object
└── no  → default gives None
            ↓
        create a fresh list
```

This works when `None` is not itself meaningful application data for that parameter.

Custom sentinels are an advanced interface topic and are outside this chapter.

## 18. A supplied mutable object can still be changed

```python
def add_topic(topic: str, topics: list[str] | None = None) -> list[str]:
    if topics is None:
        topics = []

    topics.append(topic)
    return topics


planned = ["scope"]
result = add_topic("defaults", planned)

print(planned)
print(result)
```

Output:

```text
['scope', 'defaults']
['scope', 'defaults']
```

The safe default pattern does not copy an object explicitly supplied by the caller.

Shared default state and deliberate mutation of caller-owned data are separate questions.

## 19. Positional and keyword arguments can override defaults

```python
def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(5, 3))
print(power(5, exponent=3))
```

Output:

```text
25
125
125
```

For optional settings, a keyword often makes the caller's intention clearer.

## 20. Keywords let you skip earlier defaults

```python
def export_summary(name, format="text", include_title=True):
    return f"{name}: {format}, title={include_title}"


print(export_summary("study", include_title=False))
```

Output:

```text
study: text, title=False
```

There is no blank positional placeholder for “keep this default but change the next one”.

Keyword arguments provide selective overrides.

## 21. `None` is not automatically the best default

A default can be any suitable value:

```python
def format_name(name, separator=", "):
    ...
```

Use `None` when it accurately represents the omitted-argument case you need, especially when creating a fresh mutable object.

Do not replace every default with `None` mechanically.

## 22. Common mistakes

### Mutable default object

Avoid:

```python
def collect_item(item, items=[]):
    items.append(item)
    return items
```

Prefer:

```python
def collect_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items
```

### Required parameter after a default

Avoid:

```python
# SyntaxError
def connect(timeout=30, host):
    return host, timeout
```

Prefer:

```python
def connect(host, timeout=30):
    return host, timeout
```

### Misleading fallback

If `topic` is truly required, do not hide that decision:

```python
def study(topic):
    return topic
```

## 23. Trace a complete call

```python
def create_title(topic: str, prefix: str = "Chapter", number: int = 1) -> str:
    return f"{prefix} {number}: {topic}"


title = create_title("Defaults", number=6)
print(title)
```

Trace:

```text
1. call create_title("Defaults", number=6)
2. topic = "Defaults"
3. number = 6
4. prefix is unfilled
5. prefix receives stored default "Chapter"
6. body returns "Chapter 6: Defaults"
7. title receives that returned string
```

Every parameter has a value before the body runs, either from a supplied argument or a default.

## 24. Executable example: greeting options

```python
def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"


print(greet("Avery"))
print(greet("Avery", greeting="Welcome"))
print(greet("Avery", punctuation="."))
```

Output:

```text
Hello, Avery!
Welcome, Avery!
Hello, Avery.
```

## 25. Executable example: shipping quote

```python
def calculate_shipping(weight: float, rate: float = 2.5, handling: float = 3.0) -> float:
    return weight * rate + handling


print(calculate_shipping(4.0))
print(calculate_shipping(4.0, rate=3.0))
print(calculate_shipping(4.0, handling=0.0))
```

Output:

```text
13.0
15.0
10.0
```

## 26. Executable example: safe list default

```python
def add_task(task: str, tasks: list[str] | None = None) -> list[str]:
    if tasks is None:
        tasks = []

    tasks.append(task)
    return tasks


print(add_task("study"))
print(add_task("practice"))
print(add_task("review", ["plan"]))
```

Output:

```text
['study']
['practice']
['plan', 'review']
```

The first two calls create independent lists. The third deliberately modifies the supplied list.

## 27. Connection to earlier chapters

```text
definition and call
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
required vs optional caller input
```

Defaults do not replace arguments. They define how a parameter receives a value when its argument is omitted.

## 28. Design checklist

Before adding a default, ask:

- Is this input truly optional?
- Is the fallback unsurprising?
- Would changing it later alter important behavior?
- Is the default mutable?
- If it is mutable, should `None` trigger a fresh object?
- Is `None` itself meaningful data here?
- Would a keyword override make the call clearer?
- Does the type hint include `None` when `None` is supported?

## 29. Scope boundary

This chapter focuses on ordinary defaults for regular function parameters.

It does not require:

- positional-only parameters with `/`;
- keyword-only design with `*`;
- `*args` and `**kwargs`;
- custom sentinel objects;
- decorators;
- advanced typing constructs;
- dataclasses or class constructors.

The next chapter introduces `*args` and `**kwargs`.

## 30. Exercise

Create `build_reminder`.

Requirements:

- `task` is required;
- `priority` defaults to `"normal"`;
- `done` defaults to `False`;
- use type hints;
- return one formatted string;
- call it once using both defaults;
- call it again overriding only `priority` by keyword.

```python
print(build_reminder("Study Python"))
print(build_reminder("Review functions", priority="high"))
```

### Extra challenge

Create another function with an optional list:

- do not use `[]` directly as the default;
- use `None`;
- create a fresh list inside the body;
- demonstrate that two calls without a list do not share state.

## 31. Review questions

1. What does `language="English"` mean in a definition?
2. When does Python use a default?
3. What happens when the caller supplies that argument?
4. Why do ordinary required parameters normally appear first?
5. When are default expressions evaluated?
6. Why can `items=[]` share state across calls?
7. How does the `None` pattern avoid that problem?
8. Does a default validate an argument?
9. How are type hints and defaults different?
10. Why should a default represent genuinely optional behavior?

## Quick reference

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
```

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"
```

```python
greet("Avery", greeting="Welcome")
```

```python
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items
```

```text
default
→ used when the corresponding argument is omitted

default expression
→ evaluated when the function definition executes

mutable default object
→ can be shared between calls

None sentinel pattern
→ create a fresh mutable object inside the body
```

## Executable examples

```bash
python functions/06-default-values/examples/greet_with_style.py
python functions/06-default-values/examples/shipping_quote.py
python functions/06-default-values/examples/safe_list_default.py
```

## References

- [Python 3.13 Tutorial — Default Argument Values](https://docs.python.org/3.13/tutorial/controlflow.html#default-argument-values)
- [Python 3.13 Language Reference — Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13 Language Reference — Calls](https://docs.python.org/3.13/reference/expressions.html#calls)

---

Next: **07. `*args` and `**kwargs`**.

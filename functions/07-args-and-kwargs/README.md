<div align="center">

# `*args` and `**kwargs`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous: Default Values](../06-default-values/README.md)

Earlier chapters gave functions required parameters, return values, scope, type hints, and safe defaults. This chapter adds a new design option: a function can collect a **variable number of arguments** when the exact count is intentionally flexible.

```text
extra positional arguments → *args   → tuple
extra keyword arguments    → **kwargs → dictionary
```

**Estimated study time:** 75–100 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain what `*args` collects;
- explain what `**kwargs` collects;
- identify the tuple stored by `*args`;
- identify the dictionary stored by `**kwargs`;
- use zero, one, or many collected arguments;
- combine required parameters with `*args` or `**kwargs`;
- use `*args` and `**kwargs` together in a simple signature;
- add type hints to collected argument values;
- distinguish collection in a function definition from unpacking at a call site;
- recognize when an explicit parameter list is clearer than flexible collection.

## 1. Why variable-length arguments exist

Sometimes a function naturally accepts a quantity of values that is not fixed in advance.

A function that totals scores might receive two values in one call and five in another:

```python
def total_scores(*scores):
    return sum(scores)


print(total_scores(10, 20))
print(total_scores(10, 20, 30, 40, 50))
```

Output:

```text
30
150
```

Without a variable-length parameter, you would need to decide on a fixed number of score parameters or require callers to build a collection first.

Use flexible collection when the flexibility belongs to the function's design, not merely to avoid deciding what the function should accept.

## 2. `*args` collects extra positional arguments

The syntax is one `*` before a parameter name:

```python
def show_values(*values):
    print(values)


show_values(4, 7, 9)
```

Output:

```text
(4, 7, 9)
```

Inside the function, `values` is a tuple containing the positional arguments collected by that parameter.

```text
call:       show_values(4, 7, 9)
                         ↓  ↓  ↓
*values collects:      (4, 7, 9)
```

## 3. `args` is a convention, not a special name

You often see this:

```python
def show_values(*args):
    print(args)
```

But the special part is the `*`, not the word `args`.

This is equally valid and often more descriptive:

```python
def show_scores(*scores):
    print(scores)
```

Prefer a meaningful name when the collected values have a clear role.

## 4. `*args` can collect zero arguments

A variable-length positional parameter does not require at least one value:

```python
def show_items(*items):
    print(items)


show_items()
show_items("pen")
show_items("pen", "book")
```

Output:

```text
()
('pen',)
('pen', 'book')
```

The empty call produces an empty tuple.

## 5. Iterate over the collected tuple

Because the collected value is a tuple, ordinary `for` iteration works naturally:

```python
def print_names(*names):
    for name in names:
        print(name)


print_names("Ava", "Leo", "Mia")
```

Output:

```text
Ava
Leo
Mia
```

Everything learned earlier about tuple iteration still applies.

## 6. Required parameters can come before `*args`

A function can require a value before collecting additional positional arguments. The ordinary parameter before `*args` is still positional-or-keyword unless the signature uses separate positional-only syntax:

```python
def announce(prefix, *messages):
    for message in messages:
        print(prefix, message)


announce("INFO:", "Ready", "Running")
```

Output:

```text
INFO: Ready
INFO: Running
```

In the call above, `"INFO:"` binds to `prefix` by position. The remaining positional arguments bind to `messages`:

```text
"INFO:"             → prefix
"Ready", "Running" → messages → ("Ready", "Running")
```

`prefix` is required because it has no default value, but **required** does not mean **positional-only**. If no extra messages are needed, the same parameter can bind by keyword:

```python
announce(prefix="INFO:")
```

Here `messages` becomes an empty tuple. With this signature, extra messages are positional, so when you want to provide them, the simplest call is the positional form shown above.

## 7. `**kwargs` collects extra keyword arguments

The syntax is two `*` characters before a parameter name:

```python
def show_details(**details):
    print(details)


show_details(color="blue", size="medium")
```

Output:

```text
{'color': 'blue', 'size': 'medium'}
```

Inside the function, `details` is a dictionary.

```text
color="blue"   → key "color", value "blue"
size="medium"  → key "size", value "medium"
```

## 8. `kwargs` is also only a convention

This is common:

```python
def show_details(**kwargs):
    print(kwargs)
```

But this is just as valid:

```python
def show_settings(**settings):
    print(settings)
```

Again, the `**` controls collection. The parameter name is your choice.

## 9. `**kwargs` can collect zero keyword arguments

```python
def show_options(**options):
    print(options)


show_options()
show_options(theme="dark")
```

Output:

```text
{}
{'theme': 'dark'}
```

No collected keyword arguments means an empty dictionary.

## 10. Iterate over keyword names and values

Iterating over a dictionary directly produces keys. Use `.items()` when you need both keys and values:

```python
def print_settings(**settings):
    for name, value in settings.items():
        print(name, value)


print_settings(language="Python", level="beginner")
```

Output:

```text
language Python
level beginner
```

This is ordinary dictionary behavior, not a special `**kwargs` rule.

## 11. Required parameters can come before `**kwargs`

A function can require a named piece of data and collect additional keyword information:

```python
def build_profile(name, **details):
    print("Name:", name)

    for key, value in details.items():
        print(key, value)


build_profile("Ava", role="student", active=True)
```

Output:

```text
Name: Ava
role student
active True
```

The required argument binds to `name`. The remaining keyword arguments are collected in `details`.

## 12. Use `*args` and `**kwargs` together

A simple signature can collect both forms:

```python
def describe_group(name, *members, **details):
    print("Group:", name)
    print("Members:", members)
    print("Details:", details)


describe_group("Study", "Ava", "Leo", topic="Python", active=True)
```

Output:

```text
Group: Study
Members: ('Ava', 'Leo')
Details: {'topic': 'Python', 'active': True}
```

The mental model is:

```text
required positional-or-keyword input → ordinary parameter
extra positional input               → *members → tuple
extra keyword input                  → **details → dictionary
```

An ordinary parameter such as `name` is required here, but it can bind from either a positional argument or a keyword argument. Both calls below are valid, and neither adds a value to `*members`:

```python
describe_group("Study", topic="Python")
describe_group(name="Study", topic="Python")
```

In the second call, `name="Study"` binds directly to the ordinary `name` parameter. Only `topic="Python"` remains available to be collected by `**details`.

## 13. Order matters in the function signature

For the beginner pattern in this chapter, think:

```python
def function(required, *args, **kwargs):
    pass
```

The required parameter binds first, `*args` collects remaining positional arguments, and `**kwargs` collects remaining keyword arguments.

Python supports additional parameter-ordering features, including keyword-only and positional-only parameters. Those deserve separate treatment and are intentionally outside this chapter's main scope.

## 14. Type hints describe each collected value

When you annotate `*args`, the annotation describes each positional value being collected:

```python
def total_scores(*scores: int) -> int:
    return sum(scores)
```

Conceptually, inside the function:

```text
scores → tuple of int values
```

For `**kwargs`, the annotation describes each collected dictionary value:

```python
def show_labels(**labels: str) -> None:
    for name, value in labels.items():
        print(name, value)
```

Conceptually:

```text
labels → dictionary with string keys and str values
```

As learned in Chapter 05, type hints describe intended interfaces but do not automatically enforce types at runtime.

## 15. `*args` is a tuple, not a list

A common mistake is to expect list methods:

```python
def collect(*items):
    print(type(items))


collect("a", "b")
```

Output:

```text
<class 'tuple'>
```

If the function truly needs a mutable list, create one deliberately:

```python
def collect(*items):
    result = list(items)
    result.append("done")
    return result
```

Do not mentally treat the tuple as a list just because both are ordered collections.

## 16. `**kwargs` is an ordinary dictionary inside the function

You can use familiar dictionary operations:

```python
def get_mode(**options):
    return options.get("mode", "standard")


print(get_mode())
print(get_mode(mode="compact"))
```

Output:

```text
standard
compact
```

The dictionary exists for the current function call just like other local objects created during that call.

## 17. Do not use flexibility when explicit parameters are clearer

This signature hides the expected interface:

```python
def create_user(**data):
    pass
```

If the function really requires exactly a name and email, this is clearer:

```python
def create_user(name, email):
    pass
```

Explicit parameters improve readability, editor assistance, documentation, and error messages when the accepted inputs are known.

Use `*args` and `**kwargs` because the number or names of arguments are intentionally variable, not because they make the signature shorter.

## 18. Collection in definitions is not call-site unpacking

This chapter uses stars in function definitions:

```python
def show_values(*values):
    print(values)


def show_details(**details):
    print(details)
```

Here the stars **collect** arguments.

Python can also use `*` and `**` in function calls to unpack an existing iterable or mapping. That is a different direction of data flow and is intentionally deferred so the two ideas do not blur together.

```text
definition side → collect
call side       → unpack (later topic)
```

## 19. Common mistake: expecting keyword arguments in `*args`

```python
def inspect(*values):
    print(values)


inspect(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

`*values` collects positional arguments. If you need flexible keyword arguments, use a `**` parameter.

## 20. Common mistake: iterating over `**kwargs` as if it produced pairs

```python
def show(**details):
    for item in details:
        print(item)


show(color="blue", size="medium")
```

Output:

```text
color
size
```

Direct dictionary iteration yields keys. Use `details.items()` for key-value pairs.

## 21. Common mistake: accepting everything without a reason

A signature such as:

```python
def process(*args, **kwargs):
    pass
```

is maximally flexible but minimally informative.

Before using it, ask:

1. Are the positional values genuinely variable in count?
2. Are the keyword names genuinely open-ended?
3. Can a more explicit signature communicate the contract better?
4. Will the function validate or clearly use the collected data?

Flexibility is useful when it models the problem. Unnecessary flexibility makes APIs harder to understand.

## 22. Executable examples

### Calculate an average with `*args`

File: [`examples/calculate_average.py`](examples/calculate_average.py)

```python
def calculate_average(first_score: float, *scores: float) -> float:
    return (first_score + sum(scores)) / (1 + len(scores))


print(calculate_average(8.0, 9.0, 10.0))
```

Expected output:

```text
9.0
```

An average requires at least one value, so `first_score` is required while `*scores` collects any additional scores.

### Display settings with `**kwargs`

File: [`examples/display_settings.py`](examples/display_settings.py)

```python
def display_settings(**settings: str) -> None:
    for name, value in settings.items():
        print(f"{name}: {value}")


display_settings(theme="dark", language="English")
```

Expected output:

```text
theme: dark
language: English
```

### Combine required, positional, and keyword input

File: [`examples/describe_session.py`](examples/describe_session.py)

```python
def describe_session(title: str, *topics: str, **details: str) -> None:
    print(f"Title: {title}")
    print(f"Topics: {', '.join(topics)}")

    for name, value in details.items():
        print(f"{name}: {value}")


describe_session(
    "Python Study",
    "functions",
    "arguments",
    level="beginner",
    format="guided",
)
```

Expected output:

```text
Title: Python Study
Topics: functions, arguments
level: beginner
format: guided
```

## 23. Exercise: flexible order summary

Create `summarize_order(order_id, *items, **details)`.

Requirements:

1. print the order ID;
2. print each item on its own line;
3. print each detail as `name: value`;
4. call the function with order ID `A-104`;
5. pass `"notebook"` and `"pen"` as positional items;
6. pass `priority="normal"` and `channel="online"` as keyword details.

Expected output:

```text
Order: A-104
notebook
pen
priority: normal
channel: online
```

Keep the exercise focused on collection. Do not unpack an existing list or dictionary at the call site.

## 24. Review checklist

Before continuing, confirm that you can:

- [ ] explain that one `*` collects extra positional arguments;
- [ ] explain that two `*` characters collect extra keyword arguments;
- [ ] identify the tuple created for a `*args`-style parameter;
- [ ] identify the dictionary created for a `**kwargs`-style parameter;
- [ ] handle zero collected arguments;
- [ ] iterate through collected positional values;
- [ ] iterate through keyword key-value pairs with `.items()`;
- [ ] combine a required parameter with `*args` or `**kwargs`;
- [ ] use both forms in one simple signature;
- [ ] add basic type hints to collected values;
- [ ] explain why `args` and `kwargs` are conventions rather than magic names;
- [ ] distinguish definition-side collection from call-side unpacking;
- [ ] choose explicit parameters when the interface is fixed.

## 25. Quick reference

| Need | Form | Inside the function |
|---|---|---|
| collect extra positional arguments | `def f(*values):` | `values` is a tuple |
| collect extra keyword arguments | `def f(**options):` | `options` is a dictionary |
| require one value, collect more positional | `def f(first, *rest):` | `first` is ordinary; `rest` is a tuple |
| require one value, collect keyword details | `def f(name, **details):` | `name` is ordinary; `details` is a dictionary |
| collect both forms | `def f(name, *items, **details):` | tuple plus dictionary |
| annotate positional values | `def f(*values: int):` | each collected value is intended as `int` |
| annotate keyword values | `def f(**values: str):` | each collected value is intended as `str` |

## 26. Scope boundary

This chapter intentionally defers:

- unpacking iterables with `*` at the call site;
- unpacking mappings with `**` at the call site;
- positional-only syntax with `/`;
- detailed keyword-only parameter design;
- forwarding arbitrary arguments through wrapper functions;
- decorators;
- advanced typing for flexible call signatures;
- introspection of function signatures.

The goal here is a stable mental model of **collection** before adding the reverse operation of unpacking.

## 27. What comes next

You can now design functions with fixed inputs, optional defaults, and intentionally variable argument counts.

The next question is broader:

> How should multiple functions divide work and call one another without becoming tangled?

That leads to **Chapter 08: Functions Working Together**.

Return to the [Functions learning path](../README.md) or the [full learning path](../../docs/learning-path.en.md).

## References

Primary Python documentation:

- [Python 3.13 Tutorial: Arbitrary Argument Lists](https://docs.python.org/3.13/tutorial/controlflow.html#arbitrary-argument-lists)
- [Python 3.13 Tutorial: Keyword Arguments](https://docs.python.org/3.13/tutorial/controlflow.html#keyword-arguments)
- [Python 3.13 Language Reference: Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)

<div align="center">

# `type()` and `isinstance()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: Built-in data types](../04-built-in-data-types/README.md)

Chapter 04 taught you to recognize common value types from their source notation. This chapter adds direct inspection. Python provides `type()` to reveal a value's exact type and `isinstance()` to ask whether a value belongs to a type or compatible type family.

The distinction matters. Exact type identity and type compatibility answer different questions, especially when inheritance is involved.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Chapters 01 to 04 |
| Estimated study time | 55 to 75 minutes |
| Main concepts | `type()`, `isinstance()`, exact type, compatible type, type object, tuple of types |

## Learning objectives

By the end of this chapter, you should be able to:

- inspect a value with `type()`;
- read common `type()` results;
- explain that `type()` returns a type object rather than text;
- check a value with `isinstance()`;
- pass one type or a tuple of types to `isinstance()`;
- explain the difference between exact type inspection and compatibility checks;
- understand why `isinstance(True, int)` is `True`;
- avoid comparing `type()` results with strings;
- choose between `type()` and `isinstance()` for simple beginner tasks.

## 1. Recognizing a type is not always enough

You can often predict a value's type by reading the source code:

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

But programs do not always receive values as obvious literals. Values can come from function calls, files, libraries, calculations, or user input.

Direct inspection answers questions that visual guessing cannot always answer safely.

## 2. `type()` reveals the exact type

Call `type()` with one value:

```python
course_name = "Python Study Guide"

print(type(course_name))
```

Expected output:

```text
<class 'str'>
```

The result tells you that `course_name` currently refers to an instance of `str`.

## 3. Inspect the common types from Chapter 04

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None

print(type(course_name))
print(type(chapter_number))
print(type(estimated_minutes))
print(type(is_available))
print(type(next_chapter))
```

Expected output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
```

The angle-bracket representation is Python showing type objects in a readable form.

## 4. `type()` returns an object, not a label string

This is an important distinction:

```python
chapter_number = 5
chapter_type = type(chapter_number)

print(chapter_type)
```

`chapter_type` refers to the type object `int`. It does not contain the text `"int"`.

That means this idea is incorrect:

```text
type(chapter_number) == "int"
```

The left side is a type object. The right side is a string.

## 5. Type names such as `str` and `int` are objects too

Names such as `str`, `int`, `float`, and `bool` refer to built-in type objects.

You can therefore compare an exact `type()` result with a type object:

```python
chapter_number = 5

print(type(chapter_number) is int)
print(type(chapter_number) is str)
```

Expected output:

```text
True
False
```

Here, `is` asks whether the two references point to the same object. Detailed identity comparisons belong to a later program-flow topic; for now, read this pattern as an exact-type check.

## 6. Exact type checks are deliberately strict

```python
is_available = True

print(type(is_available) is bool)
print(type(is_available) is int)
```

Expected output:

```text
True
False
```

`type()` reports the exact runtime type of the value. For `True`, that exact type is `bool`.

This strictness is sometimes useful, but it is not always the best way to ask whether a value is acceptable for a broader category.

## 7. `isinstance()` asks a compatibility question

`isinstance()` receives a value and a type:

```python
chapter_number = 5

print(isinstance(chapter_number, int))
print(isinstance(chapter_number, str))
```

Expected output:

```text
True
False
```

Read the first call as:

> Is `chapter_number` an instance of `int`, or of a type derived from `int`?

That last part is the main difference from an exact `type()` check.

## 8. `isinstance()` returns a boolean

The result of `isinstance()` is always `True` or `False`:

```python
course_name = "Python Study Guide"
is_text = isinstance(course_name, str)

print(is_text)
```

Expected output:

```text
True
```

You can store the result in a clearly named boolean variable and reuse it later.

## 9. Check against more than one accepted type

The second argument to `isinstance()` can be a tuple of types:

```python
whole_number = 5
decimal_number = 5.0
text_number = "5"

print(isinstance(whole_number, (int, float)))
print(isinstance(decimal_number, (int, float)))
print(isinstance(text_number, (int, float)))
```

Expected output:

```text
True
True
False
```

This asks whether the value is compatible with any type in the tuple.

## 10. Do not write `int or float` as the type argument

This is not the same check:

```text
isinstance(value, int or float)
```

The expression `int or float` is evaluated before `isinstance()` receives it, so it does not mean “either `int` or `float`” in this context.

Use a tuple:

```python
value = 5.0

print(isinstance(value, (int, float)))
```

## 11. The `bool` and `int` relationship

Python defines `bool` as a subclass of `int`. That creates a result that surprises many beginners:

```python
is_available = True

print(type(is_available) is bool)
print(type(is_available) is int)
print(isinstance(is_available, bool))
print(isinstance(is_available, int))
```

Expected output:

```text
True
False
True
True
```

The exact type is `bool`, but a boolean is also considered an instance of `int` for inheritance-based checks.

## 12. Why the `bool` detail matters

Suppose a program accepts whole-number quantities:

```python
quantity = True

print(isinstance(quantity, int))
```

This prints `True`, even though `True` may be a poor semantic choice for a quantity.

Type compatibility does not replace domain meaning. A program still needs to decide whether a value makes sense for its purpose.

## 13. `type()` versus `isinstance()`

A useful beginner rule is:

| Question | Prefer |
|---|---|
| What exact type is this value? | `type(value)` |
| Is this value compatible with this type? | `isinstance(value, SomeType)` |
| Is it compatible with any of several types? | `isinstance(value, (TypeA, TypeB))` |
| Do I need to account for subclasses? | Usually `isinstance()` |

Use exact checks when exactness is truly the requirement. Use `isinstance()` when compatible subclasses should count.

## 14. `input()` makes a useful inspection example

Chapter 04 stated that `input()` returns text. You can now verify that directly:

```python
response = input("Practice minutes: ")

print(type(response))
```

If the user types `45`, the final line still displays:

```text
<class 'str'>
```

The characters may look numeric, but the returned value is a string.

## 15. `None` can also be inspected

```python
review_note = None

print(type(review_note))
print(isinstance(review_note, type(None)))
```

Expected output:

```text
<class 'NoneType'>
True
```

In everyday Python, absence is normally checked with `is None` rather than by inspecting `NoneType`. This example exists to connect `None` with the type system, not to recommend a verbose absence check.

## 16. Type inspection is a diagnostic tool

`type()` is especially useful while learning, debugging, exploring unfamiliar values, and checking assumptions.

For example:

```python
value = "42"

print("Value:", value)
print("Type:", type(value))
```

The visible output and the type inspection together provide more information than either one alone.

## 17. Avoid scattering type checks everywhere

A program does not become safer merely by adding `type()` or `isinstance()` around every value.

Excessive checking can:

- duplicate assumptions already guaranteed elsewhere;
- make simple code noisy;
- hide a design problem;
- reject useful compatible objects when exact checks are too strict.

Use inspection when the question about type is relevant to the program.

## 18. Prefer behavior when behavior is the real requirement

Sometimes a program does not need to know an exact type. It only needs an object that supports a required operation.

This broader design idea is often associated with Python's “duck typing” style. It becomes more useful later, when you know functions, exceptions, protocols, and custom classes.

For now, remember: a type check should answer a real requirement, not merely satisfy curiosity inside production logic.

## 19. Repository examples

| File | Purpose | Automatic execution |
|---|---|---|
| [`inspect_types.py`](examples/inspect_types.py) | Displays the exact types of the Chapter 04 value set | Yes |
| [`check_type_families.py`](examples/check_type_families.py) | Compares exact checks, `isinstance()`, tuples of types, and the `bool`/`int` relationship | Yes |

Both examples are deterministic, non-interactive, and suitable for unattended checks.

## 20. Practical example: inspect a small value catalog

Create `inspect_types.py`:

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None

print("course_name:", type(course_name))
print("chapter_number:", type(chapter_number))
print("estimated_minutes:", type(estimated_minutes))
print("is_available:", type(is_available))
print("next_chapter:", type(next_chapter))
```

Expected output:

```text
course_name: <class 'str'>
chapter_number: <class 'int'>
estimated_minutes: <class 'float'>
is_available: <class 'bool'>
next_chapter: <class 'NoneType'>
```

## 21. Practical example: exact type and compatible type

Create `check_type_families.py`:

```python
whole_number = 5
decimal_number = 5.0
is_available = True

print("Exact int:", type(whole_number) is int)
print("Number family:", isinstance(whole_number, (int, float)))
print("Float in number family:", isinstance(decimal_number, (int, float)))
print("Exact bool:", type(is_available) is bool)
print("Bool is int-compatible:", isinstance(is_available, int))
```

Expected output:

```text
Exact int: True
Number family: True
Float in number family: True
Exact bool: True
Bool is int-compatible: True
```

## 22. Exercise

Create `value_inspector.py` with these exact names:

```python
guide_name
chapter_number
completion_rate
is_published
review_note
```

Assign one value of each type introduced in Chapter 04.

Then:

1. print each value;
2. print the result of `type()` for each value;
3. use `isinstance()` to confirm that `guide_name` is a `str`;
4. use `isinstance()` to confirm that `chapter_number` belongs to `(int, float)`;
5. test whether `completion_rate` belongs to `(int, float)`;
6. inspect `is_published` with both `type()` and `isinstance(..., int)`;
7. explain why the final boolean-related results are not contradictory.

## 23. Common mistakes

### Comparing a type object with text

```text
type(value) == "str"
```

Use the type object `str`, not the string `"str"`.

### Passing a string to `isinstance()`

```text
isinstance(value, "str")
```

The type argument must be a type object or an accepted tuple of type objects.

### Using `int or float`

```text
isinstance(value, int or float)
```

Use:

```python
isinstance(value, (int, float))
```

### Assuming `isinstance(True, int)` is false

It is `True` because `bool` is a subclass of `int`.

### Using exact checks when subclasses should count

```python
type(value) is int
```

This rejects values whose type derives from `int`. Use `isinstance(value, int)` when compatible subclasses should count.

### Using type checks instead of understanding the data

Knowing that a value is an `int` does not tell you whether it is a valid age, quantity, percentage, or identifier. Type and meaning are related but different concerns.

## 24. Self-check

You are ready for the next chapter when you can answer:

- What does `type()` return?
- Why is `<class 'str'>` not the same thing as the text `"str"`?
- What question does `isinstance()` answer?
- How do you check against either `int` or `float`?
- Why is `isinstance(True, int)` true?
- What is the exact type of `True`?
- When is an exact `type()` check stricter than `isinstance()`?
- Why should type checks not be added everywhere automatically?
- What type does `input()` return?
- What problem will type conversion solve in the next chapter?

## 25. Quick-reference summary

| Goal | Example |
|---|---|
| Inspect exact type | `type(value)` |
| Exact built-in type check | `type(value) is int` |
| Compatible type check | `isinstance(value, int)` |
| Accept several types | `isinstance(value, (int, float))` |
| Inspect input result | `type(response)` |
| Exact boolean type | `type(flag) is bool` |
| Boolean compatible with `int` | `isinstance(flag, int)` |
| Avoid string comparison | Use `str`, not `"str"` |

## 26. Run the repository examples

From the repository root:

```bash
python fundamentals/05-type-and-isinstance/examples/inspect_types.py
python fundamentals/05-type-and-isinstance/examples/check_type_families.py
```

## 27. Run the repository checks

From the repository root:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

Both examples in this chapter are approved for unattended execution.

## Official references

- [Python built-in function — `type()`](https://docs.python.org/3/library/functions.html#type)
- [Python built-in function — `isinstance()`](https://docs.python.org/3/library/functions.html#isinstance)
- [Python built-in types — Boolean values](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)
- [Python data model — Objects, values, and types](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)

[← Back to the section index](../README.md) · [← Previous chapter: Built-in data types](../04-built-in-data-types/README.md)

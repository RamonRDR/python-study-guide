<div align="center">

# Built-in Data Types

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: Variables and naming](../03-variables-and-naming/README.md)

Variables give values useful names. The next question is what kind of value each name refers to. Python values have types, and a type helps determine how a value is represented, which operations make sense, and how the program can use it.

This chapter introduces a focused first group of built-in types: `str`, `int`, `float`, `bool`, and `NoneType`. It does not try to catalog every Python type, and it leaves formal inspection with `type()` and `isinstance()` to the next chapter.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Chapters 01 through 03 |
| Estimated study time | 55 to 75 minutes |
| Main concepts | Value, type, built-in type, literal, `str`, `int`, `float`, `bool`, `None` |

## Learning objectives

By the end of this chapter, you should be able to:

- explain that every Python value has a type;
- recognize common source forms that create text, integers, floating-point numbers, Boolean values, and `None`;
- distinguish `"42"`, `42`, and `42.0`;
- explain why quotation marks change the kind of value being created;
- write `True`, `False`, and `None` with the required capitalization;
- use `None` to represent an intentionally absent value;
- predict simple behavior that changes according to the value type;
- remember that `input()` returns text;
- recognize that this chapter covers only a first subset of Python's built-in types.

## 1. Values have types

A **value** is a piece of data used by a program. A **type** classifies that value and defines important parts of its behavior.

```text
source notation ──creates──▶ value ──has──▶ type
```

Consider these assignments:

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

The names are different, but the decisive distinction is also in the values:

- `"Python Study Guide"` is text;
- `4` is a whole number;
- `60.0` is a floating-point number;
- `True` is a Boolean value;
- `None` marks the absence of a value.

## 2. What “built-in” means

A built-in type is available as part of Python itself. You do not need to install a package or write an `import` statement to create ordinary strings, integers, floats, Boolean values, or `None`.

“Built-in” does not mean “the only types Python supports.” Programs can also use collection types, library types, and types created by programmers.

## 3. Source notation creates values

A program uses recognizable source forms to create values directly. Quotation marks, decimal points, and reserved words are meaningful parts of the notation.

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

A small character change can create a different kind of value:

- `"4"` creates text;
- `4` creates an integer;
- `4.0` creates a floating-point number.

The next chapter will show how to inspect these types directly. Here, the goal is to recognize them from the source.

## 4. Text uses `str`

Python represents textual data with the built-in type `str`, pronounced “string.”

```python
course_name = "Python Study Guide"
learner_name = 'Ada'

print(course_name)
print(learner_name)
```

Expected output:

```text
Python Study Guide
Ada
```

Matching single or double quotation marks can create ordinary string literals. This project usually uses double quotation marks in small examples for consistency, but both forms are valid.

## 5. Quotation marks are not decoration

Quotation marks tell Python that the enclosed characters form text:

```python
chapter_label = "4"
```

Without quotation marks, the same digit sequence creates a number:

```python
chapter_number = 4
```

The quotation marks belong to the source code. `print()` displays the string's contents without normally displaying those surrounding quotation marks.

## 6. Whole numbers use `int`

Python represents integers with the built-in type `int`.

```python
chapter_number = 4
practice_minutes = 45

print(chapter_number)
print(practice_minutes)
```

Integers do not contain a decimal point in their ordinary decimal notation. They can be positive, negative, or zero:

```python
positive_value = 12
negative_value = -3
zero_value = 0
```

Detailed arithmetic belongs to the strings-and-numbers phase. For now, recognize that `45` is numeric data, while `"45"` is text.

## 7. Floating-point numbers use `float`

A number written with a decimal point usually creates a `float`:

```python
estimated_hours = 1.5
completion_rate = 0.75

print(estimated_hours)
print(completion_rate)
```

Floating-point values are useful for measurements, rates, averages, and many calculations that are not restricted to whole numbers.

Binary floating-point cannot represent every decimal fraction exactly. That precision topic matters in real programs, but it belongs to a later numerical chapter.

## 8. Logical values use `bool`

The type `bool` has two values:

- `True`;
- `False`.

```python
is_available = True
needs_review = False

print(is_available)
print(needs_review)
```

Expected output:

```text
True
False
```

Boolean values commonly represent yes-or-no states such as availability, completion, permission, or whether a condition was satisfied.

## 9. `True` and `False` require capitalization

The first letter must be uppercase:

```python
is_available = True
needs_review = False

print(is_available)
print(needs_review)
```

These lowercase forms are not Boolean literals:

```text
is_available = true
needs_review = false
```

Python treats lowercase `true` and `false` as ordinary names. Unless those names were assigned earlier, reading them raises `NameError`.

## 10. `None` represents an absent value

`None` is a special built-in constant frequently used to represent the absence of a value.

```python
next_chapter = None
print(next_chapter)
```

Expected output:

```text
None
```

`None` is the only instance of the type `NoneType`. Beginners usually write `None` directly rather than trying to construct a `NoneType` value.

## 11. `None` is intentional information

`None` does not necessarily mean that something went wrong. It can deliberately communicate:

- no result is available yet;
- an optional value was not supplied;
- a field has no applicable value;
- a later step is expected to provide the value.

Choose `None` when “no value” is meaningfully different from valid text or a valid number.

## 12. Similar output can hide different types

These values look related when printed:

```python
text_number = "42"
whole_number = 42
decimal_number = 42.0

print(text_number)
print(whole_number)
print(decimal_number)
```

Expected output:

```text
42
42
42.0
```

The first two lines both display `42`, but the first value is text and the second is an integer. Plain output does not always reveal the type clearly.

## 13. Type affects operations

The same operator can behave differently with different types:

```python
text_number = "42"
whole_number = 42
decimal_number = 42.0

print("Text repeated:", text_number + text_number)
print("Integer added:", whole_number + whole_number)
print("Float added:", decimal_number + decimal_number)
```

Expected output:

```text
Text repeated: 4242
Integer added: 84
Float added: 84.0
```

For strings, `+` joins text. For numbers, `+` performs addition. Python uses the operand types to decide which behavior applies.

## 14. A quoted Boolean is only text

Compare:

```python
real_flag = True
text_flag = "True"

print(real_flag)
print(text_flag)
```

Both lines display a similar word, but `real_flag` stores a Boolean and `text_flag` stores text.

Use actual Boolean values for logical states. Use strings only when the program genuinely needs the written word.

## 15. The word `"None"` is not `None`

Compare:

```python
missing_value = None
written_word = "None"

print(missing_value)
print(written_word)
```

`missing_value` stores the special absence marker. `written_word` stores four ordinary text characters.

They may print similarly, but they communicate different information to the program.

## 16. `input()` still returns `str`

Chapter 02 established an important rule:

```python
practice_minutes = input("Practice minutes: ")
print("Stored response:", practice_minutes)
```

Even when the person types `45`, the returned value is text. Python does not automatically convert terminal input into an integer or float.

Type conversion receives its own chapter after learners can inspect types reliably.

## 17. A name can later refer to another type

Python names are not permanently declared as one type:

```python
current_value = "42"
print(current_value)

current_value = 42
print(current_value)

current_value = 42.0
print(current_value)
```

The name `current_value` first refers to a string, then an integer, then a float.

This flexibility is useful, but changing the meaning and type of the same variable without a clear reason can make code difficult to understand.

## 18. Names should support, not replace, type understanding

Clear names can suggest what a value represents:

```python
age_text = "30"
age_number = 30
is_active = True
missing_note = None
```

The suffixes and prefixes improve readability, but Python does not enforce them. A programmer could still assign the wrong kind of value.

Use meaningful names together with an understanding of the actual value and its type.

## 19. This chapter is not an exhaustive catalog

Python includes many other built-in types. A brief preview:

```python
topics = ["variables", "types"]
coordinates = (10, 20)
learner = {"name": "Ada"}
tags = {"python", "beginner"}
```

These examples introduce lists, tuples, dictionaries, and sets only as a map of what exists. Their structure and operations belong to the collections phase.

Python also has other numeric and binary-data types. The learning path introduces them when they become useful.

## 20. Repository examples

| File | Purpose | Automatic execution |
|---|---|---|
| [`value_catalog.py`](examples/value_catalog.py) | Stores and displays one example from each focused value category | Yes |
| [`same_looking_values.py`](examples/same_looking_values.py) | Demonstrates that similar-looking values can behave differently | Yes |

Both examples are deterministic, non-interactive, and included in the unattended example manifest.

## 21. Practical example: value catalog

Create `value_catalog.py`:

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None

print("Course:", course_name)
print("Chapter:", chapter_number)
print("Estimated minutes:", estimated_minutes)
print("Available:", is_available)
print("Next chapter:", next_chapter)
```

Expected output:

```text
Course: Python Study Guide
Chapter: 4
Estimated minutes: 60.0
Available: True
Next chapter: None
```

The labels make the role of each value visible. The source notation reveals the type category even before the next chapter introduces direct inspection.

## 22. Exercise

Create `chapter_status.py` using exactly these names:

```python
guide_name
chapter_number
estimated_minutes
is_published
review_note
```

Store:

1. the text `"Python Study Guide"` in `guide_name`;
2. the integer `4` in `chapter_number`;
3. the float `60.0` in `estimated_minutes`;
4. the Boolean `True` in `is_published`;
5. `None` in `review_note`.

Print each value on a labeled line. Then create a text version of the chapter number called `chapter_number_text` and assign `"4"` to it.

Add two final lines:

```python
print("Number result:", chapter_number + chapter_number)
print("Text result:", chapter_number_text + chapter_number_text)
```

Before running the program, predict both results. Explain why they differ.

## 23. Common mistakes

### Adding quotation marks to every value

```python
chapter_number = "4"
```

This stores text, not an integer. Use `4` when the value must behave as a whole number.

### Forgetting the decimal point when a float is intended

```python
estimated_hours = 2
```

This creates an integer. Write `2.0` when the example specifically needs a float value.

### Writing logical states as strings

```text
is_ready = "False"
```

The string `"False"` is text. Use the Boolean value `False` for a logical state.

### Writing missing data as text

```text
next_chapter = "None"
```

The string `"None"` is not the absence marker. Use `None`.

### Using the wrong capitalization

```text
is_ready = TRUE
next_chapter = none
```

Write `True`, `False`, and `None` exactly as Python defines them.

### Trusting printed appearance alone

`print()` is designed for readable output. Different types can produce similar visible text, so output alone is not always enough to identify a value's type.

The next chapter introduces direct inspection with `type()` and relationship checks with `isinstance()`.

## 24. Self-check

You are ready for the next chapter when you can answer:

- What is the relationship between a value and a type?
- What does “built-in” mean?
- Which type represents text?
- What is the difference between `"42"`, `42`, and `42.0`?
- Which two values belong to `bool`?
- Why are `true` and `false` incorrect in Python?
- What does `None` commonly represent?
- Is `"None"` the same value as `None`?
- What type does `input()` return?
- Why can the same `+` symbol behave differently for strings and numbers?
- Does this chapter list every built-in Python type?

## 25. Quick-reference summary

| Value category | Source example | Built-in type |
|---|---|---|
| Text | `"Python"` | `str` |
| Whole number | `42` | `int` |
| Decimal-style number | `42.0` | `float` |
| Logical value | `True` or `False` | `bool` |
| Absence marker | `None` | `NoneType` |

Additional reminders:

- quotation marks create text;
- a decimal point commonly indicates a float literal;
- `True`, `False`, and `None` are case-sensitive;
- printed appearance may not reveal the type;
- `input()` returns `str`;
- type conversion is deliberate and belongs to a later chapter.

## 26. Run the repository examples

From the repository root:

```bash
python fundamentals/04-built-in-data-types/examples/value_catalog.py
python fundamentals/04-built-in-data-types/examples/same_looking_values.py
```

Both examples are approved for unattended execution.

## 27. Run the repository checks

From the repository root:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## Official references

- [Python data model — Objects, values, and types](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [Python standard library — Built-in types](https://docs.python.org/3/library/stdtypes.html)
- [Python language reference — Literals](https://docs.python.org/3/reference/lexical_analysis.html#literals)
- [Python standard library — Built-in constants](https://docs.python.org/3/library/constants.html)

[← Back to the section index](../README.md) · [← Previous chapter: Variables and naming](../03-variables-and-naming/README.md)

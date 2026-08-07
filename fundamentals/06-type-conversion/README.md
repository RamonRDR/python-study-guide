<div align="center">

# Type Conversion

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: `type()` and `isinstance()`](../05-type-and-isinstance/README.md)

Chapter 05 taught you how to inspect the type a value already has. This final Fundamentals chapter teaches the next step: deliberately creating a value of another compatible type.

This chapter focuses on explicit conversion. Calling `int()`, `float()`, `str()`, or `bool()` produces a result according to that type's conversion rules. The original value does not silently change inside the object that already existed.

Python can also perform some implicit conversions in specific contexts, such as mixed numeric operations. Those cases are outside this chapter; here, every conversion is written deliberately with one of these built-in calls.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Chapters 01 to 05 |
| Estimated study time | 60 to 80 minutes |
| Main concepts | `int()`, `float()`, `str()`, `bool()`, conversion, `ValueError`, truth value |

## Learning objectives

By the end of this chapter, you should be able to:

- convert compatible text to `int` and `float`;
- convert values to `str`;
- explain that conversion creates a result value rather than mutating the original value;
- explain why `int()` truncates a floating-point value toward zero instead of rounding it;
- recognize invalid textual conversions that raise `ValueError`;
- use `bool()` according to Python's truth-value rules;
- explain why `bool("False")` is `True`;
- convert text returned by `input()` before numeric calculations;
- avoid conversions that hide intent or discard information accidentally.

## 1. Why conversion exists

Programs often receive a value in one form and need it in another. A terminal gives `input()` results as text, while arithmetic normally needs numeric values.

Conversion creates an explicit bridge between those representations.

## 2. The basic conversion calls

The built-in type names are callable:

```python
integer_value = int(value)
decimal_value = float(value)
text_value = str(value)
boolean_value = bool(value)
```

Read `int(value)` as "create an integer from this compatible value." The same idea applies to the other calls.

## 3. Convert integer text with `int()`

A string containing a valid integer representation can be converted to `int`:

```python
age_text = "28"
age = int(age_text)

print(age)
print(type(age))
```

Expected output:

```text
28
<class 'int'>
```

The characters `"28"` are text. The result `28` is an integer value.

## 4. Convert decimal text with `float()`

A string containing a compatible floating-point representation can be converted to `float`:

```python
temperature_text = "21.5"
temperature = float(temperature_text)

print(temperature)
print(type(temperature))
```

Expected output:

```text
21.5
<class 'float'>
```

## 5. Convert values to text with `str()`

`str()` creates a string representation of a value:

```python
attempts = 3
message = "Attempts: " + str(attempts)

print(message)
print(type(message))
```

Expected output:

```text
Attempts: 3
<class 'str'>
```

Without the conversion, concatenating a string and an integer with `+` would mix incompatible operand types.

## 6. Conversion creates a new result

The original value does not silently become another type:

```python
price_text = "19.90"
price = float(price_text)

print(type(price_text))
print(type(price))
```

Expected output:

```text
<class 'str'>
<class 'float'>
```

`price_text` still refers to a string. `price` refers to the new floating-point result.

## 7. Numeric conversion can change representation

An integer can be converted to a floating-point value:

```python
whole_number = float(8)

print(whole_number)
print(type(whole_number))
```

Expected output:

```text
8.0
<class 'float'>
```

The numeric magnitude is the same here, but the resulting type is different.

## 8. `int()` does not round floating-point values

When converting a finite floating-point number, `int()` discards the fractional part toward zero:

```python
print(int(8.9))
print(int(-8.9))
```

Expected output:

```text
8
-8
```

This is truncation, not rounding.

## 9. Some textual conversions are invalid

The following text is valid for `float()`, but not for `int()`:

```python
int("8.9")
```

This call raises `ValueError`.

If a two-step conversion from decimal text to integer is truly intended, make the stages visible rather than assuming `int()` parses decimal text directly.

## 10. Invalid numeric text can raise `ValueError`

This call also fails:

```python
float("hello")
```

Python raises `ValueError` because the string cannot be interpreted as a supported floating-point representation.

Detailed exception handling belongs to a later phase. For now, recognize the error and understand why the conversion failed.

## 11. `bool()` follows truth-value testing

`bool()` does not parse human words. It applies Python's truth-value rules:

```python
print(bool(""))
print(bool("False"))
print(bool(0))
print(bool(7))
print(bool(None))
```

Expected output:

```text
False
True
False
True
False
```

Empty strings, numeric zero, and `None` are false. Many non-empty or non-zero values are true.

## 12. `bool("False")` is still `True`

A common beginner mistake is expecting the text to be interpreted as a boolean word:

```python
print(bool("False"))
print(bool("0"))
```

Expected output:

```text
True
True
```

Both strings contain characters, so both are truthy.

Turning textual words such as `"true"` and `"false"` into application booleans requires explicit parsing logic, not merely `bool(text)`.

## 13. Booleans can be converted to integers

Because `bool` is a subclass of `int`, explicit conversion maps the two boolean values to integers:

```python
print(int(True))
print(int(False))
```

Expected output:

```text
1
0
```

Use this only when the numeric representation is actually meaningful. Clear boolean intent is usually better than treating booleans as numbers casually.

## 14. `None` can become text or a boolean

Different target types apply different rules:

```python
print(str(None))
print(bool(None))
```

Expected output:

```text
None
False
```

`str(None)` creates the text `"None"`. It does not create a special missing-value marker inside the string.

## 15. Convert `input()` before numeric arithmetic

`input()` always returns text. Convert that text before arithmetic when the program expects a number:

```python
age_text = input("Age: ")
age = int(age_text)

print("Next year:", age + 1)
```

Example terminal interaction:

```text
Age: 28
Next year: 29
```

The user's keystrokes arrive as text first. The call to `int()` creates the integer used in the calculation.

## 16. Convert at a clear boundary

A useful beginner pattern is:

1. receive external text;
2. store it with a name that makes its current form clear;
3. convert it once when the intended type is known;
4. continue using the converted value.

This keeps the rest of the program from carrying ambiguous text longer than necessary.

## 17. Keep multi-step conversions readable

Conversions can be nested, but intermediate names often make the transformation easier to understand:

```python
number_text = "8.9"
number = float(number_text)
whole_number = int(number)

print(whole_number)
```

Expected output:

```text
8
```

The code makes both transformations visible: text to `float`, then `float` to `int`.

## 18. Conversion may discard information

Converting `8.9` to `8` loses the fractional part.

Before converting, ask whether the target type can represent everything you still need. A successful conversion can still be a poor design choice if it throws away meaningful information.

## 19. Conversion and validation are different jobs

A successful conversion means Python could create the requested value. It does not prove that the value is sensible for your application.

For example:

```python
quantity = int("-4")
```

The conversion itself is valid. A future program might still reject negative quantities according to its own rules.

Conversion answers "can this representation become this type?" Application validation answers a different question.

## 20. Do not convert just to make an error disappear

A conversion should represent the program's intended meaning.

Turning every value into text or forcing every value into a number can hide a modeling mistake instead of solving it. Prefer conversions at places where a value genuinely crosses from one representation to another.

## 21. Practical example: convert before calculation

Here a price arrives as text:

```python
price_text = "19.90"
price = float(price_text)
shipping = 2.50
total = price + shipping

print(total)
```

Expected output:

```text
22.4
```

The conversion happens before arithmetic, so both operands in the addition are numeric.

## 22. Common mistakes

Watch for these patterns:

- assuming `int(8.9)` rounds to `9`;
- expecting `int("8.9")` to work because the text represents a number;
- expecting `bool("False")` to return `False`;
- converting a value without considering information loss;
- repeatedly converting the same value back and forth without a clear reason;
- forgetting that `input()` returns text.

## 23. Quick reference

| Expression | Result | Meaning |
|---|---|---|
| `int("28")` | `28` | Convert valid integer text |
| `float("21.5")` | `21.5` | Convert compatible decimal text |
| `float(8)` | `8.0` | Create a floating-point value from an integer |
| `int(8.9)` | `8` | Truncate a finite float toward zero |
| `str(28)` | `"28"` | Create text |
| `bool(0)` | `False` | Apply truth-value testing |
| `bool("False")` | `True` | Non-empty strings are truthy |

## 24. Exercise

Write a small interactive program that:

1. asks for a whole-number quantity;
2. asks for a decimal price;
3. converts the two `input()` results;
4. calculates `quantity * price`;
5. prints the result.

Test once with valid numeric text. Then deliberately enter incompatible text and observe the error without trying to handle it yet.

## 25. Self-check

Before leaving Fundamentals, make sure you can answer these questions:

- What type does `input()` return?
- Why does `int("8.9")` fail while `float("8.9")` succeeds?
- Does `int(8.9)` round?
- Why is `bool("False")` true?
- Does converting `price_text` to `float` change the value stored in `price_text`?
- When can a conversion lose information?

## 26. Example: basic conversions

The first repository example keeps the original text values separate from the converted values:

```python
age_text = "28"
temperature_text = "21.5"

age = int(age_text)
temperature = float(temperature_text)
summary = str(age) + " years"

print(age, type(age))
print(temperature, type(temperature))
print(summary, type(summary))
```

Expected output:

```text
28 <class 'int'>
21.5 <class 'float'>
28 years <class 'str'>
```

## 27. Example: conversion surprises

The second example records behaviors worth remembering:

```python
print(int(8.9))
print(int(-8.9))
print(bool(""))
print(bool("False"))
print(bool(0))
print(bool(1))
```

Expected output:

```text
8
-8
False
True
False
True
```

## 28. Run the examples

From the repository root:

```bash
python fundamentals/06-type-conversion/examples/conversion_basics.py
python fundamentals/06-type-conversion/examples/conversion_surprises.py
```

Both examples are deterministic, non-interactive, network-free, and suitable for unattended execution.

## 29. Run the repository checks

After editing the chapter or examples:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 30. Phase 1 complete

With this chapter, the Fundamentals learning path is complete.

You can now execute a Python file, display and receive information, store values, recognize and inspect common types, and deliberately convert compatible values. The roadmap continues with **Phase 2: Strings and numbers**.

## Official references

- [Python built-in functions — `int()`](https://docs.python.org/3/library/functions.html#int)
- [Python built-in functions — `float()`](https://docs.python.org/3/library/functions.html#float)
- [Python built-in functions — `str()`](https://docs.python.org/3/library/functions.html#str)
- [Python built-in functions — `bool()`](https://docs.python.org/3/library/functions.html#bool)
- [Python built-in types — Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Python built-in exceptions — `ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)

[← Back to the section index](../README.md) · [← Previous chapter: `type()` and `isinstance()`](../05-type-and-isinstance/README.md)

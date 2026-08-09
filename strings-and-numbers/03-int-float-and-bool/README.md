<div align="center">

# `int`, `float`, and `bool`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: Common string methods](../02-common-string-methods/README.md) · [Next chapter: Numeric built-ins →](../04-numeric-builtins/README.md)

Python already introduced these types in the Fundamentals phase. This chapter goes one level deeper by focusing on how they behave in expressions, how their results differ, and which details matter when choosing between them.

The goal is not to memorize isolated rules. The goal is to build a reliable mental model for integers, approximate decimal values, and truth values.

## Learning goals

By the end of this chapter, you should be able to:

- choose `int`, `float`, or `bool` according to the meaning of a value;
- explain why Python integers are not limited to a fixed 32-bit or 64-bit range;
- predict the result type of common mixed numeric expressions;
- distinguish `/` from `//` and `%`;
- understand why floor division with negative numbers can surprise beginners;
- recognize the approximation limits of binary floating-point values;
- explain why `0.1 + 0.2 == 0.3` is `False`;
- use `bool()` and truth values without confusing textual content with Boolean meaning;
- explain the special relationship between `bool` and `int`;
- avoid using Boolean values as numeric quantities when that would hide intent.

## 1. Three types, three main jobs

A useful first model is:

| Type | Main job | Example |
|---|---|---|
| `int` | integer values | `12`, `0`, `-4` |
| `float` | fractional or approximate real-number values | `7.5`, `-0.25` |
| `bool` | truth values | `True`, `False` |

```python
item_count = 12
unit_price = 7.5
is_available = True

print(type(item_count))
print(type(unit_price))
print(type(is_available))
```

```text
<class 'int'>
<class 'float'>
<class 'bool'>
```

These types can interact, but they still communicate different meanings.

## 2. `int` represents integers

Use `int` for values that conceptually have no fractional part.

```python
students = 30
temperature_change = -4
balance_adjustment = 0

print(students)
print(temperature_change)
print(balance_adjustment)
```

```text
30
-4
0
```

An integer can be positive, negative, or zero.

## 3. Python integers have arbitrary precision

In many programming languages, an integer type is tied to a fixed number of bits. Python's built-in `int` is different: integers have arbitrary precision, limited mainly by available memory and implementation constraints rather than a normal fixed 32-bit or 64-bit range.

```python
large_number = 10 ** 100

print(type(large_number))
print(len(str(large_number)))
```

```text
<class 'int'>
101
```

That does not mean extremely large integers are free. Larger values require more memory and computation. The important beginner takeaway is simply that ordinary Python `int` values do not overflow at a small fixed boundary such as 2,147,483,647.

## 4. Numeric separators improve readability

Python allows underscores inside numeric literals to improve readability.

```python
annual_revenue = 1_250_000
binary_mask = 0b1010

print(annual_revenue)
print(binary_mask)
```

```text
1250000
10
```

The underscores are part of the source notation, not part of the stored numeric value.

The binary literal is included only to show that integer notation can vary. Number bases are not the focus of this chapter.

## 5. `float` represents floating-point values

Use `float` when a value needs a fractional component or when an operation naturally produces a floating-point result.

```python
unit_price = 19.90
exchange_rate = 5.42
temperature = -3.5

print(type(unit_price))
print(type(exchange_rate))
print(type(temperature))
```

```text
<class 'float'>
<class 'float'>
<class 'float'>
```

A real numeric literal containing a decimal point, such as `19.90`, produces a `float`.

## 6. `int` and `float` can participate in the same expression

Python supports mixed arithmetic between these numeric types.

```python
whole_number = 4
decimal_number = 2.5

print(whole_number + decimal_number)
print(type(whole_number + decimal_number))
```

```text
6.5
<class 'float'>
```

When an integer and a floating-point value participate in ordinary arithmetic, Python usually produces a floating-point result so that the fractional capability is preserved.

This is one example of implicit numeric conversion. It does not replace the explicit-conversion concepts learned in Fundamentals.

## 7. `/` is true division

The `/` operator performs true division.

```python
print(7 / 2)
print(type(7 / 2))
```

```text
3.5
<class 'float'>
```

Even when both operands are integers, `/` produces a floating-point result when the mathematical result can be represented as a `float`. If that result is too large to convert to a finite `float`, true division raises `OverflowError` instead.

```python
print(8 / 4)
print(type(8 / 4))
```

```text
2.0
<class 'float'>
```

When the quotient is representable as a `float`, a mathematically whole quotient still has type `float` when `/` is used.

## 8. `//` is floor division

The `//` operator performs floor division.

```python
print(7 // 2)
print(7.0 // 2)
```

```text
3
3.0
```

With two integers, the result is an integer. If a floating-point operand participates, the result is a floating-point value representing the floored quotient.

The word **floor** is important. `//` is not simply "remove the decimal part."

## 9. `%` gives the remainder associated with floor division

The `%` operator gives the remainder.

```python
print(7 % 2)
print(14 % 5)
```

```text
1
4
```

For integers, `//` and `%` fit together through this relationship:

```text
dividend == divisor * (dividend // divisor) + (dividend % divisor)
```

Example:

```python
value = 17
divisor = 5

quotient = value // divisor
remainder = value % divisor

print(quotient)
print(remainder)
print(divisor * quotient + remainder)
```

```text
3
2
17
```

This relationship becomes especially useful when splitting values into groups and leftovers.

## 10. Negative floor division can surprise you

A common mistake is to expect floor division to truncate toward zero.

```python
print(-7 // 3)
print(-7 % 3)
```

```text
-3
2
```

Why `-3` instead of `-2`?

Because floor division rounds the quotient downward toward negative infinity. The exact quotient is approximately `-2.333...`, and the floor is `-3`.

The remainder then preserves the division identity:

```text
-7 == 3 * (-3) + 2
```

You do not need to memorize every negative case. Remember the rule: `//` means floor division, not truncation.

## 11. `**` performs exponentiation

The exponentiation operator is `**`.

```python
print(2 ** 5)
print(9 ** 0.5)
```

```text
32
3.0
```

The result type depends on the values and operation. Raising `9` to `0.5` uses a floating-point exponent and produces a `float`.

## 12. Division by zero is an error

Numeric types do not make division by zero valid.

```python
print(10 / 0)
```

The operation raises:

```text
ZeroDivisionError: division by zero
```

The exact traceback contains additional lines and file information. The important part here is the exception type.

Exception handling is covered later in the roadmap. For now, recognize that invalid arithmetic can stop program execution.

## 13. Floating-point values are usually approximations

Most modern systems represent Python floating-point numbers using binary floating-point hardware.

Many simple decimal fractions cannot be represented exactly as finite binary fractions. That means a value such as `0.1` is stored as the nearest representable binary approximation.

This is not a Python-specific bug. It is a property of binary floating-point arithmetic used by many programming languages and processors.

## 14. The classic `0.1 + 0.2` example

```python
result = 0.1 + 0.2

print(result)
print(result == 0.3)
```

```text
0.30000000000000004
False
```

The printed result exposes a small representation difference.

The important lesson is not that floats are unreliable. The lesson is that they represent many decimal values approximately, so exact decimal equality can be inappropriate in some situations.

## 15. Displayed decimal text is not the whole internal story

Python normally displays a short decimal representation that maps back to the same stored floating-point value.

You can inspect an exact integer ratio for a finite float:

```python
value = 0.1

print(value)
print(value.as_integer_ratio())
```

```text
0.1
(3602879701896397, 36028797018963968)
```

On modern Python platforms that use IEEE 754 binary64 for `float`, the ratio shows the exact stored value represented by this `float`. The language does not require every Python implementation to use that hardware format.

For a beginner, the useful mental model is enough: the text `0.1` is convenient notation for a nearby representable floating-point value.

## 16. Do not use float equality blindly for measured or calculated decimals

This can be fragile:

```python
print(0.1 + 0.2 == 0.3)
```

```text
False
```

Whether exact equality is appropriate depends on the domain.

For approximate numeric comparisons, Python's standard library provides tools such as `math.isclose()`. For exact base-10 decimal arithmetic, the `decimal` module is often more appropriate.

Those tools are outside this chapter's scope. The important idea here is to recognize when plain `float` equality may not express the intended comparison.

## 17. Money deserves special attention

A tempting beginner pattern is:

```python
account_balance = 0.1 + 0.2
```

A `float` may be perfectly acceptable for many measurements, graphics calculations, simulations, and ordinary numeric tasks. But domains that require exact decimal behavior, such as many accounting calculations, often need a decimal representation designed for that requirement.

Do not conclude that "floats are bad for money" is the entire rule. The real question is what precision, rounding, storage, and domain guarantees the application requires.

## 18. `float.is_integer()` asks whether a float has an integral value

A `float` can represent a value with no fractional part.

```python
print((5.0).is_integer())
print((5.25).is_integer())
```

```text
True
False
```

`5.0` is still a `float`. `is_integer()` asks about its numeric value, not its runtime type.

```python
value = 5.0

print(type(value))
print(value.is_integer())
```

```text
<class 'float'>
True
```

## 19. `bool` represents truth values

The Boolean type has two values:

```python
is_ready = True
has_error = False

print(type(is_ready))
print(type(has_error))
```

```text
<class 'bool'>
<class 'bool'>
```

Use `bool` when the meaning is yes/no, true/false, enabled/disabled, available/unavailable, or another two-state condition.

## 20. Comparisons produce Boolean results

Comparisons answer questions about values and normally produce `True` or `False`.

```python
temperature = 18

print(temperature > 20)
print(temperature == 18)
```

```text
False
True
```

The detailed use of comparisons inside `if`, `while`, and other control-flow structures comes later. Here, focus on the result type.

## 21. Every object can participate in truth-value testing

Python can interpret many values as true or false in a Boolean context.

```python
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(None))
print(bool(1))
print(bool(-3))
print(bool("Python"))
```

```text
False
False
False
False
True
True
True
```

For the types already introduced in this guide:

- numeric zero is false;
- an empty string is false;
- `None` is false;
- nonzero numbers are true;
- nonempty strings are true.

Collections add more truth-value rules later.

## 22. Text content is not parsed as a Boolean word

This is a famous beginner trap:

```python
print(bool("False"))
print(bool("0"))
```

```text
True
True
```

Both strings are nonempty, so both are truthy.

`bool()` does not read English words and decide what they mean. It applies Python's truth-value rules to the object.

## 23. `bool` is a subclass of `int`

Python has a historical and technical relationship between Boolean and integer values.

```python
print(isinstance(True, bool))
print(isinstance(True, int))
print(int(True))
print(int(False))
```

```text
True
True
1
0
```

This is why Chapter 05 in Fundamentals showed that `isinstance(True, int)` is `True` even though `type(True) is bool`.

The relationship is real, but it should not erase semantic meaning.

## 24. Boolean arithmetic works, but it often communicates the wrong idea

Because `bool` is a subclass of `int`, this is valid Python:

```python
print(True + True)
print(False + 10)
```

```text
2
10
```

That does not mean Boolean arithmetic should be your default design.

If a variable means availability, validation, permission, or another condition, keep that meaning visible instead of treating the value as an accidental `0` or `1`.

## 25. Choose a type according to meaning, not appearance

Consider this small model:

```python
items_in_cart = 3
average_price = 14.75
is_checkout_open = True

print(type(items_in_cart))
print(type(average_price))
print(type(is_checkout_open))
```

```text
<class 'int'>
<class 'float'>
<class 'bool'>
```

The three values could all participate in numeric behavior under some circumstances, but their domain meanings are different.

Good type choices make later code easier to understand.

## 26. Avoid integer flags when a Boolean expresses the intent

Less clear:

```python
is_active = 1
```

Clearer:

```python
is_active = True
```

An integer flag can be valid when communicating with a file format, database, protocol, or legacy API that requires `0` and `1`. Inside ordinary Python logic, a `bool` usually communicates Boolean intent more directly.

## 27. Avoid adding `.0` only to make a value look decimal

This is not automatically better:

```python
employee_count = 42.0
```

If the value represents a count that cannot be fractional, `42` may express the domain more clearly.

Likewise, a value such as `5.0` may legitimately need to remain a `float` when it belongs to a calculation pipeline based on measurements or floating-point operations.

Meaning comes first.

## 28. Numeric result types can carry information

Compare:

```python
print(5 + 2)
print(5 + 2.0)
print(5 / 2)
print(5 // 2)
```

```text
7
7.0
2.5
2
```

The operators and operand types influence both the value and the result type.

When debugging numeric code, inspect both.

## 29. Practical example: numeric behavior

The file [`examples/numeric_behavior.py`](examples/numeric_behavior.py) contains:

```python
whole_number = 7
decimal_number = 2.5

print("Mixed addition:", whole_number + decimal_number)
print("True division:", 7 / 2)
print("Floor division:", 7 // 2)
print("Remainder:", 7 % 2)
print("Negative floor division:", -7 // 3)
print("Matching remainder:", -7 % 3)
```

Expected output:

```text
Mixed addition: 9.5
True division: 3.5
Floor division: 3
Remainder: 1
Negative floor division: -3
Matching remainder: 2
```

This example keeps several related numeric rules in one place.

## 30. Practical example: truth and precision

The file [`examples/truth_and_precision.py`](examples/truth_and_precision.py) contains:

```python
print("0.1 + 0.2:", 0.1 + 0.2)
print("Exactly 0.3:", 0.1 + 0.2 == 0.3)
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print('bool(""):', bool(""))
print('bool("False"):', bool("False"))
print("bool is int-compatible:", isinstance(True, int))
```

Expected output:

```text
0.1 + 0.2: 0.30000000000000004
Exactly 0.3: False
bool(0): False
bool(1): True
bool(""): False
bool("False"): True
bool is int-compatible: True
```

The example deliberately places two common surprises together: floating-point approximation and Boolean truth-value rules.

## 31. Common mistakes

### Mistake 1: expecting `/` to preserve `int`

```python
print(type(8 / 4))
```

```text
<class 'float'>
```

### Mistake 2: reading `//` as truncation toward zero

```python
print(-7 // 3)
```

```text
-3
```

### Mistake 3: expecting decimal floating-point arithmetic to be exact

```python
print(0.1 + 0.2 == 0.3)
```

```text
False
```

### Mistake 4: assuming the text `"False"` is false

```python
print(bool("False"))
```

```text
True
```

### Mistake 5: forgetting that `bool` is `int`-compatible

```python
print(isinstance(True, int))
```

```text
True
```

Compatibility does not mean the two types express the same intent.

## 32. Exercise: build a numeric profile

Create a file named `numeric_profile.py`.

Use these starting values:

```python
item_count = 12
unit_price = 7.5
is_available = True
```

Your program should:

1. calculate `subtotal` by multiplying `item_count` and `unit_price`;
2. print each original value;
3. print the type of each original value;
4. print `subtotal`;
5. print the type of `subtotal`;
6. explain, in your own words, why `subtotal` is a `float`.

One possible implementation is:

```python
item_count = 12
unit_price = 7.5
is_available = True

subtotal = item_count * unit_price

print("Item count:", item_count)
print("Item count type:", type(item_count))
print("Unit price:", unit_price)
print("Unit price type:", type(unit_price))
print("Available:", is_available)
print("Available type:", type(is_available))
print("Subtotal:", subtotal)
print("Subtotal type:", type(subtotal))
```

Expected output:

```text
Item count: 12
Item count type: <class 'int'>
Unit price: 7.5
Unit price type: <class 'float'>
Available: True
Available type: <class 'bool'>
Subtotal: 90.0
Subtotal type: <class 'float'>
```

Try the exercise yourself before comparing with the sample.

## 33. Self-check

You should now be able to answer these questions without running Python first:

1. What is the main conceptual difference between `int`, `float`, and `bool`?
2. Why can Python store an integer much larger than a normal 64-bit integer?
3. What type does `7 / 2` produce?
4. What is the difference between `/` and `//`?
5. Why is `-7 // 3` equal to `-3`?
6. What does `%` return?
7. Why can `0.1 + 0.2 == 0.3` be `False`?
8. Is `5.0` an `int` because its fractional part is zero?
9. Why is `bool("False")` equal to `True`?
10. Why does `isinstance(True, int)` return `True`?

## 34. Quick reference

| Goal | Example | Important detail |
|---|---|---|
| Integer value | `count = 12` | `int` has arbitrary precision |
| Fractional numeric value | `rate = 5.42` | `float` is usually approximate binary floating point |
| Truth value | `is_ready = True` | `bool` has `True` and `False` |
| True division | `7 / 2` | returns `3.5` |
| Floor division | `7 // 2` | returns the floor quotient |
| Remainder | `7 % 2` | pairs with floor division |
| Exponentiation | `2 ** 5` | returns `32` |
| Test float integral value | `(5.0).is_integer()` | value can be integral while type remains `float` |
| Convert to truth value | `bool(value)` | follows truth-value rules |
| Exact runtime type | `type(value)` | `type(True) is bool` |
| Compatible type | `isinstance(value, int)` | `True` is `int`-compatible |

## 35. Run the examples

From the repository root:

```bash
python strings-and-numbers/03-int-float-and-bool/examples/numeric_behavior.py
python strings-and-numbers/03-int-float-and-bool/examples/truth_and_precision.py
```

Then run the repository checks:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 36. What comes next

You now have a stronger model for whole numbers, floating-point values, and Boolean values.

The next chapter completes Phase 2 by introducing common numeric helpers: **`round()`, `abs()`, `min()`, `max()`, and `sum()`**.

That chapter will build directly on the numeric behavior established here instead of treating those functions as an isolated list.

## Official references

- [Python Built-in Types: Numeric Types](https://docs.python.org/3.14/library/stdtypes.html#numeric-types-int-float-complex)
- [Python Built-in Types: Truth Value Testing](https://docs.python.org/3.14/library/stdtypes.html#truth-value-testing)
- [Python Built-in Types: Boolean Type](https://docs.python.org/3.14/library/stdtypes.html#boolean-type-bool)
- [Python Tutorial: Floating-Point Arithmetic, Issues and Limitations](https://docs.python.org/3.14/tutorial/floatingpoint.html)

[← Back to the section index](../README.md)

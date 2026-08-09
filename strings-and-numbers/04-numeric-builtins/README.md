<div align="center">

# Numeric Built-ins: `round()`, `abs()`, `min()`, `max()`, and `sum()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Phase 2 has already introduced text, string operations, integers, floating-point values, and Boolean values. This chapter finishes the phase by combining that knowledge with five built-in functions that solve common numeric tasks without requiring imports.

These functions look small, but several of them contain details that matter in real programs. In particular, `round()` does not always behave like the everyday rule of "5 always rounds up", floating-point representation can influence rounded results, and `min()` and `max()` need special care with empty inputs.

## Chapter information

- **Level:** Beginner
- **Prerequisite:** complete Chapters 01 through 03 of Phase 2
- **Estimated study time:** 70 to 90 minutes
- **Main concepts:** `round()`, `abs()`, `min()`, `max()`, `sum()`, `ndigits`, empty iterables, numeric aggregation, floating-point rounding

## Learning objectives

By the end of this chapter, you should be able to:

- use `abs()` to obtain numeric magnitude without changing the original value;
- use `min()` and `max()` with several arguments or with an iterable;
- explain why empty iterables require care with `min()` and `max()`;
- use `sum()` to aggregate numeric values and understand its `start` argument;
- use `round()` with omitted, positive, zero, and negative `ndigits` values;
- explain Python's tie-breaking rule for built-in numeric rounding;
- recognize why floating-point representation can affect a rounded result;
- choose these built-ins for clear intent instead of manually reproducing their behavior;
- recognize where later tools such as `math.fsum()` or decimal arithmetic may be more appropriate.

---

## 1. Built-in functions are available without imports

Python provides a set of built-in functions that are available directly in normal code.

You already know examples such as:

```python
print("Python")
length = len("Python")
number = int("42")
```

The functions in this chapter work the same way from a usage perspective:

```python
print(abs(-8))
print(round(3.14159, 2))
```

You do not need this:

```python
import builtins
```

Direct use is the normal approach.

### Mental model

Think of these functions as small, standard tools that communicate intent:

```text
abs()    -> magnitude
round()  -> rounded numeric value
min()    -> smallest item
max()    -> largest item
sum()    -> accumulated total
```

Clear intent is important. `min(values)` tells a reader what you want much more directly than manually comparing every value yourself.

---

## 2. `abs()` returns an absolute value

For ordinary integers and floating-point numbers, `abs()` returns the distance from zero without a negative sign.

```python
print(abs(-12))
print(abs(12))
print(abs(-3.5))
```

```text
12
12
3.5
```

The sign of the input does not determine the sign of the result. The result represents magnitude.

### `abs()` does not mutate the original value

```python
temperature_change = -7
magnitude = abs(temperature_change)

print(temperature_change)
print(magnitude)
```

```text
-7
7
```

The original variable still refers to `-7`. `abs()` calculated and returned another value.

This matches a pattern you have already seen throughout Python:

```text
input value -> operation -> result value
```

### Practical use: distance from a target

Suppose a target value is `100`, while an observed value is `93`.

```python
observed = 93
target = 100
difference = observed - target
absolute_difference = abs(difference)

print(absolute_difference)
```

```text
7
```

When direction does not matter and only the size of the difference matters, `abs()` communicates that intention clearly.

---

## 3. `min()` finds the smallest item

`min()` can receive two or more positional arguments:

```python
print(min(8, 3, 12, -2))
```

```text
-2
```

It can also receive one iterable containing the values.

The next example uses a list only as a simple container. Lists are taught properly in Phase 3.

```python
values = [8, 3, 12, -2]
print(min(values))
```

```text
-2
```

The two forms answer the same kind of question, but they are useful in different situations:

```text
min(a, b, c)   -> values already exist as separate arguments
min(values)    -> values are already grouped in an iterable
```

### `min()` returns an existing item

With ordinary numbers, this feels obvious:

```python
smallest = min(10, 4, 7)
print(smallest)
```

```text
4
```

Later, when you study richer objects and the `key` argument, this idea becomes more important. For now, focus on numeric comparisons.

---

## 4. `max()` finds the largest item

`max()` mirrors `min()`.

With separate arguments:

```python
print(max(8, 3, 12, -2))
```

```text
12
```

With one iterable:

```python
values = [8, 3, 12, -2]
print(max(values))
```

```text
12
```

This symmetry makes the pair easy to remember:

```text
min(...) -> smallest
max(...) -> largest
```

### Practical use: range width

If the lowest measurement is `min(values)` and the highest is `max(values)`, the difference between them describes the width of the observed range.

```python
values = [8, 3, 12, -2]
range_width = max(values) - min(values)
print(range_width)
```

```text
14
```

That calculation combines several concepts without hiding the intention.

---

## 5. Empty inputs are important for `min()` and `max()`

An empty iterable has no smallest or largest element.

```python
values = []
```

Calling either function without a fallback raises `ValueError`:

```python
min(values)
```

```text
ValueError: min() iterable argument is empty
```

And similarly:

```python
max(values)
```

```text
ValueError: max() iterable argument is empty
```

When using the one-iterable form, you may provide `default=`:

```python
values = []
print(min(values, default=0))
print(max(values, default=0))
```

```text
0
0
```

### The fallback must make sense for the domain

`default=0` is not automatically the correct choice.

For example, if an empty dataset means "there is no measurement", returning zero could incorrectly suggest that zero was actually measured.

The important lesson is:

```text
default is a domain decision, not merely an error-suppression trick
```

You will make these decisions more deliberately after learning program flow and `None` handling in later phases.

---

## 6. Comparable values are required

`min()` and `max()` compare items.

Compatible numeric values can usually participate together:

```python
print(min(4, 2.5, 9))
print(max(4, 2.5, 9))
```

```text
2.5
9
```

But unrelated types may not have an ordering relationship:

```python
min(4, "2")
```

```text
TypeError: '<' not supported between instances of 'str' and 'int'
```

Do not convert values merely to silence the error. First decide what the data is supposed to mean.

---

## 7. `sum()` accumulates numeric values

`sum()` receives an iterable and adds its items from left to right conceptually, returning the total.

```python
values = [10, 20, 5]
print(sum(values))
```

```text
35
```

An empty iterable has a well-defined sum because the default starting value is zero:

```python
print(sum([]))
```

```text
0
```

This behavior differs from `min()` and `max()`, where an empty input has no natural smallest or largest item.

---

## 8. `sum()` has a `start` argument

The second argument to `sum()` provides the starting value.

```python
values = [10, 20, 5]
print(sum(values, 100))
```

```text
135
```

A useful mental model is:

```text
total = start + all iterable items
```

The default is equivalent to:

```python
sum(values, 0)
```

### `start` is not an index

A common beginner misunderstanding is to read the second argument as "start summing from this position".

It does not mean that.

```python
values = [10, 20, 5]
print(sum(values, 2))
```

```text
37
```

The `2` is added to the total. It does not tell Python to skip the first two items.

---

## 9. Do not use `sum()` to concatenate strings

This is not supported:

```python
sum(["Py", "thon"])
```

It raises `TypeError`.

For strings, the standard pattern is `join()`, which you learned earlier in this phase:

```python
parts = ["Py", "thon"]
print("".join(parts))
```

```text
Python
```

The functions communicate different intentions:

```text
sum()  -> numeric accumulation
join() -> string concatenation from an iterable
```

Keeping those responsibilities separate produces clearer code.

---

## 10. Floating-point totals can still be approximate

The previous chapter explained that many decimal fractions cannot be represented exactly as binary floating-point values.

`sum()` does not turn `float` arithmetic into exact decimal arithmetic.

```python
values = [0.1, 0.2]
print(sum(values))
```

```text
0.30000000000000004
```

This is a floating-point representation issue, not a failure of `sum()`.

Python's standard library contains tools for cases that need different numeric guarantees. For example, `math.fsum()` is designed for more accurate floating-point summation, while decimal arithmetic is useful when decimal semantics are required.

Those tools belong to later parts of the roadmap. The important idea now is to avoid assuming that aggregation removes floating-point approximation.

---

## 11. `round()` returns a rounded numeric value

With only one argument, `round()` returns the nearest integer for built-in numeric types such as `float`.

```python
print(round(3.2))
print(round(3.8))
```

```text
3
4
```

When `ndigits` is omitted or `None`, the built-in `int` and `float` cases covered here return an `int`:

```python
result = round(3.8)
print(type(result))
```

```text
<class 'int'>
```

---

## 12. `ndigits` controls the rounding position

A second argument controls the requested precision.

```python
print(round(3.14159, 2))
print(round(3.14159, 4))
```

```text
3.14
3.1416
```

For built-in numbers, providing `ndigits` changes an important type detail:

```python
print(round(2.5))
print(type(round(2.5)))
print(round(2.5, 0))
print(type(round(2.5, 0)))
```

```text
2
<class 'int'>
2.0
<class 'float'>
```

Without `ndigits`, the demonstrated `float` result is an integer. In the `int` and `float` cases covered here, providing `ndigits` keeps an `int` result as `int` and a `float` result as `float`; this is not a rule for every built-in numeric type.

---

## 13. `ndigits` may be zero or negative

Zero requests rounding to the units position. For the built-in types used in this chapter, an `int` remains an `int` and a `float` remains a `float` when `ndigits` is explicitly provided:

```python
print(round(12.7, 0))
```

```text
13.0
```

Negative values round to positions left of the decimal point:

```python
print(round(1234, -1))
print(round(1234, -2))
print(round(1234, -3))
```

```text
1230
1200
1000
```

A useful positional picture is:

```text
ndigits =  2 -> hundredths
ndigits =  1 -> tenths
ndigits =  0 -> units
ndigits = -1 -> tens
ndigits = -2 -> hundreds
```

Negative `ndigits` is especially useful when values need to be grouped or presented at a coarser scale.

---

## 14. Python does not use "5 always rounds up"

For built-in numeric types, when two candidate multiples are equally close, Python chooses the even one.

Observe:

```python
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))
```

```text
2
4
4
6
```

The result is not based on always moving upward.

The nearest even choices are selected:

```text
2.5 -> 2
3.5 -> 4
4.5 -> 4
5.5 -> 6
```

The same idea appears with negative values:

```python
print(round(-0.5))
print(round(-1.5))
print(round(-2.5))
```

```text
0
-2
-2
```

This rule is often called rounding ties to even.

---

## 15. Tie-to-even also matters with negative `ndigits`

Integers provide a clean way to observe the rule because the values are exact.

```python
print(round(125, -1))
print(round(135, -1))
```

```text
120
140
```

`125` is equally distant from `120` and `130`, so the even tens choice is `120`.

`135` is equally distant from `130` and `140`, so the even tens choice is `140`.

This example avoids mixing the tie-breaking rule with floating-point representation concerns.

---

## 16. `round()` and floating-point representation are separate ideas

A famous example is:

```python
print(round(2.675, 2))
```

```text
2.67
```

Someone expecting ordinary decimal arithmetic may predict `2.68`.

The surprising result comes from how the decimal literal `2.675` is represented as a binary `float`. The stored value is an approximation, and `round()` operates on that actual stored value.

This is not a Python bug.

A practical mental model is:

```text
source decimal text
        ↓
nearest representable binary float
        ↓
round() operates on that stored value
```

The previous chapter introduced this representation issue. Here you are seeing one of its consequences.

---

## 17. `round()` does not make floating-point arithmetic exact

Consider:

```python
print(0.1 + 0.1 + 0.1 == 0.3)
```

```text
False
```

Pre-rounding the individual values does not magically change their underlying representation into exact decimal fractions.

```python
print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))
```

```text
False
```

Use `round()` when a rounded value is what your program actually needs. Do not use it as a universal repair tool for floating-point arithmetic.

Later, you will encounter tools such as `math.isclose()` for approximate comparisons and decimal arithmetic for decimal-based requirements.

---

## 18. Rounding a value and formatting a display are different goals

Suppose you want to display two decimal places.

`round()` changes the numeric result:

```python
value = 3.1
rounded = round(value, 2)
print(rounded)
```

```text
3.1
```

It does not promise that printing the result will show trailing zeros such as `3.10`.

That is a formatting concern rather than a numeric rounding concern.

String formatting is introduced elsewhere in the learning path. Keep the distinction in mind:

```text
rounding   -> numeric value
formatting -> textual presentation
```

---

## 19. Combining the five built-ins

These functions become especially useful together.

```python
values = [12, -4, 7.5, 3]

print(abs(-12))
print(min(values))
print(max(values))
print(sum(values))
print(round(sum(values), 1))
```

```text
12
-4
12
18.5
18.5
```

The code reads almost like a short report:

```text
magnitude
minimum
maximum
total
rounded total
```

That readability is one reason built-in functions are preferable to unnecessary manual loops or repeated comparisons.

---

## 20. A preview of iterables without learning collections early

`min()`, `max()`, and `sum()` frequently receive iterables.

This chapter uses list literals such as:

```python
values = [10, 20, 30]
```

You do not need to master lists yet.

For now, treat the list as a simple ordered container of values that can be passed to a function.

Phase 3 will teach lists, tuples, sets, dictionaries, indexing behavior for collections, mutability, iteration, and common collection operations in their proper context.

This small preview exists because `sum()` would be difficult to teach meaningfully without any grouped values at all.

---

## 21. Common mistake: manually recreating `abs()`

A beginner may write logic conceptually equivalent to:

```python
value = -8

if value < 0:
    magnitude = -value
else:
    magnitude = value
```

That may be useful while learning conditionals later, but if the real intention is simply absolute value, this is clearer:

```python
magnitude = abs(value)
```

Use standard tools when they express the requirement directly.

---

## 22. Common mistake: calling `min()` or `max()` on an empty iterable

This fails:

```python
values = []
minimum = min(values)
```

Before choosing a solution, ask what an empty collection means in the program.

Possible designs later may include:

- using a meaningful `default=` value;
- checking whether data exists before calling the function;
- treating empty input as invalid data;
- representing missing data explicitly.

Do not choose a fallback only because it prevents an exception.

---

## 23. Common mistake: confusing `sum(..., start)` with slicing

This:

```python
sum([10, 20, 30], 5)
```

means:

```text
5 + 10 + 20 + 30
```

It does not mean:

```text
start at index 5
```

The result is:

```text
65
```

The parameter name `start` refers to the starting total.

---

## 24. Common mistake: using `sum()` for strings

Do not write:

```python
sum(["A", "B", "C"])
```

Use the string operation designed for that purpose:

```python
print("".join(["A", "B", "C"]))
```

```text
ABC
```

This is a useful example of choosing an operation based on data semantics, not merely on the idea that both tasks appear to "combine" values.

---

## 25. Common mistake: assuming `round()` always rounds halves upward

This expectation is wrong in Python's built-in numeric rounding:

```text
2.5 -> expected by some beginners: 3
```

Actual result:

```python
print(round(2.5))
```

```text
2
```

Remember the tie-to-even rule for equally close candidates.

---

## 26. Common mistake: using `round()` to hide every float surprise

If a calculation depends on exact decimal semantics, repeatedly applying `round()` at arbitrary intermediate steps may create a new problem rather than solve the original one.

The right tool depends on the domain.

Examples of later considerations include:

```text
approximate scientific comparison -> math.isclose()
more accurate float summation      -> math.fsum()
decimal arithmetic requirements    -> decimal.Decimal
textual decimal display             -> formatting
```

These are roadmap connections, not requirements for this beginner chapter.

---

## 27. Common mistake: forgetting that functions return values

This code prints a result but does not save it:

```python
round(9.876, 2)
```

In a script, nothing visible happens unless you use the returned value.

You can print it:

```python
print(round(9.876, 2))
```

Or assign it:

```python
rounded_value = round(9.876, 2)
```

The same principle applies to all five built-ins in this chapter.

---

## 28. Connections to earlier chapters

### Variables

Returned values can be assigned to names:

```python
maximum_value = max(4, 8, 2)
```

### Types

These functions operate on values whose types matter.

```python
print(type(round(2.5)))
print(type(round(2.5, 0)))
```

```text
<class 'int'>
<class 'float'>
```

### Type conversion

Do not confuse rounding with conversion.

```python
print(int(3.9))
print(round(3.9))
```

```text
3
4
```

`int()` converts by truncating toward zero for a finite float. `round()` performs rounding according to its rules.

### Floating-point behavior

The previous chapter's explanation of binary approximation is essential for understanding cases such as `round(2.675, 2)`.

### String methods

`sum()` is numeric aggregation; `join()` is the appropriate string-combination tool.

These connections are exactly why the guide teaches concepts as a sequence rather than as isolated syntax cards.

---

## 29. Practical exercise: numeric report

Create a file named `numeric_report.py`.

Start with:

```python
measurements = [12.5, -3.2, 8.75, 4.0]
```

Produce these results using the built-ins from this chapter:

1. the smallest measurement;
2. the largest measurement;
3. the total;
4. the absolute value of the smallest measurement;
5. the total rounded to one decimal place;
6. the range width, calculated as maximum minus minimum.

Your output should have this shape:

```text
Minimum: -3.2
Maximum: 12.5
Total: 22.05
Minimum magnitude: 3.2
Rounded total: 22.1
Range width: 15.7
```

Do not manually sort or compare the values one by one.

### Stretch exercise

Add:

```python
empty_measurements = []
```

Use `min()` and `max()` with an explicit `default=` and explain in a comment why the chosen default would or would not make semantic sense in a real measurement system.

The important part is the reasoning, not merely avoiding `ValueError`.

---

## 30. Self-check

Try answering these without running Python first.

1. What does `abs(-9)` return?
2. Does `abs()` modify the original variable?
3. What happens when `min([])` is called without `default=`?
4. What does `sum([], 10)` return?
5. What does the second argument of `sum()` mean?
6. Why should strings normally use `join()` instead of `sum()`?
7. What does `round(2.5)` return?
8. Why can `round(2.675, 2)` produce `2.67`?
9. What does `round(1234, -2)` do?
10. What is the type difference between `round(2.5)` and `round(2.5, 0)`?
11. Why can `min()` and `max()` compare `int` and `float` values but reject an `int` and an unrelated `str`?
12. Does `round()` make all floating-point calculations exact?

### Suggested answers

1. `9`.
2. No. It returns a result value.
3. `ValueError` is raised.
4. `10`.
5. It is the starting total that is added to the iterable's items.
6. `sum()` is for numeric accumulation, while `join()` is designed for combining strings.
7. `2`, because an exact tie is resolved toward the even candidate.
8. Because the stored binary `float` is an approximation of the decimal literal.
9. It rounds to the hundreds position, producing `1200`.
10. The first is `int`; with explicit `ndigits`, the built-in float result remains `float`.
11. Numeric types have compatible ordering semantics, while unrelated types may not define an ordering relationship.
12. No.

---

## 31. Quick reference

| Goal | Tool | Example | Result |
|---|---|---|---|
| Absolute magnitude | `abs()` | `abs(-8)` | `8` |
| Smallest argument | `min()` | `min(8, 2, 5)` | `2` |
| Largest argument | `max()` | `max(8, 2, 5)` | `8` |
| Smallest iterable item | `min()` | `min([8, 2, 5])` | `2` |
| Largest iterable item | `max()` | `max([8, 2, 5])` | `8` |
| Empty iterable fallback | `min()` | `min([], default=0)` | `0` |
| Numeric total | `sum()` | `sum([8, 2, 5])` | `15` |
| Total with starting value | `sum()` | `sum([8, 2, 5], 10)` | `25` |
| Nearest integer | `round()` | `round(3.6)` | `4` |
| Decimal-place rounding | `round()` | `round(3.14159, 2)` | `3.14` |
| Tens rounding | `round()` | `round(125, -1)` | `120` |

---

## 32. Repository examples

Run the deterministic examples from the repository root:

```bash
python strings-and-numbers/04-numeric-builtins/examples/numeric_summary.py
python strings-and-numbers/04-numeric-builtins/examples/rounding_behavior.py
```

Expected output for `numeric_summary.py`:

```text
Absolute: 12
Minimum: -4
Maximum: 12
Total: 18.5
Total with start: 28.5
```

Expected output for `rounding_behavior.py`:

```text
2.5: 2
3.5: 4
125 to tens: 120
135 to tens: 140
2.675 to two decimals: 2.67
Type without ndigits: <class 'int'>
Type with ndigits: <class 'float'>
```

---

## 33. Phase 2 complete

With this chapter, Phase 2 has covered:

```text
string creation and indexing
        ↓
common string methods
        ↓
int, float, and bool behavior
        ↓
common numeric built-ins
```

You now have a stronger foundation for working with individual text and numeric values.

The next curriculum phase introduces **Collections**, where multiple values become first-class structures in your programs. Lists, tuples, sets, and dictionaries will make many patterns previewed in this phase much more powerful.

Before moving forward, the repository may perform a cross-chapter audit to verify that Phase 2 reads cleanly as one continuous learning path.

---

## Official references

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [`abs()`](https://docs.python.org/3/library/functions.html#abs)
- [`max()`](https://docs.python.org/3/library/functions.html#max)
- [`min()`](https://docs.python.org/3/library/functions.html#min)
- [`round()`](https://docs.python.org/3/library/functions.html#round)
- [`sum()`](https://docs.python.org/3/library/functions.html#sum)
- [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)

---

## Next step

Phase 2 is complete. Continue with the [main roadmap](../../docs/roadmap.en.md) to review the completed phase and see **Phase 3: Collections**, which is planned next.

<div align="center">

# Return Values

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous: Parameters and Arguments](../02-parameters-and-arguments/README.md)

Chapter 01 named behavior. Chapter 02 let callers send values into that behavior. This chapter completes the first data round trip:

```text
caller → arguments → function → return value → caller
```

**Estimated study time:** 75–100 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- write `return expression`;
- explain that `return` ends the current function call;
- store and reuse returned values;
- distinguish `print()` from `return`;
- use returned values in expressions and conditions;
- return ordinary Python values, tuples, and `None`;
- use different return statements on different branches;
- distinguish `return` from `break`;
- trace input, transformation, return, and caller-side use.

## 1. Send a value back with `return`

```python
def double(number):
    return number * 2


result = double(6)
print(result)
```

Output:

```text
12
```

Trace:

```text
6 binds to number
→ number * 2 becomes 12
→ return sends 12 back
→ double(6) becomes 12
→ result receives 12
```

A function does not assign directly to a caller variable. It returns a value, and the caller decides what happens next.

## 2. A value-returning call is an expression

```python
def square(number):
    return number * number


answer = square(5)
print(answer)
```

Output:

```text
25
```

Think:

```text
square(5) → 25
```

Because the call produces a value, it can participate in another expression:

```python
def double(number):
    return number * 2


final_score = double(7) + 3
print(final_score)
```

Output:

```text
17
```

## 3. `print()` and `return` are different

```python
def show_total(price, quantity):
    print(price * quantity)


def calculate_total(price, quantity):
    return price * quantity
```

The first function displays a value. The second sends a value to its caller.

```text
print(...) → display something
return ... → send a value to the caller
```

A calculation is usually more reusable when the function returns the result and the caller chooses whether to print, compare, store, or combine it.

## 4. Store or use a returned value directly

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(8, 3)
print(total)
print(calculate_total(5, 4))
```

Output:

```text
24
20
```

A well-named intermediate variable is often easier to trace while learning or debugging.

## 5. Functions can return ordinary Python values

```python
def get_status():
    return "ready"


def is_passing(score):
    return score >= 60


def get_topics():
    return ["strings", "loops", "functions"]
```

A return value can be a string, number, Boolean, collection, tuple, `None`, or another ordinary Python value.

## 6. Returned Booleans work with conditions

```python
def is_passing(score):
    return score >= 60


if is_passing(75):
    print("Passed")
```

Output:

```text
Passed
```

`is_passing(75)` evaluates to `True`, so the Boolean and `if` rules learned earlier still apply.

## 7. `return` ends the current function call

```python
def get_message():
    return "Ready"
    print("This line never runs")
```

When `return` runs:

```text
evaluate expression
→ obtain value
→ leave function
→ continue at caller
```

Necessary work should not appear after an unconditional `return` in the same path.

## 8. Different branches can return different values

```python
def classify_score(score):
    if score >= 90:
        return "excellent"

    if score >= 60:
        return "passing"

    return "needs review"
```

Calls:

```python
print(classify_score(95))
print(classify_score(72))
print(classify_score(40))
```

Output:

```text
excellent
passing
needs review
```

Only one return statement runs per call. Once one runs, the current call is finished.

## 9. Early returns can simplify a special case

```python
def describe_quantity(quantity):
    if quantity <= 0:
        return "invalid quantity"

    return "quantity accepted"
```

The special case exits first, leaving the normal path easy to read. Use early returns when they improve clarity.

## 10. `return` inside a loop exits the whole function

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None
```

```python
print(find_first_even([3, 7, 8, 10]))
```

Output:

```text
8
```

`return number` exits the function, not only the loop.

## 11. `return` and `break` leave different boundaries

```text
break  → leave the current loop
return → leave the current function call
```

`break` can continue with later statements in the same function. `return` transfers control back to the caller.

## 12. Reaching the end returns `None`

```python
def show_ready():
    print("Ready")


result = show_ready()
print(result)
```

Output:

```text
Ready
None
```

If execution reaches the end without an explicit `return`, the call result is `None`.

## 13. Bare `return` and `return None`

```python
def show_if_nonnegative(number):
    if number < 0:
        return

    print(number)
```

Bare `return` exits immediately and produces `None`.

These can all produce `None`:

```text
reach end of function → None
bare return           → None
return None           → None
```

An explicit `return None` can communicate intent:

```python
def find_positive(numbers):
    for number in numbers:
        if number > 0:
            return number

    return None
```

Here `None` means that no positive value was found.

## 14. `None` and `False` are different values

```python
def is_empty(items):
    return len(items) == 0
```

This function returns a Boolean. A search function may return `None` to mean “not found.”

Both values are falsy in Boolean contexts, but they do not mean the same thing. When the distinction matters, test deliberately.

## 15. The return expression is evaluated first

```python
def calculate_area(width, height):
    return width * height
```

For `calculate_area(4, 6)`:

```text
evaluate width * height
→ obtain 24
→ return 24
→ leave function
```

The resulting value becomes the value of the call expression.

## 16. Returning a collection

```python
def get_even_numbers(numbers):
    evens = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)

    return evens
```

```python
result = get_even_numbers([1, 2, 3, 4, 5, 6])
print(result)
```

Output:

```text
[2, 4, 6]
```

Detailed object ownership and mutation design come later.

## 17. Comma-separated return expressions produce a tuple

```python
def get_dimensions():
    return 1920, 1080


dimensions = get_dimensions()
print(dimensions)
```

Output:

```text
(1920, 1080)
```

The function returns one tuple. Because tuple unpacking is already familiar:

```python
width, height = get_dimensions()

print(width)
print(height)
```

Output:

```text
1920
1080
```

It is one returned tuple, not two independent return values.

## 18. Common mistake: printing instead of returning

```python
def calculate_total(price, quantity):
    print(price * quantity)


total = calculate_total(8, 3)
print(total)
```

Output:

```text
24
None
```

The function displayed `24`, but the call result is `None`.

Fix:

```python
def calculate_total(price, quantity):
    return price * quantity
```

## 19. Common mistake: returning too early in a loop

Incorrect for counting every even number:

```python
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

        return count
```

The function exits on the first iteration.

Correct:

```python
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count
```

Indentation changes when the function exits.

## 20. Common mistake: an accidental implicit `None`

```python
def get_level(score):
    if score >= 90:
        return "high"

    if score >= 60:
        return "medium"
```

Scores below `60` implicitly return `None`.

If every score should have a category:

```python
def get_level(score):
    if score >= 90:
        return "high"

    if score >= 60:
        return "medium"

    return "low"
```

Design the possible results deliberately.

## 21. Trace the complete round trip

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(12, 4)
```

```text
caller has 12 and 4
↓
arguments bind to price and quantity
↓
function evaluates price * quantity
↓
result is 48
↓
return sends 48 back
↓
call expression becomes 48
↓
total receives 48
```

This is the main mental model of the chapter.

## 22. Executable examples

### Calculate a total

File: [`examples/calculate_total.py`](examples/calculate_total.py)

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(12, 4)

print(total)
print(total + 5)
```

Expected output:

```text
48
53
```

### Return by branch

File: [`examples/classify_score.py`](examples/classify_score.py)

```python
def classify_score(score):
    if score >= 90:
        return "excellent"

    if score >= 60:
        return "passing"

    return "needs review"


print(classify_score(95))
print(classify_score(72))
print(classify_score(40))
```

Expected output:

```text
excellent
passing
needs review
```

### Search with `None`

File: [`examples/find_first_even.py`](examples/find_first_even.py)

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


print(find_first_even([3, 7, 8, 10]))
print(find_first_even([1, 3, 5]))
```

Expected output:

```text
8
None
```

## 23. Exercise: temperature category

Create `classify_temperature(temperature)`.

Requirements:

1. return `"hot"` for values at least `30`;
2. return `"mild"` for values at least `18` but below `30`;
3. return `"cold"` otherwise;
4. call it with `34`, `22`, and `10`;
5. store each result before printing it.

Expected output:

```text
hot
mild
cold
```

Do not use type hints, defaults, `*args`, or `**kwargs`.

## 24. Review checklist

Before continuing, confirm that you can:

- [ ] write `return expression`;
- [ ] explain that the expression is evaluated before leaving the function;
- [ ] store and reuse returned values;
- [ ] use a returned Boolean in `if`;
- [ ] distinguish `print()` from `return`;
- [ ] use different returns on different branches;
- [ ] distinguish `return` from `break`;
- [ ] explain implicit `None`, bare `return`, and `return None`;
- [ ] explain that `return a, b` returns one tuple;
- [ ] recognize a return placed too early in a loop;
- [ ] trace values from arguments back to the caller.

## 25. Quick reference

| Need | Form | Meaning |
|---|---|---|
| return value | `return expression` | evaluate, leave function, send value to caller |
| store result | `result = function()` | bind returned value in caller |
| use result | `print(function())` | use returned value in another call |
| return Boolean | `return condition` | caller receives `True` or `False` |
| return `None` | `return` / `return None` | leave function with `None` |
| implicit `None` | reach end | call result is `None` |
| return tuple | `return a, b` | return one tuple |
| stop loop | `break` | leave current loop |
| stop function | `return value` | leave current function call |

## 26. Scope boundary

This chapter intentionally defers:

- local/global scope rules;
- type hints and return annotations;
- default values;
- `*args` and `**kwargs`;
- positional-only and keyword-only syntax;
- argument unpacking;
- nested functions and lambdas;
- decorators, generators, `yield`, and recursion;
- exception handling;
- advanced ownership and mutation design.

## 27. What comes next

You can now trace:

```text
caller → arguments → parameters → function body → return value → caller
```

The next question is:

> Where do names inside and outside a function exist, and when are they visible?

That leads to **Chapter 04: Scope**.

Return to the [Functions learning path](../README.md) or the [full learning path](../../docs/learning-path.en.md).

## References

Primary Python documentation:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Language Reference: The `return` statement](https://docs.python.org/3.13/reference/simple_stmts.html#the-return-statement)

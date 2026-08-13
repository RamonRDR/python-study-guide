<div align="center">

# Parameters and Arguments

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous: Defining and Calling Functions](../01-defining-and-calling-functions/README.md)

Chapter 01 gave behavior a name. Chapter 02 makes that behavior **work with different input values**.

The central distinction is:

```text
parameter = name in the function definition
argument  = value supplied by a function call
```

This chapter focuses on required parameters and ordinary calls. Return values, default values, type hints, `*args`, `**kwargs`, and detailed scope rules come later.

**Estimated study time:** 90–120 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- distinguish a parameter from an argument;
- define a function with one or more required parameters;
- call the same function with different arguments;
- pass literals, variables, expressions, and collections as arguments;
- explain how positional arguments bind by position;
- use basic keyword arguments;
- mix positional and keyword arguments in a valid order;
- choose meaningful parameter names;
- use parameters with familiar `if`, `for`, and `range()` logic;
- recognize missing, extra, duplicate, and unexpected arguments as call errors;
- trace input data from the caller into the function body.

## 1. From fixed behavior to configurable behavior

A function with no parameters repeats fixed behavior:

```python
def greet():
    print("Hello, Maya!")


greet()
greet()
```

Every call prints the same name.

A parameter creates a place for the caller to provide data:

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Maya")
greet("Leo")
```

Now the behavior stays the same while the input changes.

## 2. Parameter versus argument

In the definition:

```python
def greet(name):
    print(f"Hello, {name}!")
```

`name` is a **parameter**.

In the call:

```python
greet("Maya")
```

`"Maya"` is an **argument**.

Keep this mental model:

```text
definition → parameter
call       → argument
```

## 3. A required parameter needs an argument

```python
def show_city(city):
    print(f"City: {city}")


show_city("Recife")
```

The call supplies one argument for one required parameter.

Calling `show_city()` without an argument raises `TypeError` because the required input was not supplied.

## 4. The parameter list is inside the parentheses

Chapter 01 used an empty parameter list:

```python
def show_status():
    print("Ready")
```

Chapter 02 puts names inside it:

```python
def show_status(status):
    print(status)
```

Think:

```text
()             → no parameters
(status)       → one parameter
(title, year)  → two parameters
```

## 5. One definition can receive many values

```python
def show_language(language):
    print(f"Studying: {language}")


show_language("Python")
show_language("JavaScript")
show_language("SQL")
```

Output:

```text
Studying: Python
Studying: JavaScript
Studying: SQL
```

The function is defined once. Each call supplies a new argument.

## 6. Arguments can be literals

```python
def show_quantity(quantity):
    print(f"Quantity: {quantity}")


show_quantity(3)
```

Here `3` is the argument supplied to `quantity`.

## 7. Arguments can come from variables

```python
def show_quantity(quantity):
    print(f"Quantity: {quantity}")


items_in_cart = 4
show_quantity(items_in_cart)
```

The caller variable and the parameter do not need the same name.

```text
items_in_cart → name in caller code
quantity      → parameter name in function
```

## 8. Arguments can be expressions

Python evaluates an argument expression before the body uses the resulting value.

```python
def show_total(total):
    print(f"Total: {total}")


price = 12
quantity = 3
show_total(price * quantity)
```

Output:

```text
Total: 36
```

The function receives the result of `price * quantity`.

## 9. Multiple parameters create multiple inputs

Separate parameters with commas:

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book("Python Basics", 2026)
```

The definition has two parameters, and the call supplies two arguments.

## 10. Positional arguments bind by position

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")


show_route("Home", "Library")
```

Binding:

```text
origin      ← "Home"
destination ← "Library"
```

The first positional argument goes to the first compatible parameter, the second goes to the second, and so on.

## 11. Positional order can change meaning

```python
show_route("Library", "Home")
```

That call is valid, but now the route points in the opposite direction.

Python follows the position. It does not guess your intended meaning.

## 12. Basic keyword arguments name the target parameter

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book(title="Python Basics", year=2026)
```

Keyword arguments make the target parameter explicit.

For ordinary parameters, their order can also be changed when every argument is named:

```python
show_book(year=2026, title="Python Basics")
```

## 13. Positional and keyword calls can represent the same input

These calls bind the same values:

```python
show_book("Python Basics", 2026)
show_book(title="Python Basics", year=2026)
show_book("Python Basics", year=2026)
```

The third form mixes styles: positional first, keyword second.

Use the form that makes the call easiest to read.

## 14. Positional arguments come before keyword arguments

Valid:

```python
show_book("Python Basics", year=2026)
```

Invalid syntax:

```python
show_book(title="Python Basics", 2026)
```

Once a keyword argument appears, an ordinary positional argument cannot follow it in that call.

## 15. Do not supply the same parameter twice

```python
show_book("Python Basics", title="Another Title")
```

The positional argument already binds `title`, and the keyword argument tries to bind it again.

Python raises `TypeError`.

## 16. Parameter names are part of the interface

Compare:

```python
def show_route(a, b):
    print(f"{a} -> {b}")
```

with:

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")
```

The second definition communicates the role of each input more clearly.

Good parameter names describe meaning, not merely data type.

## 17. A parameter can be used more than once

```python
def show_name_box(name):
    print("---")
    print(name)
    print(name)
    print("---")


show_name_box("Maya")
```

This uses one parameter twice. It does not create two parameters.

## 18. Parameters work with `if`

```python
def show_score_status(name, score):
    if score >= 70:
        print(f"{name}: ready")
    else:
        print(f"{name}: review")


show_score_status("Ana", 82)
show_score_status("Luis", 61)
```

Output:

```text
Ana: ready
Luis: review
```

`if` keeps its normal meaning. The condition simply uses values supplied by the caller.

## 19. Parameters work with loops

```python
def repeat_message(message, times):
    for repetition in range(times):
        print(message)


repeat_message("Practice", 3)
```

Output:

```text
Practice
Practice
Practice
```

The loop owns repetition. The parameters make the behavior configurable.

## 20. Collections can be arguments

```python
def show_topics(topics):
    for topic in topics:
        print(topic)


study_topics = ["functions", "parameters", "arguments"]
show_topics(study_topics)
```

Output:

```text
functions
parameters
arguments
```

This chapter only reads the collection. Mutation and deeper object-sharing behavior are intentionally deferred.

## 21. Trace the input flow

```python
def greet(name):
    print(f"Hello, {name}!")


person = "Maya"
greet(person)
```

Trace:

```text
"Maya"
  ↓
person
  ↓
argument in greet(person)
  ↓
parameter name
  ↓
function body
```

The names can differ. Trace the value.

## 22. The call must satisfy required parameters

This function requires two inputs:

```python
def show_book(title, year):
    print(f"{title} ({year})")
```

Too few:

```python
show_book("Python Basics")
```

Too many:

```python
show_book("Python Basics", 2026, "Beginner")
```

Both calls raise `TypeError`.

Later chapters will introduce optional and flexible inputs.

## 23. Keyword names must match parameters

Valid:

```python
show_book(title="Python Basics", year=2026)
```

Unexpected keyword:

```python
show_book(name="Python Basics", year=2026)
```

The function has no parameter named `name`, so Python raises `TypeError`.

## 24. Parameters and outside variable names are different roles

```python
def show_city(city):
    print(city)


home_city = "Curitiba"
show_city(home_city)
```

`home_city` belongs to caller code. `city` is the function parameter.

Detailed local-versus-global rules belong to Chapter 04: Scope.

## 25. Common mistakes

### Missing a required argument

```python
def greet(name):
    print(f"Hello, {name}!")


greet()
```

### Supplying too many arguments

```python
greet("Maya", "Leo")
```

### Swapping positional meaning

```python
show_route("Library", "Home")
```

### Binding the same parameter twice

```python
show_book("Python Basics", title="Another Title")
```

### Putting a positional argument after a keyword argument

```python
show_book(title="Python Basics", 2026)
```

### Using vague parameter names

Prefer:

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")
```

## 26. Executable example: one parameter, many calls

File: [`examples/greet_people.py`](examples/greet_people.py)

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Maya")
greet("Leo")
greet("Nina")
```

Expected output:

```text
Hello, Maya!
Hello, Leo!
Hello, Nina!
```

## 27. Executable example: positional and keyword arguments

File: [`examples/book_details.py`](examples/book_details.py)

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book("Python Basics", 2026)
show_book(year=2025, title="Study Notes")
```

Expected output:

```text
Python Basics (2026)
Study Notes (2025)
```

## 28. Executable example: parameters and program flow

File: [`examples/score_status.py`](examples/score_status.py)

```python
def show_score_status(name, score):
    if score >= 70:
        print(f"{name}: ready")
    else:
        print(f"{name}: review")


show_score_status("Ana", 82)
show_score_status("Luis", 61)
```

Expected output:

```text
Ana: ready
Luis: review
```

## 29. Exercise: configurable study card

Create `show_study_card` with two required parameters: `topic` and `minutes`.

Requirements:

1. define it with `def`;
2. use both parameters in the body;
3. print `Topic: ...` and `Minutes: ...`;
4. call it once with positional arguments for `"Python"` and `45`;
5. call it again with keyword arguments for `"SQL"` and `30`;
6. do not use default values;
7. do not use `return` yet.

Expected output:

```text
Topic: Python
Minutes: 45
Topic: SQL
Minutes: 30
```

## 30. Review questions

- Which name is the parameter in `def greet(name):`?
- Which value is the argument in `greet("Maya")`?
- Can one parameter receive different arguments in different calls?
- What determines positional binding?
- Why can keyword arguments improve readability?
- Can an ordinary positional argument follow a keyword argument?
- What happens when a required argument is missing?
- What happens when one parameter receives two attempted values?
- Do the caller variable name and parameter name need to match?
- Can a list be passed as an argument?

## 31. Review checklist

Before continuing, confirm that you can:

- [ ] explain parameter versus argument;
- [ ] define required parameters;
- [ ] call the same function with different values;
- [ ] pass literals, variables, expressions, and collections;
- [ ] bind positional arguments by order;
- [ ] write basic keyword arguments;
- [ ] mix positional then keyword arguments correctly;
- [ ] avoid duplicate parameter binding;
- [ ] choose meaningful parameter names;
- [ ] use parameters with `if` and loops;
- [ ] recognize missing, extra, duplicate, and unexpected arguments;
- [ ] trace input from caller to parameter to body.

## 32. Quick reference

| Need | Form | Meaning |
|---|---|---|
| one required input | `def greet(name):` | `name` is a parameter |
| supply input | `greet("Maya")` | `"Maya"` is an argument |
| multiple inputs | `def show_book(title, year):` | two parameters |
| positional call | `show_book("Python", 2026)` | bind by position |
| keyword call | `show_book(title="Python", year=2026)` | bind by parameter name |
| mixed valid call | `show_book("Python", year=2026)` | positional first, then keyword |
| missing required input | too few arguments | `TypeError` |
| extra input | too many arguments | `TypeError` |
| unknown keyword | no matching parameter | `TypeError` |
| duplicate binding | same parameter twice | `TypeError` |

## 33. Scope boundary

This chapter intentionally does not teach in depth:

- `return` and return-value design;
- local and global scope rules;
- type hints and annotations;
- default parameter values;
- mutable default pitfalls;
- `*args` and `**kwargs`;
- positional-only `/` parameters;
- keyword-only `*` parameters;
- argument unpacking with `*` or `**`;
- mutation and object-sharing semantics;
- nested functions, lambdas, decorators, generators, or recursion.

The goal here is a reliable model of **required inputs and ordinary calls**.

## 34. What comes next

You can now give a function required input values and map ordinary call arguments to parameters.

The next question is:

> How can a function send a useful result back to the caller?

That leads to **Chapter 03: Return Values**.

Return to the [Functions learning path](../README.md) or the [full learning path](../../docs/learning-path.en.md).

## References

Primary Python documentation:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Tutorial: More on Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Python 3.13 Tutorial: Keyword Arguments](https://docs.python.org/3.13/tutorial/controlflow.html#keyword-arguments)
- [Python 3.13 Language Reference: Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13 Language Reference: Calls](https://docs.python.org/3.13/reference/expressions.html#calls)

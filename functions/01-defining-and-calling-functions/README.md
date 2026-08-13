<div align="center">

# Defining and Calling Functions

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous phase: Program Flow](../../program-flow/README.md)

Functions give a meaningful name to behavior that a program may need to execute more than once.

This chapter begins Phase 5 with one distinction:

```text
definition = describe and name behavior
call       = execute that behavior now
```

Parameters, arguments, return-value design, and scope come later.

**Estimated study time:** 75–100 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain why functions exist;
- define a simple function with `def`;
- identify the function name, empty parameter list, colon, and indented body;
- call a function after its definition has executed;
- explain that defining a function does not run its body;
- trace execution into and out of a function call;
- call the same function more than once;
- distinguish `name` from `name()`;
- use meaningful `snake_case` function names;
- use `pass` for an intentionally empty body;
- place familiar flow statements inside a function;
- recognize that a function without an explicit `return` produces `None`.

## 1. Why functions exist

A program can already store values, choose branches, and repeat work.

As programs grow, groups of statements start representing recognizable jobs:

```text
show a heading
show a menu
print a separator
display a status
```

A function lets the program give one of those jobs a name.

The first mental model is:

> **Functions name behavior.**

A good function can also reduce duplication and make the flow of a program easier to read.

## 2. Define first, call later

```python
def show_welcome():
    print("Welcome to Python functions.")


show_welcome()
```

The definition is:

```python
def show_welcome():
    print("Welcome to Python functions.")
```

The call is:

```python
show_welcome()
```

These are different operations.

## 3. Anatomy of `def`

```python
def show_welcome():
    print("Welcome to Python functions.")
```

| Part | Meaning |
|---|---|
| `def` | starts a function definition |
| `show_welcome` | function name |
| `()` | parameter list, empty in this chapter |
| `:` | starts the function suite |
| indented statement | function body |

This chapter keeps `()` empty on purpose. Chapter 02 will add parameters and arguments.

## 4. A definition does not run the body

When Python executes a `def` statement, it creates the function and binds it to the function name.

The body is prepared for later execution.

So this prints nothing:

```python
def show_welcome():
    print("Welcome")
```

The body runs only after a call:

```python
show_welcome()
```

Think:

```text
def       → prepare behavior
name()    → execute behavior
```

## 5. A call redirects execution temporarily

```python
def show_step():
    print("Inside function")


print("Before call")
show_step()
print("After call")
```

Output:

```text
Before call
Inside function
After call
```

Trace:

1. Python defines `show_step`.
2. Top-level execution prints `Before call`.
3. `show_step()` calls the function.
4. Execution enters the body.
5. The body prints `Inside function`.
6. The body finishes.
7. Execution continues after the call.
8. Python prints `After call`.

The caller does not disappear. Execution returns to the point after the call.

## 6. One definition, many calls

```python
def show_separator():
    print("---")


print("Start")
show_separator()
print("Study")
show_separator()
print("Finish")
```

Output:

```text
Start
---
Study
---
Finish
```

The function is defined once and called twice.

That is basic reuse:

```text
define once
call when needed
```

## 7. Reuse is more than copy and paste

Repeated code may work, but a function adds meaning.

Compare the idea:

```text
print("---")
```

with:

```text
show_separator()
```

The second form explains *why* the line exists.

When the behavior changes, one function definition can update every call site that uses it.

## 8. Function names should describe actions

Prefer names such as:

```text
show_status
print_summary
validate_choice
calculate_total
```

Normal Python function names use `snake_case`.

Avoid names such as:

```text
x
thing
func1
do_it
```

unless the surrounding context truly makes them clear.

A call should read like a meaningful action.

## 9. `name` and `name()` are different

```python
def show_message():
    print("Hello")


print(show_message)
show_message()
```

`show_message` refers to the function object.

`show_message()` calls the function.

You do not need advanced knowledge of function objects yet. Keep this rule:

```text
name   → reference
name() → call
```

## 10. Indentation defines the body

Valid:

```python
def show_message():
    print("Hello")
```

Invalid:

```python
def show_message():
print("Hello")
```

A function definition introduces an indented suite, just like other compound statements you already know.

The header also requires a colon:

```python
def show_message():
```

## 11. Program flow can live inside a function

```python
def show_even_numbers():
    for number in range(1, 6):
        if number % 2 == 0:
            print(number)


show_even_numbers()
```

Output:

```text
2
4
```

`for` and `if` keep their normal meaning.

The function simply gives that combined behavior a reusable name.

This connects the phases:

```text
program flow → controls what happens
functions    → name a unit of behavior
```

## 12. A body can contain several statements

```python
def show_study_plan():
    print("Read")
    print("Practice")
    print("Review")


show_study_plan()
```

Output:

```text
Read
Practice
Review
```

Every correctly indented statement belongs to the function body.

## 13. Definition order matters

At top level, this order fails:

```python
show_welcome()


def show_welcome():
    print("Welcome")
```

Python reaches the call before it has executed the definition that binds `show_welcome`.

Use:

```python
def show_welcome():
    print("Welcome")


show_welcome()
```

The precise rule is:

> The definition must have executed before the call happens.

Call order can still differ from definition order after the names exist.

## 14. `pass` can mark an intentionally empty body

```python
def planned_step():
    pass


planned_step()
```

`pass` is a valid statement that does nothing.

It is useful when a function body must exist structurally but its real behavior has not been written yet.

Do not add `pass` to a body that already contains real statements.

## 15. A function without explicit `return` produces `None`

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

This chapter does not teach return-value design yet.

For now, notice only that reaching the end of a function without an explicit `return` still completes the call, and the call result is `None`.

Chapter 03 will treat return values as a full topic.

## 16. Printing is not returning

This function:

```python
def show_ready():
    print("Ready")
```

displays output.

It does not explicitly send a useful value back to the caller.

Keep the concepts separate:

```text
print(...) → display something
return ... → send a result to the caller
```

The second idea comes later.

## 17. Functions should represent meaningful jobs

A function should usually answer:

```text
What job does this function perform?
```

For example:

```python
def show_menu():
    print("1. Study")
    print("2. Practice")
```

The responsibility is clear.

Do not create functions only because functions are the current lesson. Tiny wrappers with no meaningful purpose can make code harder to follow.

## 18. Calls and loops can work together

A loop can own repetition:

```python
def show_tick():
    print("Tick")


for repetition in range(3):
    show_tick()
```

Or the function can own repetition:

```python
def show_three_ticks():
    for repetition in range(3):
        print("Tick")


show_three_ticks()
```

Both print three ticks, but they assign responsibility differently.

The descriptive loop target keeps the iteration model familiar. Its value is not needed by these particular bodies; the loop only needs to repeat three times.

Later chapters will give the caller more control by introducing parameters.

## 19. Trace before debugging

When a function surprises you, write the execution path:

```text
define function
run top-level code
call function
enter body
run body
leave body
continue after call
```

This simple trace catches many beginner mistakes.

## 20. Common mistakes

### Defining but never calling

```python
def show_message():
    print("Hello")
```

No call means no body execution.

### Forgetting parentheses

```python
show_message
```

references the function. Use `show_message()` to call it.

### Calling before the definition executes

```python
show_message()


def show_message():
    print("Hello")
```

At top level, put the definition before the call.

### Breaking indentation

```python
def show_message():
print("Hello")
```

The body must be indented.

### Adding later concepts too soon

You may have seen:

```python
def greet(name):
    print(f"Hello, {name}")
```

That is useful, but now the function receives data.

First make this model reliable:

```text
define
call
trace
reuse
```

Then parameters are much easier.

## 21. Executable example: define and call

File: [`examples/define_and_call.py`](examples/define_and_call.py)

```python
def show_welcome():
    print("Welcome to Python functions.")


show_welcome()
```

Expected output:

```text
Welcome to Python functions.
```

## 22. Executable example: repeated calls

File: [`examples/repeated_calls.py`](examples/repeated_calls.py)

```python
def show_separator():
    print("---")


print("Start")
show_separator()
print("Study")
show_separator()
print("Finish")
```

Expected output:

```text
Start
---
Study
---
Finish
```

## 23. Executable example: execution order

File: [`examples/execution_order.py`](examples/execution_order.py)

```python
def show_step():
    print("Inside function")


print("Before call")
show_step()
print("After call")
```

Expected output:

```text
Before call
Inside function
After call
```

## 24. Exercise: reusable study banner

Create a function named `show_study_banner`.

Requirements:

1. define it with `def`;
2. keep the parameter list empty;
3. print exactly:

```text
==========
STUDY TIME
==========
```

4. print `Before`;
5. call the function;
6. print `After`;
7. call the same function again.

Expected output:

```text
Before
==========
STUDY TIME
==========
After
==========
STUDY TIME
==========
```

Do not use parameters or `return` yet.

## 25. Review questions

- Which lines define behavior?
- Which lines call behavior?
- How many times is the function defined?
- How many times is it called?
- Why does the body execute twice?
- What happens if both calls are removed?
- What changes if you write the function name without parentheses?
- Which statements are top-level?
- Which statements belong to the body?

## 26. Review checklist

Before continuing, confirm that you can:

- [ ] explain why functions exist;
- [ ] write `def name():`;
- [ ] indent the body;
- [ ] distinguish definition from call;
- [ ] call a function with `name()`;
- [ ] distinguish `name` from `name()`;
- [ ] trace execution into and out of a call;
- [ ] call the same function more than once;
- [ ] explain why definition execution order matters;
- [ ] choose a meaningful `snake_case` name;
- [ ] use `pass` for an intentionally empty body;
- [ ] place familiar flow tools inside a function;
- [ ] recognize implicit `None` when there is no explicit `return`.

## 27. Quick reference

| Need | Form | Meaning |
|---|---|---|
| define a function | `def name():` | create and bind a function |
| write its behavior | indented body | statements run by a call |
| call it | `name()` | execute the body |
| refer to it | `name` | access the function object |
| keep body empty temporarily | `pass` | valid no-operation statement |
| normal naming style | `snake_case` | readable function naming convention |
| no explicit `return` | end of body | call result is `None` |

## 28. Scope boundary

This chapter intentionally does not teach in depth:

- parameters and arguments;
- return-value design;
- local and global scope;
- type hints;
- default values;
- `*args` and `**kwargs`;
- nested functions;
- lambdas;
- decorators;
- generators;
- recursion.

Those ideas deserve separate mental models.

## 29. What comes next

You can now define behavior, call it, reuse it, and trace its execution.

The next question is:

> How can one function work with different input values?

That leads to **Chapter 02: Parameters and Arguments**.

Return to the [Functions learning path](../README.md) or the [full learning path](../../docs/learning-path.en.md).

## References

Primary Python documentation:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Language Reference: Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13 Language Reference: Calls](https://docs.python.org/3.13/reference/expressions.html#calls)

<div align="center">

# Scope

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Functions](../README.md) · [← Previous: Return Values](../03-return-values/README.md)

Chapter 01 named behavior. Chapter 02 moved data into a function. Chapter 03 sent results back to the caller. This chapter answers the next question:

> Where does each name exist, and where can Python find it?

The beginner mental model becomes:

```text
caller → arguments → function local scope → return value → caller
```

**Estimated study time:** 80–105 minutes.

## Learning objectives

By the end of this chapter, you should be able to:

- explain the beginner difference between a **scope** and a **namespace**;
- identify module-level global names and function-local names;
- explain that parameters are local names;
- explain that each function call gets its own local namespace;
- read a module-level name from inside a function;
- predict when assignment creates a local binding;
- recognize shadowing when the same spelling is bound in different scopes;
- explain that ordinary `if`, `for`, and `while` statements do not create a new function-local scope;
- recognize `NameError` and the common scope-related `UnboundLocalError`;
- explain what `global` changes and why parameter/return flow is often clearer;
- trace the beginner lookup path from local names toward global and built-in names.

## 1. Scope answers where a name is visible

A **scope** is a region of code where a name can be accessed directly.

```python
course = "Python"


def show_course():
    message = "Studying"
    print(course)
    print(message)


show_course()
print(course)
```

Output:

```text
Python
Studying
Python
```

`course` is bound at module level, so the function can read it. `message` is created inside the function and is local to that function call.

The spelling of a name is only one part of the story. **Where the name is bound matters.**

## 2. Namespace and scope are related, but different

A **namespace** maps names to objects. A **scope** describes where those names are directly visible.

```text
namespace → which names are bound to which objects
scope     → where those names are directly visible
```

For example:

```python
course = "Python"
chapter = 4

print(course)
print(chapter)
```

Output:

```text
Python
4
```

The module namespace contains bindings for `course` and `chapter`.

## 3. Module-level names are global to that module

A name bound at the top level of a Python file belongs to that module's global namespace.

```python
course = "Python"
chapter = 4

print(course)
print(chapter)
```

Both names are global names in this module.

In beginner code, “global” here means global to the current module, not magically shared with every Python program.

## 4. A function call creates a local namespace

When a function is called, Python creates a local namespace for that call.

```python
def show_message():
    message = "Ready"
    print(message)


show_message()
```

Output:

```text
Ready
```

`message` is a local name created during this call. A later call receives its own local namespace.

## 5. Parameters are local names

Function parameters participate in the function's local namespace.

```python
def greet(name):
    message = f"Hello, {name}"
    print(message)


greet("Avery")
```

Output:

```text
Hello, Avery
```

During the call:

```text
argument "Avery"
↓
local parameter name → "Avery"
↓
local message is created
```

The argument supplies an object. The parameter is the local name used by the function.

## 6. Local names do not automatically escape the function

```python
def create_message():
    message = "Ready"


create_message()
print(message)
```

The call succeeds, but the final line raises `NameError`. There is no visible module-level binding named `message`.

```text
inside function  → message is local
outside function → that local name is not directly visible
```

If the caller needs the value, return it.

## 7. Each call gets its own local namespace

```python
def build_label(topic):
    label = f"Learning {topic}"
    print(label)


build_label("scope")
build_label("functions")
```

Output:

```text
Learning scope
Learning functions
```

Think of them as separate workspaces:

```text
call 1 → topic and label for "scope"
call 2 → topic and label for "functions"
```

The source-code names are reused, but each invocation has its own local namespace.

## 8. A function can read a global name

A function can read a module-level name without declaring it `global` when it only reads that name.

```python
course = "Python"


def show_course():
    print(course)


show_course()
```

Output:

```text
Python
```

Python does not find a local binding named `course`, so lookup continues outward and finds the module-level binding.

Reading a global name and **rebinding** a global name are different operations.

## 9. Module constants can be reasonable shared inputs

```python
TAX_RATE = 0.10


def calculate_tax(amount):
    return amount * TAX_RATE


print(calculate_tax(200))
```

Output:

```text
20.0
```

Uppercase names such as `TAX_RATE` are a style convention for constants. Python does not enforce immutability because a name is uppercase.

Reading a clear module constant can be understandable. Hidden mutable global state is a different design problem and is deferred.

## 10. Assignment inside a function normally creates a local binding

Without `global` or `nonlocal`, assigning to a name inside a function normally binds that name locally.

```python
status = "module"


def show_status():
    status = "function"
    print(status)


show_status()
print(status)
```

Output:

```text
function
module
```

The assignment inside `show_status()` does not replace the module-level binding. It creates a local binding with the same spelling.

## 11. Shadowing uses the same spelling for different bindings

The previous example contains **shadowing**:

```text
inside show_status → status = "function"
module level       → status = "module"
```

Shadowing is legal. Unnecessary shadowing can still make a program harder to trace, so prefer distinct names when the meanings are genuinely different.

## 12. Beginner name lookup: LEGB

Consider:

```python
topic = "scope"


def show_topic():
    message = "ready"
    print(message)
    print(topic)
    print(len(topic))


show_topic()
```

Output:

```text
ready
scope
5
```

The traditional lookup mnemonic is:

```text
Local → Enclosing → Global → Built-in
```

- **Local:** names in the current function call;
- **Enclosing:** names in enclosing functions when functions are nested;
- **Global:** names in the current module;
- **Built-in:** names such as `len`, `print`, and `abs`.

This chapter uses Local, Global, and Built-in directly. Nested functions and `nonlocal` are deferred, so Enclosing is introduced only as part of the lookup map.

## 13. Avoid shadowing built-in names

Avoid rebinding familiar built-ins:

```python
len = 10

print(len("scope"))
```

Now `len` refers to the integer `10` in the current scope, so the built-in function is shadowed and the call fails.

Names such as `list`, `str`, `type`, `sum`, `min`, `max`, `input`, and `print` deserve the same caution.

## 14. `if` does not create a new function-local scope

```python
def classify_score(score):
    if score >= 60:
        result = "passing"
    else:
        result = "review"

    print(result)


classify_score(75)
```

Output:

```text
passing
```

`result` belongs to the surrounding function's local scope. Both branches bind it, so the later read is safe.

## 15. `for` does not create a new function-local scope

```python
def show_last_number():
    for number in [1, 2, 3]:
        print(number)

    print("Last:", number)


show_last_number()
```

Output:

```text
1
2
3
Last: 3
```

The loop target `number` belongs to the surrounding function scope. Ordinary `while` statements follow the same surrounding-scope idea.

Do not generalize this to every Python construct. Functions, classes, comprehensions, and other constructs have their own rules.

## 16. Ask whether the name was definitely bound before use

Scope and program flow work together.

A useful question is:

> On the path that actually ran, was this name bound before Python tried to read it?

This matters with branches and loops because some paths may not execute an assignment.

## 17. A missing visible name raises `NameError`

Revisit:

```python
def create_message():
    message = "Ready"


create_message()
print(message)
```

The final line cannot resolve `message` at module level and raises `NameError`.

A useful debugging checklist is:

1. Is the spelling correct?
2. Was the name bound before this use?
3. Was it bound in a scope visible from here?
4. Did I expect a local value to leave a function without returning it?

## 18. Assignment anywhere in a function can make a name local

This rule is subtle and important:

```python
count = 10


def show_count():
    print(count)
    count = 20


show_count()
```

Calling `show_count()` raises `UnboundLocalError`.

Why? The assignment `count = 20` makes `count` a local name for the function block. The earlier `print(count)` therefore tries to read that local name before the local binding receives a value.

```text
function contains local binding for count
↓
print(count) runs before local count receives a value
↓
UnboundLocalError
```

`UnboundLocalError` is a subclass of `NameError`. Exception handling comes later; here the goal is understanding the lookup failure.

## 19. Prefer explicit input and return flow when possible

Instead of silently rebinding shared global state, pass the value in and return the new value.

```python
count = 10


def increase(value):
    return value + 1


count = increase(count)
print(count)
```

Output:

```text
11
```

The movement is explicit:

```text
module count
↓ argument
local parameter value
↓ return
new module count
```

This builds directly on Chapters 02 and 03.

## 20. Reading a global name does not require `global`

```python
mode = "study"


def show_mode():
    print(mode)


show_mode()
```

Output:

```text
study
```

No `global` statement is needed. `global` is about binding a name at module level, not granting permission to read it.

## 21. `global` allows explicit module-level rebinding

```python
mode = "study"


def enable_practice_mode():
    global mode
    mode = "practice"


enable_practice_mode()
print(mode)
```

Output:

```text
practice
```

Inside that function, `global mode` directs uses and assignments of `mode` to the module-level binding.

The `global` declaration must appear before uses or assignments of that name in the same scope.

## 22. Use `global` cautiously

Compare:

```text
global rebinding
function → hidden change to module state

parameter/return flow
caller → explicit input → function → explicit output → caller
```

The second model is often easier to test, reuse, and reason about.

Use `global` when module-level shared state is genuinely the intended design and the tradeoff is understood. Prefer parameters and return values when they make data flow clearer.

This is a design recommendation, not a Python prohibition.

## 23. Scope and return values work together

```python
course = "Python"


def build_message(topic):
    label = f"{course}: {topic}"
    return label


message = build_message("scope")
print(message)
```

Output:

```text
Python: scope
```

`topic` and `label` are local. The caller receives the useful object through `return` and binds it to `message`.

Scope creates the boundary. `return` provides an explicit path across it.

## 24. Trace the complete round trip

For the previous example:

```text
module binds course → "Python"
↓
caller passes "scope"
↓
local parameter topic is bound
↓
local label is bound
↓
course is found in module global scope
↓
function returns "Python: scope"
↓
caller binds message to returned value
```

This combines the mental models from Chapters 02, 03, and 04.

## 25. Executable examples

### Local and global names

File: [`examples/local_and_global_names.py`](examples/local_and_global_names.py)

```python
course = "Python"


def show_course():
    message = "Studying"
    print(course)
    print(message)


show_course()
print(course)
```

Expected output:

```text
Python
Studying
Python
```

### Separate local namespaces per call

File: [`examples/separate_function_calls.py`](examples/separate_function_calls.py)

```python
def build_label(topic):
    label = f"Learning {topic}"
    print(label)


build_label("scope")
build_label("functions")
```

Expected output:

```text
Learning scope
Learning functions
```

### Shadowing without changing the global binding

File: [`examples/shadowing_names.py`](examples/shadowing_names.py)

```python
status = "module"


def show_status():
    status = "function"
    print(status)


show_status()
print(status)
```

Expected output:

```text
function
module
```

## 26. Exercise: trace global and local names

Study this program:

```python
language = "Python"


def describe_topic(topic):
    label = f"{language}: {topic}"
    return label


result = describe_topic("scope")
print(result)
```

Expected output:

```text
Python: scope
```

Before running it, answer:

1. Which names are module-level?
2. Which names are local to `describe_topic()`?
3. Why can the function read `language` without `global`?
4. Why can the caller use the returned value but not directly use local `label`?
5. What changes if the function assigns to `language` without declaring it `global`?

Then run the program and verify your explanation.

## 27. Review checklist

Before continuing, confirm that you can:

- [ ] explain scope and namespace at a beginner level;
- [ ] identify module-level global names and function-local names;
- [ ] explain that parameters are local names;
- [ ] explain that each function call gets its own local namespace;
- [ ] read a global name from a function without `global`;
- [ ] recognize local shadowing and built-in shadowing;
- [ ] explain Local → Enclosing → Global → Built-in lookup;
- [ ] explain ordinary `if`, `for`, and `while` scope behavior;
- [ ] recognize `NameError` caused by a missing visible name;
- [ ] explain the common `UnboundLocalError` caused by reading a local name before binding it;
- [ ] explain what `global` changes;
- [ ] prefer parameters and return values when they make data flow clearer.

## 28. Quick reference

| Need | Beginner rule |
|---|---|
| module-level name | global name for that module |
| function parameter | local name |
| assignment in a function | normally binds a local name |
| read global from function | no `global` needed |
| rebind global from function | declare it with `global` |
| same spelling locally and globally | local binding shadows global binding |
| ordinary `if` / `for` / `while` | no new function-local scope |
| name cannot be found | `NameError` |
| local name read before local binding | `UnboundLocalError` |
| send a local result to caller | `return` it |
| clearer state change | often parameters + return values |

## 29. Scope boundary

This chapter intentionally postpones:

- nested functions as a programming technique;
- `nonlocal`;
- closures;
- lambda functions;
- class scopes and method-specific lookup details;
- comprehension-scope details;
- mutation and aliasing of shared global objects;
- module importing as a main topic;
- exception handling;
- decorators and generators.

These topics belong later in the learning path or need their own context.

## 30. What comes next

You can now trace:

```text
caller
↓
arguments
↓
local parameter names
↓
local function work
↓
name lookup across visible scopes
↓
return value
↓
caller
```

The next question is:

> How can a function communicate the kinds of inputs and outputs it expects?

That leads to **Chapter 05: Type Hints**.

Return to the [Functions learning path](../README.md) or the [full learning path](../../docs/learning-path.en.md).

## References

Primary Python documentation:

- [Python 3.13 Language Reference: Execution model](https://docs.python.org/3.13/reference/executionmodel.html)
- [Python 3.13 Tutorial: Python Scopes and Namespaces](https://docs.python.org/3.13/tutorial/classes.html#python-scopes-and-namespaces)
- [Python 3.13 Language Reference: The `global` statement](https://docs.python.org/3.13/reference/simple_stmts.html#the-global-statement)

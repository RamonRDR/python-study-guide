<div align="center">

# Output with `print()` and Input with `input()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: How Python runs a program](../01-how-python-runs-a-program/README.md)

A program becomes easier to understand when it can show what it is doing and receive information from the person using it. Python provides two built-in functions for these first conversations: `print()` displays output, and `input()` reads a line of text from the terminal.

This chapter builds a small interactive program while keeping the distinction between program output, typed input, and source code clear.

## Chapter information

| Item | Details |
|---|---|
| Level | Absolute beginner |
| Prerequisites | Create, save, and execute a `.py` file from the terminal |
| Estimated study time | 45 to 65 minutes |
| Main concepts | Output, input, function call, argument, prompt, `sep`, `end`, returned text |

## Learning objectives

By the end of this chapter, you should be able to:

- use `print()` to display text and other values;
- pass more than one value to `print()`;
- control the separator and line ending with `sep` and `end`;
- use `input()` with a clear prompt;
- explain why `input()` pauses the program;
- store the text returned by `input()` under a name;
- distinguish program output from text typed by the user;
- recognize when interactive input is inappropriate for unattended programs.

## 1. Output and input are different directions

**Output** is information that the program sends outward. It may appear in a terminal, graphical interface, file, log, or another destination.

**Input** is information that enters the program. It may come from a keyboard, file, network request, sensor, or another system.

In this chapter:

- `print()` sends text to the terminal;
- `input()` receives one line typed in the terminal.

```text
person ──input──▶ program ──output──▶ terminal
```

## 2. `print()` and `input()` are built-in functions

A function is a reusable operation. Calling a function means writing its name followed by parentheses.

```python
print("Hello, World!")
```

In this call:

- `print` is the function name;
- the parentheses call the function;
- `"Hello, World!"` is an argument supplied to the function.

Both `print()` and `input()` are built into Python, so these first examples do not require an `import` statement.

## 3. Display one value with `print()`

The simplest form displays one value:

```python
print("Python is running.")
```

Expected output:

```text
Python is running.
```

The quotation marks belong to the source code. They indicate a text value. They are not displayed as part of the output.

## 4. Display several values

Separate multiple arguments with commas:

```python
print("Python", "Study", "Guide")
```

Expected output:

```text
Python Study Guide
```

By default, `print()` inserts one space between the displayed arguments.

A comma between arguments is Python syntax. A comma written inside quotation marks is ordinary text:

```python
print("Hello,", "student!")
```

Expected output:

```text
Hello, student!
```

## 5. Change the separator with `sep`

The `sep` argument controls what appears between multiple displayed values:

```python
print("2026", "08", "06", sep="-")
```

Expected output:

```text
2026-08-06
```

Another example:

```python
print("Python", "Study", "Guide", sep=" | ")
```

Expected output:

```text
Python | Study | Guide
```

`sep` matters only when `print()` receives more than one value.

## 6. Change the line ending with `end`

By default, `print()` finishes with a newline, so the next output begins on the following line.

The `end` argument replaces that final newline:

```python
print("Loading", end="...")
print("done!")
```

Expected output:

```text
Loading...done!
```

Use `end` deliberately. Removing line breaks everywhere can make terminal output difficult to read.

## 7. Print a blank line

Calling `print()` without arguments writes only its default newline:

```python
print("First section")
print()
print("Second section")
```

Expected output:

```text
First section

Second section
```

This is useful for separating small groups of terminal output.

## 8. Read a line with `input()`

`input()` can display a prompt and wait for the person to type a response:

```python
name = input("What is your name? ")
```

The program pauses at this line. After the person types a response and presses Enter, `input()` returns that response as text.

The space before the closing quotation mark keeps the cursor visually separated from the prompt:

```text
What is your name? Ada
```

Without that space, the typed response may appear crowded against the question.

## 9. Store the returned text

This line performs two connected operations:

```python
name = input("What is your name? ")
```

1. `input()` reads and returns text.
2. `name =` stores that returned text under the name `name`.

The next chapter explains variables and naming in detail. For now, treat `name` as a label that lets the program use the response later.

## 10. Display the response

After storing the result, pass it to `print()`:

```python
name = input("What is your name? ")
print("Hello,", name)
```

A possible terminal session is:

```text
What is your name? Ada
Hello, Ada
```

The first line contains both the program's prompt and the response typed by the person. The terminal normally shows typed characters as they are entered. The second line is produced by `print()`.

## 11. Ask more than one question

Instructions still execute in order:

```python
name = input("What is your name? ")
city = input("Which city do you live in? ")

print("Name:", name)
print("City:", city)
```

Python waits for the first response before displaying the second prompt.

A possible session is:

```text
What is your name? Ada
Which city do you live in? London
Name: Ada
City: London
```

## 12. `input()` returns text

Even when a person types digits, `input()` returns a text value. The following response is text containing the characters `2` and `5`, not yet a number:

```python
age = input("How old are you? ")
print("You entered:", age)
```

The later type-conversion chapter will explain how to convert compatible text into numeric values. Until then, use the result as text.

## 13. Pressing Enter can return empty text

A person may press Enter without typing any visible character:

```python
answer = input("Press Enter without typing: ")
print("You entered:", answer)
```

In that case, `answer` contains an empty text value. The program does not automatically decide that empty input is invalid. Validation will be introduced after conditions and program flow.

## 14. `input()` removes the final Enter newline

Pressing Enter finishes the response. The line-ending character used to submit the response is not included in the returned text.

This is why the following output stays on one line:

```python
word = input("Type one word: ")
print("Received:", word)
```

The typed word is returned, but the newline used to submit it is removed.

## 15. When to use `input()`

`input()` is useful for:

- beginner exercises;
- small terminal conversations;
- manual utilities used by one person at a time;
- quick experiments where waiting for a response is expected.

Avoid depending on `input()` when a program must run without a person, such as:

- scheduled jobs;
- automated tests;
- background services;
- continuous integration;
- data-processing pipelines.

An unattended program can remain paused forever or fail when no input source is available. Such programs usually receive configuration through arguments, files, environment variables, APIs, or other explicit interfaces.

## 16. Repository examples

| File | Purpose | Automatic execution |
|---|---|---|
| [`output_basics.py`](examples/output_basics.py) | Demonstrates multiple values, `sep`, `end`, and blank lines | Yes |
| [`interactive_greeting.py`](examples/interactive_greeting.py) | Reads a name and displays a greeting | No; it waits for terminal input |

The interactive example is intentionally not included in the unattended example manifest.

## 17. Practical example: a student card

Create `student_card.py`:

```python
name = input("Name: ")
city = input("City: ")
learning_goal = input("Learning goal: ")

print()
print("STUDENT CARD")
print("Name:", name)
print("City:", city)
print("Goal:", learning_goal)
```

A possible session is:

```text
Name: Ada
City: London
Learning goal: Build useful programs

STUDENT CARD
Name: Ada
City: London
Goal: Build useful programs
```

This program already has a simple data flow: questions produce text, names retain the text, and `print()` displays it in a new arrangement.

## 18. Exercise

Create a file named `learning_check_in.py` that:

1. asks for the learner's name;
2. asks which Python topic the learner wants to study;
3. asks how many minutes the learner plans to practice, keeping the answer as text;
4. prints a blank line;
5. prints the heading `LEARNING CHECK-IN`;
6. displays the three responses on separate labeled lines;
7. prints `Study`, `Understand`, and `Practice` separated by ` -> `;
8. finishes with `Ready!` on the same line as `Starting...`.

Use these exact final three calls:

```python
print("Study", "Understand", "Practice", sep=" -> ")
print("Starting", end="...")
print("Ready!")
```

Run the program at least twice with different responses.

## 19. Common mistakes

### Forgetting parentheses

```text
print "Hello"
```

Python 3 requires a function call with parentheses:

```python
print("Hello")
```

### Forgetting quotation marks around literal text

```text
print(Hello)
```

Without quotation marks, Python treats `Hello` as a name rather than literal text.

### Using the wrong separator syntax

Write `sep` inside the `print()` call:

```python
print("A", "B", sep="-")
```

### Expecting `input()` to continue immediately

`input()` waits until a line is submitted. A program that appears frozen may simply be waiting for a response.

### Forgetting to store the response

Calling `input()` by itself reads text, but the response is discarded if the program does not store or use the returned value.

### Treating typed digits as a number

`input()` returns text. Numeric conversion belongs to a later chapter.

### Confusing terminal echo with `print()`

The terminal may display what the person types. That visible response is not an additional `print()` call.

## 20. Self-check

You are ready for the next chapter when you can answer these questions:

- What direction does output travel?
- What does `print()` place between multiple arguments by default?
- What does `end` replace?
- Why does `input()` pause the program?
- What kind of value does `input()` return?
- What happens when the person presses Enter without typing?
- Why should an unattended script usually avoid interactive input?
- Which visible terminal text was produced by the program, and which was typed by the person?

## 21. Quick-reference summary

| Goal | Example |
|---|---|
| Display text | `print("Hello")` |
| Display several values | `print("Name:", name)` |
| Change the separator | `print("A", "B", sep="-")` |
| Stay on the same line | `print("Loading", end="...")` |
| Print a blank line | `print()` |
| Ask a question | `input("Question: ")` |
| Store a response | `answer = input("Question: ")` |
| Important input type | `input()` returns text |
| Empty response | Pressing Enter can return empty text |
| Unattended execution | Avoid waiting for `input()` |

## 22. Run the repository examples

From the repository root, run the automatic example:

```bash
python fundamentals/02-print-and-input/examples/output_basics.py
```

Run the interactive example and answer its prompt:

```bash
python fundamentals/02-print-and-input/examples/interactive_greeting.py
```

## 23. Run the repository checks

From the repository root:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

The approved-example runner executes `output_basics.py` but does not execute `interactive_greeting.py`, because unattended checks must not wait for keyboard input.

## Official references

- [Python documentation — Built-in functions: `print()` and `input()`](https://docs.python.org/3/library/functions.html)
- [Python tutorial — Input and output](https://docs.python.org/3/tutorial/inputoutput.html)

[← Back to the section index](../README.md) · [← Previous chapter: How Python runs a program](../01-how-python-runs-a-program/README.md)

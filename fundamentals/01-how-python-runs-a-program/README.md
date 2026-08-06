<div align="center">

# How Python Runs a Program

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md)

A Python program begins as text written by a person. Saving that text in a `.py` file does not run it. The program runs only when the Python interpreter is asked to read and execute the file.

This chapter takes you from an empty file to a working program, then shows how to change it, run it again, and correct a basic syntax error.

## Chapter information

| Item | Details |
|---|---|
| Level | Absolute beginner |
| Prerequisites | Python installed; access to a text editor and terminal |
| Estimated study time | 40 to 60 minutes |
| Main concepts | Program, source code, `.py` file, editor, terminal, interpreter, execution order, syntax error |

## Learning objectives

By the end of this chapter, you should be able to:

- explain what a program and source code are;
- identify the purpose of a `.py` file;
- distinguish an editor, a terminal, and the Python interpreter;
- describe the difference between writing, saving, and running code;
- create and execute a Python file from the terminal;
- explain how ordinary top-level instructions run from top to bottom;
- locate the useful parts of a basic `SyntaxError` message;
- modify, save, and run a program again.

## 1. What is a program?

A program is a set of instructions that a computer can execute.

A cooking recipe also contains ordered instructions, but a computer needs instructions written in a language it can process. In this guide, that language is Python.

A program may contain one instruction or millions of instructions. Your first program contains only one:

```python
print("Hello, World!")
```

This instruction asks Python to display text.

## 2. What is source code?

**Source code** is the human-readable text used to describe a program.

The following text is Python source code:

```python
print("Hello, World!")
```

Source code is not a screenshot, a formatted document, or the result displayed by the program. It is the text that you write and save so that a language implementation can process it.

## 3. What is a `.py` file?

A file ending in `.py` is commonly used to store Python source code.

For example:

```text
hello_world.py
```

The name has two parts:

- `hello_world` is the file name;
- `.py` is the file extension associated with Python source files.

The extension helps people and tools recognize the file type. It does not execute the file by itself.

## 4. Editor, terminal, and interpreter have different jobs

These three tools often appear on the same screen, but they are not the same thing.

| Tool | Main job |
|---|---|
| Editor | Write and change source code |
| Terminal | Enter commands and view command output |
| Python interpreter | Read Python code and execute it |

An editor may include an integrated terminal. A terminal may start the Python interpreter. The tools can work together without becoming the same tool.

## 5. Writing, saving, and running are separate actions

A beginner often performs these actions quickly and assumes they are one step. They are three steps:

1. **Write:** enter or modify source code in the editor.
2. **Save:** store the current text in a file.
3. **Run:** ask the Python interpreter to execute the saved file.

If you change the editor but do not save, the interpreter usually runs the previous saved version. The unsaved text still exists only in the editor.

## 6. Create `hello_world.py`

Open a plain-text or code editor and create a new file named:

```text
hello_world.py
```

Enter exactly this code:

```python
print("Hello, World!")
```

Use ordinary straight quotation marks (`"`), not decorative quotation marks such as `“` and `”`.

Save the file in a folder that you can find again.

## 7. Open the terminal in the file's folder

The terminal works with a **current directory**, which is the folder where commands are being run.

Before executing the program, make sure the terminal is in the folder containing `hello_world.py`.

Many editors provide a command such as **Open in Integrated Terminal**. You can also open a system terminal and navigate to the folder.

To see the files in the current folder, a common command is:

```text
dir
```

on Windows, or:

```text
ls
```

on macOS and Linux.

You should see `hello_world.py` in the result.

## 8. Execute the file

Run:

```bash
python hello_world.py
```

Depending on how Python was installed, the command may instead be:

```bash
python3 hello_world.py
```

or, on some Windows installations:

```bash
py hello_world.py
```

The expected output is:

```text
Hello, World!
```

The output is not part of the source file. It is produced when the program runs.

## 9. What happens after the command?

For this command:

```bash
python hello_world.py
```

a simplified execution path is:

1. the terminal receives the command;
2. the operating system starts the Python interpreter;
3. the interpreter opens `hello_world.py`;
4. Python checks whether the source follows Python's grammar;
5. Python executes the program's top-level instructions in order;
6. `print()` sends text to the program's standard output;
7. the interpreter finishes because no instructions remain.

Python implementations perform internal work that this beginner-level description does not show. You do not need to understand bytecode or virtual machines to create and run your first scripts.

## 10. Top-level instructions normally run from top to bottom

Consider this file:

```python
print("First")
print("Second")
print("Third")
```

Its output is:

```text
First
Second
Third
```

The visible effects happen in the same order as the top-level instructions.

Later chapters will introduce conditions, loops, functions, exceptions, and imports. Those features can repeat, skip, postpone, or redirect execution. For a simple file containing consecutive `print()` calls, top-to-bottom is the correct mental model.

## 11. A file is different from interactive mode

Running a file:

```bash
python hello_world.py
```

asks Python to execute the saved script.

Running Python without a file name:

```bash
python
```

usually opens the interactive interpreter and displays a prompt such as:

```text
>>>
```

Interactive mode is useful for small experiments. A `.py` file is better when you want to save, review, rerun, share, or version the program.

To leave interactive mode, use `exit()` or the exit shortcut shown by your terminal.

## 12. Modify and run the program again

Change the file to:

```python
print("Hello, World!")
print("I changed my first program.")
```

Then:

1. save the file;
2. return to the terminal;
3. run the same command again.

```bash
python hello_world.py
```

Expected output:

```text
Hello, World!
I changed my first program.
```

Python does not automatically use the unsaved editor contents. Save before rerunning.

## 13. What is a syntax error?

Python source code must follow Python's grammar. A **syntax error** means Python could not understand the program's structure well enough to execute it.

For example, this line is missing its closing quotation mark:

```python
print("Hello, World!)
```

When Python reads the file, it stops before running the program and reports a `SyntaxError`.

A simplified error message may look like this:

```text
  File "hello_world.py", line 1
    print("Hello, World!)
          ^
SyntaxError: unterminated string literal
```

The exact wording, path, and caret position can vary by Python version and environment.

## 14. Read a basic error message from the bottom upward

For a basic syntax error, inspect these parts:

1. **Error type and message:** the last line says `SyntaxError` and describes the problem.
2. **File and line:** Python identifies the file and an approximate line where parsing failed.
3. **Source excerpt:** Python displays the relevant source line.
4. **Caret (`^`):** it points near the place where Python detected that something was wrong.

The detection position is not always the original cause. A missing symbol earlier in the line or on a previous line can make Python complain later.

Fix the first reported syntax error, save the file, and run it again.

## 15. Correct the program

Restore the missing quotation mark:

```python
print("Hello, World!")
```

Save the file and run:

```bash
python hello_world.py
```

The program should display:

```text
Hello, World!
```

Errors are part of programming. The useful habit is not avoiding every error; it is reading the evidence, changing one cause, and testing again.

## 16. Common first-program problems

### The command cannot find Python

Try the command used by your installation: `python`, `python3`, or `py`. If none works, Python may not be installed or may not be available in the terminal's command search path.

### Python cannot open the file

The terminal may be in the wrong directory, or the file name may differ. Check the current folder and spelling.

### The output did not change

Save the file before running it again. Also confirm that you are editing and executing the same file.

### The file is really `hello_world.py.txt`

Some systems hide known file extensions. Confirm the complete file name in the editor or file properties.

### The quotation marks look curved

Replace decorative quotation marks with straight ASCII quotation marks.

### The editor shows a run button

That button may be convenient, but learn the terminal command too. It makes the editor, terminal, interpreter, file, and current directory easier to distinguish.

## 17. Practical exercise

Create a new file named:

```text
first_steps.py
```

Add these instructions:

```python
print("Python is running.")
print("I wrote this program.")
print("I saved the file.")
print("I ran it from the terminal.")
```

Complete the following sequence:

1. save the file;
2. run it from the terminal;
3. confirm that the four lines appear in order;
4. change the third instruction to the following:

```python
print("I changed the program.")
```

5. save and run the file again;
6. deliberately remove the final quotation mark from the last instruction;
7. save and run the file;
8. identify the file name, line number, error type, and message;
9. restore the quotation mark;
10. save and run the corrected program.

Your final program must run without a syntax error and display four lines.

## 18. Self-check

You are ready for the next chapter when you can answer these questions:

- What is the difference between source code and program output?
- Why does changing text in an editor not necessarily change the next execution?
- Which tool receives `python hello_world.py`?
- Which tool understands the Python source?
- In what order do simple top-level `print()` instructions run?
- Which part of a basic error message identifies the error type?
- What should you do after correcting the source code?

## 19. Quick-reference summary

| Situation | Action |
|---|---|
| Write code | Use a plain-text or code editor |
| Store current changes | Save the `.py` file |
| Run a script | `python file_name.py` |
| Alternative commands | `python3 file_name.py` or `py file_name.py` |
| Experiment interactively | Run `python` without a file |
| Output did not update | Save and confirm the executed file |
| File was not found | Check directory and file name |
| Syntax error | Read the last line, file, line, source excerpt, and caret |
| After a correction | Save and run again |
| Simple execution order | Top-level instructions run in order, usually top to bottom |

## 20. Run the repository example

From the repository root:

```bash
python fundamentals/01-how-python-runs-a-program/examples/hello_world.py
```

Expected output:

```text
Hello, World!
```

## 21. Run the repository checks

From the repository root:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## Official references

- [Python tutorial — Using the Python interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [Python tutorial — Syntax errors](https://docs.python.org/3/tutorial/errors.html#syntax-errors)
- [Python documentation — Command line and environment](https://docs.python.org/3/using/cmdline.html)

[← Back to the section index](../README.md)

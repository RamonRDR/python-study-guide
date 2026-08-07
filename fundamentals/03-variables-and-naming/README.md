<div align="center">

# Variables and Naming

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md) · [← Previous chapter: `print()` and `input()`](../02-print-and-input/README.md)

Programs become more useful when they can keep information under understandable names and reuse it later. Python assignment connects a name to a value, allowing later instructions to read that value without repeating it.

This chapter introduces variables, assignment, reassignment, valid identifiers, and practical naming conventions. It deliberately postpones detailed data types, comparisons, and scope to later chapters.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Chapters 01 and 02 |
| Estimated study time | 50 to 70 minutes |
| Main concepts | Variable, name, assignment, identifier, reassignment, keyword, `snake_case` |

## Learning objectives

By the end of this chapter, you should be able to:

- assign a value to a name with `=`;
- read a stored value by using its name;
- explain that the right-hand side is evaluated before assignment;
- reassign a name to a new value;
- recognize valid and invalid identifiers;
- explain why Python keywords cannot be variable names;
- choose clear `snake_case` names;
- avoid shadowing built-in functions such as `print` and `input`;
- distinguish Python syntax rules from project naming conventions.

## 1. Why programs store values

Without names, a program must repeat the same value wherever it is needed:

```python
print("Python Study Guide")
print("Current course:", "Python Study Guide")
```

A name lets the program store the value once and reuse it:

```python
course_name = "Python Study Guide"

print(course_name)
print("Current course:", course_name)
```

This reduces repetition and makes later changes easier.

## 2. Assignment uses `=`

A basic assignment statement has a target on the left and a value-producing expression on the right:

```python
learner_name = "Ada"
```

Read this as:

> Assign the text `"Ada"` to the name `learner_name`.

For a beginner, it is reasonable to call `learner_name` a variable. More precisely, Python binds the name `learner_name` to the resulting value.

The `=` symbol performs assignment. It does not ask whether two values are equal. Comparisons with `==` belong to a later chapter.

## 3. Use the name to read the value

After assignment, using the name retrieves the value currently associated with it:

```python
learner_name = "Ada"

print(learner_name)
print("Learner:", learner_name)
```

Expected output:

```text
Ada
Learner: Ada
```

Quotation marks create literal text. A name without quotation marks asks Python for its stored value.

## 4. The right-hand side is evaluated first

Python evaluates the expression on the right before assigning its result to the name on the left:

```python
topic = input("Topic: ")
```

The order is:

1. `input("Topic: ")` displays the prompt and returns text;
2. the returned text is assigned to `topic`.

This same pattern works with other expressions:

```python
full_title = "Python" + " Study Guide"
print(full_title)
```

The expression creates the final text before `full_title` receives it.

## 5. Reassignment updates what a name refers to

A name can receive a new value later:

```python
current_topic = "Output and input"
print("Before:", current_topic)

current_topic = "Variables and naming"
print("After:", current_topic)
```

Expected output:

```text
Before: Output and input
After: Variables and naming
```

The second assignment replaces the value retrieved through `current_topic` from that point onward.

Python does not require a special declaration before the first assignment.

## 6. Names are case-sensitive

Python treats uppercase and lowercase letters as different:

```python
topic = "Variables"
Topic = "Naming"

print(topic)
print(Topic)
```

`topic` and `Topic` are two different names. Avoid names that differ only by capitalization because they are easy to confuse.

## 7. A beginner-safe identifier rule

A variable name is an **identifier**. For portable beginner code using English identifiers, follow this safe rule:

- begin with an English letter or underscore;
- continue with English letters, digits, or underscores;
- do not include spaces or hyphens;
- do not begin with a digit.

Valid examples:

```python
name = "Ada"
learner_name = "Ada"
topic_2 = "Variables"
_private_note = "Draft"
```

Invalid examples:

```text
2topic = "Variables"
learner-name = "Ada"
learner name = "Ada"
```

Python supports a wider range of Unicode letters in identifiers. This project nevertheless uses descriptive English identifiers as a repository convention.

## 8. Keywords cannot be variable names

Keywords have reserved grammatical meanings in Python. They cannot be reused as ordinary identifiers:

```text
class = "beginner"
for = "practice"
```

Both lines are invalid because `class` and `for` are keywords.

You do not need to memorize every keyword immediately. Editors usually highlight them, and the standard-library `keyword` module can check them later.

## 9. Prefer `snake_case`

PEP 8 recommends lowercase words separated by underscores for variable and function names:

```python
learner_name = "Ada"
study_topic = "Variables and naming"
practice_minutes = "30"
```

This style is called `snake_case`.

Compare:

```text
learnername
LearnerName
learner-name
learner_name
```

For ordinary variables in this project, `learner_name` is the preferred form.

## 10. Choose names that reveal meaning

A name should help the reader understand the value's role:

```python
x = "45"
```

The name `x` provides almost no context.

```python
practice_minutes = "45"
```

The clearer name reveals both purpose and unit.

Useful questions when naming a variable:

- What information does this value represent?
- Why will the program use it?
- Does a unit such as minutes, kilograms, or reais matter?
- Will the name still make sense several lines later?

## 11. Avoid unexplained abbreviations

Short names save keystrokes but can cost understanding:

```python
nm = "Ada"
tp = "Variables"
mins = "30"
```

Prefer complete, readable names:

```python
learner_name = "Ada"
study_topic = "Variables"
practice_minutes = "30"
```

Widely understood abbreviations can be appropriate, but inventing local abbreviations usually creates a decoding puzzle.

## 12. Avoid shadowing built-in functions

Python allows some built-in function names to be reassigned, but doing so hides the original function under that name:

```python
print = "not a function anymore"
```

After that assignment, this call fails because `print` now refers to text:

```text
print("Hello")
```

Avoid variable names such as:

- `print`;
- `input`;
- `str`;
- `int`;
- `list`;
- `sum`.

They are not all keywords, but preserving built-in names prevents confusing failures.

## 13. English identifiers are a project convention

Python can accept identifiers from many writing systems. The Python Study Guide uses English identifiers in shared code:

```python
learner_name = "Ada"
study_goal = "Build useful programs"
```

This is a repository convention, not a universal Python requirement. Explanations remain multilingual, while shared code stays identical across translations.

## 14. Constants use an uppercase convention

A value intended to remain unchanged during a program is often written with uppercase words:

```python
COURSE_NAME = "Python Study Guide"
DEFAULT_TOPIC = "Fundamentals"
```

This style communicates intent to readers. Python does not prevent reassignment, so uppercase naming is a convention rather than enforcement.

## 15. Store and reuse input

Chapter 02 used assignment as a bridge. You can now describe the parts more precisely:

```python
learner_name = input("Name: ")
study_topic = input("Topic: ")

print("Learner:", learner_name)
print("Topic:", study_topic)
```

Each prompt returns text. Each assignment gives that returned text a meaningful name, and each later `print()` reads the stored value.

## 16. A name is not the same as text containing its spelling

Compare these calls:

```python
learner_name = "Ada"

print(learner_name)
print("learner_name")
```

Expected output:

```text
Ada
learner_name
```

The first call reads the variable. The second prints literal text because the characters are inside quotation marks.

## 17. Using a name before assignment causes an error

Python must encounter an assignment before the name can be read in the current program flow:

```text
print(current_topic)
current_topic = "Variables"
```

Running this top-level example raises `NameError` because `current_topic` has not been assigned when the first line executes.

Move the assignment before the read:

```python
current_topic = "Variables"
print(current_topic)
```

## 18. Repository examples

| File | Purpose | Automatic execution |
|---|---|---|
| [`variable_basics.py`](examples/variable_basics.py) | Demonstrates assignment, reuse, clear names, and reassignment | Yes |
| [`learning_profile.py`](examples/learning_profile.py) | Collects and displays a small learning profile | No; it waits for terminal input |

The interactive example is intentionally excluded from the unattended example manifest.

## 19. Practical example: learning profile

Create `learning_profile.py`:

```python
learner_name = input("Name: ")
current_topic = input("Current topic: ")
study_goal = input("Study goal: ")

print()
print("LEARNING PROFILE")
print("Name:", learner_name)
print("Topic:", current_topic)
print("Goal:", study_goal)
```

A possible session is:

```text
Name: Ada
Current topic: Variables
Study goal: Build useful programs

LEARNING PROFILE
Name: Ada
Topic: Variables
Goal: Build useful programs
```

The names explain what each response represents and make the final output easy to assemble.

## 20. Exercise

Create `study_session.py` that:

1. stores the guide name in `GUIDE_NAME`;
2. asks for the learner's name;
3. asks for the topic;
4. asks for the planned practice time as text;
5. prints a blank line;
6. prints a labeled session summary;
7. reassigns the topic to `"Review completed"`;
8. prints the updated topic.

Use these exact names:

```python
GUIDE_NAME
learner_name
study_topic
practice_minutes
```

Run the program twice with different responses. Then replace one clear name with a vague name such as `x`, read the program, and restore the clearer name.

## 21. Common mistakes

### Reading before assignment

```text
print(city)
city = "London"
```

Assign first, then read.

### Putting a variable name inside quotation marks

```python
city = "London"
print("city")
```

This prints `city`, not `London`.

### Starting a name with a digit

```text
1st_topic = "Variables"
```

Use a valid identifier such as `first_topic`.

### Using spaces or hyphens

```text
learner name = "Ada"
learner-name = "Ada"
```

Use `learner_name`.

### Using a keyword

```text
class = "beginner"
```

Choose a descriptive alternative such as `course_level`.

### Reusing a built-in name

```text
input = "stored text"
```

Choose a name that describes the value, such as `user_response`.

### Using mismatched capitalization

```text
study_topic = "Variables"
print(Study_Topic)
```

Names are case-sensitive.

## 22. Self-check

You are ready for the next chapter when you can answer:

- What does `=` do?
- Which side of an assignment is evaluated first?
- What happens during reassignment?
- Why are `topic` and `Topic` different?
- Which characters are safe for an English identifier?
- Why can `class` not be a variable name?
- What does `snake_case` look like?
- Why should a variable not be called `print`?
- Is uppercase constant naming enforced by Python?
- What is the difference between `print(name)` and `print("name")`?

## 23. Quick-reference summary

| Goal | Example |
|---|---|
| Assign a value | `topic = "Variables"` |
| Read a value | `print(topic)` |
| Reassign a name | `topic = "Naming"` |
| Clear variable style | `practice_minutes` |
| Constant convention | `COURSE_NAME` |
| Store input | `name = input("Name: ")` |
| Literal text | `print("name")` |
| Stored value | `print(name)` |
| Avoid built-in shadowing | Do not assign to `print` or `input` |
| Case sensitivity | `name` and `Name` are different |

## 24. Run the repository examples

From the repository root, run the automatic example:

```bash
python fundamentals/03-variables-and-naming/examples/variable_basics.py
```

Run the interactive example and answer its prompts:

```bash
python fundamentals/03-variables-and-naming/examples/learning_profile.py
```

## 25. Run the repository checks

From the repository root:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

The approved-example runner executes `variable_basics.py` but does not execute `learning_profile.py`, because unattended checks must not wait for keyboard input.

## Official references

- [Python language reference — Assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)
- [Python language reference — Identifiers and keywords](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
- [Python standard library — Keyword testing](https://docs.python.org/3/library/keyword.html)
- [PEP 8 — Naming conventions](https://peps.python.org/pep-0008/#naming-conventions)

[← Back to the section index](../README.md) · [← Previous chapter: `print()` and `input()`](../02-print-and-input/README.md)

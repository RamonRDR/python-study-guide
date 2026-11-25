# Manual Coding and Debugging

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../../practical-projects/08-simulated-automation-flow/README.md) · [Module index](../README.md) · [Next →](../02-specification-driven-development/README.md)
<!-- /chapter-navigation:top -->

## Goal and prerequisites

**Level:** beginner after the core curriculum. **Estimated time:** 35–50 minutes. Review [functions](../../functions/README.md), [exceptions](../../errors-files-and-modules/01-try-except-else-finally/README.md) and [Git basics](../../getting-started/06-git-and-version-control/README.md) if needed. Learn to reproduce, diagnose and correct a small error yourself. Use a separate practice folder, not the repository's source files.

## 1. Think before typing

Write down the input, output and a small example by hand. A reading tracker should report pages remaining: total pages 20, pages read 7, expected 13. Predict before running. Break the work into small steps, write the simplest possible code, run it, inspect what happened and explain it. Keep a short note of attempts; a failed attempt is useful evidence.

## 2. Reproduce a defect

Create `practice.py` and type this deliberately incorrect example (not a published executable solution):

```python
def remaining_pages(total_pages, pages_read):
    return total_pages + pages_read

print(remaining_pages(20, 7))
```

Run `python practice.py` using your verified interpreter. Expected behavior is 13; this code prints 27. That is a logic error: execution succeeded, but behavior is wrong. Inspect the operands, trace the expression on paper and correct the operator yourself. Try (20, 0) and (20, 20). Do not assume passing one input proves correctness.

## 3. Read errors from the bottom upward

A syntax error prevents parsing; a runtime exception interrupts execution; a logic error may produce plausible but wrong output. In a disposable practice file, change the call to `remaining_pages(20, "7")` after correcting the operator. Inspect the traceback: start with the exception type and message at the bottom, then find the relevant frame and source line. Exact messages and line numbers depend on the interpreter and file. Check values and types rather than suppressing the exception.

Use `print(repr(value), type(value).__name__)` with a real variable name to inspect a value; remove temporary diagnostics after fixing it. Optionally set a breakpoint in VS Code, use its Python debugger and inspect local variables. A debugger helps investigate; it does not decide the intended behavior.

## 4. Consult documentation and test a hypothesis

Read the relevant [Python tutorial on errors and exceptions](https://docs.python.org/3.13/tutorial/errors.html) or use `help()` for a known Python object. Identify the exact question first. Change one thing at a time; compare expected and actual values. If stuck, seek a hint or explanation, not a completed answer. Try a fresh attempt without looking at the reference. Never send private code, credentials or data to a public service.

## 5. Independent practice

- Predict results for (0, 0), (20, 0), (20, 20).
- Identify the missing behavior for negative or excessive values and non-integers; do not invent the policy. Record questions for the next lesson.
- In a separate file, reproduce a syntax error (e.g. missing closing parenthesis) and fix it.
- Explain the difference between syntax, runtime and logic errors without reading the answer.

**Quick reference:** reproduce, predict, inspect, hypothesize, change one thing, rerun, test boundaries, explain. Next, specify what valid behavior actually means.

<!-- chapter-navigation:bottom -->
[← Previous](../../practical-projects/08-simulated-automation-flow/README.md) · [Module index](../README.md) · [Next →](../02-specification-driven-development/README.md)
<!-- /chapter-navigation:bottom -->

# Run your first program

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../02-configure-vscode/README.md) · [Module index](../README.md) · [Next →](../04-virtual-environments/README.md)
<!-- /chapter-navigation:top -->

## Goal and prerequisites

**Level:** absolute beginner. **Estimated time:** 15–25 minutes. Python is installed and its command verified; your practice folder is open in an editor. You will write, save, run, modify and rerun a file manually. Fundamentals will explain the code's meaning in more detail.

## 1. Create a Python file

In the VS Code Explorer, choose New File and name it `first_program.py` inside `python-practice`. Alternatively, use a plain-text editor and save with that exact name. Make sure the extension is .py, not .py.txt. Enter the following code yourself:

```python
print("Python is ready!")
```

Save with `Ctrl+S` (Windows/Linux) or `Cmd+S` (macOS). Use straight quotation marks, not typographic quotes. Saving does not run the program.

## 2. Run from the terminal

Open the integrated terminal or your OS terminal. Check that it is in your practice folder. On Windows PowerShell use `Get-Location` and `Get-ChildItem`; on macOS/Linux use `pwd` and `ls`. The file should appear in the listing. If necessary, use `cd` followed by the quoted path to your folder, replacing the path with your own.

Run the file with the interpreter command verified earlier:

Windows:

```powershell
py -3.13 first_program.py
```

macOS (official 3.13 installation):

```bash
python3.13 first_program.py
```

Linux (or another verified Python 3 installation on macOS):

```bash
python3 first_program.py
```

If you verified another command, substitute it, keeping the filename. Expected output:

```text
Python is ready!
```

You can also use the Python extension's **Run Python File in Terminal** action in VS Code. That runs the file with the selected interpreter. Prefer typing the terminal command at least once so you understand how execution begins.

## 3. Modify and repeat

Change the message to `My first program!`, save and rerun with the same command. Predict the output before running. Writing, saving and executing are separate actions. No Git account, internet connection, external package or AI assistant is needed to run this example once Python is installed.

## 4. Troubleshooting

| Symptom | Action |
| --- | --- |
| Can't open file / No such file | Check the current folder and exact filename; use quotes for paths containing spaces. |
| Output did not change | Save the file and check that you ran the intended file. |
| `SyntaxError` | Check matching quotes and parentheses; read the indicated line. |
| Command not found | Return to interpreter verification; do not type shell commands at the Python `>>>` prompt. |
| Terminal shows `>>>` | Type `exit()` and return to the shell before running the file. |

## Practice and completion checklist

- [ ] I created and saved a .py file myself.
- [ ] I can locate it in the terminal's current folder.
- [ ] I executed it with a verified interpreter and saw the expected output.
- [ ] I modified the message, predicted the result and ran it again.

For comparison, the repository includes [the same original example](examples/first_program.py). From the repository root, you can run it with your verified interpreter followed by `getting-started/03-run-your-first-program/examples/first_program.py`. This file is not required to complete the manual exercise.

## Next step

Continue to [Virtual Environments](../04-virtual-environments/README.md) to isolate project dependencies. The conceptual lesson [How Python runs a program](../../fundamentals/01-how-python-runs-a-program/README.md) follows the introductory module.

## Official references

- [Using the Python interpreter](https://docs.python.org/3.13/tutorial/interpreter.html)
- [Running Python in VS Code](https://code.visualstudio.com/docs/python/run)

<!-- chapter-navigation:bottom -->
[← Previous](../02-configure-vscode/README.md) · [Module index](../README.md) · [Next →](../04-virtual-environments/README.md)
<!-- /chapter-navigation:bottom -->

# Virtual Environments

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../03-run-your-first-program/README.md) · [Module index](../README.md) · [Next →](../05-packages-and-dependencies/README.md)
<!-- /chapter-navigation:top -->

## Goal

**Level:** absolute beginner. **Estimated time:** 25–40 minutes. Complete the first-program lesson. A virtual environment is a project-specific Python environment. It normally keeps installed third-party packages separate from other projects. It is not a virtual machine, security sandbox or independent copy of the OS.

Imagine two projects that need different versions of the same package. Give each its own environment rather than changing the system Python:

```text
workspace/
├── project_a/
│   ├── .venv/
│   └── main.py
└── project_b/
    ├── .venv/
    └── main.py
```

## 1. Create the environment inside the project

Open your existing `python-practice` folder in VS Code or a terminal. Check your current folder with `Get-Location` in PowerShell or `pwd` on macOS/Linux. Create **one** environment there, using the interpreter verified in Chapter 01.

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
```

macOS (official 3.13 installation):

```bash
python3.13 -m venv .venv
```

Linux (or another verified installation on macOS):

```bash
python3 -m venv .venv
```

Substitute your verified base interpreter command if different. Do not create a new environment inside an existing .venv. On Debian/Ubuntu, if creation fails because ensurepip is unavailable, install the matching distribution venv package (for the default interpreter, commonly `sudo apt install python3-venv`) using authorized administrative access. For a separately installed version use its documented matching package. Never replace system Python.

## 2. Activate and verify

Activation changes command lookup in the current shell. It is not required if you call the environment's Python directly.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt (cmd.exe, not PowerShell):

```bat
.venv\Scripts\activate.bat
```

macOS/Linux (bash or zsh):

```bash
source .venv/bin/activate
```

The prompt may show `(.venv)`, but verify rather than relying on it:

```shell
python --version
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
python -m pip --version
```

The executable and pip location should refer to this project's .venv; the comparison should print True. Use `python -m pip` with this verified interpreter, not a bare pip command or the base launcher. If PowerShell blocks scripts, do not weaken security policy; use the direct executable instead:

```powershell
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe first_program.py
```

On macOS/Linux without activation:

```bash
.venv/bin/python -m pip --version
.venv/bin/python first_program.py
```

## 3. Select .venv in VS Code

Open Command Palette > **Python: Select Interpreter**. Select the interpreter inside this project's .venv (Windows: .venv/Scripts/python.exe; macOS/Linux: .venv/bin/python). Open a new integrated terminal and repeat the verification. If automatic activation does not occur, activate manually or use the direct path. Run your existing first_program.py with that interpreter.

## 4. Leave and recreate

In an activated shell, type `deactivate`. Closing the shell also ends its activation. The directory and installed packages remain. Do not copy or move .venv between machines; recreate it using the base Python and dependency file. If recreating, close terminals using it, confirm the exact directory and remove only that environment using the file manager; keep source files and requirements.

Add `.venv/` to the project's root .gitignore (this repository already ignores .venv). Never commit the generated environment. [Chapter 06](../06-git-and-version-control/README.md) explains how to initialize Git and inspect ignored files. Keep your code outside it. Environment variables, browser binaries, OS libraries and services may live elsewhere; venv isolates Python packages, not all resources.

## 5. Practice and troubleshooting

Create two separate practice folders, each with its own .venv. Select and verify each executable path and run the first program in one. No packages need to be downloaded for this exercise. If the wrong interpreter appears, reopen the correct folder, reselect the interpreter and verify again. If pip is missing, consult the matching Python installation instructions; do not install into system Python as a workaround.

**Quick reference:** create with the verified base interpreter + `-m venv .venv`; activate or use the direct path; verify executable and pip; deactivate when done. Next, learn to install and record packages.

## Official references

- [Python venv](https://docs.python.org/3.13/library/venv.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [VS Code environments](https://code.visualstudio.com/docs/python/environments)

<!-- chapter-navigation:bottom -->
[← Previous](../03-run-your-first-program/README.md) · [Module index](../README.md) · [Next →](../05-packages-and-dependencies/README.md)
<!-- /chapter-navigation:bottom -->

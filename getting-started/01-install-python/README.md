# Install Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[Module index](../README.md) · [Next →](../02-configure-vscode/README.md)
<!-- /chapter-navigation:top -->

## Goal and prerequisites

**Level:** absolute beginner. **Estimated time:** 20–40 minutes, excluding downloads. You need a supported desktop OS and permission to install software. You will finish with a terminal command that identifies Python and its executable.

Python is the language; the interpreter is the application that executes Python code. Downloading an editor alone does not install the interpreter. Use official sources, not third-party download advertisements. This guide tests Python 3.13 in CI. Prefer a supported 3.13 patch release for consistency; another supported Python 3 version can run this introductory exercise, but later chapters and dependency versions may differ.

## 1. Check before installing

Open PowerShell on Windows, Terminal on macOS or a terminal on Linux. Type the command, then press Enter. Do not type any prompt symbols such as `PS>` or `$`.

Windows:

```powershell
py -3.13 --version
```

macOS or Linux:

```bash
python3 --version
```

If you already have the intended version, skip installation. If a command is missing or the version differs, follow your OS instructions below. A version such as `Python 3.13.x` is illustrative; the last number is a patch release.

## 2. Windows

Open the [official Python downloads](https://www.python.org/downloads/). Choose the Python install manager for Windows on a supported system, install it and follow its configuration prompts. Open a new PowerShell window. With the manager installed, run:

```powershell
py install 3.13
py -3.13 --version
py -3.13 -c "import sys; print(sys.executable)"
```

The second command reports the version; the third prints the interpreter's actual location. On a machine with an older traditional installer, `py -3.13` may already work without the manager. If you use an official traditional installer that offers an **Add Python to PATH** option, select it before installation for convenient command lookup. Do not install an older insecure release just to obtain that option. If the existing launcher does not recognize `py install`, consult the install-manager troubleshooting guide before changing it.

`PATH` is a list of directories the shell searches for commands. The launcher can select a specific installed version even when `python` refers to a different version. Keep using the command you verified.

## 3. macOS

Download the macOS installer for a supported 3.13 release from [Python.org](https://www.python.org/downloads/), matching your OS and architecture. Open the installer, follow the steps and, when provided by the installer, run `Install Certificates.command` from the installed Python application folder to complete certificate setup. Open a fresh Terminal window:

```bash
python3.13 --version
python3.13 -c "import sys; print(sys.executable)"
```

If you use another supported installation, `python3` may be its command. Check its version and location. Do not replace or delete the operating system's Python.

## 4. Linux

Many distributions already include Python. Check `python3 --version` first. If absent, use your distribution's official package manager. For Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3
```

For Fedora (if not already installed):

```bash
sudo dnf install python3
```

Use administrative commands only on a machine you are authorized to manage. Confirm:

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

The distribution may supply a different supported Python 3 version. If it is not 3.13, check the distribution's documented parallel installation options or ask the machine administrator; do not replace the system interpreter, change system symlinks or run an untrusted installer. If a separate `python3.13` is available, verify and use it. The first program works on supported Python 3 versions; later examples may require the guide's tested version.

## 5. Troubleshooting

| Symptom | What to check |
| --- | --- |
| Command not found | Reopen the terminal; verify installation and the OS-specific command. |
| Windows opens a store or a different Python | Use `py -3.13 --version`; consult official alias/launcher troubleshooting if it fails. |
| Version differs from expected | Inspect the executable location; choose the intended interpreter instead of reinstalling blindly. |
| `>>>` appears | You entered Python's interactive prompt. Type `exit()` and press Enter to return to the shell. |
| Permission or installation failure | Use official instructions or ask the administrator; never bypass security controls. |

## Practice and quick reference

Run the version and executable-location checks for your OS and note the result. Explain in your own words what the interpreter does. Keep the verified command for the next lessons. You do not need to install packages for this module.

## Official references

- [Python downloads](https://www.python.org/downloads/)
- [Python install manager and troubleshooting on Windows](https://docs.python.org/3.14/using/windows.html)
- [Python 3.13 Windows installation and launcher](https://docs.python.org/3.13/using/windows.html)
- [Python 3.13 on macOS](https://docs.python.org/3.13/using/mac.html)
- [Python setup on Ubuntu](https://documentation.ubuntu.com/ubuntu-for-developers/howto/python-setup/)
- [Python on Fedora](https://developer.fedoraproject.org/tech/languages/python/python-installation.html)

<!-- chapter-navigation:bottom -->
[Module index](../README.md) · [Next →](../02-configure-vscode/README.md)
<!-- /chapter-navigation:bottom -->

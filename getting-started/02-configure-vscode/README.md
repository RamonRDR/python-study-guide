# Configure VS Code

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../01-install-python/README.md) · [Module index](../README.md) · [Next →](../03-run-your-first-program/README.md)
<!-- /chapter-navigation:top -->

## Goal and prerequisites

**Level:** absolute beginner. **Estimated time:** 20–30 minutes, excluding downloads. Complete the previous lesson and keep your verified Python command. VS Code is a free desktop code editor. Its Python extension helps the editor communicate with the interpreter; it does not replace the interpreter. You can use another plain-text editor and a terminal instead. No account, AI tool or extra package is required.

## 1. Install Visual Studio Code

Use the [official VS Code download page](https://code.visualstudio.com/download). Choose the build for your OS and architecture.

- **Windows:** download the User Installer, open it and follow the prompts. Adding VS Code to PATH, if offered, is optional for this guide; it enables the separate `code` command.
- **macOS:** download the appropriate build, open the downloaded archive if needed and move Visual Studio Code to Applications.
- **Linux:** choose the package supported by your distribution (for example, .deb for Debian/Ubuntu or .rpm for Fedora). Follow the official Linux setup instructions, including any required package manager steps.

Do not use unofficial downloads or grant administrator privileges unnecessarily. Open VS Code after installation.

## 2. Install the Python extension

1. Open the Extensions view from the activity bar (the icon made of squares).
2. Search for **Python**.
3. Choose the extension published by **Microsoft** (identifier `ms-python.python`) and click Install.
4. Follow any required restart/reload prompts. Other companion extensions may be installed automatically; no separate AI extension is required.

## 3. Open a learning folder

Create an empty folder named `python-practice` in a personal, writable location using your OS file manager. In VS Code, choose **File > Open Folder** and select it. This is your workspace, not the Python installation directory. If Workspace Trust asks about the folder, trust it only if you created it or understand its contents; never trust unknown downloaded code automatically.

## 4. Select the interpreter

Open the Command Palette using `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS). Search for **Python: Select Interpreter** and select the installed interpreter you verified earlier. If necessary, choose Enter interpreter path and locate the executable reported by the previous lesson. The version shown in the editor should match your intended Python. If you already use a virtual environment, select its interpreter deliberately. For now use the verified interpreter; [Chapter 04](../04-virtual-environments/README.md) teaches how to create and select a project-local environment after the first program.

## 5. Verify in the integrated terminal

Choose **Terminal > New Terminal**. A terminal is where you enter shell commands and view their output. Use the same verified command as before:

Windows:

```powershell
py -3.13 --version
py -3.13 -c "import sys; print(sys.executable)"
```

macOS (official 3.13 installation):

```bash
python3.13 --version
python3.13 -c "import sys; print(sys.executable)"
```

Linux (or another verified Python 3 installation on macOS):

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

If a different command was verified earlier, use it instead. Compare the executable to the interpreter selected in VS Code. Selecting an interpreter controls extension actions, but a shell command can still select another installed Python. Close and reopen the integrated terminal after changing the interpreter; if paths still differ, choose the appropriate verified command or use the selected interpreter's executable path.

## 6. Troubleshooting

| Symptom | Action |
| --- | --- |
| Python command works outside VS Code only | Restart VS Code completely so it inherits the updated environment. |
| Python: Select Interpreter is absent | Check that the Microsoft Python extension is installed and enabled. |
| Wrong interpreter | Select the intended executable and compare its path again. |
| Cannot save files | Open a personal writable folder; do not work inside the Python installation. |
| Editor differs from screenshots or menu language | Use the Command Palette and look for the equivalent translated command. |

## Practice and quick reference

Open your practice folder, locate the Explorer and integrated terminal, select the interpreter and verify its version and location. Explain the difference between an editor, an interpreter and a terminal. Keep the folder open for the next lesson.

## Official references

- [VS Code downloads](https://code.visualstudio.com/download)
- [VS Code installation](https://code.visualstudio.com/docs/getstarted/overview)
- [VS Code Linux setup](https://code.visualstudio.com/docs/setup/linux)
- [Python in VS Code tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
- [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

<!-- chapter-navigation:bottom -->
[← Previous](../01-install-python/README.md) · [Module index](../README.md) · [Next →](../03-run-your-first-program/README.md)
<!-- /chapter-navigation:bottom -->

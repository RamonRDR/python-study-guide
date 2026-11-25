# Packages and Dependency Management

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../04-virtual-environments/README.md) · [Module index](../README.md) · [Next →](../06-git-and-version-control/README.md)
<!-- /chapter-navigation:top -->

## Goal

**Level:** absolute beginner. **Estimated time:** 30–45 minutes. Use the project environment created in Chapter 04. A dependency is software your project needs to work. Python already provides a standard library (for example, pathlib); third-party packages are installed separately. pip is Python's package installer and normally retrieves packages from the Python Package Index (PyPI). Install only what your project needs.

## 1. Install one package

Activate your project's .venv and confirm `python -m pip --version` points to it. If activation is unavailable, substitute the direct environment executable from Chapter 04 for python in every command below. With internet access, install the official Requests package:

```shell
python -m pip install requests
python -m pip show requests
python -m pip list
python -m pip check
```

pip can install dependencies of Requests too. The check command detects inconsistent installed requirements; it does not establish that a package is safe. Check the exact package name, publisher, official documentation and supported Python version before installing. Avoid untrusted install commands, global installation and sudo pip.

Create `check_package.py` beside first_program.py (not inside .venv):

```python
from importlib.metadata import version

print(version("requests"))
```

Run `python check_package.py`. It should display the installed version (the number varies). No HTTP request is made. You will learn imports and HTTP usage later. The package name used for installation is not always the name imported in code (beautifulsoup4 uses bs4, for example).

## 2. Record dependencies

From the clean practice environment, capture installed package versions to a new file:

```shell
python -m pip freeze > requirements.txt
```

This overwrites requirements.txt; review the file before committing. In Windows PowerShell 5.1 use `python -m pip freeze | Out-File -Encoding ascii requirements.txt` for this simple ASCII package list to avoid UTF-16 output. Do not overwrite an existing hand-maintained dependency contract blindly. A freeze records installed versions, including indirect dependencies; it is not a complete cross-platform lockfile. Record the Python version separately. Do not include private package URLs, secrets or local machine paths.

A project may instead maintain a requirements.txt with only its direct dependencies and supported version ranges, then resolve or lock the complete set with appropriate tooling. The guide's own [requirements-external.txt](../../requirements-external.txt) is a separate, maintained contract for its existing examples; do not replace it with your practice freeze.

## 3. Recreate and compare

Leave the activated shell with deactivate. Create a second practice folder using the file manager. Copy only your source files and requirements.txt into it, not .venv. Open that folder, create and activate its own environment following Chapter 04 using the same Python version, verify its executable and install:

```shell
python -m pip install -r requirements.txt
python -m pip check
python check_package.py
```

Compare the version printed in both environments. This demonstrates recreation on your machine; compatibility can differ on another OS or Python version. For removal, use `python -m pip uninstall requests` in the intended environment only; dependencies are not automatically removed. Do not uninstall from a real project merely to practice.

## 4. Library map

| Package | Purpose | Guide |
| --- | --- | --- |
| `pandas` | Data analysis | [Chapter](../../external-libraries/01-pandas/README.md) |
| `openpyxl` | Excel workbook automation | [Chapter](../../external-libraries/02-openpyxl/README.md) |
| `requests` | HTTP and APIs | [Chapter](../../external-libraries/03-requests/README.md) |
| `pytest` | Automated testing | [Chapter](../../external-libraries/04-pytest/README.md) |
| `numpy` | Numerical arrays | Future candidate |
| `playwright` | Browser automation | Future candidate |
| `selenium` | Browser automation | Future candidate |
| `beautifulsoup4` | HTML parsing | Future candidate |
| `httpx` | HTTP clients, including async | Future candidate |
| `fastapi` | API development | Future candidate |
| `pydantic` | Data validation | Future candidate |
| `sqlalchemy` | Database access and ORM | Future candidate |
| `matplotlib` | Data visualization | Future candidate |
| `python-dotenv` | Read configuration from .env files | Future candidate |

The four existing chapters are the tested curriculum. Other entries are candidates for later lessons, not required installations or tested contracts. Some need additional resources: Playwright, for instance, downloads browser binaries separately from its Python package. For an optional, authorized experiment in a separate environment, the [official library guide](https://playwright.dev/python/docs/library) describes:

```shell
python -m pip install playwright
python -m playwright install chromium
```

Browser downloads require network access, storage and sometimes OS dependencies. They may be cached outside .venv. Do not run this for the required exercise, and do not add Playwright to the repository dependency file merely because it is listed here.

## 5. Practice and quick reference

- [ ] Verify the active interpreter and pip location.
- [ ] Install Requests in the practice environment and inspect its version.
- [ ] Save requirements.txt and recreate the environment in a second folder.
- [ ] Explain why source and requirements are committed but .venv is not.

If installation fails, read the error, confirm Python compatibility and internet access, and verify the environment. Do not bypass certificate or security checks. If an import fails, compare the interpreter used for installation with the interpreter used to run the file.

**Quick reference:** install with python -m pip install PACKAGE, inspect with show/list, check with check, record with freeze, recreate with install -r requirements.txt. Continue to [Git basics](../06-git-and-version-control/README.md) to record your project safely before Fundamentals.

## Official references

- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
- [Python Package Index](https://pypi.org/)
- [Playwright browsers](https://playwright.dev/python/docs/browsers)

<!-- chapter-navigation:bottom -->
[← Previous](../04-virtual-environments/README.md) · [Module index](../README.md) · [Next →](../06-git-and-version-control/README.md)
<!-- /chapter-navigation:bottom -->

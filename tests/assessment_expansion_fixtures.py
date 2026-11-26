"""Trusted expansion fixtures; never execute code read from assessment records."""

EXPECTED = {}
CODE_FIXTURES = {}
EXPECTED["quiz.hash-inside-string"] = (False, True)
EXPECTED["quiz.docstring-first-statement"] = (True, False)
EXPECTED["quiz.docstring-runtime-attribute"] = ("__doc__", "__name__")
CODE_FIXTURES["quiz.docstring-runtime-attribute"] = ("def ping():\n    \"\"\"Check availability.\"\"\"\n    return True\n\ndescription = ping.____", "def ping():\n    \"\"\"Check availability.\"\"\"\n    return True\n\ndescription = ping.__doc__\nassert description == \"Check availability.\"", "", None)
EXPECTED["quiz.name-with-explicit-unit"] = ("milliseconds", "generic")
EXPECTED["quiz.task-marker-no-runtime"] = (False, True)
EXPECTED["quiz.log-fallback-level"] = ("warning", "debug")
EXPECTED["quiz.pep8-guidance-not-syntax"] = (False, True)
EXPECTED["quiz.none-check-preserve-zero"] = ("identity", "not-count")

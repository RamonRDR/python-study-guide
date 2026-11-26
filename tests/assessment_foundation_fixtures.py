"""Trusted literal fixtures for foundation quizzes; never load learner code."""

EXPECTED = {}
CODE_FIXTURES = {}
EXPECTED["quiz.unsaved-source-edit"] = (True, False)
EXPECTED["quiz.venv-direct-executable"] = (True, False)
EXPECTED["quiz.venv-recreate"] = ("recreate", "copy-venv")
EXPECTED["quiz.install-declared-requirements"] = ("install", "freeze")
EXPECTED["quiz.git-inspect-staged"] = ("cached", "add")

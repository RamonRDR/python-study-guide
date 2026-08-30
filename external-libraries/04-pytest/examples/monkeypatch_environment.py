from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


TEST_SOURCE = '''
import os


def read_mode() -> str:
    return os.getenv("STUDY_MODE", "default")


def test_default_mode(monkeypatch) -> None:
    monkeypatch.delenv("STUDY_MODE", raising=False)
    assert read_mode() == "default"


def test_configured_mode(monkeypatch) -> None:
    monkeypatch.setenv("STUDY_MODE", "focused")
    assert read_mode() == "focused"
'''


class ResultCounter:
    def __init__(self) -> None:
        self.passed = 0

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        if report.when == "call" and report.passed:
            self.passed += 1


def run_suite() -> tuple[int, int]:
    with TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test_environment.py"
        test_file.write_text(TEST_SOURCE, encoding="utf-8")
        counter = ResultCounter()
        captured = StringIO()
        with redirect_stdout(captured), redirect_stderr(captured):
            exit_code = pytest.main(
                [str(test_file), "-q", "-p", "no:cacheprovider"],
                plugins=[counter],
            )
        return int(exit_code), counter.passed


if __name__ == "__main__":
    exit_code, passed = run_suite()
    print(f"exit code: {exit_code}")
    print(f"passed: {passed}")

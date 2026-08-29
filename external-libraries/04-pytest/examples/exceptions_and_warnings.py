from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


TEST_SOURCE = '''
import warnings

import pytest


def parse_positive(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise ValueError("value must be positive")
    return number


def legacy_parser() -> str:
    warnings.warn("legacy parser", DeprecationWarning, stacklevel=2)
    return "ok"


def test_invalid_value_raises() -> None:
    with pytest.raises(ValueError, match="must be positive"):
        parse_positive("0")


def test_warning_is_explicit() -> None:
    with pytest.warns(DeprecationWarning, match="legacy parser"):
        assert legacy_parser() == "ok"
'''


class ResultCounter:
    def __init__(self) -> None:
        self.passed = 0

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        if report.when == "call" and report.passed:
            self.passed += 1


def run_suite() -> tuple[int, int]:
    with TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test_failures.py"
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

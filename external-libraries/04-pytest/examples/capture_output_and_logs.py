from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


TEST_SOURCE = '''
import logging


def announce(topic: str) -> None:
    print(f"Studying: {topic}")


def record_status(logger: logging.Logger) -> None:
    logger.info("study session ready")


def test_stdout_capture(capsys) -> None:
    announce("pytest")
    captured = capsys.readouterr()
    assert captured.out == "Studying: pytest\\n"
    assert captured.err == ""


def test_log_capture(caplog) -> None:
    logger = logging.getLogger("study.example")
    with caplog.at_level(logging.INFO, logger="study.example"):
        record_status(logger)
    assert "study session ready" in caplog.text
'''


class ResultCounter:
    def __init__(self) -> None:
        self.passed = 0

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        if report.when == "call" and report.passed:
            self.passed += 1


def run_suite() -> tuple[int, int]:
    with TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test_capture.py"
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

from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


TEST_SOURCE = '''
import pytest


def normalize_score(score: int) -> int:
    return max(0, min(score, 100))


def test_normalize_score_keeps_valid_value() -> None:
    assert normalize_score(82) == 82


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(-5, 0), (40, 40), (130, 100)],
)
def test_normalize_score_boundaries(raw: int, expected: int) -> None:
    assert normalize_score(raw) == expected
'''


class ResultCounter:
    def __init__(self) -> None:
        self.passed = 0

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        if report.when == "call" and report.passed:
            self.passed += 1


def run_suite() -> tuple[int, int]:
    with TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test_scores.py"
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

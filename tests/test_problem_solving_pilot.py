"""Expose the trusted pilot tests to the repository unittest discovery."""

from pathlib import Path
import runpy


PILOT = (Path(__file__).resolve().parents[1] / "exercises" /
         "problem-solving" / "vowel-counter" / "test_solution.py")


def load_tests(loader, standard_tests, pattern):
    namespace = runpy.run_path(str(PILOT))
    return loader.loadTestsFromTestCase(namespace["VowelCounterTests"])

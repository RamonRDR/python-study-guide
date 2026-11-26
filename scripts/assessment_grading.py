"""Deterministic grading primitives; never evaluate submitted source text."""
from copy import deepcopy
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO


def exact_equal(actual, expected):
    """Compare JSON-shaped values recursively, including key and value types."""
    if type(actual) is not type(expected):
        return False
    if type(expected) is list:
        return len(actual) == len(expected) and all(
            exact_equal(a, b) for a, b in zip(actual, expected)
        )
    if type(expected) is dict:
        if any(type(key) is not str for key in actual):
            return False
        return actual.keys() == expected.keys() and all(
            exact_equal(actual[key], value) for key, value in expected.items()
        )
    return actual == expected


def normalize_text(value, comparison):
    if comparison == "exact":
        return value
    if comparison == "normalize_lf":
        return value.replace("\r\n", "\n").replace("\r", "\n")
    raise ValueError("unsupported comparison")


def grade_quiz(record, response):
    """Grade a validated quiz record; malformed responses raise ValueError."""
    kind, answer = record["type"], record["answer"]
    if kind in ("multiple_choice", "error_identification"):
        if type(response) is not str or response not in {
            choice["id"] for choice in record["choices"]
        }:
            raise ValueError("response must be a known choice ID")
        return response == answer["choice_id"]
    if kind == "true_false":
        if type(response) is not bool:
            raise ValueError("response must be boolean")
        return response is answer["value"]
    if kind in ("output_prediction", "objective_code_completion"):
        if type(response) is not str:
            raise ValueError("response must be text")
        comparison = answer["comparison"]
        value = normalize_text(response, comparison)
        return any(value == normalize_text(a, comparison) for a in answer["accepted"])
    raise ValueError("unsupported quiz type")


def case_passes(candidate, case, *, new_container=False):
    """Call only trusted finite fixtures/references. Not a sandbox or timeout."""
    args = deepcopy(case["args"])
    before = deepcopy(args)
    stdout, stderr = StringIO(), StringIO()
    try:
        with redirect_stdout(stdout), redirect_stderr(stderr):
            actual = candidate(*args)
    except Exception:
        return False
    return (
        exact_equal(actual, case["expected"])
        and exact_equal(args, before)
        and not stdout.getvalue()
        and not stderr.getvalue()
        and not (
            new_container and type(actual) in (list, dict)
            and any(actual is arg for arg in args)
        )
    )

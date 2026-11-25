"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(value: int, lower: int, upper: int) -> int:
    return min(value, upper)

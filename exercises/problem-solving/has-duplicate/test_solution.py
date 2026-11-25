"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list[int]) -> bool:
    return len(values) == len(set(values))

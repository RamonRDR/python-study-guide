"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list[int], threshold: int) -> int:
    return sum(value > threshold for value in values)

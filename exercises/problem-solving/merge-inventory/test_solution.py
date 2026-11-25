"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    result = first.copy()
    result.update(second)
    return result

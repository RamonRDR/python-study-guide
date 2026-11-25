"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(first: list[int], second: list[int]) -> list[int]:
    return sorted(set(first + second))

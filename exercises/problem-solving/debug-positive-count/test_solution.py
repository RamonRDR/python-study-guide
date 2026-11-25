"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list[int]) -> int:
    count = 0
    for value in values:
        if value >= 0:
            count += 1
    return count

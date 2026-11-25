"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list[int], target: int) -> int:
    result = -1
    for index, value in enumerate(values):
        if value == target:
            result = index
    return result

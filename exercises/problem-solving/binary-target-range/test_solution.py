"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list[int], target: int) -> list[int]:
    for index, value in enumerate(values):
        if value == target:
            return [index, index]
    return [-1, -1]

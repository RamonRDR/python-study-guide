"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list[int], target: int) -> int:
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] <= target:
            left = middle + 1
        else:
            right = middle
    return left

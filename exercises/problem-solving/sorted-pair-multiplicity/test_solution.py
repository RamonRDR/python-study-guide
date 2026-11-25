"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list[int], target: int) -> int:
    left, right = 0, len(values) - 1
    count = 0
    while left < right:
        total = values[left] + values[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            count += 1
            left += 1
            right -= 1
    return count

"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list[int], size: int) -> int:
    total = 0
    for index in range(size):
        total += values[index]
    best = max(0, total)
    for index in range(size, len(values)):
        total += values[index] - values[index - size]
        best = max(best, total)
    return best

"""Reference solution for debug-negative-window."""


def max_window_sum(values: list[int], size: int) -> int:
    total = 0
    for index in range(size):
        total += values[index]
    best = total
    for index in range(size, len(values)):
        total += values[index] - values[index - size]
        best = max(best, total)
    return best

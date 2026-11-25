"""Independent practice starter."""


def max_window_sum(values: list[int], size: int) -> int:
    total = 0
    for index in range(size):
        total += values[index]
    best = max(0, total)
    for index in range(size, len(values)):
        total += values[index] - values[index - size]
        best = max(best, total)
    return best

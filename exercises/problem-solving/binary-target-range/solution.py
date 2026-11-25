"""Reference solution for binary-target-range."""


def target_range(values: list[int], target: int) -> list[int]:
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    first = left
    if first == len(values) or values[first] != target:
        return [-1, -1]
    right = len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] <= target:
            left = middle + 1
        else:
            right = middle
    return [first, left - 1]

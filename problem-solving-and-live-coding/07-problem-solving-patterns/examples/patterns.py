"""Demonstrate frequency counting, two pointers and a fixed window."""


def frequencies(items: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def has_pair_sum(values: list[int], target: int) -> bool:
    """Require ascending sorted input; use distinct positions."""
    left, right = 0, len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if total == target:
            return True
        if total < target:
            left += 1
        else:
            right -= 1
    return False


def max_window_sum(values: list[int], size: int) -> int:
    """Require an integer list and an exact integer window size."""
    if type(size) is not int:
        raise TypeError("Expected an exact integer window size")
    if not 1 <= size <= len(values):
        raise ValueError("Window size outside input")
    total = 0
    for index in range(size):
        total += values[index]
    best = total
    for index in range(size, len(values)):
        total += values[index] - values[index - size]
        best = max(best, total)
    return best


if __name__ == "__main__":
    assert frequencies(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert has_pair_sum([1, 3, 6, 8], 9)
    assert not has_pair_sum([4], 8)
    print(max_window_sum([4, -1, 3, 2], 2))

"""Find the first matching index using two search strategies."""


def linear_search(values: list[int], target: int) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values: list[int], target: int) -> int:
    """Require ascending sorted input; return first match or -1."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    if left < len(values) and values[left] == target:
        return left
    return -1


if __name__ == "__main__":
    assert linear_search([8, 4, 4, 9], 4) == 1
    assert binary_search([], 4) == -1
    assert binary_search([2, 4, 4, 7, 9], 4) == 1
    print(binary_search([2, 4, 4, 7, 9], 4))

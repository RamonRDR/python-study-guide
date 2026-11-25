"""Independent practice starter."""


def count_positive(values: list[int]) -> int:
    count = 0
    for value in values:
        if value >= 0:
            count += 1
    return count

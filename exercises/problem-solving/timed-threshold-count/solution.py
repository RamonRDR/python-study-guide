"""Reference solution for timed-threshold-count."""


def count_at_least(values: list[int], threshold: int) -> int:
    count = 0
    for value in values:
        if value >= threshold:
            count += 1
    return count

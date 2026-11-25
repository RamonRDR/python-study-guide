"""Reference solution for timed-longest-streak."""


def longest_streak(values: list[int], threshold: int) -> int:
    current = best = 0
    for value in values:
        if value >= threshold:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best

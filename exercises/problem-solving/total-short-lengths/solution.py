"""Reference solution for total-short-lengths."""


def total_short_lengths(labels: list[str], limit: int) -> int:
    total = 0
    for label in labels:
        length = len(label)
        if length <= limit:
            total += length
    return total

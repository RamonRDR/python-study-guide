"""Reference solution for unordered-pair-count."""


def pair_count(size: int) -> int:
    return size * (size - 1) // 2

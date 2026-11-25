"""Reference solution for has-duplicate."""


def has_duplicate(values: list[int]) -> bool:
    seen = set()
    for value in values:
        if value in seen:
            return True
        seen.add(value)
    return False

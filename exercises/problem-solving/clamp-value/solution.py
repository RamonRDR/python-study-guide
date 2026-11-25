"""Reference solution for clamp-value."""


def clamp_value(value: int, lower: int, upper: int) -> int:
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value

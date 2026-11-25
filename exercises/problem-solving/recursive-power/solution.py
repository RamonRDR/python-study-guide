"""Reference solution for recursive-power."""


def integer_power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return base * integer_power(base, exponent - 1)

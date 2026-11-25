"""Reference solution for recursive-factorial."""


def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)

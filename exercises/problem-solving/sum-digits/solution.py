"""Reference solution for sum-digits."""


def sum_digits(number: int) -> int:
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

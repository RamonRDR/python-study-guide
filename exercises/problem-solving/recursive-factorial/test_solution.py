"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(number: int) -> int:
    if number == 0:
        return 0
    return number * wrong_solution(number - 1)

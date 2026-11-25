"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(total: int, member: bool) -> int:
    if total >= 100 and member:
        return 0
    return 12

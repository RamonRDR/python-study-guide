"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(labels: list[str]) -> dict[str, int]:
    return dict.fromkeys(labels, 1)

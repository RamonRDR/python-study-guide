"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(labels: list[str]) -> list[str]:
    return sorted(set(labels))

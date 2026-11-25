"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(labels: list[str], limit: int) -> int:
    count = 0
    for label in labels:
        if len(label) <= limit:
            count += 1
    return count

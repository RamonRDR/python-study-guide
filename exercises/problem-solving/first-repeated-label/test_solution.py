"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(labels: list[str]) -> str | None:
    for label in labels:
        if labels.count(label) > 1:
            return label
    return None

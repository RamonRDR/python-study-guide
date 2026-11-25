"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(text: str) -> bool:
    return text.lower() == text.lower()[::-1]

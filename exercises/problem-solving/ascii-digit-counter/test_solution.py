"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(text: str) -> int:
    return sum(character.isdigit() for character in text)

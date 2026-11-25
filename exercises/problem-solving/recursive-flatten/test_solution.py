"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(values: list) -> list[int]:
    result = []
    for item in values:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(expected: list[list], actual: list[list]) -> list[list]:
    expected_totals = dict(expected)
    actual_totals = dict(actual)
    result = []
    for label in dict.fromkeys(list(expected_totals) + list(actual_totals)):
        before = expected_totals.get(label, 0)
        after = actual_totals.get(label, 0)
        if before != after:
            result.append([label, before, after, after - before])
    return result

"""Trusted incorrect implementation for discrimination tests."""


def wrong_solution(scores: list[int]) -> dict[str, int]:
    passed = sum(score > 60 for score in scores)
    return {"total": len(scores), "passed": passed, "failed": len(scores) - passed}

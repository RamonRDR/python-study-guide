"""Reference solution for refactor-score-summary."""


def summarize_scores(scores: list[int]) -> dict[str, int]:
    passed = 0
    for score in scores:
        if score >= 60:
            passed += 1
    total = len(scores)
    return {"total": total, "passed": passed, "failed": total - passed}

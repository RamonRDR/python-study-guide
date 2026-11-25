"""Independent practice starter."""


def summarize_scores(scores: list[int]) -> dict[str, int]:
    a = 0
    for x in scores:
        if x >= 60:
            a += 1
    b = 0
    for x in scores:
        if x < 60:
            b += 1
    return {"total": len(scores), "passed": a, "failed": b}

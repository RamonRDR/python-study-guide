def classify_score(score: int) -> str:
    if score >= 80:
        return "ready"
    return "review"

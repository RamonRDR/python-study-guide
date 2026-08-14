def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"


def build_score_report(student: str, score: int) -> str:
    status = classify_score(score)
    return format_score_report(student, score, status)


print(build_score_report("Ava", 84))

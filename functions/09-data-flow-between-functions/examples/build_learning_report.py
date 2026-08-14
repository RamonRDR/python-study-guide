def summarize_sessions(sessions: list[int]) -> tuple[int, float]:
    total = sum(sessions)
    if not sessions:
        return total, 0.0
    return total, total / len(sessions)


def classify_total(total: int) -> str:
    if total >= 120:
        return "deep"
    if total >= 60:
        return "steady"
    return "light"


def build_learning_report(subject: str, sessions: list[int]) -> str:
    total, average = summarize_sessions(sessions)
    workload = classify_total(total)
    return (
        f"{subject}: {total} minutes, "
        f"average {average:.1f}, workload {workload}"
    )


print(build_learning_report("Python", [30, 45, 60]))

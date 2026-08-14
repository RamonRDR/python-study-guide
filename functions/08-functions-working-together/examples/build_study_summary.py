def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


def build_study_summary(subject: str, sessions: list[int]) -> str:
    total_minutes = calculate_total_minutes(sessions)
    workload = classify_workload(total_minutes)
    return f"{subject}: {total_minutes} minutes ({workload})"


print(build_study_summary("Python", [30, 45, 60]))

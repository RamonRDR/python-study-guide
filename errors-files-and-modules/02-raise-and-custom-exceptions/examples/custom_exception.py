class EmptyStudyPlanError(Exception):
    pass


def summarize_plan(topics: list[str]) -> str:
    if not topics:
        raise EmptyStudyPlanError("study plan must contain at least one topic")
    return ", ".join(topics)


plans = [["Functions", "Exceptions"], []]

for topics in plans:
    try:
        print(summarize_plan(topics))
    except EmptyStudyPlanError as error:
        print(f"Plan error: {error}")

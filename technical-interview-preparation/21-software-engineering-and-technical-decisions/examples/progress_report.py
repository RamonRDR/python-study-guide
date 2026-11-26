"""Separate a read-only reporting rule from its storage dependency."""
from collections.abc import Callable, Iterable


def progress_report(
    learner: str,
    load_completed: Callable[[str], Iterable[int]],
) -> dict[str, int]:
    if not isinstance(learner, str) or not learner.strip():
        raise ValueError("learner must be nonblank text")
    completed = set()
    for lesson_id in load_completed(learner):
        if type(lesson_id) is not int or lesson_id < 1:
            raise ValueError("invalid lesson identifier")
        completed.add(lesson_id)
    return {"completed": len(completed)}


if __name__ == "__main__":
    def load_completed(learner):
        return [1, 2, 2] if learner == "learner-a" else []

    print(progress_report("learner-a", load_completed))

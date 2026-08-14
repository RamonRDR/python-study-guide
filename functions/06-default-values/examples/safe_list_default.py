def add_task(task: str, tasks: list[str] | None = None) -> list[str]:
    if tasks is None:
        tasks = []

    tasks.append(task)
    return tasks


print(add_task("study"))
print(add_task("practice"))
print(add_task("review", ["plan"]))

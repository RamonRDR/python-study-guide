"""Reference solution for recursive-flatten."""


def flatten(values: list) -> list[int]:
    result = []

    def visit(items):
        for item in items:
            if isinstance(item, list):
                visit(item)
            else:
                result.append(item)

    visit(values)
    return result

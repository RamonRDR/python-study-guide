"""Reference solution for descending-insertion-sort."""


def descending_sort(values: list[int]) -> list[int]:
    result = values.copy()
    for index in range(1, len(result)):
        value = result[index]
        position = index
        while position > 0 and result[position - 1] < value:
            result[position] = result[position - 1]
            position -= 1
        result[position] = value
    return result

"""Return sorted copies using three elementary algorithms."""


def bubble_sort(values: list[int]) -> list[int]:
    result = values.copy()
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = (
                    result[index + 1], result[index]
                )
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(values: list[int]) -> list[int]:
    result = values.copy()
    for index in range(len(result)):
        minimum = index
        for candidate in range(index + 1, len(result)):
            if result[candidate] < result[minimum]:
                minimum = candidate
        result[index], result[minimum] = result[minimum], result[index]
    return result


def insertion_sort(values: list[int]) -> list[int]:
    result = values.copy()
    for index in range(1, len(result)):
        value = result[index]
        position = index
        while position > 0 and result[position - 1] > value:
            result[position] = result[position - 1]
            position -= 1
        result[position] = value
    return result


if __name__ == "__main__":
    original = [4, 2, 2, 1]
    for algorithm in (bubble_sort, selection_sort, insertion_sort):
        assert algorithm(original) == [1, 2, 2, 4]
        assert original == [4, 2, 2, 1]
    print(insertion_sort(original))

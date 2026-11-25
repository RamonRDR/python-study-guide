"""Reference solution for merge-inventory."""


def merge_inventory(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    result = first.copy()
    for label, quantity in second.items():
        result[label] = result.get(label, 0) + quantity
    return result

"""Reference solution for sorted-pair-multiplicity."""


def count_target_pairs(values: list[int], target: int) -> int:
    left, right = 0, len(values) - 1
    count = 0
    while left < right:
        total = values[left] + values[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        elif values[left] == values[right]:
            size = right - left + 1
            count += size * (size - 1) // 2
            break
        else:
            low, high = values[left], values[right]
            low_count = high_count = 0
            while left <= right and values[left] == low:
                low_count += 1
                left += 1
            while left <= right and values[right] == high:
                high_count += 1
                right -= 1
            count += low_count * high_count
    return count

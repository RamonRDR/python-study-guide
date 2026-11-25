"""Validate a fictional workshop capacity contract."""


def accepts_group(group_size: int, capacity: int) -> bool:
    if type(group_size) is not int or type(capacity) is not int:
        raise TypeError("Expected exact integers")
    if group_size < 0 or capacity < 1:
        raise ValueError("Invalid size or capacity")
    return 1 <= group_size <= capacity


if __name__ == "__main__":
    assert not accepts_group(0, 5)
    assert accepts_group(1, 5)
    assert accepts_group(5, 5)
    assert not accepts_group(6, 5)
    print(accepts_group(5, 5))

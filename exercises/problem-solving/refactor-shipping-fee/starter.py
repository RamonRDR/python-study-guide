"""Independent practice starter."""


def shipping_fee(total: int, member: bool) -> int:
    if total >= 100:
        return 0
    if member:
        return 0
    return 12

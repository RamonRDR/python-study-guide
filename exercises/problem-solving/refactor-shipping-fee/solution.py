"""Reference solution for refactor-shipping-fee."""


def shipping_fee(total: int, member: bool) -> int:
    if total >= 100 or member:
        return 0
    return 12

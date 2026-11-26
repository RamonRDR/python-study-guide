"""Convert text at a boundary without hiding invalid input."""


class InvalidQuantity(ValueError):
    """A quantity does not meet the input contract."""


def parse_quantity(text: str) -> int:
    if not isinstance(text, str):
        raise InvalidQuantity("quantity must be text")
    try:
        quantity = int(text)
    except ValueError as error:
        raise InvalidQuantity("quantity must be an integer") from error
    if quantity < 0:
        raise InvalidQuantity("quantity cannot be negative")
    return quantity


if __name__ == "__main__":
    print(parse_quantity(" 12 "))
    try:
        parse_quantity("unknown")
    except InvalidQuantity as error:
        print(error)

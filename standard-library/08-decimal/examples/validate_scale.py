from decimal import Context, Decimal, Inexact, InvalidOperation


TWO_PLACES = Decimal("0.01")
MAX_COEFFICIENT_DIGITS = 28
validator = Context(
    prec=MAX_COEFFICIENT_DIGITS,
    traps=[Inexact, InvalidOperation],
)


def normalize_two_places(raw_value: str) -> Decimal:
    value = Decimal(raw_value)

    if (
        not value.is_finite()
        or len(value.as_tuple().digits) > MAX_COEFFICIENT_DIGITS
    ):
        raise ValueError("unsupported decimal value")

    normalized = value.quantize(TWO_PLACES, context=validator)

    if not normalized.is_finite():
        raise ValueError("quantization produced a non-finite result")

    return normalized


for raw_value in [
    "12.50",
    "7.00",
    "3.141",
    "12345678901234567890123456789.00",
    "NaN",
]:
    try:
        normalized = normalize_two_places(raw_value)
    except (Inexact, InvalidOperation, ValueError):
        print(f"rejected: {raw_value}")
    else:
        print(f"accepted: {normalized}")

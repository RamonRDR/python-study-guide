from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")

unit_price = Decimal("19.95")
quantity = 3
discount = Decimal("2.50")

subtotal = unit_price * quantity
final_amount = (subtotal - discount).quantize(
    CENT,
    rounding=ROUND_HALF_UP,
)

print(f"subtotal: {subtotal}")
print(f"final: {final_amount}")

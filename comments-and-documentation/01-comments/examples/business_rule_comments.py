# A fictional workshop offers a discount for early registration.

from datetime import date


EARLY_REGISTRATION_DAYS = 14
EARLY_DISCOUNT_PERCENT = 10


def calculate_registration_fee(
    base_fee_cents,
    event_date,
    registration_date,
):
    days_before_event = (event_date - registration_date).days

    # The fictional policy includes the fourteenth day in the discount window,
    # so this comparison must remain inclusive.
    if days_before_event >= EARLY_REGISTRATION_DAYS:
        discount_cents = base_fee_cents * EARLY_DISCOUNT_PERCENT // 100
        return base_fee_cents - discount_cents

    return base_fee_cents


event_date = date(2030, 6, 30)

assert calculate_registration_fee(5000, event_date, date(2030, 6, 16)) == 4500
assert calculate_registration_fee(5000, event_date, date(2030, 6, 17)) == 5000

print(calculate_registration_fee(5000, event_date, date(2030, 6, 16)))

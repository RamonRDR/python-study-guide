from decimal import Decimal, getcontext, localcontext


default_precision = getcontext().prec

with localcontext(prec=8):
    result = Decimal(1) / Decimal(7)

print(f"default precision: {default_precision}")
print(f"local result: {result}")
print(f"restored precision: {getcontext().prec}")

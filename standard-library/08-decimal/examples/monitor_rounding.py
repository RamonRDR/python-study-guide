from decimal import Decimal, Inexact, Rounded, localcontext


with localcontext(prec=5) as context:
    context.clear_flags()
    result = Decimal(1) / Decimal(7)

    print(f"result: {result}")
    print(f"rounded: {context.flags[Rounded]}")
    print(f"inexact: {context.flags[Inexact]}")

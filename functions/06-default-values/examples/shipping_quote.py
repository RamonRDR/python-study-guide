def calculate_shipping(weight: float, rate: float = 2.5, handling: float = 3.0) -> float:
    return weight * rate + handling


print(calculate_shipping(4.0))
print(calculate_shipping(4.0, rate=3.0))
print(calculate_shipping(4.0, handling=0.0))

whole_number = 5
decimal_number = 5.0
is_available = True

print("Exact int:", type(whole_number) is int)
print("Number family:", isinstance(whole_number, (int, float)))
print("Float in number family:", isinstance(decimal_number, (int, float)))
print("Exact bool:", type(is_available) is bool)
print("Bool is int-compatible:", isinstance(is_available, int))

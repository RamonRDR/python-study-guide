from collections import Counter


required = Counter({"sensor": 4, "cable": 3, "case": 2})
packed = Counter({"sensor": 4, "cable": 1, "case": 3})

missing = required - packed
surplus = packed - required

print(f"required units: {required.total()}")
print(f"missing: {dict(missing)}")
print(f"surplus: {dict(surplus)}")

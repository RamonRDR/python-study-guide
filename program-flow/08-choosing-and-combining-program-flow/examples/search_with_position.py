items = ["pen", "book", "cable", "mug"]
target = "cable"

for position, item in enumerate(items, start=1):
    if item == target:
        print(f"Found {target} at position {position}")
        break
else:
    print(f"{target} not found")

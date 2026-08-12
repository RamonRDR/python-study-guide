codes = ["PEN", "BOOK", "MUG", "CABLE"]
target = "MUG"

for code in codes:
    print(f"Checking {code}")
    if code == target:
        print(f"Found {target}")
        break

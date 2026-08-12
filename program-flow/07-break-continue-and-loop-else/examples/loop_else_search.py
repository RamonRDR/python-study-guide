names = ["Ari", "Mina", "Leo"]
target = "Nora"

for name in names:
    if name == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} was not found")

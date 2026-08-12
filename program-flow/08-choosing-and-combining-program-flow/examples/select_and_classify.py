scores = [92, 67, 81, 45]

for score in scores:
    if score >= 90:
        label = "excellent"
    elif score >= 70:
        label = "ready"
    else:
        label = "review"

    print(f"{score}: {label}")

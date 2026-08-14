def clamp_score(score: int) -> int:
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score


def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


raw_score = 108
clean_score = clamp_score(raw_score)
status = classify_score(clean_score)

print(f"Raw: {raw_score}")
print(f"Clean: {clean_score}")
print(f"Status: {status}")

def classify_score(score):
    if score >= 90:
        return "excellent"

    if score >= 60:
        return "passing"

    return "needs review"


print(classify_score(95))
print(classify_score(72))
print(classify_score(40))

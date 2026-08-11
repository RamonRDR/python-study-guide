scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)

print("Passing scores:", passing_scores)
print("Passing count:", len(passing_scores))

scores = [8, 10, 7, 9, 10]

scores[2] = 8
scores.append(9)

print("Tens:", scores.count(10))
print("First ten index:", scores.index(10))

scores.sort()

print("Sorted:", scores)
print("Lowest:", min(scores))
print("Highest:", max(scores))
print("Total:", sum(scores))

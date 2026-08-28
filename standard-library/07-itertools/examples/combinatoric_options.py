"""Generate a small deterministic option space with itertools."""

from itertools import combinations, product

regions = ["north", "south"]
levels = ["basic", "pro"]
plans = list(product(regions, levels))
review_pairs = list(combinations(["A", "B", "C"], 2))

print(plans)
print(review_pairs)

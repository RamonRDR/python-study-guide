def calculate_average(first_score: float, *scores: float) -> float:
    return (first_score + sum(scores)) / (1 + len(scores))


print(calculate_average(8.0, 9.0, 10.0))

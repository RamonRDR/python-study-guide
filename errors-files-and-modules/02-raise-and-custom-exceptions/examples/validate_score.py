def validate_score(score: int) -> int:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score


scores = [85, 120]

for score in scores:
    try:
        valid_score = validate_score(score)
    except ValueError as error:
        print(f"Rejected {score}: {error}")
    else:
        print(f"Accepted {valid_score}")

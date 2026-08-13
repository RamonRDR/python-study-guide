def show_score_status(name, score):
    if score >= 70:
        print(f"{name}: ready")
    else:
        print(f"{name}: review")


show_score_status("Ana", 82)
show_score_status("Luis", 61)

from grade_calculator import GradeCalculator, format_report


def main() -> None:
    calculator = GradeCalculator()
    calculator.add("Homework", "82.50", "20")
    calculator.add("Midterm", "91", "30")
    calculator.add("Project", "88.25", "20")
    calculator.add("Final exam", "94", "30")

    print(format_report(calculator.final_report()))


if __name__ == "__main__":
    main()

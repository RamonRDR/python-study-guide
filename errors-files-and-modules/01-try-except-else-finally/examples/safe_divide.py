def safe_divide(numerator_text: str, denominator_text: str) -> str:
    try:
        numerator = float(numerator_text)
        denominator = float(denominator_text)
        result = numerator / denominator
    except ValueError:
        return "invalid number"
    except ZeroDivisionError:
        return "division by zero"
    else:
        return f"result: {result:.2f}"


print(safe_divide("12", "4"))
print(safe_divide("twelve", "4"))
print(safe_divide("12", "0"))

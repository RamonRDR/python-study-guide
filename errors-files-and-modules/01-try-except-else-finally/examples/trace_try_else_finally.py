def inspect_number(text: str) -> None:
    print(f"start: {text!r}")

    try:
        value = int(text)
    except ValueError:
        print("except: invalid integer")
    else:
        print(f"else: parsed {value}")
    finally:
        print("finally: finished attempt")

    print("after try")


inspect_number("12")
print("---")
inspect_number("twelve")

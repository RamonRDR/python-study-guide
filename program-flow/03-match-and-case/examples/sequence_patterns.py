event = ("move", 4, -2)

match event:
    case ("move", x, y):
        print(f"Move to: {x}, {y}")
    case ("message", text):
        print(f"Message: {text}")
    case _:
        print("Unknown event")

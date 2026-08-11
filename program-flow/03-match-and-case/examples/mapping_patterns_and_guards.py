request = {
    "action": "open",
    "resource": "chapter",
    "level": 2,
    "theme": "dark",
}

match request:
    case {"action": "open", "resource": resource, "level": level} if level >= 2:
        print(f"Open advanced resource: {resource}")
    case {"action": "open", "resource": resource}:
        print(f"Open resource: {resource}")
    case _:
        print("Unsupported request")

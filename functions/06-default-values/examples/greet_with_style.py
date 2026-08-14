def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"


print(greet("Avery"))
print(greet("Avery", greeting="Welcome"))
print(greet("Avery", punctuation="."))

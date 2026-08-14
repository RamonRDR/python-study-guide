def display_settings(**settings: str) -> None:
    for name, value in settings.items():
        print(f"{name}: {value}")


display_settings(theme="dark", language="English")

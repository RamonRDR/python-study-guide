settings = {
    "theme": "light",
    "language": "en",
}

settings["theme"] = "dark"
settings["autosave"] = True
removed_language = settings.pop("language")

print("Removed:", removed_language)
print("Settings:", settings)

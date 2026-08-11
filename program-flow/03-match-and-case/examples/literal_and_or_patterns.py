command = "pause"

match command:
    case "start" | "resume":
        message = "Session running"
    case "pause":
        message = "Session paused"
    case "stop":
        message = "Session stopped"
    case _:
        message = "Unknown command"

print(message)

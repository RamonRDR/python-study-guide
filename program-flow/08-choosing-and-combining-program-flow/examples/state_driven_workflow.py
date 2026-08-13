state = "queued"
processed_steps = 0

while state != "done":
    match state:
        case "queued":
            print("Preparing")
            state = "running"
        case "running":
            print("Processing")
            processed_steps += 1

            if processed_steps >= 2:
                state = "done"
        case _:
            print("Unknown state")
            break

print(f"Final state: {state}")

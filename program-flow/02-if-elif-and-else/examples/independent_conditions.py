minutes = 50
completed = True

if completed:
    print("Session completed")

if minutes >= 30:
    print("At least 30 minutes")

if minutes >= 60:
    session_type = "Extended"
elif minutes >= 30:
    session_type = "Focused"
else:
    session_type = "Short"

print("Session type:", session_type)

from collections import deque


recent_events: deque[str] = deque(maxlen=3)

for event in ["boot", "load-config", "connect", "ready", "heartbeat"]:
    recent_events.append(event)

print(f"window: {list(recent_events)}")
print(f"oldest retained: {recent_events[0]}")
print(f"newest retained: {recent_events[-1]}")

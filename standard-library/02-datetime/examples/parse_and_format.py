from datetime import datetime

text = "2026-08-27 19:45"
moment = datetime.strptime(text, "%Y-%m-%d %H:%M")

print(moment.isoformat(timespec="minutes"))
print(moment.strftime("%d/%m/%Y %H:%M"))

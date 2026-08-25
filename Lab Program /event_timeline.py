events = [
    ("2026-08-25 09:10:00", "User login"),
    ("2026-08-25 09:15:00", "evidence.txt created"),
    ("2026-08-25 09:20:00", "Suspicious process executed"),
    ("2026-08-25 09:25:00", "evidence.txt modified")
]

# Sort events by timestamp
events.sort()

print("===== DIGITAL EVENT TIMELINE =====")

for timestamp, event in events:
    print(timestamp, "-", event)

output:
===== DIGITAL EVENT TIMELINE =====
2026-08-25 09:10:00 - User login
2026-08-25 09:15:00 - evidence.txt created
2026-08-25 09:20:00 - Suspicious process executed
2026-08-25 09:25:00 - evidence.txt modified

from collections import Counter

event_log = [
    "4625 user1 192.168.1.20",
    "4625 admin 192.168.1.50",
    "4625 admin 192.168.1.50",
    "4625 admin 192.168.1.50",
    "4625 admin 192.168.1.50",
    "4624 user2 192.168.1.30"
]

failed_logins = Counter()

for event in event_log:
    event_id, user, ip = event.split()

    if event_id == "4625":
        failed_logins[ip] += 1

print("===== WINDOWS EVENT LOG ANALYSIS =====")

for ip, count in failed_logins.items():
    print(ip, "-", count, "failed attempts")

    if count >= 3:
        print("ALERT: Repeated failed login attempts from", ip)

output:
===== WINDOWS EVENT LOG ANALYSIS =====
192.168.1.20 - 1 failed attempts
192.168.1.50 - 4 failed attempts
ALERT: Repeated failed login attempts from 192.168.1.50

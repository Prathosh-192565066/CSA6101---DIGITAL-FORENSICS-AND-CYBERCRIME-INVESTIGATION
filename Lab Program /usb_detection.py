usb_log = [
    "08:10 Kingston-123 AUTHORIZED",
    "09:20 Unknown-999 UNAUTHORIZED",
    "10:30 SanDisk-456 AUTHORIZED",
    "11:45 Unknown-777 UNAUTHORIZED"
]

print("===== USB ACTIVITY ANALYSIS =====")

for record in usb_log:
    time, device, status = record.split()

    if status == "UNAUTHORIZED":
        print("ALERT: Unauthorized USB detected")
        print("Time:", time, "| Device:", device)

output:
===== USB ACTIVITY ANALYSIS =====
ALERT: Unauthorized USB detected
Time: 09:20 | Device: Unknown-999

ALERT: Unauthorized USB detected
Time: 11:45 | Device: Unknown-777

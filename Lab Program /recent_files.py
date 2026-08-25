activity_log = [
    "10:00 OPEN report.docx",
    "10:05 OPEN evidence.pdf",
    "10:10 MODIFY notes.txt",
    "10:15 OPEN secret.txt",
    "10:20 OPEN report.docx"
]

print("===== RECENTLY ACCESSED FILES =====")

for record in activity_log:
    time, action, file_name = record.split()

    if action == "OPEN":
        print("Time:", time, "| File:", file_name)

ouptu:
===== RECENTLY ACCESSED FILES =====
Time: 10:00 | File: report.docx
Time: 10:05 | File: evidence.pdf
Time: 10:15 | File: secret.txt
Time: 10:20 | File: report.docx

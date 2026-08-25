files = [
    "report.pdf",
    "photo.jpg",
    "invoice.pdf.exe",
    "document.docx",
    "image.jpg.scr",
    "notes.txt"
]

dangerous = [".exe", ".scr", ".bat", ".cmd", ".vbs"]

print("===== SUSPICIOUS FILE ANALYSIS =====")

for file_name in files:
    parts = file_name.lower().split(".")

    if len(parts) >= 3:
        extension = "." + parts[-1]

        if extension in dangerous:
            print("ALERT:", file_name, "- Double extension detected")

      output:
===== SUSPICIOUS FILE ANALYSIS =====
ALERT: invoice.pdf.exe - Double extension detected
ALERT: image.jpg.scr - Double extension detected

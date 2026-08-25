import os

folder = "test_folder"

print("===== HIDDEN FILE ANALYSIS =====")

for file_name in os.listdir(folder):

    # Check hidden files
    if file_name.startswith("."):
        print("Hidden File:", file_name)

    # Check suspicious extensions
    if file_name.lower().endswith((".exe", ".bat", ".scr")):
        print("Suspicious File:", file_name)

output:
===== HIDDEN FILE ANALYSIS =====
Hidden File: .secret.txt
Suspicious File: malware.exe

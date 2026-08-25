process_log = [
    "explorer.exe",
    "chrome.exe",
    "powershell.exe -enc malicious_code",
    "notepad.exe",
    "cmd.exe /c suspicious.bat"
]

suspicious_words = ["powershell", "-enc", "malicious", "suspicious"]

print("===== PROCESS ANALYSIS =====")

for process in process_log:
    if any(word in process.lower() for word in suspicious_words):
        print("ALERT: Suspicious Process -", process)

output:
===== PROCESS ANALYSIS =====
ALERT: Suspicious Process - powershell.exe -enc malicious_code
ALERT: Suspicious Process - cmd.exe /c suspicious.bat

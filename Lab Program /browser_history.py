from collections import Counter
from urllib.parse import urlparse

history = [
    "https://google.com",
    "https://example.com/news",
    "https://google.com/search",
    "http://malicious-login.xyz/verify",
    "https://example.com/home",
    "https://google.com/maps"
]

domains = []
suspicious_words = ["login", "verify", "malicious", "phishing"]

print("===== BROWSER HISTORY ANALYSIS =====")

for url in history:
    domain = urlparse(url).netloc
    domains.append(domain)

    if any(word in url.lower() for word in suspicious_words):
        print("Suspicious URL:", url)

print("\nFrequently Visited Websites:")

for domain, count in Counter(domains).most_common():
    print(domain, "-", count, "visits")

output:
===== BROWSER HISTORY ANALYSIS =====
Suspicious URL: http://malicious-login.xyz/verify

Frequently Visited Websites:
google.com - 3 visits
example.com - 2 visits
malicious-login.xyz - 1 visits

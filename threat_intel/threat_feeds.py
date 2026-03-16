
import requests

FEEDS = [
    "https://rules.emergingthreats.net/blockrules/compromised-ips.txt"
]

def fetch_feeds():
    results = []
    for url in FEEDS:
        try:
            r = requests.get(url, timeout=10)
            results.extend(r.text.splitlines())
        except:
            pass
    return results

if __name__ == "__main__":
    feeds = fetch_feeds()
    print("Loaded", len(feeds), "threat indicators")

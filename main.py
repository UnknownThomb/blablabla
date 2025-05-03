import feedparser
import random
import time
import urllib.parse
from datetime import datetime, timezone

# ---- CONFIGURATION ----
# Hardcoded Ostium referral link
REFERRAL_LINK = "https://ostium.app/trade?from=SPX&to=USD&ref=4DB1D"
# ------------------------

keywords = [
    "forex trading", "commodities trading", "index trading",
    "gold futures", "silver trading", "crude oil trading"
]

replies = [
    "Ostium is a decentralized platform where you can trade real-world assets like gold, forex, and indices with leverage: {link}",
    "Try Ostium for on-chain leveraged trading in RWAs like forex and commodities: {link}",
    "Decentralized RWA perps (indices, gold, forex) are live on Ostium. My invite: {link}"
]

LOG_FILE = "manual_reply_suggestions.txt"


def log_suggestions(tweet_id, username, text, keyword, message):
    timestamp = datetime.now(timezone.utc).isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] @{username}: \"{text}\"
")
        f.write(f"Suggested reply: @{username} {message}
")
        f.write(f"Tweet link: https://twitter.com/{username}/status/{tweet_id}
")
        f.write(f"Matched keyword: {keyword}

")


def fetch_and_log():
    for kw in keywords:
        query = urllib.parse.quote(kw)
        url = f"https://nitter.net/search/rss?f=tweets&q={query}"
        feed = feedparser.parse(url)
        if feed.entries:
            for entry in feed.entries:
                tweet_id = entry.id.split("/")[-1]
                username = entry.author
                text = entry.title
                message = random.choice(replies).format(link=REFERRAL_LINK)
                log_suggestions(tweet_id, username, text, kw, message)
                time.sleep(random.uniform(1, 2))
        time.sleep(random.uniform(10, 15))


if __name__ == "__main__":
    while True:
        print("Fetching RSS suggestions...")
        fetch_and_log()
        time.sleep(random.uniform(900, 1200))  # 15–20 minutes

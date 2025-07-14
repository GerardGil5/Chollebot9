import feedparser

def fetch_deals():
    feed = feedparser.parse("https://www.chollometro.com/rss")
    deals = []
    for entry in feed.entries[:5]:
        deals.append({
            "title": entry.title,
            "price": "Consultar en enlace",
            "url": entry.link
        })
    return deals

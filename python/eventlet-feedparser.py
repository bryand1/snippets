import eventlet
feedparser = eventlet.import_patched('feedparser')

pool = eventlet.GreenPool()

urls = [
    "https://www.zdnet.com/news/rss.xml",
    "http://adage.com/rss-feed",
    "http://feeds.arstechnica.com/arstechnica/index",
    "https://www.recode.net/rss/index.xml",
    "https://www.crn.com/rss/crn-feed.rss",
    "http://www.wsj.com/xml/rss/3_7455.xml",
    "http://feeds.reuters.com/reuters/technologyNews",
    "https://www.theverge.com/rss/index.xml",
    "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://www.theregister.co.uk/headlines.atom",
    "http://feeds.feedburner.com/variety/news/technology"
]


def fetch_title(url):
    d = feedparser.parse(url)
    return d.feed.get('title')


if __name__ == '__main__':
    # TO-DO: While true, fetch urls, then parse results, then sleep for 1 minute
    pile = eventlet.GreenPile(pool)
    for url in urls:
        pile.spawn(fetch_title, url)
    for title in pile:
        print(title)

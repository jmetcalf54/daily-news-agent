import feedparser


feeds = [
    "https://rss.app/feeds/eDX1McvTcYaXduhZ.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://www.npr.org/rss/rss.php?id=1001",
]


def fetch_stories():
    stories = []

    for feed_url in feeds:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            story = {
                "title": entry.title,
                "link": entry.link,
                "source": feed.feed.get("title", "Unknown Source"),
            }

            stories.append(story)

    return stories


def main():
    stories = fetch_stories()

    print(f"Fetched {len(stories)} stories.\n")

    for story in stories[:10]:
        print(story["title"])
        print(story["source"])
        print(story["link"])
        print()


if __name__ == "__main__":
    main()
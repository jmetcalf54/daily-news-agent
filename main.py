import feedparser

# Constants
feeds = [
    "https://rss.app/feeds/eDX1McvTcYaXduhZ.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://www.npr.org/rss/rss.php?id=1001",
]

STORY_LIMIT = 10

# Functions
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

def select_top_stories(stories, limit=10):
    return stories[:limit]


# Main workflow function
def main():
    stories = fetch_stories()
    selected_stories = select_top_stories(stories, STORY_LIMIT)

    print(f"Fetched {len(stories)} stories.")
    print(f"Selected {len(selected_stories)} stories.\n")

    for story in selected_stories:
        print(story["title"])
        print(story["source"])
        print(story["link"])
        print()


# Script entry point
if __name__ == "__main__":
    main()
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

def select_top_stories(stories, limit):
    return stories[:limit]

def format_digest(stories):
    digest = "Metcalf Mayhem Roundup\n"
    digest += "=================\n\n"

    for index, story in enumerate(stories, start=1):
        digest += f"{index}. {story['title']}\n"
        digest += f"   Source: {story['source']}\n"
        digest += f"   Link: {story['link']}\n\n"

    return digest

# Main workflow function
def main():
    stories = fetch_stories()
    selected_stories = select_top_stories(stories, STORY_LIMIT)
    digest = format_digest(selected_stories)

    print(f"Fetched {len(stories)} stories.")
    print(f"Selected {len(selected_stories)} stories.\n")
    print(digest)


# Script entry point
if __name__ == "__main__":
    main()
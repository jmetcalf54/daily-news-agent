import os
import smtplib
import feedparser
from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()

# Constants
feeds = [
    "https://rss.app/feeds/eDX1McvTcYaXduhZ.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://www.npr.org/rss/rss.php?id=1001",
]

STORY_LIMIT = 10

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# Functions
def validate_email_config():
    if not EMAIL_SENDER:
        raise ValueError("EMAIL_SENDER is missing from .env")

    if not EMAIL_RECEIVER:
        raise ValueError("EMAIL_RECEIVER is missing from .env")

    if not EMAIL_PASSWORD:
        raise ValueError("EMAIL_PASSWORD is missing from .env")

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

def format_digest(stories):
    digest = "Metcalf Mayhem Roundup\n"
    digest += "=================\n\n"

    for index, story in enumerate(stories, start=1):
        digest += f"{index}. {story['title']}\n"
        digest += f"   Source: {story['source']}\n"
        digest += f"   Link: {story['link']}\n\n"

    return digest

def select_top_stories(stories, limit):
    return stories[:limit]

def send_email(subject, body):
    message = EmailMessage()
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER
    message["Subject"] = subject
    message.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(message)


# Main workflow function
def main():
    validate_email_config()

    stories = fetch_stories()
    selected_stories = select_top_stories(stories, STORY_LIMIT)
    digest = format_digest(selected_stories)

    print(f"Fetched {len(stories)} stories.")
    print(f"Selected {len(selected_stories)} stories.\n")
    print(digest)

    send_email("Metcalf Mayhem Roundup", digest)
    print("Email sent.")

# Script entry point
if __name__ == "__main__":
    main()
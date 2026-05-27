import os
from dotenv import load_dotenv


load_dotenv()


FEEDS = [
    "https://rss.app/feeds/eDX1McvTcYaXduhZ.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://www.npr.org/rss/rss.php?id=1001",
]

STORY_LIMIT = 15

EMAIL_SUBJECT = "Metcalf Mayhem Roundup"

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def validate_email_config():
    if not EMAIL_SENDER:
        raise ValueError("EMAIL_SENDER is missing from .env")

    if not EMAIL_RECEIVER:
        raise ValueError("EMAIL_RECEIVER is missing from .env")

    if not EMAIL_PASSWORD:
        raise ValueError("EMAIL_PASSWORD is missing from .env")
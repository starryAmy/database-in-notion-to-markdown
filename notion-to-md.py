from notion_client import Client
from notion_to_md import NotionToMarkdown
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Environment Variables
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = os.getenv('DATABASE_ID')
STATUS_PROPERTY = os.getenv('STATUS_PROPERTY')
PUBLISH_DATE_PROPERTY = os.getenv('PUBLISH_DATE_PROPERTY')
TITLE_PROPERTY = os.getenv('TITLE_PROPERTY')
STATUS_VALUE = os.getenv('STATUS_VALUE')
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER')

# Check essential env variables
if not NOTION_TOKEN or not DATABASE_ID:
    raise ValueError("Please make sure NOTION_TOKEN and DATABASE_ID are set in the .env file.")

# Get Current Date in Asia/Tokyo timezone
now = datetime.now(ZoneInfo('Asia/Tokyo'))
TODAY = now.date().isoformat()

# Initialize Notion Client
notion = Client(auth=NOTION_TOKEN)
n2m = NotionToMarkdown(notion)

# Query Notion Database
try:
    selected_posts = notion.databases.query(
        database_id=DATABASE_ID,
        filter={
            "and": [
                {
                    "property": STATUS_PROPERTY,
                    "status": {
                        "equals": STATUS_VALUE
                    }
                },
                {
                    "property": PUBLISH_DATE_PROPERTY,
                    "date": {
                        "equals": TODAY
                    }
                },
            ]
        }
    )["results"]
except Exception as e:
    print(f"Failed to fetch Notion database: {e}")
    exit(1)

if not selected_posts:
    print("No posts scheduled for today.")
else:
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    for post in selected_posts:

        md_blocks = n2m.page_to_markdown(post["id"])
        md_str = n2m.to_markdown_string(md_blocks).get("parent")

        if not md_str or not md_str.strip():
            print(f"Post {post['id']} has empty content, skipping.")
            continue

        title = post["properties"][TITLE_PROPERTY]["title"][0]["text"]["content"]
        safe_title = title.replace("/", "_").replace(":", "-")
        content = f"# {title}\n\n{md_str}"
        filename = f"{TODAY}-{safe_title}.md"
        filepath = os.path.join(OUTPUT_FOLDER, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

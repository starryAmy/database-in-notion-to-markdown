# Notion to Markdown Exporter

Automatically fetch posts from a specific Notion database based on customizable filters, convert them into clean Markdown files, and save them locally.
This makes it easy to reuse your content across different publishing platforms by simply copying and pasting the generated Markdown.

## Features

- Fetch posts from a Notion database
- Filter posts by a customizable status and scheduled publish date
- Convert Notion pages to clean Markdown
- Save files to a customizable output folder
- Fully automated via GitHub Actions (daily or manual run)

## Folder Structure

```bash
├── notion_to_md.py         # Main script
├── .env.example            # Environment variable template
├── requirements.txt        # Python package requirements
├── posts/            # Folder to save exported markdowns
└── .github/workflows/
    └── run-notion-to-md.yml # GitHub Actions workflow
Note: posts/ is the default output folder. You can customize it.
```

##  Setup Instructions

1. Clone this Repository

```bash
git clone https://github.com/starryAmy/database-in-notion-to-markdown.git
cd database-in-notion-to-markdown
```

2. Set Up Environment Variables
```bash
Create a .env file by copying .env.example:
cp .env.example .env
# Fill in your Notion Integration Token and Database ID inside .env.
```

You can also customize:

```bash
Variable	Description
NOTION_TOKEN	Your Notion Integration Secret	
DATABASE_ID	Your Notion Database ID	
STATUS_PROPERTY	Property name for status (in your database)	
STATUS_VALUE	Status value to match (e.g., Published)	
PUBLISH_DATE_PROPERTY	Property name for publish date	
TITLE_PROPERTY	Property name for page title	
# All fields are customizable according to your Notion database structure.
```

## How it Works
1. Query your Notion database
2. Filter posts that match: The specified status (STATUS_PROPERTY = STATUS_VALUE) and The scheduled publish date = Today (Tokyo time)
3. Convert each page to Markdown
4. Save it to the specified folder

## Running Locally
Install dependencies:
```bash
pip install -r requirements.txt
```

Run the script:
```bash
python notion_to_md.py
# Markdown files will be saved in your specified output folder!
```

## Enable GitHub Actions Automation
This repository includes a GitHub Actions workflow to:

- Automatically run the script every day (00:00 UTC)
- Commit and push generated markdown files back to your repository

If you fork or clone this repo:

- Go to your repository Settings → Actions → Enable GitHub Actions
- Ensure you grant "Read and Write" permissions to workflows
- Add your Notion secrets as repository secrets if needed (optional)

## Tips
- If your database uses different property names, just edit .env.
- If you want a different timezone, adjust the timezone setting inside the script.
- You can manually trigger the GitHub Action anytime via the "Run workflow" button.

## License
This project is open-sourced under the MIT License.

## Contributions
Pull requests are welcome.
Feel free to fork and create your own customized Notion to Markdown automations!

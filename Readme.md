
# CAREERPILOT-AI
AI-powered job intelligence and automation system.

## Overview
CAREERPILOT-AI is an AI-powered automation system that: 
- Collects job postings from job sites using browser automation.
- Extracts skills and key requirements from each posting.
- Matches jobs against a user resume using embeddings and similarity scoring.
- Provides a dashboard and notifications for high-match opportunities.

## Project Status

🚧 In development – initial project scaffold only.

## Tech Stack (planned)

- Python
- Playwright (job scraping)
- SentenceTransformers (embeddings)
- SQLite (storage)
- Streamlit (dashboard)
- Telegram / Email (notifications)
- MCP tools (optional, for ChatGPT integration)

## Repository Structure (initial)

```text
career-pilot-ai/
  ├── README.md
  ├── .gitignore
  ├── requirements.txt
  ├── src/
  │   ├── scraper/
  │   ├── matcher/
  │   ├── automation/
  │   ├── dashboard/
  │   ├── database/
  │   └── mcp/
  └── data/
      └── resume/

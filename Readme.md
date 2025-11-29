
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

## Planned Architecture

CareerPilot AI will consist of the following core modules:

- **Job Scraper (Playwright):** Collects jobs from online platforms.
- **Resume Matcher (Embeddings + NLP):** Calculates similarity scores between job  descriptions and resume content.
- **Database Layer (SQLite):** Stores job history and metadata.
- **Automation Engine:** Schedules scraping and pushes notifications.
- **Dashboard (Streamlit):** Provides interactive job insights.
- **MCP Integration:** Enables querying job data via ChatGPT tools.

A detailed architecture diagram will be added as the system evolves.


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

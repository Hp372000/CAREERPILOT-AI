import asyncio
from playwright.async_api import async_playwright
from .linkedin_parser import extract_job_cards
from .logger import get_logger

logger = get_logger("scraper")

SEARCH_URL = (
    "https://www.linkedin.com/jobs/search/?keywords=DevOps&location=Canada"
)


async def scrape_linkedin_jobs():
    """Navigate to LinkedIn job search and extract job cards."""

    logger.info(f"Navigating to LinkedIn search: {SEARCH_URL}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        PAGE_HEADERS = {
          "User-Agent": (
             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
             "AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/120.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        }
    
        page = await browser.new_page(extra_http_headers=PAGE_HEADERS)

        await page.goto(SEARCH_URL, timeout=60000)
        await page.wait_for_timeout(4000)  # wait for dynamic content

        job_cards = await extract_job_cards(page)

        logger.info(f"Found {len(job_cards)} job cards")

        await browser.close()

        return job_cards

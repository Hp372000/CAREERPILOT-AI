import asyncio
from playwright.async_api import async_playwright


async def test_browser():
    """Opens a browser and navigates to example.com for validation."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("[Scraper] Navigating to https://example.com ...")
        await page.goto("https://example.com")
        title = await page.title()
        print(f"[Scraper] Page title: {title}")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(test_browser())

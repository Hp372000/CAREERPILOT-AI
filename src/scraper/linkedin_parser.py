from playwright.async_api import Page

async def extract_job_cards(page: Page):
    """Extract job cards from a LinkedIn Jobs search results page (no login required)."""

    # LinkedIn uses dynamically generated selectors, but job-card-container is stable.
    job_cards = await page.locator("div.job-card-container").all()

    results = []

    for card in job_cards:
        title = await card.locator("h3").text_content() or ""
        company = await card.locator("h4").text_content() or ""
        location = await card.locator(".job-card-container__metadata-item").text_content() or ""
        link = await card.locator("a").get_attribute("href") or ""

        # Normalize link (LinkedIn uses relative)
        if link.startswith("/"):
            link = "https://www.linkedin.com" + link

        results.append({
            "title": title.strip(),
            "company": company.strip(),
            "location": location.strip(),
            "link": link.strip()
        })

    return results

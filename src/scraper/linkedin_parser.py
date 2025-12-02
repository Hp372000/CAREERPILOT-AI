from playwright.async_api import Page

async def extract_job_cards(page: Page):
    """Extract job cards from a LinkedIn Jobs search results page (no login required)."""

    # LinkedIn uses dynamically generated selectors, but job-card-container is stable.
    job_cards = await page.locator("li.jobs-search-results__list-item").all()

    results = []

    for card in job_cards:
        # Try primary selectors
        title = await card.locator("h3.base-search-card__title").text_content()
        company = await card.locator("h4.base-search-card__subtitle").text_content()
        location = await card.locator("span.job-search-card__location").text_content()
        link = await card.locator("a").get_attribute("href")

        # Fallbacks
        if not title:
            title = await card.locator(".base-search-card__title").text_content()
        if not company:
            company = await card.locator(".base-search-card__subtitle").text_content()
        if not location:
            location = await card.locator(".job-search-card__location").text_content()

        title = title or ""
        company = company or ""
        location = location or ""
        link = link or ""

        if link.startswith("/"):
            link = "https://www.linkedin.com" + link

        results.append({
            "title": title.strip(),
            "company": company.strip(),
            "location": location.strip(),
            "link": link.strip(),
        })
    
    return results

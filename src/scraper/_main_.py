import asyncio
from .play_scraper import scrape_linkedin_jobs
from .logger import get_logger

logger = get_logger("cli")


def main():
    logger.info("Running LinkedIn scraper test...")
    jobs = asyncio.run(scrape_linkedin_jobs())

    logger.info(f"Sample result:\n{jobs[:3]}")


if __name__ == "__main__":
    main()


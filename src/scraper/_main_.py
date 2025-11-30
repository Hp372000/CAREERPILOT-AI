import asyncio
from .play_scraper import test_browser

def main():
    print("[Scraper] Starting scraper module...")
    asyncio.run(test_browser())

if __name__ == "__main__":
    main()

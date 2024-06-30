import asyncio
import pytest
from playwright.async_api import async_playwright
from pages.resources_page import ResourcesPage


@pytest.mark.asyncio
async def test_count_posts():
    print("Starting test to verify the total number of posts on the resources page")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        resources_page = ResourcesPage(page)
        await resources_page.goto()

        total_number_of_posts = await resources_page.count_posts()

        print(f"Total number of posts found: {total_number_of_posts}")
        assert total_number_of_posts > 0

        await browser.close()
    print("Test completed")


if __name__ == "__main__":
    asyncio.run(test_count_posts())

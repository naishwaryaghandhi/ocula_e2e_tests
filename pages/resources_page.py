from playwright.async_api import Page


class ResourcesPage:
    def __init__(self, page: Page):
        self.page = page
        self.resources_page_url = 'https://ocula.tech/resources'
        self.next_posts_selector = '//*[@id="sections"]/section[2]/div[2]/div/div/nav/div[2]/a/span'
        self.resources_selector = 'blog-basic-grid collection-content-wrapper'

    async def goto(self):
        print(f"Navigating to {self.resources_page_url}")
        await self.page.goto(self.resources_page_url)

    async def count_posts(self):
        total_number_of_posts = 0
        page_number = 1
        while True:
            number_of_posts = await self.page.evaluate("""resources_selector => {
              const total_number_of_posts = document.getElementsByClassName(resources_selector)[0].childElementCount;
              return total_number_of_posts;
            }""", self.resources_selector)

            print(f"Page {page_number}: Found {number_of_posts} number of posts")
            total_number_of_posts += number_of_posts

            next_button = await self.page.query_selector(self.next_posts_selector)
            if next_button:
                print("Next posts button found, clicking to go to the next resources page")
                await next_button.click()
                await self.page.wait_for_timeout(1000)  # Adjust as needed
                page_number += 1
            else:
                print("No next posts button found, stopping")
                break
        return total_number_of_posts

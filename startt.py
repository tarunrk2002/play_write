from playwright.sync_api import sync_playwright

play = sync_playwright().start()
Browser = play.webkit.launch(headless=True)
page = Browser.new_page()
page.goto("https://arxiv.org/search/")

page.get_by_placeholder("Search term...").fill("machine learning")
page.get_by_role("button", name="Search").nth(1).click()
# url = page.url
# print(url)
# print(page.content)


page.screenshot(path="ss1.png")

# page.locator("text=arXiv:2502.17437").click()



# page.get_by_role("link", name="arXiv:2502.17437").click()




page.screenshot(path="ss2.png")
page.go_back()
page.screenshot(path="ss3.png")
page.close()




Browser.close()
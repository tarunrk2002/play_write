from playwright.sync_api import sync_playwright

play = sync_playwright().start()
Browser = play.webkit.launch(headless=True)
page = Browser.new_page()
page.goto("https://arxiv.org/search/")

page.get_by_placeholder("Search term...").fill("machine learning")
page.screenshot(path="ss.png")




Browser.close()
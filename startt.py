from playwright.sync_api import sync_playwright

play = sync_playwright().start()
Browser = play.webkit.launch()
page = Browser.new_page()
page.goto("https://www.youtube.com/")
page.screenshot(path="google.png")

Browser.close()
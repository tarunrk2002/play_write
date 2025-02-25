from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve

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


links = page.locator("xpath=//a[contains(@href, 'pdf')]")


a=0
for link in links.all():
    url = link.get_attribute("href")
    urlretrieve(url, f"{a}" + ".pdf")
    a = a+1









Browser.close()
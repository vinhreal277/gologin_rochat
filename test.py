from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(color_scheme='dark')
    page = context.new_page()
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto("https://www.fastmail.com/login/")
    page.frame_locator
    page.wait_for_timeout(35000)
    page.screenshot(path="example.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
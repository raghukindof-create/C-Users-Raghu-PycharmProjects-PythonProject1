from playwright.sync_api import expect, Page

#playwright built in locators
#test 1

def test_pageurl(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(2000)
    login = page.get_by_alt_text("company-branding")        #locator 1
    expect(login).to_be_visible()

#test 2

def test_pagetitle(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(2000)
    text = page.get_by_text("Forgot your password?")             #locator 2
    expect(text).to_be_visible()

#test 3

def test_role(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    role = page.get_by_role("heading", name= "Login")             #locator 3
    expect(role).to_be_visible()
#test 4
    page.get_by_placeholder("Username").fill("Raghavendra")          #locator 4
    page.get_by_placeholder("Password").fill("Raghu@35")
    page.wait_for_timeout(5000)


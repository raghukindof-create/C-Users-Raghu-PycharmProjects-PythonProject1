from playwright.sync_api import Page, expect

def test_xpath_locators (page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("/html/body/div[4]/div[1]/div[4]/div[1]/div[2]/div[1]/strong")  #absolute xpath
    page.locator("//strong[normalize-space()='Manufacturers']")    #relative xpath  format: //tagname[@attibute='value']
    items=page.locator("h2 > a[href*='comp']")   #it is CSS and the xpath for same is //h2//a[contains(@href,'comp')
    expect(items).to_have_count(4)
    print("the count is", items.count())
    page.wait_for_timeout(5000)
    print("the first computer name is:", items.first.text_content())
    print("the 3 product is:", items.nth(3).text_content())


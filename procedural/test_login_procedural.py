from playwright.sync_api import Page

LOGIN_URL = "https://www.saucedemo.com/"
USERNAME_FIELD = "#user-name"
PASSWORD_FIELD = "#password"
LOGIN_BTN = "#login-button"
ERR_MSG = "[data-test='error']"


def test_login_success(page: Page):
    page.goto(LOGIN_URL)
    page.locator(USERNAME_FIELD).fill("standard_user")
    page.locator(PASSWORD_FIELD).fill("secret_sauce")
    page.locator(LOGIN_BTN).click()

    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_login_failed(page: Page):
    page.goto(LOGIN_URL)
    page.locator(USERNAME_FIELD).fill("fufufafa")
    page.locator(PASSWORD_FIELD).fill("lupa_password")
    page.locator(LOGIN_BTN).click()

    assert (
        page.locator(ERR_MSG).inner_text()
        == "Epic sadface: Username and password do not match any user in this service"
    )

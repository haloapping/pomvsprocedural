from playwright.sync_api import Page

USERNAME_FIELD = "#user-name"
PASSWORD_FIELD = "#password"
LOGIN_BTN = "#login-button"
ERR_MSG = "[data-test='error']"


def login(page: Page, url: str, username: str, password: str):
    page.goto(url)
    page.locator(USERNAME_FIELD).fill(username)
    page.locator(PASSWORD_FIELD).fill(password)
    page.locator(LOGIN_BTN).click()


def test_login_success(page: Page):
    login(
        page,
        "https://www.saucedemo.com/",
        "standard_user",
        "secret_sauce",
    )

    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_login_failed(page: Page):
    login(
        page,
        "https://www.saucedemo.com/",
        "fufufafa",
        "lupa_password",
    )

    assert (
        page.locator(ERR_MSG).inner_text()
        == "Epic sadface: Username and password do not match any user in this service"
    )

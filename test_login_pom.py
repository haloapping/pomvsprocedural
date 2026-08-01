from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__username_field = page.locator("#user-name")
        self.__password_field = page.locator("#password")
        self.__login_btn = page.locator("#login-button")
        self.__err_msg = page.locator("[data-test='error']")

    def open_url(self, url: str):
        self.__page.goto(url)

    def fill_username(self, username: str):
        self.__username_field.fill(username)

    def fill_password(self, password: str):
        self.__password_field.fill(password)

    def click_login(self):
        self.__login_btn.click()

    def get_curr_url(self) -> str:
        return self.__page.url

    def get_err_msg(self) -> str:
        return self.__err_msg.inner_text()

    def login(self, url: str, username: str, password: str):
        self.open_url(url)
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()


def test_login_success(page: Page):
    lp = LoginPage(page)
    lp.login(
        url="https://www.saucedemo.com/",
        username="standard_user",
        password="secret_sauce",
    )

    assert lp.get_curr_url() == "https://www.saucedemo.com/inventory.html"


def test_login_failed(page: Page):
    lp = LoginPage(page)
    lp.login(
        url="https://www.saucedemo.com/",
        username="fufufafa",
        password="lupa_password",
    )

    assert (
        lp.get_err_msg()
        == "Epic sadface: Username and password do not match any user in this service"
    )

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.err_msg = page.locator("[data-test='error']")

    def open_url(self, url: str):
        self.page.goto(url)

    def fill_username(self, username: str):
        self.username_field.fill(username)

    def fill_password(self, password: str):
        self.password_field.fill(password)

    def click_login(self):
        self.login_btn.click()

    def get_curr_url(self) -> str:
        return self.page.url

    def get_err_msg(self) -> str:
        return self.err_msg.inner_text()

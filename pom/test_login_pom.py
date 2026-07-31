from login_page import LoginPage
from playwright.sync_api import Page


def test_login_success(page: Page):
    lp = LoginPage(page)
    lp.open_url("https://www.saucedemo.com/")
    lp.fill_username("standard_user")
    lp.fill_password("secret_sauce")
    lp.click_login()

    assert lp.get_curr_url() == "https://www.saucedemo.com/inventory.html"


def test_login_failed(page: Page):
    lp = LoginPage(page)
    lp.open_url("https://www.saucedemo.com/")
    lp.fill_username("fufufafa")
    lp.fill_password("lupa_password")
    lp.click_login()

    assert (
        lp.get_err_msg()
        == "Epic sadface: Username and password do not match any user in this service"
    )

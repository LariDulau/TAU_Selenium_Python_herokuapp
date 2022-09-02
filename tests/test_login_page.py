from pages.login_page import LoginPage
from time import sleep
import pytest
from assertpy import assert_that, soft_assertions

def test_url(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    # url = 'https://www.reserved.com/ro/ro/customer/account/login/#login'
    # url_current = browser.current_url
    # assert url == url_current
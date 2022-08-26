from pages.login_page import LoginPage
from time import sleep
import pytest

from pages.secure_page import SecurePage

@pytest.mark.pozitive
def test_check_login_functionality(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    assert "Welcome to the Secure Area. When you are done click logout below." == secure_page.getWelcomeMessage()
    assert browser.current_url == secure_page.URL


def test_url(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    url = 'https://the-internet.herokuapp.com/login'
    url_current = browser.current_url
    assert url == url_current


def testInvalidError(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.click_login()
    assert login_page.isInvalidErrorTextDisplayed()
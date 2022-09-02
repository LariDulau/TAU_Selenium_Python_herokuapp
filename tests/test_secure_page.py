from pages.login_page import LoginPage
from time import sleep
import pytest
from pages.secure_page import SecurePage


def test_check_logout_functionality(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    secure_page.click_logout()


def test_url(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    assert browser.current_url == secure_page.URL


def test_welcome_text(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    assert "Welcome to the Secure Area. When you are done click logout below." == secure_page.get_welcome_message()


def test_flash_text(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    assert secure_page.is_flash_text_displayed()

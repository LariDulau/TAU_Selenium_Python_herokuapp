from time import sleep
from pages.dropdown_page import DropdownPage


def test_select_option1(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.select_option1()


def test_select_option2(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.select_option2()


def test_url(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    url = 'https://the-internet.herokuapp.com/dropdown'
    url_current = browser.current_url
    assert url == url_current
    sleep(3)


def test_subtitle_displayed(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.issubtitledisplayed()
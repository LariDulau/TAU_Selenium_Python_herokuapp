from assertpy import assert_that
from pages.dropdown_page import DropdownPage
from time import sleep



def test_select_option(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.select_option('Option 1')


def test_url(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    url = 'https://the-internet.herokuapp.com/dropdown'
    url_current = browser.current_url
    assert_that(url == url_current)


def test_subtitle_displayed(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.is_subtitle_displayed()




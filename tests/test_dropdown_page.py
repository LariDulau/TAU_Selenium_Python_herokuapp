from assertpy import assert_that
from pages.dropdown_page import DropdownPage


def test_select_option(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.select_by_text('Option 1')
    assert_that(dropdown_page.is_value_selected("1")).is_true()
    dropdown_page.select_by_value("2")
    assert_that(dropdown_page.is_value_selected("2")).is_true()


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


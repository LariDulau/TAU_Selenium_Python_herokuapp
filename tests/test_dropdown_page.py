from assertpy import assert_that, soft_assertions
from pages.dropdown_page import DropdownPage


def test_select_option(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.select_by_text('Option 1')
    assert_that(dropdown_page.is_value_selected("1")).is_true()
    dropdown_page.select_by_value("2")
    assert_that(dropdown_page.is_value_selected("2")).is_true()


def test_dropdown_page(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    with soft_assertions():
        assert_that(browser.current_url).is_equal_to(dropdown_page.URL)
        assert_that(dropdown_page.get_subtitle()).is_equal_to('Dropdown List')


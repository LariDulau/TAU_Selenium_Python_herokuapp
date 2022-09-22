from assertpy import assert_that
from pages.iframe_page import IFramePage
from time import sleep

# def test_iframe_page(browser):
#     iframe_page = IFramePage(browser)
#     iframe_page.load_page()
#     iframe_page.write('The car is new.')
#     assert_that(iframe_page.get_text()).is_equal_to('The car is new.')

def test_iframe_page(browser):
    iframe_page = IFramePage(browser)
    iframe_page.load_page()
    iframe_page.write("anaaa")
    assert_that(iframe_page.get_text()).is_equal_to("anaaa")

def test_url(browser):
    iframe_page = IFramePage(browser)
    iframe_page.load_page()
    assert_that(iframe_page.URL).is_equal_to(browser.current_url)


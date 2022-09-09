from assertpy import assert_that
from pages.iframe_page import IFramePage


def test_iframe_page(browser):
    iframe_page = IFramePage(browser)
    iframe_page.load_page()
    iframe_page.write('The car is new.')
    assert_that(iframe_page.get_text() == 'The car is new.')


def test_url(browser):
    iframe_page = IFramePage(browser)
    iframe_page.load_page()
    url = 'https://the-internet.herokuapp.com/iframe'
    url_current = browser.current_url
    assert_that(url == url_current)


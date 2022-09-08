from assertpy import assert_that
from pages.iframe_page import IFramePage

# ASTA NU IMI IESE
# def test_insert_text(browser):
#     iframe_page = IFramePage(browser)
#     iframe_page.load_page()
#     iframe_page.insert_text('The car')
#     sleep(4)


def test_iframe_text_is_displayed(browser):
    iframe_page = IFramePage(browser)
    iframe_page.load_page()
    assert_that(iframe_page.is_iframe_text_displayed())


def test_url(browser):
    iframe_page = IFramePage(browser)
    iframe_page.load_page()
    url = 'https://the-internet.herokuapp.com/iframe'
    url_current = browser.current_url
    assert_that(url == url_current)


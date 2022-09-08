from assertpy import assert_that
from pages.frames_page import FramesPage
from pages.iframe_page import IFramePage
from time import sleep



def test_url(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()
    url = 'https://the-internet.herokuapp.com/frames'
    url_current = browser.current_url
    assert_that(url == url_current)


def test_click_nested_frames(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()
    frames_page.click_nested_frames()


def test_click_iframe(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()
    frames_page.click_iframe()
    iframe_page = IFramePage(browser)
    assert_that(iframe_page.is_iframe_text_displayed())

def test_subtitle(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()
    assert_that(frames_page.is_subtitle_displayed())
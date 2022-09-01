from time import sleep
import pytest

from pages.frames_page import FramesPage
from pages.iframe_page import IFramePage


def test_url(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()
    url = 'https://the-internet.herokuapp.com/frames'
    url_current = browser.current_url
    assert url == url_current


def test_click_nested_frames(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()
    frames_page.click_nested_frames()


def test_click_iframe(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()
    frames_page.click_iframe()
    iframe_page = IFramePage(browser)
    assert iframe_page.isIFrameTextDisplayed()

def test_subtitle(browser):
    frames_page = FramesPage(browser)
    frames_page.load_page()
    assert frames_page.isSubtitleDisplayed()
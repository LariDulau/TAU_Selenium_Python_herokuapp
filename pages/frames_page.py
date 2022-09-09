from selenium.webdriver.common.by import By


class FramesPage:
    NESTED_FRAMES = (By. CSS_SELECTOR, '[href="/nested_frames"]')
    IFRAME = (By. CSS_SELECTOR, '[href="/iframe"]')
    SUBTITLE = (By. CSS_SELECTOR, 'h3')


    URL = 'https://the-internet.herokuapp.com/frames'


    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_nested_frames(self):
        self.browser.find_element(*self.NESTED_FRAMES).click()

    def click_iframe(self):
        self.browser.find_element(*self.IFRAME).click()

    def is_subtitle_displayed(self):
        return self.browser.find_element(*self.SUBTITLE).is_displayed()
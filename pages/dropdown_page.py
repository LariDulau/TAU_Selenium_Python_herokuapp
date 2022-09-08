from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class DropdownPage:
    SELECT_AN_OPTION = (By. ID, 'dropdown')
    DROPDOWN_SUBTITLE = (By. CSS_SELECTOR, 'h3')


    URL = 'https://the-internet.herokuapp.com/dropdown'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def select_option(self, option):
        select_option = Select(self.browser.find_element(*self.SELECT_AN_OPTION))
        select_option.select_by_visible_text(option)

    def is_subtitle_displayed(self):
        self.browser.find_element(*self.DROPDOWN_SUBTITLE).is_displayed()



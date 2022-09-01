from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropdownPage:
    SELECT_AN_OPTION = (By. ID, 'dropdown')
    DROPDOWN_SUBTITLE = (By. CSS_SELECTOR, 'h3')


    URL = 'https://the-internet.herokuapp.com/dropdown'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def select_option1(self):
        option1 = Select(self.browser.find_element(*self.SELECT_AN_OPTION))
        option1.select_by_visible_text('Option 1')

    def select_option2(self):
        option2 = Select(self.browser.find_element(*self.SELECT_AN_OPTION))
        option2.select_by_index(2)

    def issubtitledisplayed(self):
        self.browser.find_element(*self.DROPDOWN_SUBTITLE).is_displayed()
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

    def select_by_text(self, option):
        select_option = Select(self.browser.find_element(*self.SELECT_AN_OPTION))
        select_option.select_by_visible_text(option)

    def select_by_value(self, value):
        select = Select(self.browser.find_element(*self.SELECT_AN_OPTION))
        select.select_by_value(value)

    def is_value_selected(self, value):
        return self.browser.find_element(By.CSS_SELECTOR, f'[value="{value}"][selected="selected"]').is_displayed()

    def get_subtitle(self):
        return self.browser.find_element(*self.DROPDOWN_SUBTITLE).text



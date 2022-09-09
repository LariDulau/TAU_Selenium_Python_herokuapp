from selenium.webdriver.common.by import By


class IFramePage:
    IFRAME_TITLE = (By.CSS_SELECTOR, 'h3')
    IFRAME = (By.CLASS_NAME, "tox-edit-area__iframe")
    EDIT_SECTION = (By.CLASS_NAME, "mce-content-body")
    TEXT_FROM_EDIT = (By.CSS_SELECTOR, ".mce-content-body > p")
    BOLD = (By.CSS_SELECTOR, "[title = 'Bold']")

    URL = 'https://the-internet.herokuapp.com/iframe'


    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_page(self):
        return self.browser.find_element(*self.IFRAME_TITLE).text

    def write(self, text):
        iframe = self.browser.find_element(*self.IFRAME)
        self.browser.switch_to.frame(iframe)
        self.browser.find_element(*self.EDIT_SECTION).clear()
        self.browser.find_element(*self.EDIT_SECTION).send_keys(text)

    def get_text(self):
        iframe = self.browser.find_element(*self.IFRAME)
        self.browser.switch_to.frame(iframe)
        self.browser.find_element(*self.EDIT_SECTION).clear()
        return self.browser.find_element(*self.TEXT_FROM_EDIT).text




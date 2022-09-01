from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class IFramePage:
    IFRAME_TEXT = (By.CSS_SELECTOR, 'h3')
    INPUT_TEXT = (By. ID, 'mce_0_ifr')
    FILE = (By. XPATH, "//span[text()='File']")
    NEW_DOCUMENT = (By. XPATH, "//span[text()='New Document']")

    URL = 'https://the-internet.herokuapp.com/iframe'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def isIFrameTextDisplayed(self):
        return self.browser.find_element(*self.IFRAME_TEXT).is_displayed()

    def click_file(self):
       self.browser.find_element(*self.FILE).click()

    def click_new_document(self):
       self.browser.find_element(*self.NEW_DOCUMENT).click()

    def insert_text(self, text):
        insert_text = self.browser.switch_to.frame
        insert_text.send_keys(text)





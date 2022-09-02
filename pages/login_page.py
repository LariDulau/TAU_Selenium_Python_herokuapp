from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL_INPUT = (By.ID, 'login[username]_id')
    PASSWORD_INPUT = (By.ID, 'login[password]_id')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-selen = "login-submit" ]')
    REMEMBER_ME = (By.ID, 'login[remember_me]_id')
    ERROR_TEXT = (By.CLASS_NAME, 'sc-dlfnuX XGRlC')


    URL = 'https://www.reserved.com/ro/ro/customer/account/login/#login'

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def insert_password(self, password):
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def insert_email(self, email):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(username)

    def click_login(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def login(self, email, password):
        self.insert_email(email)
        self.insert_password(password)
        self.click_login()

    def isErrortextDisplayed(self):
        return self.browser.find_element(*self.ERROR_TEXT).is_displayed()

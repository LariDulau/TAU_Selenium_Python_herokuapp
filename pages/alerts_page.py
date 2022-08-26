from selenium.webdriver.common.by import By

class AlertsPage:
    ALERT = (By.CSS_SELECTOR, '[onclick="jsAlert()"]')
    CONFIRM = (By.CSS_SELECTOR, '[onclick="jsConfirm()"]')
    PROMPT = (By.CSS_SELECTOR, '[onclick="jsPrompt()"]')
    CONFIRM_RESULT_CANCEL = (By.CSS_SELECTOR, '[id="result"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, '[id="result"]')

    # URL
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def open_alert(self):
        self.browser.find_element(*self.ALERT).click()

    def open_confirm(self):
        self.browser.find_element(*self.CONFIRM).click()

    def open_promt(self):
        self.browser.find_element(*self.PROMPT).click()

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def cancel_alert(self):
        alert = self.browser.switch_to.alert
        alert.dismiss()

    def insert_alert(self, text):
        alert = self.browser.switch_to.alert
        alert.send_keys(text)

    def isConfirm_result_cancel_displayed(self):
        return self.browser.find_element(*self.CONFIRM_RESULT_CANCEL).is_displayed()

    def isPrompt_result_displayed(self):
        return self.browser.find_element(*self.PROMPT_RESULT).is_displayed()
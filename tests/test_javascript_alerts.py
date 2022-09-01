from pages.javascript_alerts_page import AlertsPage


def test_alert_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_alert()
    alert_page.accept_alert()
    alert_page.isResult_displayed()


def test_confirm_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    alert_page.accept_alert()
    alert_page.isResult_displayed()


def test_confirm_dismiss(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    alert_page.cancel_alert()
    alert_page.isResult_displayed()


def test_prompt_dismiss(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    alert_page.cancel_alert()
    alert_page.isResult_displayed()


def test_prompt_accept_notext(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    alert_page.accept_alert()
    alert_page.isResult_displayed()


def test_prompt_accept_text(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    alert_page.insert_alert("Java Alerts")
    alert_page.accept_alert()
    alert_page.isResult_displayed()



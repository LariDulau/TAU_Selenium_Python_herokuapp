from time import sleep
# import pytest

from pages.alerts_page import AlertsPage


def test_alert_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_alert()
    sleep(5)
    alert_page.accept_alert()
    sleep(5)


def test_confirm_dismiss(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    sleep(5)
    alert_page.cancel_alert()
    alert_page.isConfirm_result_cancel_displayed()
    sleep(5)


def test_text_prompt(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_promt()
    sleep(5)
    alert_page.insert_alert("tata")
    alert_page.accept_alert()
    alert_page.isPrompt_result_displayed()
    sleep(10)


from assertpy import assert_that
from selenium.webdriver.common.by import By
from pages.add_remove_elements_page import AddRemoveElementsPage
import pytest


def test_check_add_element_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # deschidem o pagina
    add_remove_page.load_page()
    add_remove_page.click_add_button()
    assert_that(add_remove_page.is_add_button_displayed())


def test_check_url(browser):
    check_url = AddRemoveElementsPage(browser)
    check_url.load_page()
    assert_that(check_url.URL == browser.current_url)


def test_title(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # deschidem o pagina
    add_remove_page.load_page()
    assert_that("Add/Remove Elements" == add_remove_page.get_title_page())

def test_link(browser):
    link_check = AddRemoveElementsPage(browser)
    link_check.load_page()
    assert_that(link_check.is_link_displayed())
    link_check.click_link()
    browser.switch_to.window(browser.window_handles[1])
    assert_that('http://elementalselenium.com/' == browser.current_url)

@pytest.mark.pozitive
def test_add_and_delete_functionality(browser):
    # deschidem o pagina
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    add_element_button = browser.find_element(By.CSS_SELECTOR, "[onclick='addElement()']")
    for i in range(10):
      add_element_button.click()
    delete_button_list = browser.find_elements(By.CLASS_NAME, "added-manually")
    assert_that(len(delete_button_list) == 10, "Not all delete button is displayed")
    for i in range(10):
        delete_button_list[0].click()
        delete_button_list = browser.find_elements(By.CLASS_NAME, "added-manually")
        assert_that(len(delete_button_list) == 10-i-1, "Not all delete button is displayed")


from assertpy import assert_that
from pages.context_menu_page import ContextMenuPage


def test_context_menu(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
    context_menu_page.open_menu()


def test_accept_alert(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
    context_menu_page.open_menu()
    context_menu_page.accept_alert()
    assert_that(browser.current_url).is_equal_to(context_menu_page.URL)


def test_check_alert_text(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
    context_menu_page.open_menu()
    assert_that(context_menu_page.get_text_alert() == 'You selected a context menu')


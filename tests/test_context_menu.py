from pages.context_menu_page import ContextMenuPage
from time import sleep

def test_context_menu(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
    sleep(10)
    context_menu_page.open_menu()
    sleep(10)
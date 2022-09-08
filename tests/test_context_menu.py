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

def test_check_alert_text(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
    context_menu_page.open_menu()
    assert context_menu_page.get_text_alert() == 'You selected a context menu'


from pages.login_page import LoginPage


def test_guest_can_go_to_login_page_and_elements_present(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()




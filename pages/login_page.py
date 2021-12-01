import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators, LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Url should be contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_BUTTON), "Login form button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM_BUTTON), "Registration form button is not presented"

    def register_new_user(self, email, password):
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_BUTTON)
        user_name = self.browser.find_element(*LoginPageLocators.USER_NAME_INPUT)
        password1 = self.browser.find_element(*LoginPageLocators.USER_PASSWD_INPUT)
        password2 = self.browser.find_element(*LoginPageLocators.USER_PASSWD_CONFIRM_INPUT)
        user_name.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)
        button.click()

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    REGISTRATION_FORM_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
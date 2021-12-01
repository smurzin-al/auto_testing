from selenium.webdriver.common.by import By


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass

class LoginPageLocators():
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    REGISTRATION_FORM_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    INFO_MESSAGE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    INFO_MESSAGE_BASKET_PRICE = (
    By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)')

    INFO_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')

    INFO_MESSAGE_PRODUCT_PRICE_VALUE = (
    By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    PRODUCT_PRICE_VALUE = (
    By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR,"#content_inner > p")
    SOME_ITEM_IN_BASKET = (By.CSS_SELECTOR,'#basket_formset > div')

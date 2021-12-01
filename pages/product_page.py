import time

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.button_add_to_basket_is_present()
        self.button_add_to_basket_click()
        self.solve_quiz_and_get_code()

    def add_to_basket_without_code(self):
        self.button_add_to_basket_is_present()
        self.button_add_to_basket_click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        alert = self.browser.switch_to_alert()
        alert.accept()


    def success_message_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Cant be success message"

    def button_add_to_basket_is_present(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), \
            "Button add to basket is not presented"

    def button_add_to_basket_click(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_VALUE).text

    def checking_basket(self):
        info_message_product_in_basket = (self.browser.find_element(
            *ProductPageLocators.INFO_MESSAGE_PRODUCT_IN_BASKET).text)
        assert "has been added to your basket" in info_message_product_in_basket, \
            "No such message: has been added to your basket"

        info_message_basket_price = (self.browser.find_element(
            *ProductPageLocators.INFO_MESSAGE_BASKET_PRICE).text)
        assert "Your basket total is now " in info_message_basket_price, \
            "No such message: Your basket total is now"

        product_name = self.get_product_name()
        product_price = self.get_product_price()
        self.compare_product_name(product_name)
        self.compare_product_price(product_price)

    def compare_product_name(self, product_name):
        info_message_product_name = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME).text
        assert self.compare_values(info_message_product_name, product_name), "Wrong product's name in basket"

    def compare_product_price(self, product_price):
        info_message_product_price = self.browser.find_element(
            *ProductPageLocators.INFO_MESSAGE_PRODUCT_PRICE_VALUE).text
        assert self.compare_values(info_message_product_price, product_price), "Wrong product's price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message don't dissappeared"
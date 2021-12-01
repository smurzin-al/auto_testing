from pages.base_page import BasePage
from pages.locators import BasePageLocators


class BasketPage(BasePage):
    def check_basket_for_empty(self):
        self.check_basket_for_empty_message()
        self.check_basket_for_empty_no_items()

    def check_basket_for_empty_message(self):
        assert 'Ваша корзина пуста' in self.browser.find_element(*BasePageLocators.MESSAGE_EMPTY_BASKET).text, "basket " \
                                                                                                               "not " \
                                                                                                               "empty "

    def check_basket_for_empty_no_items(self):
        assert self.is_not_element_present(*BasePageLocators.SOME_ITEM_IN_BASKET), "basket not empty"

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_btn_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button basket is not presented"

    def add_to_basket(self):
        btn_basket = self.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_basket.click()

    def should_be_book_name_in_basket_match(self):
        book_name_in_basket = self.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
        book_name = self.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name_in_basket == book_name, "Book name is different in the basket"

    def should_be_book_price_in_basket_match(self):
        book_price_in_basket = self.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text
        book_price = self.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price_in_basket == book_price, "Book name is different in the basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"

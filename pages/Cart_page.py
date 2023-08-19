from base.base_class import Base
from decimal import Decimal

from utilities.logger import Logger


class Cart(Base):

    def __init__(self, driver):
        super().__init__(driver)

    #locators
    cart_total_to_pay_1_xpath = '//span[@class="cart_total"]'
    cart_total_to_pay_2_xpath = '//span[@class="cart_total_all"]'

    #Getters
    def get_cart_total_to_pay_1(self):
        return self.get_locator(self.cart_total_to_pay_1_xpath)
    def get_cart_total_to_pay_2(self):
        return self.get_locator(self.cart_total_to_pay_2_xpath)

    #Actions

    def check(self, sum_price):
        print()


    #Methods

    def check_total_to_pay(self, total_payment):
        Logger.add_start_step(method='check_total_to_pay')
        self.scroll_to_xpath_locator(self.cart_total_to_pay_1_xpath)
        total_to_pay_1_local = self.get_text_from_xpath_locator(self.cart_total_to_pay_1_xpath)
        total_to_pay_1_local = Decimal(total_to_pay_1_local.split()[0])
        assert total_to_pay_1_local == total_payment
        print('1st total to pay field is checked')
        self.scroll_to_xpath_locator(self.cart_total_to_pay_2_xpath)
        total_to_pay_2_local = self.get_text_from_xpath_locator(self.cart_total_to_pay_2_xpath)
        total_to_pay_2_local = Decimal(total_to_pay_2_local.split()[0])
        assert total_to_pay_2_local == total_payment
        print('2nd total to pay field is checked')
        Logger.add_end_step(url=self.driver.current_url, method='check_total_to_pay')







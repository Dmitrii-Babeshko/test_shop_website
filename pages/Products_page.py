from selenium.webdriver.common.by import By
from time import sleep
from base.base_class import Base
from decimal import Decimal

from utilities.logger import Logger


class Products(Base):

    def __init__(self, driver):
        super().__init__(driver)


    #locators
    xl_size_xpath = '//label[@for="psize-XL"]'
    add_to_cart_locator_xpath = '//button[contains(@class, "submit_but add_to_card")]'
    continue_shopping_button_xpath = '//a[@class="light_button hide_adding"]'
    cart_icon_xpath = '//a[@title="Cart"]'
    price_xpath = '//span[@class="product_page_price_actual"]'
    sum_price = 0

    #Getters
    def get_xl_size(self):
        return self.get_locator(self.xl_size_xpath)

    def get_add_to_cart(self):
        return self.driver.find_element(By.XPATH, self.add_to_cart_locator_xpath)

    def get_continue_shopping_button(self):
        return self.driver.find_element(By.XPATH, self.continue_shopping_button_xpath)

    def get_cart_button(self):
        return self.driver.find_element(By.XPATH, self.cart_icon_xpath)

    def get_price(self):
        return self.driver.find_element(By.XPATH, self.price_xpath)


    #Actions

    def click_xl_size(self):
        self.get_xl_size().click()
        print('Click xl size')

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print('Click t shirt paul and shark add to cart')

    def click_continue_shopping(self):
        sleep(1)
        self.get_continue_shopping_button().click()
        print('Click continue shopping')

    def click_go_to_cart(self):
        self.get_cart_button().click()
        print('Click go to cart button')

    def add_to_sum_price(self):
        price_ = self.get_text_from_xpath_locator(self.price_xpath)
        print(price_)
        pp = price_.split()
        self.sum_price += Decimal(pp[0])
        print(f'Total payable: {self.sum_price} GEL')

    #Methods

    def t_shirt_paul_and_shark_add_to_cart(self):
        Logger.add_start_step(method='t_shirt_paul_and_shark_add_to_cart')
        self.scroll_to_xpath_locator(self.add_to_cart_locator_xpath)
        self.click_add_to_cart()
        print('Bug, button is not clickable')
        sleep(1)
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='t_shirt_paul_and_shark_add_to_cart')

    def add_to_cart_xl_product(self):
        Logger.add_start_step(method='add_to_cart_xl_product')
        self.click_xl_size()
        self.add_to_sum_price()
        self.click_add_to_cart()
        self.click_continue_shopping()
        Logger.add_end_step(url=self.driver.current_url, method='add_to_cart_xl_product')






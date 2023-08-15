from time import sleep
from selenium.webdriver import Keys
from base.base_class import Base


class Men_Cloth(Base):

    def __init__(self, driver):
        super().__init__(driver)

    #locators
    men_cloth_button_xpath = '//a[@href="https://elitesport.ge/en/mens/"]'
    left_price_holder_xpath = '//span[@style="left: 0%;"]'
    right_price_holder_xpath = '//span[@style="left: 100%;"]'
    l_checkbox_xpath = '//label[@for="checkbox-L"]'
    xl_checkbox_xpath = '//label[@for="checkbox-XL"]'
    xxl_checkbox_xpath = '//label[@for="checkbox-XXL"]'
    price_max_text_xpath = '//input[@id="amount1"]'
    price_min_text_xpath = '//input[@id="amount"]'
    sort_button_xpath = '//a[@class="chosen-single"]'
    sort_search_button_xpath = '//input[@class="chosen-search-input"]'
    t_shirt_paul_and_shark_xpath = '//*[@id="catalog_holder"]/li[1]/div[3]/a'
    tracksuit_xpath = '//*[@id="catalog_holder"]/li[8]/div[3]/a'
    product_2_xpath = '//*[@id="catalog_holder"]/li[2]/div[3]/a'
    hypers_t_shirt_xpath = '//*[@id="catalog_holder"]/li[3]/div[3]/a'

    #Getters
    def get_men_cloth_button(self):
        return self.get_locator(self.men_cloth_button_xpath)
    def get_l_checkbox(self):
        return self.get_locator(self.l_checkbox_xpath)
    def get_xl_checkbox(self):
        return self.get_locator(self.xl_checkbox_xpath)
    def get_xxl_checkbox(self):
        return self.get_locator(self.xxl_checkbox_xpath)
    def get_price_max(self):
        return self.get_locator(self.price_max_text_xpath)
    def get_price_min(self):
        return self.get_locator(self.price_min_text_xpath)
    def get_sort_button(self):
        return self.get_locator(self.sort_button_xpath)
    def get_sort_search_button(self):
        return self.get_locator(self.sort_search_button_xpath)
    def get_t_shirt_paul_and_shark(self):
        return self.get_locator(self.t_shirt_paul_and_shark_xpath)
    def get_tracksuit(self):
        return self.get_locator(self.tracksuit_xpath)
    def get_product_2(self):
        return self.get_locator(self.product_2_xpath)
    def get_hypers_t_shirt(self):
        return self.get_locator(self.hypers_t_shirt_xpath)

    #Actions

    def click_men_cloth_button(self):
        self.get_men_cloth_button().click()
        print('Click men cloth button')

    def move_left_price_holder(self, pixels):
        self.click_and_hold(self.left_price_holder_xpath, pixels, 0)
        print('Change left price filter')
        self.wait_loading()

    def move_right_price_holder(self, pixels):
        self.click_and_hold(self.right_price_holder_xpath, pixels, 0)
        print('Change right price filter')
        self.wait_loading()

    def click_l_checkbox(self):
        self.get_l_checkbox().click()
        print('Click l checkbox')
        self.wait_loading()

    def click_xl_checkbox(self):
        self.get_xl_checkbox().click()
        print('Click xl checkbox')
        self.wait_loading()

    def click_xxl_checkbox(self):
        self.get_xxl_checkbox().click()
        print('Click xxl checkbox')
        self.wait_loading()

    def check_price_filter(self):
        max_ = int(self.get_price_max().get_attribute('value'))
        min_ = int(self.get_price_min().get_attribute('value'))
        assert (max_ < 326) and (min_ > 49)
        print(f'Min price "{min_}", max price {max_} checked')

    def click_sort_button_ascending_price(self):
        self.get_sort_button().click()
        sleep(1)
        self.get_sort_search_button().send_keys(Keys.ARROW_DOWN)
        self.get_sort_search_button().send_keys(Keys.ARROW_DOWN)
        self.get_sort_search_button().send_keys(Keys.RETURN)
        self.wait_loading()
        print('Choose sort button ascending price')

    def click_t_shirt_paul_and_shark(self):
        self.get_t_shirt_paul_and_shark().click()
        print('Click t shirt paul and shark')

    def click_tracksuit(self):
        self.get_tracksuit().click()
        print('Click tracksuit')

    def click_product_2(self):
        self.get_product_2().click()
        print('Click yachting_t_shirt')

    def click_hypers_t_shirt(self):
        self.get_hypers_t_shirt().click()
        print('Click hypers t shirt')


    #Methods

    def filter_and_choose_t_shirt(self):
        self.click_men_cloth_button()
        self.move_left_price_holder(4)
        self.move_right_price_holder(-40)
        self.check_price_filter()
        self.scroll_to_xpath_locator(self.xl_checkbox_xpath)
        self.click_xl_checkbox()
        self.click_sort_button_ascending_price()
        self.scroll_to_xpath_locator(self.t_shirt_paul_and_shark_xpath)
        self.click_t_shirt_paul_and_shark()


    def filter_the_1st_variant(self):
        self.click_men_cloth_button()
        self.move_left_price_holder(4)
        self.move_right_price_holder(-40)
        self.check_price_filter()
        self.scroll_to_xpath_locator(self.xl_checkbox_xpath)
        self.click_xl_checkbox()
        self.click_sort_button_ascending_price()
    def choose_1st_product(self):
        self.scroll_to_xpath_locator(self.tracksuit_xpath)
        self.click_tracksuit()

    def choose_2nd_product(self):
        self.wait_loading()
        self.scroll_to_xpath_locator(self.product_2_xpath)
        self.click_product_2()

    def choose_3_product(self):
        self.wait_loading()
        self.scroll_to_xpath_locator(self.hypers_t_shirt_xpath)
        self.click_hypers_t_shirt()


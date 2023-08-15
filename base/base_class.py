from datetime import datetime, timezone, timedelta
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_locator(self, locator):
        #sleep(1)
        return WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, locator))
        )

    def scroll_to_xpath_locator(self, xpath_locator):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_locator(xpath_locator)).perform()

    def get_text_from_xpath_locator(self, xpath_locator):
        try:
            # Attempt to find the element by the given XPath
            element = self.driver.find_element(By.XPATH, xpath_locator)
            txt = element.text
        except:
            try:
                # If the first attempt fails, try using the custom get_locator method
                element = self.get_locator(xpath_locator)
                txt = element.text
            except:
                try:
                    # If both attempts fail, try using various attribute methods
                    txt = element.get_attribute("textContent") or \
                          element.get_attribute("innerText") or \
                          element.get_property("innerText") or \
                          element.get_attribute('value')
                except:
                    txt = "Text extraction failed"  # Handle failure case

        return txt

    def click_and_hold(self, xpath_locator, left_right, up_down):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_locator(xpath_locator)).move_by_offset(left_right, up_down).release().perform()

    def scroll(self, up_down, left_right=0):
        self.driver.execute_script(f'window.scrollTo({left_right}, {up_down})')

    def wait_loading(self):
        sleep(5)

    def print_current_url(self):
        url = self.driver.current_url
        print(f'Current url: {url}')

    def assert_word(self, element, word):
        value_word = element.text
        assert value_word == word
        print(f'Word "{word}" is on the page')

    def get_screenshot(self):
        now_date = datetime.now(timezone(timedelta(hours=3), "UTC+3")).strftime("%d.%m.%Y %H.%M.%S %Z")
        screenshot_name = 'Shop_test ' + now_date + '.png'
        self.driver.save_screenshot(f'C:/Pycharm/test_shop/screen/' + screenshot_name)

    def assert_and_print_url(self, result):
        url = self.driver.current_url
        assert url == result
        print(f'Url is asserted: {result} ')


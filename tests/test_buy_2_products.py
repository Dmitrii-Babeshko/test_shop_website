from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
from pages.Cart_page import Cart
from pages.Login_page import Login
from pages.Men_Cloth_page import Men_Cloth
from pages.Products_page import Products


#@pytest.mark.run(order=1)
@allure.description('Test of buying products № 2')
def test_buy_product_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # False/True Закрытие/нет браузера
    options.page_load_strategy = 'normal' # normal/eager/none загружать/нет полностью страницы
    driver = webdriver.Chrome(options=options, service=Service())
    print('Start test 2')

    login_page = Login(driver)
    login_page.authorization()
    men_cloth_page = Men_Cloth(driver)
    men_cloth_page.filter_the_1st_variant()
    men_cloth_page.choose_1st_product()
    products_page = Products(driver)
    products_page.add_to_cart_xl_product()
    driver.back()
    men_cloth_page.choose_2nd_product()
    products_page.add_to_cart_xl_product()
    driver.back()
    men_cloth_page.choose_3_product()
    products_page.add_to_cart_xl_product()
    products_page.click_go_to_cart()
    cart_page = Cart(driver)
    cart_page.check_total_to_pay(products_page.sum_price)
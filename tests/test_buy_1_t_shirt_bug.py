from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.Login_page import Login
from pages.Men_Cloth_page import Men_Cloth
from pages.Products_page import Products


#@pytest.mark.run(order=1)
def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", False)  # False/True Закрытие/нет браузера
    options.page_load_strategy = 'normal' # normal/eager/none загружать/нет полностью страницы
    driver = webdriver.Chrome(options=options, service=Service())
    print('Start test 1')

    login = Login(driver)
    login.authorization()
    men = Men_Cloth(driver)
    men.filter_and_choose_t_shirt()
    products = Products(driver)
    products.t_shirt_paul_and_shark_add_to_cart()
    sleep(10)
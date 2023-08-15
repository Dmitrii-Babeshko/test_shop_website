from base.base_class import Base

class Login(Base):

    url = 'https://elitesport.ge/en/'

    def __init__(self, driver):
        super().__init__(driver)

    #locators xpath
    login_text_xpath = '4ssss@mail.ru'
    login_email_input_xpath = '//input[@name="login[email]"]'
    password_input_xpath = '//input[@name = "login[password]"]'
    password_text_xpath = 'qwerty_12345'
    login_button_xpath = '//a[@class="login_button"]'
    login_continue_button_xpath = '//a[@class="login_button light_button submit_but"]'
    cabinet_user_name_xpath = '//span[@class="cabinet_user_name"]'



    #Getters
    def get_login_button(self):
        return self.get_locator(self.login_button_xpath)

    def get_login_email_input(self):
        return self.get_locator(self.login_email_input_xpath)

    def get_password_input(self):
        return self.get_locator(self.password_input_xpath)

    def get_login_continue_button(self):
        return self.get_locator(self.login_continue_button_xpath)

    def get_cabinet_user_name(self):
        return self.get_locator(self.cabinet_user_name_xpath)

    #Actions

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    def input_login_email(self, text):
        self.get_login_email_input().send_keys(text)
        print('Input user login')

    def input_password(self, text):
        self.get_password_input().send_keys(text)
        print('Password has been set')

    def click_login_continue_button(self):
        self.get_login_continue_button().click()
        print('Click login continue button')

    #Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_login_button()
        self.input_login_email(self.login_text_xpath)
        self.input_password(self.password_text_xpath)
        self.click_login_continue_button()
        self.assert_word(self.get_cabinet_user_name(), 'Dimitrii')
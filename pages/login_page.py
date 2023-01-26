import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page(Base):

    url = 'https://shop.kz/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    login_button = "//a[@id='btn_show_auth']"
    login = "//input[@id='ppUSER_LOGIN']"
    password = '//input[@id="ppUSER_PASSWORD"]'
    final = "//input[@id='login_btn']"
    main_word = '//span[@class="bx-user-name"]'

    # Getters

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_final(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final)))

    def get_main_word(self):
        mw = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.main_word)))
        return mw


    # Actions

    def click_login_button(self):
        self.get_login_button().click()
        print("Click on login button")

    def input_login(self, login):
        self.get_login().send_keys(login)
        print("Input login")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_final(self):
        self.get_final().click()
        print("Click on final")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_button()
        self.input_login('87076838297')
        self.input_password('Aa31133113')
        self.click_final()
        self.assert_word(self.get_main_word(), "Анна Хамылова")
        print("Вы успешно авторизованы")



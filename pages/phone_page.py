import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Phone_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    price_filter = "//a[@data-value='price-asc']"
    buy_button = "//a[@id='bx_3966226736_1388077_buy_link']"


    # Getters

    def get_price_filter(self):
        action = ActionChains(self.driver)
        a = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter)))
        action.move_to_element(a)
        return a

    def get_buy_button(self):
        action = ActionChains(self.driver)
        a = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))
        action.move_to_element(a)
        return a


    # Actions

    def click_get_price_filter(self):
        self.get_price_filter().click()
        print("Filter price is chosen")

    def click_buy_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.get_buy_button())
        self.get_buy_button().click()
        print("You added product to cart")

    def click_in_cart(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.get_buy_button())
        self.get_buy_button().click()
        print("You are in cart")

    # Methods

    def filter_price(self):
        self.get_current_url()
        self.click_get_price_filter()

    def add_to_cart(self):
        self.get_current_url()
        self.click_buy_button()
        time.sleep(1)
        self.click_in_cart()
        self.assert_url('https://shop.kz/personal/basket/')




import time

from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Filter_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    price_min_shop = "//input[@name='filter_02_P7_MIN']"
    price_max_shop = "//input[@name='filter_02_P7_MAX']"
    another_town_full_price = "//input[@name='filter_02_10308_2571320779']"
    screen_size = "//input[@name='filter_02_16002_1258568867']"
    matrice_type = "//input[@id='filter_02_2863_2318049086']"
    accumulator = "//input[@name='filter_02_6551_2361151060']"
    screen_update_min = "//input[@id='filter_02_14676_MIN']"
    screen_update_max = "//input[@id='filter_02_14676_MAX']"
    interface = "//input[@id='filter_02_395_52458567']"
    color = "//input[@id='filter_02_403_3369651866']"
    confirm_button = "//input[@id='set_filter']"





    # Getters

    def get_price_min_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min_shop)))

    def get_price_max_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max_shop)))

    def get_another_town_full_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.another_town_full_price)))

    def get_screen_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_size)))

    def get_matrice_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.matrice_type)))

    def get_accumulator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accumulator)))

    def get_screen_update_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_update_min)))

    def get_screen_update_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_update_max)))

    def get_interface(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.interface)))

    def get_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    # Actions

    def select_price_min_shop(self):
        self.get_price_min_shop().send_keys("100")
        print("Price_min_shop send keys")

    def select_price_max_shop(self):
        self.get_price_max_shop().send_keys("1000000")
        print("Price_max_shop send keys")

    def select_another_town_full_price(self):
        self.get_another_town_full_price().click()
        print("another_town_full_price unselected")

    def select_screen_size(self):
        self.get_screen_size().click()
        print("screen_size unchecked")

    def select_matrice_type(self):
        self.get_matrice_type().click()
        print("matrice_type selected")

    def select_accumulator(self):
        self.get_accumulator().click()
        print("accumulator selected")

    def select_screen_update_min(self):
        self.get_screen_update_min().send_keys("60")
        print("screen_update_min selected")

    def select_screen_update_max(self):
        self.get_screen_update_max().send_keys("144")
        print("screen_update_max selected")

    def select_interface(self):
        self.get_interface().click()
        print("interface selected")

    def select_color(self):
        self.get_color().click()
        print("color selected")

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("button is clicked")


    # Methods

    def select_filter(self):
        self.get_current_url()
        self.select_price_min_shop()
        self.select_price_max_shop()
        self.select_another_town_full_price()
        self.select_screen_size()
        self.select_matrice_type()
        self.select_accumulator()
        self.select_screen_update_min()
        self.select_screen_update_max()
        self.select_interface()
        self.select_color()
        time.sleep(1)
        self.click_confirm_button()
        time.sleep(1)





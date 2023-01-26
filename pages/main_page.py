from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    phones = "//a[@href='/catalog/smartfony-i-gadzhety/']"
    smartphones = "//a[@href='/smartfony/']"
    page_title = "//h1[@id='pagetitle']"

    # Getters

    def get_phones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phones)))

    def get_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones)))

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))


    # Actions

    def move_to_phones(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_phones()).perform()
        print("Move to phones")

    def click_to_smartphones(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_smartphones()).click().perform()
        print("Click to smartphones")


    # Methods

    def select_category(self):
        self.get_current_url()
        self.move_to_phones()
        self.click_to_smartphones()
        self.assert_word(self.get_page_title(), 'Смартфоны в Алматы')
        print("You have chosen phones: smartphones")







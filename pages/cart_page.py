from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    finish = "//button[@id='CartSubmit']"

    # Getters

    def get_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish)))


    # Actions

    def click_finish(self):
        self.get_finish().click()
        print("Click finish button")

    # Methods

    def payment_finish(self):
        self.get_current_url()
        self.click_finish()
        self.assert_url('https://shop.kz/personal/order/')

    def finish_screen(self, url):
        self.get_current_url()
        self.assert_url(url)
        self.screenshot()
        self.driver.quit()




import time

from base.base_class import Base
from pages.filter_page import Filter_page
from pages.phone_page import Phone_page
from pages.login_page import Login_page
from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import Main_page
from pages.cart_page import  Cart_page


def test_smoke():
    new_driver_path = "C:\\Users\\Anna\\PycharmProjects\\pythonProject3\\geckodriver.exe"
    new_binary_path = 'C:\\Users\\Anna\\AppData\\Local\\Mozilla Firefox\\firefox.exe'
    option = FirefoxOptions()
    option.binary_location = new_binary_path
    serv = Service(new_driver_path)
    driver = webdriver.Firefox(service=serv, options=option)

    driver.get('https://shop.kz/')

    """Авторизация"""

    login = Login_page(driver)
    login.authorization()

    """Выбор категории товара"""

    mp = Main_page(driver)
    mp.select_category()

    """Заполнение фильтров"""

    cp = Filter_page(driver)
    cp.select_filter()

    client_page = Phone_page(driver)
    client_page.filter_price()

    """Выбор нужного товара"""

    client_page.add_to_cart()

    finish = Cart_page(driver)
    finish.payment_finish()
    finish.finish_screen('https://shop.kz/personal/order/')

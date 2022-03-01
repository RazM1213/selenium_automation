from unittest import TestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from MainPage import MainPage
from HeaderPage import HeaderPage
from LoginPopUpPage import LoginPopUpPage
from CartPage import CartPage
from CategoryPage import CategoryPage
from ProductPage import ProductPage
from CheckoutPage import CheckoutPage
from MyOrdersPage import MyOrdersPage


class test_AOS(TestCase):
    def setup(self):
        self.service = Service(r"C:\Users\razm1\selenium_drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://advantageonlineshopping.com/#/")
        self.driver.maximize_window()

    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass

    def test_10(self):
        pass

    def tearDown(self):
        self.driver.close()


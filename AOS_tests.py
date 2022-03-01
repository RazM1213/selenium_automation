from unittest import TestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from MainPage import MainPage
from HeaderPage import HeaderPage
from LoginPopUpPage import LoginPopUpPage
from CartPage import CartPage
from CategoryPage import CategoryPage
from ProductPage import ProductPage
from CheckoutPage import CheckoutPage
from MyOrdersPage import MyOrdersPage


class test_AOS(TestCase):
    def setUp(self):
        """
        Setting Up the webdriver at the AOS's url.
        Instantiating all relevant page objects for the upcoming tests.
        """
        self.service = Service(r"C:\Users\razm1\selenium_drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.header_page = HeaderPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.login_pop_up_page = LoginPopUpPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.category_page = CategoryPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.my_orders_page = MyOrdersPage(self.driver)

    def test_1(self):
        """
        This test checks that the number next to the cart icon
        updates correctly according to the actual number of products in the cart
        """
        self.main_page.click_category("speakersImg")
        self.category_page.product_click(0)
        self.product_page.increase_quantity(1)
        self.product_page.add_to_cart_button_click()
        self.product_page.return_to_category_button_click()
        self.category_page.product_click(1)
        self.product_page.increase_quantity(2)
        self.product_page.add_to_cart_button_click()

        self.assertEqual(self.header_page.shopping_cart_number(), "5")

    def test_2(self):
        self.main_page.click_category("laptopsImg")
        self.category_page.product_click(0)
        self.product_page.increase_quantity(1)
        self.product_page.add_to_cart_button_click()
        product1 = {"name": self.product_page.product_title(),
                    "qty": "2",
                    "color": self.product_page.product_color()}
        self.product_page.return_to_category_button_click()
        self.category_page.product_click(1)
        self.product_page.increase_quantity(2)
        self.product_page.add_to_cart_button_click()
        product2 = {"name": self.product_page.product_title(),
                    "qty": "3",
                    "color": self.product_page.product_color()}
        self.product_page.return_to_category_button_click()
        self.category_page.product_click(2)
        self.product_page.increase_quantity(3)
        self.product_page.add_to_cart_button_click()
        product3 = {"name": self.product_page.product_title(),
                    "qty": "4",
                    "color": self.product_page.product_color()}

        self.header_page.shopping_cart_button_hover()
        self.assertIn(self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_first_product())["name"][:-4], product3["name"])
        self.assertEqual(product3["color"], self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_first_product())["color"])
        self.assertEqual(product3["qty"], self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_first_product())["qty"])

        self.assertIn(self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_second_product())["name"][:-4], product2["name"])
        self.assertEqual(product2["color"], self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_second_product())["color"])
        self.assertEqual(product2["qty"], self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_second_product())["qty"])

        self.assertIn(self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_third_product())["name"][:-4], product1["name"])
        self.assertEqual(product1["color"], self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_third_product())["color"])
        self.assertEqual(product1["qty"], self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_third_product())["qty"])

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
        sleep(10)



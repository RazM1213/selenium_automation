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
from random import choice,randint

class test_AOS(TestCase):
    def setUp(self):
        """
        Setting Up the webdriver at the AOS's url.
        Instantiating all relevant page objects for the upcoming tests.
        """
        #self.service = Service(r"C:\Users\razm1\selenium_drivers\chromedriver.exe")
        self.service = Service(r"C:\Users\97255\Desktop\driverdownload\chromedriver.exe")

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
        self.categories = ["speakersImg","laptopsImg","tabletsImg","headphonesImg","miceImg"]
        self.soldout = False

    def test_1(self):
        """
        This test checks that the number next to the cart icon
        updates correctly according to the actual number of products in the cart
        """
        self.main_page.click_category(choice(self.categories))
        self.category_page.product_click(0)
        self.product_page.increase_quantity(1)
        self.product_page.add_to_cart_button_click()
        self.product_page.return_to_category_button_click()
        self.category_page.product_click(1)
        self.product_page.increase_quantity(2)
        self.product_page.add_to_cart_button_click()

        self.assertEqual(self.header_page.shopping_cart_number(), "5")

    def test_2(self):
        self.main_page.click_category(choice(self.categories))
        list_randoms = []
        products = {1: None, 2: None, 3: None}
        i = 1
        while i < 4:
            self.soldout = False
            randnum = randint(0, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                pass
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout == True:
                self.product_page.return_to_category_button_click()
                pass
            qty = randint(1, 4)
            self.product_page.increase_quantity(qty)
            self.product_page.add_to_cart_button_click()
            products[i] = {"name": self.product_page.product_title(),
                           "qty": str(qty + 1),
                           "color": self.product_page.product_color()}
            self.product_page.return_to_category_button_click()
            i += 1

        self.header_page.shopping_cart_button_hover()

        self.assertIn(
            self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_third_product())[
                "name"][:-4], products[1]["name"])
        self.assertEqual(products[1]["color"], self.header_page.cart_hover_table_product_details(
            self.header_page.cart_hover_table_third_product())["color"])
        self.assertEqual(products[1]["qty"], self.header_page.cart_hover_table_product_details(
            self.header_page.cart_hover_table_third_product())["qty"])

        self.assertIn(
            self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_second_product())[
                "name"][:-4], products[2]["name"])
        self.assertEqual(products[2]["color"], self.header_page.cart_hover_table_product_details(
            self.header_page.cart_hover_table_second_product())["color"])
        self.assertEqual(products[2]["qty"], self.header_page.cart_hover_table_product_details(
            self.header_page.cart_hover_table_second_product())["qty"])

        self.assertIn(
            self.header_page.cart_hover_table_product_details(self.header_page.cart_hover_table_first_product())[
                "name"][:-4], products[3]["name"])
        self.assertEqual(products[3]["color"], self.header_page.cart_hover_table_product_details(
            self.header_page.cart_hover_table_first_product())["color"])
        self.assertEqual(products[3]["qty"], self.header_page.cart_hover_table_product_details(
            self.header_page.cart_hover_table_first_product())["qty"])


    def test_3(self):
        self.main_page.click_category(choice(self.categories))
        list_randoms = []
        products = {1: None, 2: None}
        i = 1
        while i < 3:
            randnum = randint(0, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                pass
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout == True:
                self.product_page.return_to_category_button_click()
                pass
            qty = randint(1, 4)
            self.product_page.increase_quantity(qty)
            self.product_page.add_to_cart_button_click()
            products[i] = {"name": self.product_page.product_title(),
                           "qty": str(qty + 1),
                           "color": self.product_page.product_color()}
            self.product_page.return_to_category_button_click()
            i += 1

        #now deletes a product
        self.header_page.remove_product_button_click(1)
        #check if the product is not in the cart
        self.assertNotIn(products[2]["name"][:5], self.header_page.cart_hover_table().text)
        self.assertIn(products[1]["name"][:5], self.header_page.cart_hover_table().text)




    def test_4(self):
        self.main_page.click_category(choice(self.categories))
        i = 0
        while i < 1:
            self.soldout = False
            self.category_page.product_click(randint(0, len(self.category_page.products_list()) - 1))
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout is True:
                self.product_page.return_to_category_button_click()
                pass
            self.product_page.increase_quantity(randint(1, 4))
            self.product_page.add_to_cart_button_click()
            i += 1
        self.header_page.shopping_cart_button_click()
        self.assertTrue(self.cart_page.check_if_the_page_is_cart())




    def test_5(self):
        self.main_page.click_category(choice(self.categories))
        list_randoms = []
        products = {1: None, 2: None, 3: None}
        i = 1
        while i < 4:
            self.soldout = False
            randnum = randint(1, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                pass
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout == True:
                pass
            qty = randint(1, 2)
            self.product_page.increase_quantity(qty)
            self.product_page.add_to_cart_button_click()
            products[i] = {"name": self.product_page.product_title(),
                           "qty": str(qty + 1),
                           "price": self.product_page.product_price()}
            self.product_page.return_to_category_button_click()
            i += 1
        total_prices = 0.0
        for product in range(1, len(products)-1):
            total_prices += products[product]["price"]
            print(products[product]["price"])


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



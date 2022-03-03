from unittest import TestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from MainPage import MainPage
from HeaderPage import HeaderPage
from LoginPopUpPage import LoginPopUpPage
from CartPage import CartPage
from CategoryPage import CategoryPage
from ProductPage import ProductPage
from MyOrdersPage import MyOrdersPage
from OrderPaymentPage import OrderPaymentPage
from CreateAccountPage import CreateAccountPage
from random import choice,randint
from MyAccountPage import MyAccountPage


class test_AOS(TestCase):
    def setUp(self):
        """
        Setting Up the webdriver at the AOS's url.
        Instantiating all relevant page objects for the upcoming tests.
        """
        self.service = Service(r"C:\Users\razm1\selenium_drivers\chromedriver.exe")
        #self.service = Service(r"C:\Users\97255\Desktop\driverdownload\chromedriver.exe")

        # Setting up the webdriver and browser:
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        # Instantiating page objects:
        self.header_page = HeaderPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.login_pop_up_page = LoginPopUpPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.category_page = CategoryPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.my_orders_page = MyOrdersPage(self.driver)
        self.order_payment_page = OrderPaymentPage(self.driver)
        self.create_account_page = CreateAccountPage(self.driver)
        self.my_account_page = MyAccountPage(self.driver)

        # Useful attributes for randomizing tests:
        self.categories = ["speakersImg","laptopsImg","tabletsImg","headphonesImg","miceImg"]
        self.soldout = False

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
        """
        This test chooses 3 random products, sets 3 random quantities for them - and
        checks that they appear correctly in the cart hover window
        """
        # self.main_page.click_category(choice(self.categories))
        self.main_page.click_category("headphonesImg")
        list_randoms = []
        products = {1: None, 2: None, 3: None}
        i = 1
        while i < 4:
            self.soldout = False
            randnum = randint(0, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                continue
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout == True:
                self.product_page.return_to_category_button_click()
                continue
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
        """
        This test checks that after adding 2 random products to the cart, and deleting
        one of them - the correct product is removed and no longer appears in the cart
        """
        self.main_page.click_category(choice(self.categories))
        list_randoms = []
        products = {1: None, 2: None}
        i = 1
        while i < 3:
            randnum = randint(0, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                continue
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout == True:
                self.product_page.return_to_category_button_click()
                continue
            qty = randint(1, 4)
            self.product_page.increase_quantity(qty)
            self.product_page.add_to_cart_button_click()
            products[i] = {"name": self.product_page.product_title(),
                           "qty": str(qty + 1),
                           "color": self.product_page.product_color()}
            self.product_page.return_to_category_button_click()
            i += 1

        # now deletes a product
        self.header_page.remove_product_button_click(0)
        # check if the product is not in the cart
        self.assertNotIn(products[2]["name"][:5], self.header_page.cart_hover_table().text)
        self.assertIn(products[1]["name"][:5], self.header_page.cart_hover_table().text)

    def test_4(self):
        """
        This test checks that the user can navigate to the shopping cart page
        by pressing on the cart icon after adding a product to the cart
        """
        self.main_page.click_category(choice(self.categories))
        i = 0
        while i < 1:
            self.soldout = False
            self.category_page.product_click(randint(0, len(self.category_page.products_list()) - 1))
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout is True:
                self.product_page.return_to_category_button_click()
                continue
            self.product_page.increase_quantity(randint(1, 4))
            self.product_page.add_to_cart_button_click()
            i += 1
        self.header_page.shopping_cart_button_click()
        self.assertTrue(self.cart_page.check_if_the_page_is_cart())

    def test_5(self):
        """
        This test checks that the total order price is the sum of all the products
        which are in the cart - according to the actual products' price as shown
        when ordering them
        Moreover the test prints for every product: name, quantity and price
        """
        self.main_page.click_category(choice(self.categories))
        list_randoms = []
        products = {1: None, 2: None, 3: None}
        i = 1
        while i < 4:
            self.soldout = False
            randnum = randint(0, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                continue
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout == True:
                self.product_page.return_to_category_button_click()
                continue
            qty = randint(1, 2)
            self.product_page.increase_quantity(qty)
            self.product_page.add_to_cart_button_click()
            products[i] = {"name": self.product_page.product_title(),
                           "qty": str(qty + 1),
                           "price": self.product_page.product_price() * (qty + 1)}
            self.product_page.return_to_category_button_click()
            i += 1
        total_prices = products[1]['price'] + products[2]['price'] + products[3]['price']
        self.header_page.shopping_cart_button_click()
        for product in products.values():
            for k,v in product.items():
                print(f"{k}:{v}")
        self.assertEqual(round(total_prices, 2), self.cart_page.the_total_amount_in_the_checkout_button())

    def test_6(self):
        """
        BUG
        This checks that the feature of editing quantities of products in the cart
        works as expected.
        The expected result is that the edit button will edit the corresponding
        product quantity
        The actual result is that the edit button edits the quantity of the first
        product in the cart table
        """
        self.main_page.click_category(choice(self.categories))
        list_randoms = []
        quantities = []
        i = 1
        while i < 3:
            randnum = randint(0, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                continue
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout:
                self.product_page.return_to_category_button_click()
                continue
            qty = randint(1, 4)
            self.product_page.increase_quantity(qty)
            quantities.append(str(qty+1))
            self.product_page.add_to_cart_button_click()
            self.product_page.return_to_category_button_click()
            i += 1

        self.header_page.shopping_cart_button_click()
        self.cart_page.edit_button_click(0)
        self.product_page.increase_quantity(5)
        self.header_page.shopping_cart_button_click()
        self.cart_page.edit_button_click(1)
        self.product_page.increase_quantity(7)
        self.header_page.shopping_cart_button_click()

        self.assertEqual(quantities[0], self.cart_page.product_quantity(0))
        self.assertEqual(quantities[1], self.cart_page.product_quantity(1))

    def test_7(self):
        """
        This test checks that the navigation from product page to the main page
        works as expected
        """
        self.main_page.click_category("tabletsImg")
        self.category_page.product_click(0)
        self.product_page.return_to_category_button_click()
        self.assertEqual(self.category_page.category_title(), "TABLETS")
        self.header_page.logo_click()
        self.assertTrue(self.main_page.is_it_main_page())

    def test_8(self):
        """
        This test checks an E2E process of order placement via SafePay method for
        a new user
        """
        self.main_page.click_category(choice(self.categories))
        list_randoms = []
        products = {1: None, 2: None}
        i = 1
        while i < 3:
            randnum = randint(0, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                continue
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout == True:
                self.product_page.return_to_category_button_click()
                continue
            qty = randint(1, 4)
            self.product_page.increase_quantity(qty)
            self.product_page.add_to_cart_button_click()
            products[i] = {"name": self.product_page.product_title(),
                           "qty": str(qty + 1),
                           "color": self.product_page.product_color()}
            self.product_page.return_to_category_button_click()
            i += 1

        self.header_page.shopping_cart_button_click()
        self.cart_page.click_checkout()
        self.order_payment_page.registration_button_click()
        self.create_account_page.create_account("TestingSel1", "testingsel@gmail.com", "Ts12")
        self.order_payment_page.next_button_click()
        self.order_payment_page.safepay_payment("SafePayA", "Ts12")
        self.assertTrue(self.order_payment_page.is_it_thank_you_page())
        self.header_page.shopping_cart_button_click()
        self.assertTrue(self.cart_page.is_cart_empty())
        self.header_page.user_menu_button_click()
        self.header_page.my_orders_page_button_click()
        for product in products.values():
            for k, v in product.items():
                if k == "color":
                    continue
                self.assertIn(v.lower(), self.my_orders_page.my_orders_table())
        self.header_page.user_menu_button_click()
        self.header_page.my_account_page_button_click()
        self.my_account_page.delete_account_button_click()

    def test_9(self):
        """
        This test checks an E2E process of order placement via MasterCredit for
        an existing user
        """
        self.main_page.click_category(choice(self.categories))
        list_randoms = []
        products = {1: None, 2: None}
        i = 1
        while i < 3:
            randnum = randint(0, len(self.category_page.products_list()) - 1)
            if randnum in list_randoms:
                continue
            list_randoms.append(randnum)
            self.category_page.product_click(randnum)
            self.soldout = self.product_page.check_if_not_sold_out()
            if self.soldout == True:
                self.product_page.return_to_category_button_click()
                continue
            qty = randint(1, 4)
            self.product_page.increase_quantity(qty)
            self.product_page.add_to_cart_button_click()
            products[i] = {"name": self.product_page.product_title(),
                           "qty": str(qty + 1),
                           "color": self.product_page.product_color()}
            self.product_page.return_to_category_button_click()
            i += 1

        self.header_page.shopping_cart_button_click()
        self.cart_page.click_checkout()
        self.order_payment_page.login_existing_user("RazSelenium", "Neverhood1")
        self.order_payment_page.next_button_click()
        self.order_payment_page.manual_payment("433241235633", "123", "Tester")
        self.assertTrue(self.order_payment_page.is_it_thank_you_page())
        self.header_page.shopping_cart_button_click()
        self.assertTrue(self.cart_page.is_cart_empty())
        self.header_page.user_menu_button_click()
        self.header_page.my_orders_page_button_click()
        for product in products.values():
            for k, v in product.items():
                if k == "color":
                    continue
                self.assertIn(v.lower(), self.my_orders_page.my_orders_table())

    def test_10(self):
        """
        This test checks an E2E process of login and logout
        """
        self.header_page.user_menu_button_click()
        self.login_pop_up_page.sign_in("aaaaa", "Jc12", "no")

        self.header_page.user_menu_button_click()
        self.header_page.my_account_page_button_click()
        self.assertTrue(self.my_account_page.check_user_is_connected("Johnathan cohen"))
        self.header_page.user_menu_button_click()
        self.header_page.sign_out_button_click()

        self.header_page.user_menu_button_click()
        self.assertTrue(self.login_pop_up_page.login_x_button().is_displayed())
        self.login_pop_up_page.login_x_button_click()

    def tearDown(self):
        """
        After each test go to main page and close the browser
        """
        self.header_page.logo_click()
        self.driver.close()



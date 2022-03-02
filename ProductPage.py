from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Each page in the website gets a class - called page object


class ProductPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def product_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h1").text

    def product_price(self):
        return float(self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").text[1:].replace(',',''))

    def product_color(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "#productProperties>div>div>span")[0].get_attribute("title")

    def minus_button(self):
        return self.driver.find_element(By.CLASS_NAME, "minus")

    def plus_button(self):
        return self.driver.find_element(By.CLASS_NAME, "plus")

    def add_to_cart_button(self):
        return self.driver.find_element(By.NAME, "save_to_cart")

    def return_to_category_button(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "a.ng-binding")[0]

    def return_to_home_button(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "div>nav>a")[0]

    def return_to_category_button_click(self):
        self.return_to_category_button().click()

    def return_to_home_button_click(self):
        self.return_to_home_button().click()

    def decrease_quantity(self, i):
        for x in range(i):
            self.minus_button().click()

    def increase_quantity(self, i):
        for x in range(i):
            self.plus_button().click()

    def add_to_cart_button_click(self):
        self.add_to_cart_button().click()

    def check_if_not_sold_out(self):
        for elem in self.driver.find_elements(By.CSS_SELECTOR, "#Description"):
            if "SOLD OUT" in elem.text:
                return True

        return False



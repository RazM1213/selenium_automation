from selenium import webdriver
from selenium.webdriver.common.by import By

# Each page in the website gets a class - called page object


class ProductPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def product_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h1")

    def product_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h2")

    def available_colors(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "span[id='rabbit']")

    def minus_button(self):
        return self.driver.find_element(By.CLASS_NAME, "minus")

    def plus_button(self):
        return self.driver.find_element(By.CLASS_NAME, "plus")

    def add_to_cart_button(self):
        return self.driver.find_element(By.NAME, "save_to_cart")

    def decrease_quantity(self):
        self.minus_button().click()

    def increase_quantity(self):
        self.plus_button().click()

    def add_to_cart_button_click(self):
        self.add_to_cart_button().click()

    def choose_color(self, index):
        self.available_colors()[index].click()




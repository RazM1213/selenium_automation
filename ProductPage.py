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

    def choose_color(self, index):
        self.available_colors()[index].click()




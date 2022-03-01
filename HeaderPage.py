from selenium import webdriver
from selenium.webdriver.common.by import By

# Each page in the website gets a class - called page object


class HeaderPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def nav_bar(self):
        return self.driver.find_element(By.CLASS_NAME, ".desktop-handler")

    def nav_bar_options(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul.desktop-handler")

    def logo(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".logo>a")

    def user_menu_button(self):
        return self.driver.find_element(By.ID, "menuUserLink")

    def shopping_cart_button(self):
        return self.driver.find_element(By.ID, "shoppingCartLink")

    def shopping_cart_number(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "span.cart.ng-binding")[1]

    def help_button(self):
        return self.driver.find_element(By.ID, "helpLink")

    def search_bar(self):
        return self.driver.find_element(By.NAME, "mobile_search")

    def logo_click(self):
        self.logo().click()

    def user_menu_button_click(self):
        self.user_menu_button().click()

    def shopping_cart_button_click(self):
        self.shopping_cart_button().click()

    def help_button_click(self):
        self.help_button().click()

    def send_search_bar(self, key):
        self.search_bar().send_keys(key)


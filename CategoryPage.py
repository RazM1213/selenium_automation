from selenium import webdriver
from selenium.webdriver.common.by import By

# Each page in the website gets a class - called page object


class CategoryPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def category_title(self):
        return self.driver.find_element(By.CLASS_NAME, "categoryTitle")

    def products_list(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".categoryRight>ul>li")

    def product_click(self, index):
        self.products_list()[index].click()

    def filter_menu_options(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".categoryLeft>#mobileSlide>ul")

    def filter_price(self):
        return self.filter_menu_options()[0]

    def filter_compatibility(self):
        return self.filter_menu_options()[1]

    def filter_manufacturer(self):
        return self.filter_menu_options()[2]

    def filter_weight(self):
        return self.filter_menu_options()[3]

    def filter_wireless(self):
        return self.filter_menu_options()[4]

    def filter_color(self):
        return self.filter_menu_options()[5]



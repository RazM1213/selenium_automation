from selenium import webdriver
from selenium.webdriver.common.by import By

# Each page in the website gets a class - called page object


class MyOrdersPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def my_orders_table(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#myAccountContainer>div>table").text.lower()
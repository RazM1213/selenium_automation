from selenium import webdriver
from selenium.webdriver.common.by import By

# Each page in the website gets a class - called page object


class CheckoutPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
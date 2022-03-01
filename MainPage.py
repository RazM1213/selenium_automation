from selenium import webdriver
from selenium.webdriver.common.by import By

# Each page in the website gets a class - called page object


class MainPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def speakers(self):
        return self.driver.find_element(By.ID, "speakersImg")

    def tablets(self):
        return self.driver.find_element(By.ID, "tabletsImg")

    def headphones(self):
        return self.driver.find_element(By.ID, "speakersImg")

    def laptops(self):
        return self.driver.find_element(By.ID, "laptopsImg")

    def mice(self):
        return self.driver.find_element(By.ID, "headphonesImg")

    def click_category(self, id):
        self.driver.find_element(By.ID, id).click()








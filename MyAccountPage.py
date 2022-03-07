from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Each page in the website gets a class - called page object


class MyAccountPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def delete_account_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".cube>.deleteMainBtnContainer")

    def delete_account_confirm_button(self):
        return self.driver.find_element(By.CLASS_NAME, "deleteRed")

    def delete_account_button_click(self):
        while True:
            try:
                self.delete_account_button().click()
                break
            except:
                pass
        self.delete_account_confirm_button().click()

    def account_details_boxes(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".borderBox").text

    def check_user_is_connected(self, name):
        return name in self.account_details_boxes()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Each page in the website gets a class - called page object


class MyAccountPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def delete_account_button(self):
        return self.driver.find_element(By.CLASS_NAME, "deleteMainBtnContainer")

    def delete_account_confirm_button(self):
        return self.driver.find_element(By.CLASS_NAME, "deleteRed")

    def delete_account_button_click(self):
        self.delete_account_button().click()
        self.wait.until(EC.visibility_of(self.delete_account_confirm_button()))
        self.delete_account_confirm_button().click()
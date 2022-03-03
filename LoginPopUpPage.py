from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Each page in the website gets a class - called page object


class LoginPopUpPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self):
        return self.driver.find_element(By.NAME, "username")

    def password_field(self):
        return self.driver.find_element(By.NAME, "password")

    def remember_me_box(self):
        return self.driver.find_element(By.NAME, "remember_me")

    def sign_in_button(self):
        return self.driver.find_element(By.ID, "sign_in_btnundefined")

    def create_new_account_link(self):
        return self.driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT")

    def login_x_button(self):
        self.wait.until(EC.visibility_of(self.driver.find_element(By.CLASS_NAME, "loginPopUpCloseBtn")))
        return self.driver.find_element(By.CLASS_NAME, "loginPopUpCloseBtn")

    def send_username(self, username):
        self.username_field().send_keys(username)

    def send_password(self, password):
        self.password_field().send_keys(password)

    def check_remember_me_box(self):
        self.remember_me_box().click()

    def sign_in_button_click(self):
        self.sign_in_button().click()

    def create_new_account_link_click(self):
        self.create_new_account_link().click()

    def login_x_button_click(self):
        self.login_x_button().click()

    def sign_in(self, username, password, remember_me="no"):
        """
        E2E Login process
        """
        self.send_username(username)
        self.send_password(password)
        if remember_me == "yes":
            self.remember_me_box().click()
        self.sign_in_button_click()
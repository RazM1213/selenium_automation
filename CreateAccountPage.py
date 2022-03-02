from selenium import webdriver
from selenium.webdriver.common.by import By

# Each page in the website gets a class - called page object


class CreateAccountPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def username_field(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def email_field(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def password_field(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def confirm_password_field(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def agree_button(self):
        return self.driver.find_element(By.NAME, "i_agree")

    def register_button(self):
        return self.driver.find_element(By.ID, "register_btnundefined")

    def send_username(self, username):
        self.username_field().send_keys(username)

    def send_email(self, email):
        self.email_field().send_keys(email)

    def send_password(self, password):
        self.password_field().send_keys(password)

    def send_confirm_password(self, confirm_password):
        self.confirm_password_field().send_keys(confirm_password)

    def agree_button_click(self):
        self.agree_button().click()

    def register_button_click(self):
        self.register_button().click()
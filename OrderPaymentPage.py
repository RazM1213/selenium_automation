from selenium import webdriver
from selenium.webdriver.common.by import By


class OrderPaymentPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def user_name_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='usernameInOrderPayment']")

    def send_user_to_user_name_field_(self, username):
        self.user_name_field().send_keys(username)

    def password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='passwordInOrderPayment']")

    def send_password_to_password_field_(self, password):
        self.password_field().send_keys(password)

    def login_button(self):
        return self.driver.find_element(By.ID, "login_btnundefined")

    def login_button_click(self):
        self.login_button().click()

    def registration_button(self):
        return self.driver.find_element(By.ID, "registration_btnundefined")

    def registration_button_click(self):
        self.registration_button().click()
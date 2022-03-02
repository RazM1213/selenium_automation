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

    def next_button(self):
        return self.driver.find_element(By.ID, "next_btn")

    def safepay_username_field(self):
        return self.driver.find_element(By.NAME, "safepay_username")

    def safepay_password_field(self):
        return self.driver.find_element(By.NAME, "safepay_password")

    def pay_now_button(self):
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def send_safepay_username_field(self, safepay_username):
        self.safepay_username_field().send_keys(safepay_username)

    def send_safepay_password_field(self, safepay_password):
        self.safepay_password_field().send_keys(safepay_password)

    def pay_now_button_click(self):
        self.pay_now_button().click()

    def safepay_payment(self, username, password):
        self.send_safepay_username_field(username)
        self.send_safepay_password_field(password)
        self.pay_now_button_click()

    def is_it_thank_you_page(self):
        return len(self.driver.find_elements(By.ID, "orderPaymentSuccess")) > 0

    def next_button_click(self):
        self.next_button().click()

    def login_button_click(self):
        self.login_button().click()

    def registration_button(self):
        return self.driver.find_element(By.ID, "registration_btnundefined")

    def registration_button_click(self):
        self.registration_button().click()
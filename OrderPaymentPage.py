from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


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

    def master_card_button(self):
        return self.driver.find_elements(By.NAME, "masterCredit")[0]

    def card_number_field(self):
        return self.driver.find_element(By.ID, "creditCard")

    def CVV_number_field(self):
        return self.driver.find_element(By.NAME, "cvv_number")

    def cardholder_name_field(self):
        return self.driver.find_element(By.NAME, "cardholder_name")

    def pay_now_credit_card_button(self):
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    def edit_card_button(self):
        return self.driver.find_element(By.CLASS_NAME, "edit")

    def edit_card_button_click(self):
        self.edit_card_button().click()

    def send_card_number_field(self, card_number):
        self.card_number_field().clear()
        self.card_number_field().send_keys(card_number)

    def send_CVV_number_field(self, cvv_number):
        self.card_number_field().send_keys(cvv_number)

    def send_cardholder_name_field(self, cardholder_name):
        self.card_number_field().send_keys(cardholder_name)

    def pay_now_credit_card_button_click(self):
        self.pay_now_credit_card_button().click()

    def master_card_button_click(self):
        self.master_card_button().click()

    def manual_payment(self, card_number, cvv_number, cardholder_name):
        """
        E2E Process of payment with MasterCredit card
        """
        self.master_card_button_click()
        self.edit_card_button_click()
        self.send_card_number_field(card_number)
        self.send_CVV_number_field(cvv_number)
        self.send_cardholder_name_field(cardholder_name)
        self.pay_now_credit_card_button_click()
        sleep(3)

    def login_existing_user(self, username, password):
        self.send_user_to_user_name_field_(username)
        self.send_password_to_password_field_(password)
        self.login_button_click()

    def send_safepay_username_field(self, safepay_username):
        self.safepay_username_field().send_keys(safepay_username)

    def send_safepay_password_field(self, safepay_password):
        self.safepay_password_field().send_keys(safepay_password)

    def pay_now_button_click(self):
        self.pay_now_button().click()

    def safepay_payment(self, username, password):
        """
        E2E Process of payment by SafePay
        """
        self.send_safepay_username_field(username)
        self.send_safepay_password_field(password)
        self.pay_now_button_click()
        sleep(3)

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
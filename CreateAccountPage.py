from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Each page in the website gets a class - called page object


class CreateAccountPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def email_field(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def password_field(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def confirm_password_field(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def agree_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']")

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
        self.wait.until(EC.element_to_be_clickable(self.agree_button()))
        self.agree_button().click()

    def register_button_click(self):
        self.wait.until(EC.element_to_be_clickable(self.register_button()))
        self.register_button().click()

    def create_account(self, username, email, password):
        """
        E2E Process of user registration
        """
        self.send_username(username)
        self.send_email(email)
        self.send_password(password)
        self.send_confirm_password(password)
        self.agree_button_click()
        self.register_button_click()
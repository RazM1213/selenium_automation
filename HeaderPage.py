from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Each page in the website gets a class - called page object


class HeaderPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def nav_bar(self):
        return self.driver.find_element(By.CLASS_NAME, ".desktop-handler")

    def logo(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".logo>a")

    def user_menu_button(self):
        return self.driver.find_element(By.ID, "menuUserLink")

    def shopping_cart_button(self):
        return self.driver.find_element(By.ID, "shoppingCartLink")

    def shopping_cart_number(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "span.cart.ng-binding")[1].text

    def help_button(self):
        return self.driver.find_element(By.ID, "helpLink")

    def open_search_bar_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#search>a")

    def search_field(self):
        return self.driver.find_element(By.ID, "autoComplete")

    def submit_search_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a>#menuSearch")

    def connected_user_name(self):
        self.wait.until(EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, "#menuUserLink>.hi-user")))
        return self.driver.find_element(By.CSS_SELECTOR, "#menuUserLink>.hi-user").text

    def cart_hover_table(self):
        return self.driver.find_element(By.TAG_NAME, "table")

    def cart_hover_table_first_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")[0]

    def cart_hover_table_second_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")[1]

    def cart_hover_table_third_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")[2]

    def cart_hover_table_product_details(self, product_elem):
        name = product_elem.find_elements(By.CSS_SELECTOR, "td>a>h3")[0].text
        qty = product_elem.find_elements(By.CSS_SELECTOR, "td>a>label")[0].text[5:]
        color = product_elem.find_elements(By.CSS_SELECTOR, "td>a>label")[1].text[7:]

        return {"name": name, "qty": qty, "color": color}

    def logo_click(self):
        self.logo().click()

    def user_menu_button_click(self):
        self.wait.until(EC.element_to_be_clickable(self.user_menu_button()))
        self.user_menu_button().click()

    def shopping_cart_button_click(self):
        self.shopping_cart_button().click()

    def help_button_click(self):
        self.help_button().click()

    def open_search_bar_button_click(self):
        self.open_search_bar_button().click()

    def send_search_bar_field(self, key):
        self.search_field().send_keys(key)

    def submit_search_bar_button_click(self):
        self.submit_search_button().click()

    def shopping_cart_button_hover(self):
        self.wait.until(EC.element_to_be_clickable(self.shopping_cart_button()))
        hover = ActionChains(self.driver).move_to_element(self.shopping_cart_button())
        hover.perform()

    def search(self, key):
        self.open_search_bar_button_click()
        self.send_search_bar_field(key)
        self.submit_search_bar_button_click()

    def remove_product_button(self, product_num):
        return self.driver.find_elements(By.CSS_SELECTOR, ".removeProduct")[product_num]

    def remove_product_button_click(self, product_num):
        self.remove_product_button(product_num).click()

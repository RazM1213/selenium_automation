from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HeaderPage import HeaderPage
from LoginPopUpPage import LoginPopUpPage
from ProductPage import ProductPage
from CategoryPage import CategoryPage
from MainPage import MainPage
from CartPage import CartPage

# Set Up:
service = Service(r"C:\Users\razm1\selenium_drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://advantageonlineshopping.com/#/")
driver.maximize_window()

# Page Objects Instantiation:
header_page = HeaderPage(driver)
login_pop_up_page = LoginPopUpPage(driver)
product_page = ProductPage(driver)
category_page = CategoryPage(driver)
main_page = MainPage(driver)
cart_page = CartPage(driver)

# # Login test:
# header_page.user_menu_button_click()
# login_pop_up_page.sign_in("RazSelenium", "Neverhood1")
# if header_page.connected_user_name() == "RazSelenium":
#     print("PASS")
# else:
#     print("FAIL")

# # Test 1:
# main_page.click_category("speakersImg")
# category_page.product_click(0)
# product_page.increase_quantity(1)
# product_page.add_to_cart_button_click()
# product_page.return_to_category_button_click()
# category_page.product_click(1)
# product_page.increase_quantity(2)
# product_page.add_to_cart_button_click()
# if int(header_page.shopping_cart_number()) == 5:
#     print("PASS")
# else:
#     print("FAIL")


# Test 2:
main_page.click_category("laptopsImg")
category_page.product_click(0)
product_page.increase_quantity(1)
product_page.add_to_cart_button_click()
product1 = {"name": product_page.product_title(), "qty": "2", "color": product_page.product_color().get_attribute("title")}
product_page.return_to_category_button_click()
category_page.product_click(1)
product_page.increase_quantity(2)
product_page.add_to_cart_button_click()
product2 = {"name": product_page.product_title().text, "qty": "3", "color": product_page.product_color().get_attribute("title")}
product_page.return_to_category_button_click()
category_page.product_click(2)
product_page.increase_quantity(3)
product_page.add_to_cart_button_click()
product3 = {"name": product_page.product_title().text, "qty": "4", "color": product_page.product_color().get_attribute("title")}

header_page.shopping_cart_button_hover()

list_tr = header_page.cart_hover_table().find_elements(By.TAG_NAME, "tr")
print(header_page.cart_hover_table_product_details(header_page.cart_hover_table_first_product()))

print(product3)

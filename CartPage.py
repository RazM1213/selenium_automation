from selenium import webdriver
from selenium.webdriver.common.by import By


# Each page in the website gets a class - called page object


class CartPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def shopping_Cart_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, "section>article>h3")

    def shopping_Cart_table(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[id='shoppingCart']>table")

    def shopping_Cart_trs(self):
        return self.shopping_Cart_table().find_elements(By.TAG_NAME, "tr")

    def shopping_Cart_tr_from_specific_tr(self, trnum):
        return self.shopping_Cart_trs()[trnum]

    def shopping_Cart_checkoutBt(self):
        return self.driver.find_element(By.ID, "checkOutButton")

    """return list of all the prices"""

    def shopping_Cart_all_prices_list(self):
        list_prices = self.driver.find_elements(By.CSS_SELECTOR, "td>p")
        rlist = []
        for i in range(len(list_prices)):
            if list_prices[i].text != '':
                rlist.append(float(list_prices[i].text[1:].replace(',', '')))
        return rlist

    def the_specific_product_name_and_price(self, trnum):
        """this method returns a dictionary of the name, quantity, and price """
        list_tr = []
        for item in self.shopping_Cart_tr_from_specific_tr(trnum).find_elements(By.TAG_NAME, 'td'):
            list_tr.append(item.text)
        name = list_tr[1]
        amount = list_tr[4]
        price = self.shopping_Cart_all_prices_list()[trnum]
        rdict = {"name": name, "amount": amount, "price": price}
        return rdict

    def click_checkout(self):
        self.shopping_Cart_checkoutBt().click()

    def total_order_amount_summedUp(self):
        return sum(self.shopping_Cart_all_prices_list())

    def the_total_amount_in_the_checkout_button(self):
        total = self.driver.find_element(By.CSS_SELECTOR, "#checkOutButton").text
        index = total.find('$')
        total = total[index + 1:-1]
        return float(total)

    def check_if_cart_is_empty(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#shoppingCart>.bigEmptyCart ").is_displayed()

    def check_if_the_page_is_cart(self):
        return self.shopping_Cart_header().is_displayed()

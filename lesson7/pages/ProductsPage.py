from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 11)
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.add_to_cart_buttons = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (
                By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }

    def add_product_to_cart(self, product_name):
        button_locator = self.add_to_cart_buttons.get(product_name)
        if button_locator:
            element = self.wait.until(
                EC.element_to_be_clickable(button_locator))
            element.click()
        return self

    def go_to_cart(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.cart_icon))
        element.click()
        return self

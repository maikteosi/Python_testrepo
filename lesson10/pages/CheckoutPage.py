from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name):
        element = self.wait.until(
            EC.presence_of_element_located(self.first_name_input))
        element.clear()
        element.send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        element = self.wait.until(
            EC.presence_of_element_located(self.last_name_input))
        element.clear()
        element.send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        element = self.wait.until(
            EC.presence_of_element_located(self.postal_code_input))
        element.clear()
        element.send_keys(postal_code)
        return self

    def click_continue(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.continue_button))
        element.click()
        return self

    def get_total_amount(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.total_amount))
        return element.text

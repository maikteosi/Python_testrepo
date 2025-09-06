from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            '0': (By.XPATH, "//span[text()='0']"),
            '1': (By.XPATH, "//span[text()='1']"),
            '2': (By.XPATH, "//span[text()='2']"),
            '3': (By.XPATH, "//span[text()='3']"),
            '4': (By.XPATH, "//span[text()='4']"),
            '5': (By.XPATH, "//span[text()='5']"),
            '6': (By.XPATH, "//span[text()='6']"),
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '9': (By.XPATH, "//span[text()='9']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '=': (By.XPATH, "//span[text()='=']")
        }

    def open(self):
        self.driver.get("https://bonigarcia."
                        "dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, delay_seconds):
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.delay_input))
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
        return self

    def click_button_7(self):
        button = self.wait.until(EC.element_to_be_clickable(self.buttons['7']))
        button.click()
        return self

    def click_button_plus(self):
        button = self.wait.until(EC.element_to_be_clickable(self.buttons['+']))
        button.click()
        return self

    def click_button_8(self):
        button = self.wait.until(EC.element_to_be_clickable(self.buttons['8']))
        button.click()
        return self

    def click_button_equals(self):
        button = self.wait.until(EC.element_to_be_clickable(self.buttons['=']))
        button.click()
        return self

    def get_result_text(self):
        result_element = self.wait.until(
            EC.presence_of_element_located(self.result_display))
        return result_element.text

    def wait_for_result(self, timeout=46):
        try:
            custom_wait = WebDriverWait(self.driver, timeout)
            custom_wait.until(
                lambda driver:
                self.get_result_text() != "" and self.get_result_text() != " "
            )
            return True
        except TimeoutException:
            return False

    def wait_for_specific_result(self, expected_result, timeout=60):
        try:
            custom_wait = WebDriverWait(self.driver, timeout)
            custom_wait.until(
                lambda driver: self.get_result_text() == expected_result
            )
            return True
        except TimeoutException:
            return False

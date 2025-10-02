from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CalculatorPage:
    """Page Object для страницы калькулятора с задержкой"""
    def __init__(self, driver):
        """ Инициализация CalculatorPage
        Args: driver: WebDriver instance """
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
        """ Открывает страницу калькулятора
        Returns: CalculatorPage: текущий экземпляр CalculatorPage """
        self.driver.get("https://bonigarcia."
                        "dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, delay_seconds):
        """ Устанавливает задержку вычислений
        Args: delay_seconds (int): задержка в секундах
        Returns: CalculatorPage: текущий экземпляр CalculatorPage """
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.delay_input))
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
        return self

    def click_button_7(self):
        """ Нажимает указанную кнопку калькулятора
        Args: button (str): символ кнопки
        Returns: CalculatorPage: текущий экземпляр CalculatorPage """
        button = self.wait.until(EC.element_to_be_clickable(self.buttons['7']))
        button.click()
        return self

    def click_button_plus(self):
        """ Нажимает указанную кнопку калькулятора
        Args: button (str): символ кнопки
        Returns: CalculatorPage: текущий экземпляр CalculatorPage """
        button = self.wait.until(EC.element_to_be_clickable(self.buttons['+']))
        button.click()
        return self

    def click_button_8(self):
        """ Нажимает указанную кнопку калькулятора
        Args: button (str): символ кнопки
        Returns: CalculatorPage: текущий экземпляр CalculatorPage """
        button = self.wait.until(EC.element_to_be_clickable(self.buttons['8']))
        button.click()
        return self

    def click_button_equals(self):
        """ Нажимает указанную кнопку калькулятора
        Args: button (str): символ кнопки
        Returns: CalculatorPage: текущий экземпляр CalculatorPage """
        button = self.wait.until(EC.element_to_be_clickable(self.buttons['=']))
        button.click()
        return self

    def get_result_text(self):
        """ Получает текст с результатом вычислений
        Returns: str: текст результата """
        result_element = self.wait.until(
            EC.presence_of_element_located(self.result_display))
        return result_element.text

    def wait_for_result(self, timeout=46):
        """ Ожидает появления результата вычислений
        Args: timeout (int): время ожидания в секундах
        Returns: bool: True если результат появился, False при таймауте """
        try:
            custom_wait = WebDriverWait(self.driver, timeout)
            custom_wait.until(
                lambda driver:
                self.get_result_text() != "" and self.get_result_text() != " "
            )
            return True
        except TimeoutException:
            return False

    def wait_for_specific_result(self, expected_result: str,
                                 timeout: int = 60) -> bool:
        """ Ожидает конкретного результата вычислений
        Args:
            expected_result (str): ожидаемый результат
            timeout (int): время ожидания в секундах
        Returns: bool: True если получен ожидаемый результат,
        False при таймауте """
        try:
            custom_wait = WebDriverWait(self.driver, timeout)
            custom_wait.until(
                lambda driver: self.get_result_text() == expected_result
            )
            return True
        except TimeoutException:
            return False

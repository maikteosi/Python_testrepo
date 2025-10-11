from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """Page Object для страницы формы ввода данных"""

    def __init__(self, driver):
        """ Инициализация FormPage
        Args:  driver: WebDriver instance """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """ Открывает страницу с формой
        Returns: FormPage: текущий экземпляр FormPage """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        return self

    def fill_first_name(self, value: str):
        """ Заполняет поле First Name
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "first-name"))).send_keys(value)
        return self

    def fill_last_name(self, value: str):
        """ Заполняет поле Last Name
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "last-name"))).send_keys(value)
        return self

    def fill_address(self, value: str):
        """ Заполняет поле Address
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "address"))).send_keys(value)
        return self

    def fill_email(self, value: str):
        """ Заполняет поле Email
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "e-mail"))).send_keys(value)
        return self

    def fill_phone(self, value: str):
        """ Заполняет поле Phone
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "phone"))).send_keys(value)
        return self

    def fill_zip_code(self, value: str):
        """ Заполняет поле Zip Code
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "zip-code"))).send_keys(value)
        return self

    def fill_city(self, value: str):
        """ Заполняет поле City
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "city"))).send_keys(value)
        return self

    def fill_country(self, value: str):
        """ Заполняет поле Country
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "country"))).send_keys(value)
        return self

    def fill_job_position(self, value: str):
        """ Заполняет поле Job Position
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "job-position"))).send_keys(value)
        return self

    def fill_company(self, value: str):
        """ Заполняет поле Company
        Args: value (str): значение для поля
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "company"))).send_keys(value)
        return self

    def submit_form(self):
        """ Отправляет форму
        Returns: FormPage: текущий экземпляр FormPage """
        self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[type="submit"]'))).click()
        return self

    def is_zip_code_invalid(self) -> bool:
        """ Проверяет, что поле Zip code подсвечено красным
        Returns: bool: True если поле невалидно (подсвечено красным) """
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, "zip-code")))
        return "alert-danger" in element.get_attribute("class")

    def is_field_valid(self, field_id: str) -> bool:
        """ Проверяет, что поле подсвечено зеленым
        Args: field_id (str): ID поля для проверки
        Returns: bool: True если поле валидно (подсвечено зеленым) """
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id)))
        return "alert-success" in element.get_attribute("class")

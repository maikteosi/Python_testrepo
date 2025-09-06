from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        return self

    def fill_first_name(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "first-name"))).send_keys(value)
        return self

    def fill_last_name(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "last-name"))).send_keys(value)
        return self

    def fill_address(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "address"))).send_keys(value)
        return self

    def fill_email(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "e-mail"))).send_keys(value)
        return self

    def fill_phone(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "phone"))).send_keys(value)
        return self

    def fill_zip_code(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "zip-code"))).send_keys(value)
        return self

    def fill_city(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "city"))).send_keys(value)
        return self

    def fill_country(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "country"))).send_keys(value)
        return self

    def fill_job_position(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "job-position"))).send_keys(value)
        return self

    def fill_company(self, value):
        self.wait.until(EC.presence_of_element_located((
            By.NAME, "company"))).send_keys(value)
        return self

    def submit_form(self):
        self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '[type="submit"]'))).click()
        return self

    def is_zip_code_invalid(self):
        """Проверяет, что поле Zip code подсвечено красным"""
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, "zip-code")))
        return "alert-danger" in element.get_attribute("class")

    def is_field_valid(self, field_id):
        """Проверяет, что поле подсвечено зеленым"""
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id)))
        return "alert-success" in element.get_attribute("class")

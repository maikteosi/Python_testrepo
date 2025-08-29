from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    edge_driver_path = r"C:\Users\Михаил\Desktop\PyCharm\msedgedriver.exe"
    driver = webdriver.Edge(service=Service(edge_driver_path))

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        driver.find_element(
            By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        driver.find_element(
            By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        driver.find_element(
            By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        driver.find_element(
            By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(
            "test@skypro.com")
        driver.find_element(
            By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        driver.find_element(
            By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
        driver.find_element(
            By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
        driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        driver.find_element(
            By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

        submit_button = driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )

        zip_code_field = driver.find_element(By.CSS_SELECTOR, '#zip-code')
        assert "alert-danger" in zip_code_field.get_attribute("class")

        fields_to_check = [
            'first-name', 'last-name', 'address', 'e-mail',
            'phone', 'city', 'country', 'job-position', 'company'
        ]

        for field in fields_to_check:
            field_element = driver.find_element(By.CSS_SELECTOR, f'#{field}')
            assert "alert-success" in field_element.get_attribute("class")

    finally:
        driver.quit()

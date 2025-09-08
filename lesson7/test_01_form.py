import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from pages.FormPage import FormPage


@pytest.fixture()
def driver():
    edge_driver_path = r"C:\Users\Михаил\Desktop\PyCharm\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    page = FormPage(driver)

    (page.open()
     .fill_first_name("Иван")
     .fill_last_name("Петров")
     .fill_address("Ленина, 55-3")
     .fill_email("test@skypro.com")
     .fill_phone("+7985899998787")
     .fill_zip_code("")
     .fill_city("Москва")
     .fill_country("Россия")
     .fill_job_position("QA")
     .fill_company("SkyPro")
     .submit_form())

    assert page.is_zip_code_invalid(), \
        "Поле Zip code должно быть подсвечено красным"

    valid_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field in valid_fields:
        assert page.is_field_valid(
            field), (f"Поле {field} должно быть подсвечено зеленым")

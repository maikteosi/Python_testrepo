import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from pages.FormPage import FormPage


@pytest.fixture()
def driver():
    """Фикстура для инициализации WebDriver"""
    edge_driver_path = r"C:\Users\Михаил\Desktop\PyCharm\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Проверка формы")
@allure.severity(allure.severity_level.CRITICAL)
# устанавливает критичность теста как CRITICAL
@allure.title("Проверка формы zip code")
@allure.description("Тест подтверждает, что проверка формы"
                    " работает корректно, когда поле с zip code пустое")
def test_form_validation(driver):
    form_page = FormPage(driver)

    with allure.step("Открыть страницу формы"):
        form_page.open()

    with allure.step("Заполнить формы достоверными данными, кроме zip code"):
        (
            form_page.fill_first_name("Иван")
            .fill_last_name("Петров")
            .fill_address("Ленина, 55-3")
            .fill_email("test@skypro.com")
            .fill_phone("+7985899998787")
            .fill_zip_code("")
            .fill_city("Москва")
            .fill_country("Россия")
            .fill_job_position("QA")
            .fill_company("SkyPro")
            .submit_form()
        )

    with allure.step("Убедиться, что поле с zip code выделено красным"):
        assert (
            form_page.is_zip_code_invalid()
        ), "Поле Zip code должно быть подсвечено красным"
        allure.dynamic.description(
            "Zip code должно быть выделено красным"
        )

    with allure.step("Убедиться, что все остальные поля выделены зелёным"):
        valid_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]

        for field in valid_fields:
            assert form_page.is_field_valid(
                field
            ), f"Поле {field} должно быть подсвечено зеленым"
            allure.dynamic.description(
                f"Поле {field} должно быть выделено зелёным цветом,"
                f" если оно заполнено"
            )

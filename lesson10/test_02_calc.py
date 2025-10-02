import pytest
import allure
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture()
def driver():
    """ Фикстура для инициализации WebDriver """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Операции с калькулятором")
@allure.severity(allure.severity_level.NORMAL)
# устанавливает критичность теста как NORMAL
@allure.title("Добавление тестового калькулятора с задержкой")
@allure.description("Тест подтверждает, что калькулятор "
                    "правильно выполняет сложение с указанной задержкой")
def test_calculator_addition_delay(driver):
    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()

    with allure.step("Установить задержку расчёта на 45 секунд"):
        calculator_page.set_delay(45)

    with allure.step("Выполнить сложение: 7 + 8"):
        (calculator_page.click_button_7()
         .click_button_plus()
         .click_button_8()
         .click_button_equals())

    with (allure.step("Подождать результата вычислений и "
                      "подтвердить, что он равен 15")):
        calculation_completed = calculator_page.wait_for_specific_result("15")
        assert calculation_completed, ("Результат сложения"
                                       " 7 + 8 должен быть равен 15")
        allure.dynamic.description(
            "Addition operation 7 + 8 should result in 15")

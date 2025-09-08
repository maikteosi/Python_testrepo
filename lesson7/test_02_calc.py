import pytest
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_slojenue_delay(driver):
    calculator_page = CalculatorPage(driver)
    (calculator_page.open()
     .set_delay(45)
     .click_button_7()
     .click_button_plus()
     .click_button_8()
     .click_button_equals())

    calculation_completed = calculator_page.wait_for_specific_result("15")
    assert calculation_completed, "Сложение"

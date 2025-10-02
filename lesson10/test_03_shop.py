import pytest
import allure
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture()
def driver():
    """ Фикстура для инициализации WebDriver Firefox """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature('группирует тест в категорию "E-commerce Shopping Flow"')
@allure.severity(allure.severity_level.CRITICAL)
# устанавливает критичность теста как CRITICAL
@allure.title("Полный тест процесса совершения покупок"
              " — добавление товаров в корзину и оформление заказа")
@allure.description("""
Этот тест проверяет весь процесс совершения покупки:
1. Вход пользователя в систему с использованием действительных учётных данных
2. Добавление нескольких товаров в корзину
3. Переход к корзине и оформление заказа
4.Заполнение данных для оформления заказа
5. Проверка правильности общей суммы
""")
def test_03_shop(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Откройте страницу входа и авторизуйтесь,"
                     " используя действительные учётные данные"):
        (login_page.open()
         .enter_username("standard_user")
         .enter_password("secret_sauce")
         .click_login())

    with allure.step("Добавление товаров в корзину"):
        (products_page.add_product_to_cart("Sauce Labs Backpack")
         .add_product_to_cart("Sauce Labs Bolt T-Shirt")
         .add_product_to_cart("Sauce Labs Onesie")
         .go_to_cart())

    with allure.step("Переход на страницу оформления заказа"):
        cart_page.click_checkout()

    with allure.step("Заполнение формы заказа, указав данные пользователя"):
        (checkout_page.enter_first_name("Иван")
         .enter_last_name("Петров")
         .enter_postal_code("123456")
         .click_continue())

    with allure.step("Проверка общей суммы"):
        total_text = checkout_page.get_total_amount()
        allure.dynamic.description(f"Итоговая сумма 58.29, "
                                   f"actual: {total_text}")

        assert "58.29" in total_text, (f"Итоговая сумма должна быть 58.29, "
                                       f"но получено: {total_text}")

        with allure.step(f"Log final amount: {total_text}"):
            print(f"\nИтоговая сумма: {total_text}")
            allure.attach(f"Total amount: {total_text}",
                          name="Checkout Total",
                          attachment_type=allure.attachment_type.TEXT)

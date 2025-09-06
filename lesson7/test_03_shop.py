import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_03_shop(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    (login_page.open()
     .enter_username("standard_user")
     .enter_password("secret_sauce")
     .click_login())

    (products_page.add_product_to_cart("Sauce Labs Backpack")
     .add_product_to_cart("Sauce Labs Bolt T-Shirt")
     .add_product_to_cart("Sauce Labs Onesie")
     .go_to_cart())

    cart_page.click_checkout()

    (checkout_page.enter_first_name("Иван")
     .enter_last_name("Петров")
     .enter_postal_code("123456")
     .click_continue())

    total_text = checkout_page.get_total_amount()
    assert "58.29" in total_text, f"Итоговая сумма {total_text}"
    print(f"\nИтоговая сумма: {total_text}")

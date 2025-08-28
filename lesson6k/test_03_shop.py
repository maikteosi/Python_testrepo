from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sauce_demo_checkout():
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        assert "Swag Labs" in driver.title

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory.html")
        )

        products_to_add = [
            "add-to-cart-sauce-labs-backpack",  # Sauce Labs Backpack
            "add-to-cart-sauce-labs-bolt-t-shirt",  # Sauce Labs Bolt T-Shirt
            "add-to-cart-sauce-labs-onesie"  # Sauce Labs Onesie
        ]

        for product_id in products_to_add:
            driver.find_element(By.ID, product_id).click()

        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "3"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "title"), "Your Cart"
            )
        )

        driver.find_element(By.ID, "checkout").click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "title"), "Checkout: Your Information"
            )
        )

        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "title"), "Checkout: Overview"
            )
        )

        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )

        total_text = total_element.text
        total_amount = total_text.split("$")[1]
        print(f" \nИтоговая стоимость: ${total_amount}")
        expected_amount = "58.29"
        assert total_amount == expected_amount, (
            f"ожидание ${expected_amount}, факт ${total_amount}"
        )

    finally:
        driver.quit()

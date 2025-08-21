from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


for i in range(3):
    print(f"нажатие синей кнопки #{i + 1}")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://uitestingplayground.com/classattr")
    sleep(2)

    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    sleep(2)

    driver.quit()
    sleep(2)

print("три клика завершены")

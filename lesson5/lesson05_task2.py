from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

for i in range(3):
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://uitestingplayground.com/dynamicid")
    sleep(2)

    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    print("Кликаем на синюю кнопку...")
    button.click()
    print("Клик выполнен успешно!")
    sleep(2)

    driver.quit()
    sleep(1)

print("три клика завершены")

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Открываем браузер и загружаем сайт")
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")
sleep(2)

for i in range(3):
    print(f"клик синей кнопки #{i + 1}")

    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    sleep(2)

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    print(" в всплывающем окне клик ОК")

    sleep(2)

print("три клика завершены")
sleep(2)
driver.quit()
print("Браузер закрыт")

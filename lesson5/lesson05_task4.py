from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

print("ввод username")
driver.find_element(By.ID, "username").send_keys("tomsmith")
print("ввод завершён")
sleep(2)
print("ввод password")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
print("ввод завершён")
sleep(2)
print('нажать кнопку login')
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print('кнопка нажата')
sleep(4)


flash_text = driver.find_element(By.ID, "flash").text
print("ввывод текста с зелёной плашки")
print("Текст плашки:", flash_text)
sleep(2)

driver.quit()
sleep(2)

print("авторизация завершина")

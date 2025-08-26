from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")
print("ввод Sky")
input_field.send_keys("Sky")
sleep(2)
print("очистка")
input_field.clear()
print("ввод Pro")
input_field.send_keys("Pro")
sleep(2)

driver.quit()
sleep(2)

print("ввод завершён")

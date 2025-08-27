from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "spinner"))
)

images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
third_image_src = images[2].get_attribute("src")

print(third_image_src)

driver.quit()

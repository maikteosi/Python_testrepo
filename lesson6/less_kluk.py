from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
blue_button.click()

green_banner = WebDriverWait(driver, 22).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

text = green_banner.text
print(text)

driver.quit()

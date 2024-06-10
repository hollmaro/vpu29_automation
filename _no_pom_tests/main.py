import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# ініціалізація драйвера браузера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")

#додати код для визначення текстового поля пошуку Google
gmail_link = driver.find_element(By.XPATH, "//a[text()='Gmail']")
gmail_link.click()

time.sleep(15)

driver.quit()



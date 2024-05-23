import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click_on_web_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()

    def open_page(self, base_url):
        self.driver.get(base_url)
        WebDriverWait(self.driver, 20).until(EC.url_to_be(base_url))

    def get_element_text(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator)).text

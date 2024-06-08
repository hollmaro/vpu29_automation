from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.test_exceptions_page import TestExceptionsPage
#f
class PracticePage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_page_link(self):
        self.driver.find_element(By.LINK_TEXT, "Test login page").click()
        return LoginPage(self.driver)

    def click_test_exceptions_link(self):
        self.driver.find_element(By.LINK_TEXT, "Test exceptions").click()
        return TestExceptionsPage(self.driver)

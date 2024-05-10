from selenium.webdriver.common.by import By

from pages.logged_in_successfully_page import LoggedInSuccessPage
from pages.base_page import BasePage


# Class LoginPage inherits from BasePage
# and contains locators and methods for the login page
# representation of https://practicetestautomation.com/practice-test-login/

class PracticePage(BasePage):
    def __init__(self, driver):
        # Викликаємо конструктор базового класу BasePage через super() і передаємо йому драйвер
        # (об'єкт WebDriver який потім буде використовуватися в методах класу)
        super().__init__(driver)

    # локатори елементів сторінки логіну
    title = (By.XPATH, "//h1")
    test_login_page_link = (By.XPATH, "//*[text()='Test Login Page']")
    practice_url = "https://practicetestautomation.com/practice/"

    def get_title_text(self):
        return self.get_element_text(self.title)

    def open_practice_page(self):
        self.open_page(self.practice_url)
        return self

    def is_test_login_link_present(self):
        return self.is_element_present(self.test_login_page_link)

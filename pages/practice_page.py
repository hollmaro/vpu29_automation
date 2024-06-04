from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage


# Class PracticePage inherits from BasePage
# and contains locators and methods for the practice page
# representation of https://practicetestautomation.com/practice/

class PracticePage(BasePage):
    def __init__(self, driver):
        # Викликаємо конструктор базового класу BasePage через super() і передаємо йому драйвер
        # (об'єкт WebDriver який потім буде використовуватися в методах класу)
        super().__init__(driver)

    # локатори елементів сторінки Practice
    login_page_link = (By.XPATH, "//*[text()='Test Login Page']")
    title_text = (By.XPATH, "//h1")
    practice_url = "https://practicetestautomation.com/practice/"

    def get_title_practice_text(self) -> str:
        return self.get_element_text(self.title_text)

    # Метод для переходу на сторінку логіну
    def click_on_login_page_link(self):
        self.click_on_web_element(self.login_page_link)
        return LoginPage(self.driver)

    #Написати Метод для отримання URL сторінки Practice
    #def get_practice_url(self):
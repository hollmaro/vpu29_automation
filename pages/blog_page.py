from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# Class BlogPage inherits from BasePage
# and contains locators and methods for the login page
# representation of https://practicetestautomation.com/practice-test-login/
class BlogPage(BasePage):
    def __init__(self, driver):
        # Викликаємо конструктор базового класу BasePage через super() і передаємо йому драйвер
        # (об'єкт WebDriver який потім буде використовуватися в методах класу)
        super().__init__(driver)

    # локатори елементів сторінки Blog
    title_text = (By.XPATH, "//h2")

    def get_title_blog_text(self) -> str:
        return self.get_element_text(self.title_text)

from selenium.webdriver.common.by import By

from pages.blog_page import BlogPage
from pages.logged_in_successfully_page import LoggedInSuccessPage
from pages.base_page import BasePage


# Class LoginPage inherits from BasePage
# and contains locators and methods for the login page
# representation of https://practicetestautomation.com/practice-test-login/

class LoginPage(BasePage):
    def __init__(self, driver):
        # Викликаємо конструктор базового класу BasePage через super() і передаємо йому драйвер
        # (об'єкт WebDriver який потім буде використовуватися в методах класу)
        super().__init__(driver)

    # локатори елементів сторінки логіну
    search_field = (By.XPATH, "//*[@id='search2']")
    blog_tab = (By.XPATH, "//*[text()='Blog']")
    user_name_field = (By.ID, "username")
    password_field = (By.ID, "password")
    submit_button = (By.ID, "submit")
    username_invalid_text = (By.ID, "error")
    title_text = (By.XPATH, "//h2")
    login_url = "https://practicetestautomation.com/practice-test-login/"

    def enterUserCred(self, username, password):
        self.enter_text(self.user_name_field, username)
        self.enter_text(self.password_field, password)
        return self

    def open_login_page(self):
        self.open_page(self.login_url)
        return self

    def clickOnSubmit(self):
        self.click_on_web_element(self.submit_button)
        return LoggedInSuccessPage(self.driver)

    def get_username_invalid_text(self):
        return self.get_element_text(self.username_invalid_text)

    def get_title_login_text(self) -> str:
        return self.get_element_text(self.title_text)

    def click_on_blog_tab(self):
        self.click_on_web_element(self.blog_tab)
        return BlogPage(self.driver)
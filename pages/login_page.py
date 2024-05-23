from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.logged_in_successfully_page import LoggedInSuccessPage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # локатори елементів сторінки логіну
    search_field = (By.XPATH, "//*[@id='search2']")
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

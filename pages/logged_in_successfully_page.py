from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoggedInSuccessPage(BasePage):
    search_field = (By.XPATH, "//*[@id='search2']")
    title_text = (By.XPATH, "//h1")
    logout_button = (By.XPATH, "//a[text()='Log out']")
    success_url = "https://practicetestautomation.com/logged-in-successfully/"

    def __init__(self, driver):
        super().__init__(driver)

    def get_title_text(self):
        return self.get_element_text(self.title_text)

    def open_logged_in_success_page(self):
        self.open_page(self.success_url)
        return self

    def click_on_logout_button(self):
        self.click_on_web_element(self.logout_button)

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.blog_page import BlogPage


#from pages.login_page import LoginPage


# Class LoggedInSuccessPage inherits from BasePage
# and contains locators and methods for the login page
# representation of https://practicetestautomation.com/logged-in-successfully/

class LoggedInSuccessPage(BasePage):
    search_field = (By.XPATH, "//*[@id='search2']")
    title_text = (By.XPATH, "//h1")
    logout_button = (By.XPATH, "//a[text()='Log out']")
    blog_tab = (By.XPATH, "//a[contains(text(),'Blog')]")
    login_url = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver):
        # Initialize the LoginPage instance with a WebDriver object and locators.
        super().__init__(driver)

    def get_title_text(self):
        return self.get_element_text(self.title_text)

    def open_logged_in_success_page(self):
        self.open_page(self.login_url)
        return self

    def click_on_logout_button(self):
        self.click_on_web_element(self.logout_button)

    def click_on_blog_tab(self):
        self.click_on_web_element(self.blog_tab)
        return BlogPage(self.driver)

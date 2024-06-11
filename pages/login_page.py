from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'submit')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()


class PracticePage:
    HOME_LINK = (By.LINK_TEXT, 'Home')
    TEST_LOGIN_PAGE_LINK = (By.LINK_TEXT, 'Test Login Page')
    TEST_EXCEPTIONS_LINK = (By.LINK_TEXT, 'Test Exceptions')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_home_link_displayed(self) -> bool:
        return self.driver.find_element(*self.HOME_LINK).is_displayed()

    def are_links_displayed(self) -> bool:
        return self.driver.find_element(*self.TEST_LOGIN_PAGE_LINK).is_displayed() and \
               self.driver.find_element(*self.TEST_EXCEPTIONS_LINK).is_displayed()

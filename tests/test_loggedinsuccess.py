import pytest
from pages.login_page import LoginPage
from pages.practice_page import PracticePage


@pytest.mark.usefixtures("driver_init")
class TestLoggedInSuccess:

    def test_login_and_navigate_to_login_page(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

        login_page = LoginPage(self.driver)
        login_page.enter_username("student")
        login_page.enter_password("Password123")
        login_page.click_submit()

        practice_page = PracticePage(self.driver)
        login_page = practice_page.click_login_page_link()

        assert "Test Login Page" in self.driver.title

    def test_login_and_navigate_to_exceptions_page(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

        login_page = LoginPage(self.driver)
        login_page.enter_username("student")
        login_page.enter_password("Password123")
        login_page.click_submit()

        practice_page = PracticePage(self.driver)
        test_exceptions_page = practice_page.click_test_exceptions_link()

        assert test_exceptions_page.is_displayed()

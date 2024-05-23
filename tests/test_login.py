import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from tests.base_test import BaseTest

@pytest.mark.usefixtures("driver_init")
class TestLogin(BaseTest):

    def test_login_positive(self, driver_init):
        login_p = LoginPage(driver_init)
        title = (login_p
                 .open_login_page()
                 .enterUserCred('student', 'Password123')
                 .clickOnSubmit()
                 .get_title_text())
        assert "Logged In Successfully" in title

    def test_logout_positive(self, driver_init):
        login_p = LoginPage(driver_init)
        (login_p
         .open_login_page()
         .enterUserCred('student', 'Password123')  \
         .clickOnSubmit()
         .click_on_logout_button())
        text = login_p.get_title_login_text()
        assert "Test login" in text

    def test_login_scenario(self, driver_init):
        # Open login page
        login_page = LoginPage(driver_init)
        login_page.open_login_page()

        # Enter username and password
        login_page.enterUserCred('student', 'Password123')

        # Submit the form
        logged_in_page = login_page.clickOnSubmit()

        # Verify successful login message
        success_message = logged_in_page.get_title_text()
        assert "Logged In Successfully" in success_message  # виправлено очікуване значення

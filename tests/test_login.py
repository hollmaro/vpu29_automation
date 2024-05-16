import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.logged_in_successfully_page import LoggedInSuccessPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("driver_init")
# TestLogin клас, який успадковує BaseTest клас для виведення назви тесту перед його виконанням
# Тестовий клас має починатися зі слова Test для того, щоб pytest визначив його як тест
class TestLogin(BaseTest):
    # Позитивний тест на вхід в систему
    # Тестовий метод має починається зі слова test_ для того, щоб pytest визначив його як тест
    def test_login_positive(self, driver_init):
        login_p = LoginPage(driver_init)
        title = (login_p
                 .open_login_page()
                 .enterUserCred('student', 'Password123')
                 .clickOnSubmit()
                 .get_title_text())
        time.sleep(2)  # для цілей демонстрації
        assert "Logged In Successfully" in title

    # def test_login_negative_username(self, driver_init):
    #     login_p = LoginPage(driver_init)
    #     (login_p
    #      .open_login_page()
    #      .enterUserCred('student123', 'Password123')
    #      .clickOnSubmit())
    #     error_message = login_p.get_username_invalid_text()
    #     time.sleep(2)  # для цілей демонстрації
    #     assert "Your username is invalid!" in error_message

    def test_logout_positive(self, driver_init):
        login_p = LoginPage(driver_init)
        # loggedin = LoggedInSuccessPage(driver_init)
        (login_p
         .open_login_page()
         .enterUserCred('student', 'Password123')
         .clickOnSubmit()
         .click_on_logout_button())
        text = login_p.get_title_login_text()
        time.sleep(2)  # для цілей демонстрації
        assert "Test login" in text

    def test_successful_login(self, driver_init):
        login_page = LoginPage(driver_init)
        logged_in_page = (
            login_page.open_login_page()
            .enterUserCred("student", "Password123")
            .clickOnSubmit()
        )
        assert logged_in_page.is_logout_button_displayed()

    def test_username_with_symbols(self, driver_init):
        username_with_symbols = (
            "!@#$%^&*()-_=+[{]}\\|;:',<.>/?~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGhvbsjhfbvosjhfbvHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[{]}\\|;:',<.>/?~"
        )
        login_page = LoginPage(driver_init)
        login_page.open_login_page().enterUserCred(username_with_symbols, "Password123")
        username_value = login_page.get_username_field_value()
        assert username_value == username_with_symbols and username_value != ""

import time

import pytest

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


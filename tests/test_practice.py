import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("driver_init")
class TestPractice(BaseTest):
    #Тестовий метод має починається зі слова test_ для того, щоб pytest визначив його як тест
    def test_navigation_from_practice_to_login(self, driver_init):
        #описати кроки тесту і перевірку




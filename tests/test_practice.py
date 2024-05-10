import time

import pytest

from pages.practice_page import PracticePage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("driver_init")
# TestLogin клас, який успадковує BaseTest клас для виведення назви тесту перед його виконанням
# Тестовий клас має починатися зі слова Test для того, щоб pytest визначив його як тест
class TestPractice(BaseTest):
    # Позитивний тест на вхід в систему
    # Тестовий метод має починається зі слова test_ для того, щоб pytest визначив його як тест
    def test_practice(self, driver_init):
        practice_page = PracticePage(driver_init)
        (practice_page
         .open_practice_page())
        assert "Practice" in practice_page.get_title_text()
        assert practice_page.is_test_login_link_present()


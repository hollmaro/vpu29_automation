import time

import pytest

from pages.blog_page import BlogPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("driver_init")
# TestBlog клас, який успадковує BaseTest клас для виведення назви тесту перед його виконанням
# Тестовий клас має починатися зі слова Test для того, щоб pytest визначив його як тест
class TestBlog(BaseTest):

    # Тестовий метод має починається зі слова test_ для того, щоб pytest визначив його як тест

    #Дописати тест керуючись інструкціями з файлу Завдання.txt
    #def test_blog_tab_is_active(self, driver_init):



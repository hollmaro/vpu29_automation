import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage, PracticePage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_login_failure(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('student123', 'Password_wrong')

    assert driver.current_url == "https://practicetestautomation.com/practice-test-login/"
    assert driver.title == "Test login"


def test_login_success_and_practice_links(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login('student', 'Password123')

    practice_page = PracticePage(driver)
    driver.find_element(By.LINK_TEXT, 'Practice').click()

    assert practice_page.are_links_displayed()

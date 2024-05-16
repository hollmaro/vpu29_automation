from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Test 1
def test_login_redirect():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Fill in username and password
    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    submit_button = driver.find_element_by_xpath("//input[@type='submit']")

    username_field.send_keys("student")
    password_field.send_keys("Password123")
    submit_button.click()

    # Verify the URL
    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"

    driver.quit()


# Test 2
def test_home_link_display():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    submit_button = driver.find_element_by_xpath("//input[@type='submit']")

    username_field.send_keys("student")
    password_field.send_keys("Password123")
    submit_button.click()

    home_link = driver.find_element_by_xpath("//*[text()='Home']")
    assert home_link.is_displayed()

    driver.quit()


# Run the tests
test_login_redirect()
test_home_link_display()
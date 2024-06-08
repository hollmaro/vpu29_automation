import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLoggedInSuccess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_login_flow(self):
        driver = self.driver
        # 1. Open the page
        driver.get("https://practicetestautomation.com/logged-in-successfully/")

        # 2. Save page title value to a variable
        actual_title = driver.title

        # 3. Click on "Practice" tab
        practice_tab = driver.find_element(By.LINK_TEXT, "Practice")
        practice_tab.click()

        # 4. Click on "Test Login Page" link
        test_login_page_link = driver.find_element(By.LINK_TEXT, "Test Login Page")
        test_login_page_link.click()

        # 5. Verify that page title is equal to "Log In"
        self.assertEqual(driver.title, "Log In")

        # 6. Fill in username and password
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # 7. Click on "Submit" button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()


if __name__ == "__main__":
    unittest.main()
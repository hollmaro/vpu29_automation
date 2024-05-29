import unittest

import pytest


from pages.login_page import LoginPage
from pages.blog_page import BlogPage


@pytest.mark.usefixtures("driver_init")
class TestLogin:
    def test_blog_page_title(self, driver_init):
        login_page = LoginPage(driver_init)
        logged_in_success = (login_page
                           .open_login_page()
                           .enterUserCred('student', 'Password123')
                           .clickOnSubmit())

        logged_in_success.click_on_blog_tab()

        expected_title = "Headless Browser Testing with Selenium: Elevate Your Expertise"
        actual_title = BlogPage(driver_init).get_title_blog_text()
        assert (actual_title, expected_title, "Title doesn't match")


if __name__ == "__main__":
    unittest.main()

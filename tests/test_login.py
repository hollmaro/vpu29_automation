import unittest

from pages.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def test_blog_page_title(self):

        login_page = LoginPage()
        blog_page = login_page.click_on_blog_tab()

        expected_title = "Headless Browser Testing with Selenium: Elevate Your Expertise"
        actual_title = blog_page.get_title()
        self.assertEqual(actual_title, expected_title, "Title doesn't match")


if __name__ == "__main__":
    unittest.main()

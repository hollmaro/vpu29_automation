from selenium.webdriver.common.by import By

from pages.logged_in_successfully_page import LoggedInSuccessPage
from pages.base_page import BasePage


# Class BlogPage inherits from BasePage
# and contains locators and methods for the BLOG page
# representation of https://practicetestautomation.com/blog/

class BlogPage(BasePage):
    def __init__(self, driver):
        # Викликаємо конструктор базового класу BasePage через super() і передаємо йому драйвер
        # (об'єкт WebDriver який потім буде використовуватися в методах класу)
        super().__init__(driver)

    # локатори елементів сторінки BLOG
    article_title_text = (By.XPATH, "//h2")
    blog_tab = (By.XPATH, "//*[text()='Blog']")
    blog_url = "https://practicetestautomation.com/blog/"

    def open_blog_page(self):
        self.open_page(self.blog_url)
        return self

    def get_article_title_text(self) -> str:
        return self.get_element_text(self.article_title_text)

    def click_on_article_by_title_text(self, title_text):
        self.click_on_web_element((By.XPATH, f"//*[text()='{title_text}']"))
        return self

    def is_blob_tab_active(self) -> str:
        return self.get_element_has_attribute(self.blog_tab, "aria-current")
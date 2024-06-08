class TestExceptionsPage:
    def __init__(self, driver):
        self.driver = driver

    def is_displayed(self):
        return "Test Exceptions" in self.driver.title

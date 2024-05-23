import pytest
from pages.logged_in_successfully_page import LoggedInSuccessPage

@pytest.mark.usefixtures("driver_init")
class TestLoggedInSuccessPage:
    def test_logged_success_title(self, driver_init):
        logged = LoggedInSuccessPage(driver_init)
        logged.open_logged_in_success_page()
        assert "Logged in successfully" in logged.get_title_text()

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from checker import verify_completeness, verify_max_length, verify_allowed_values


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    # TODO: add documentation
    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        # TODO: implement

    # TODO: add documentation
    def test_data(self, test_setup):
        data = self.get_table(self.test_setup, "menu_admin_viewAdminModule")
        errors = []

        # TODO: implement

        assert not errors, "errors occurred:\n{}".format("\n".join(errors))

    # TODO: add documentation
    def get_table(self, test_setup, table_id: str) -> dict:
        self.test_login(self)

        # TODO: implement

        column_names_with_records = {}

        return column_names_with_records

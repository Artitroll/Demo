import allure
import pytest
from playwright.sync_api import Page, expect

from data.credentials import User
from pages.login import LoginPage


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)

    #@pytest.mark.devRun
    @allure.title("Login with valid credentials test")
    def test_valid_login(self, base_url, page: Page):
        self.login_page.navigate()
        self.login_page.login(User.DEFAULT_USER, User.DEFAULT_USER_PASSWORD)
        expect(page).to_have_url(f"{base_url}/admin/qr6akbz4dxy")

    # @pytest.mark.parametrize(
    #     "username, password, expected_error",
    #     [
    #         (
    #             User.DEFAULT_USER,
    #             "secret_sauce1",
    #             "Epic sadface: Username and password do not match any user in this service",
    #         )
    #     ],
    #     ids=["invalid_password"],
    # )
    # @allure.title("Login with invalid credentials test")
    # def test_login_error(
    #     self, page: Page, username: str, password: str, expected_error: str
    # ):
    #     self.login_page.login(username, password)
    #     expect(self.login_page.error_message).to_have_text(expected_error)

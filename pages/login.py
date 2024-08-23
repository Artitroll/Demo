from typing import Union
from data.credentials import User
import allure

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):

        self.page = page
        self.user_name_field = page.get_by_placeholder("Username/Email")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_label("action-Action-Sign in")
        self.error_message = page.locator(".ant-notification-notice")

    def navigate(self):
        self.page.goto("/")

    @allure.step("Login with username {username} and password {password}")
    def login(self, username: User.DEFAULT_USER, password: User.DEFAULT_USER_PASSWORD):
        if hasattr(username, "value"):
            self.user_name_field.fill(username.value)
        else:
            self.user_name_field.fill(username)
        self.password_field.fill(password.value)
        self.login_button.click()

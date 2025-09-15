# pages/login_page.py

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator('input[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def goto(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()
    
    def click_login_btn(self):
        self.login_button.click()

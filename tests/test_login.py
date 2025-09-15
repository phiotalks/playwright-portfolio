from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("invalid_user", "wrong_password")
    assert "Username and password do not match" in login_page.get_error_message()

def test_empty_page(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.click_login_btn()
    assert "Epic sadface: Username is required" in login_page.get_error_message()

import time
import datetime
import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.parametrize("username, password", [
    ("standard_user","secret_sauce"), # Valid Credentials
    ("standarduser","secret_sauce"),  # Invalid Username
    ("standard_user","secretsauce")   # Invalid Password
])
def test_login_with_various_credentials(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    
    if username == "standard_user" and password == "secret_sauce":
        assert "/inventory.html" in driver.current_url
    else:
        error = login.get_error_message()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"./screenshots/login_failed_{timestamp}.png")
        assert "Username and password do not match any user in this service" in error
from utils.logger import get_logger
import datetime
import pytest
from pages.login_page import LoginPage

logger = get_logger(__name__)

@pytest.mark.smoke
@pytest.mark.parametrize("username, password", [
    ("standard_user","secret_sauce"), # Valid Credentials
    ("standarduser","secret_sauce"),  # Invalid Username
    ("standard_user","secretsauce")   # Invalid Password
])
def test_login_with_various_credentials(driver, username, password):
    logger.info(f"Starting login test with username: {username} and password: {password}")
    driver.get("https://www.saucedemo.com/")
    
    logger.info(f"Starting login test with username: {username} and password: {password}")
    login = LoginPage(driver)
    
    login.enter_username(username)
    logger.info(f"Entered username: {username}")
    
    login.enter_password(password)
    logger.info("Entered password")
    login.click_login()
    logger.info("Clicked login button")
    
    if username == "standard_user" and password == "secret_sauce":
        assert "/inventory.html" in driver.current_url
        logger.info("Login successful, navigated to inventory page")
    else:
        error = login.get_error_message()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"./screenshots/login_failed_{timestamp}.png")
        logger.error(f"Login failed: {error}")
        assert "Username and password do not match any user in this service" in error
import time
import datetime
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from utils.waits import Waits
logger = get_logger(__name__)

@pytest.fixture(autouse=True)
def Login(driver):
    logger.info("Logging in with standard_user")
    driver.get("https://www.saucedemo.com")
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    logger.info("Login successful")
    yield

def test_checkout(driver):
    logger.info("Starting checkout test")
    
    inv = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    wait = Waits()
    
    logger.info("Adding products to cart")
    inv.add_product_to_cart(1)
    inv.add_product_to_cart(2)

    inv.go_to_cart()
    logger.info("Navigated to cart page")

    cart.click_checkout()
    logger.info("Clicked checkout button")

    logger.info("Filling checkout information")
    checkout.enter_checkout_info("Micheal", "Grey", "123456")
    checkout.click_continue()
    logger.info("Clicked continue")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"./screenshots/Checkout_summary_{timestamp}.png"
    driver.save_screenshot(screenshot_path)

    wait.wait_for_presence(driver, (By.CLASS_NAME,"checkout_summary_container"),10)
    logger.info(f"Saved checkout summary screenshot: {screenshot_path}")

    checkout.click_finish()
    logger.info("Clicked finish on checkout page")

    confirmation_message = checkout.get_confirmation_message()
    logger.info(f"Order confirmation message: {confirmation_message}")
    assert "Thank you for your order" in confirmation_message
    logger.info("Checkout test completed successfully")
    
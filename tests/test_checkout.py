import time
import datetime
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def Login(driver):
    driver.get("https://www.saucedemo.com")
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    yield

def test_checkout(driver):
    inv= InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    
    inv.add_product_to_cart(1)
    inv.add_product_to_cart(2)
    time.sleep(2)
    inv.go_to_cart()
    
    cart.click_checkout()

    checkout.enter_checkout_info("Micheal", "Grey", "123456")
    checkout.click_continue()
    time.sleep(1)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"./screenshots/Checkout_summary{timestamp}.png")
    
    checkout.click_finish()
    assert "Thank you for your order" in checkout.get_confirmation_message()
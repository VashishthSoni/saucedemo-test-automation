from utils.logger import get_logger
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from utils.waits import Waits

logger = get_logger(__name__)

@pytest.fixture(autouse=True)
def Login(driver):
    driver.get("https://www.saucedemo.com")
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    yield
    
def test_product_list(driver):
    logger.info("Starting test: Verify product list")
    inventory_page = InventoryPage(driver)
    products = inventory_page.get_all_products()
    logger.info(f"Found {len(products)} products on inventory page")
    assert len(products) != 0, f"Found {len(products)} Products"  

def test_add_product_to_cart(driver):
    logger.info("Starting test: Add product to cart")
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart(3)
    badge_count = int(driver.find_element(By.CLASS_NAME ,"shopping_cart_badge").text)
    logger.info(f"Products in cart after adding: {badge_count}")
    assert badge_count > 0
    
def test_remove_product_from_cart(driver):
    logger.info("Starting test: Remove product from cart")
    inv_page = InventoryPage(driver)
    wait = Waits()
    inv_page.add_product_to_cart(3)
    
    wait.wait_for_element_visible(driver,(By.CLASS_NAME ,"btn_secondary"),10)
    before = len(driver.find_elements(By.CLASS_NAME ,"btn_secondary"))
    logger.info(f"Remove buttons before removal: {before}")
    
    inv_page.remove_product_from_cart(3)
    after = len(driver.find_elements(By.CLASS_NAME ,"btn_secondary"))
    logger.info(f"Remove buttons after removal: {after}")
    assert after == (before-1)
    
def test_navigate_to_cart(driver):
    logger.info("Starting test: Navigate to cart")
    inv_page = InventoryPage(driver)
    inv_page.go_to_cart()
    logger.info(f"Current URL: {driver.current_url}")
    assert "/cart.html" in driver.current_url
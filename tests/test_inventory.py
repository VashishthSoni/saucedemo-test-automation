import time
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def Login(driver):
    driver.get("https://www.saucedemo.com")
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    time.sleep(3)
    yield
    time.sleep(5)
    
# @pytest.mark.skip(reason="Tested Successfully")
def test_product_list(driver):
    inventory_page = InventoryPage(driver)
    products = inventory_page.get_all_products()
    assert len(products) != 0, f"Found {len(products)} Products"    

# @pytest.mark.skip(reason="Tested Successfully")
def test_add_product_to_cart(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart(3)
    assert int(driver.find_element(By.CLASS_NAME ,"shopping_cart_badge").text) > 0


def test_remove_product_from_cart(driver):
    inv_page = InventoryPage(driver)
    inv_page.add_product_to_cart(3)
    time.sleep(5)
    
    before = len(driver.find_elements(By.CLASS_NAME ,"btn_secondary"))
    print(before)
    
    inv_page.remove_product_from_cart(3)
    time.sleep(5)
    
    assert len(driver.find_elements(By.CLASS_NAME ,"btn_secondary")) == (before-1)

# @pytest.mark.skip(reason="Tested Successfully")
def test_navigate_to_cart(driver):
    inv_page = InventoryPage(driver)
    time.sleep(7) # Time to accept google alert
    
    inv_page.go_to_cart()
    assert "/cart.html" in driver.current_url
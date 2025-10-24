import time
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.products = (By.CLASS_NAME, "cart_item")
        self.remove_btn = (By.CSS_SELECTOR, ".btn_secondary.btn_small")
        self.checkout_btn = (By.ID, "checkout")
    
    def get_cart_items(self):
        return self.driver.find_elements(*self.products)
    
    def remove_item(self, index):
        self.driver.find_elements(*self.remove_btn)[index].click()
        #Name = ID
    
    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()
        
from selenium.webdriver.common.by import By
from utils.waits import Waits

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_list = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart_btn = (By.CLASS_NAME, "btn_primary")
        self.remove_from_cart_btn = (By.CLASS_NAME, "btn_secondary")
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.wait = Waits()

    def get_all_products(self):
        self.wait.wait_for_element_visible(self.driver, self.inventory_list, 10)
        return self.driver.find_elements(*self.inventory_list)
    
    def add_product_to_cart(self, index):
        self.driver.find_elements(*self.add_to_cart_btn)[index].click()
            
    def remove_product_from_cart(self, index):
        path = f"//*[@id='inventory_container']/div/div[{index+1}]/div[2]/div[2]/button"
        self.wait.wait_for_element_visible(self.driver, (By.XPATH,path),10).click()
    
    def go_to_cart(self):
        self.wait.wait_for_element_visible(self.driver, self.shopping_cart,10).click()
    
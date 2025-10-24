from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_list = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart_btn = (By.CLASS_NAME, "btn_primary")
        self.remove_from_cart_btn = (By.CLASS_NAME, "btn_secondary")
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
    
    def get_all_products(self):
        return self.driver.find_elements(*self.inventory_list)
    
    def add_product_to_cart(self, index):
        self.driver.find_elements(*self.add_to_cart_btn)[index].click()
            
    def remove_product_from_cart(self, index):
        self.driver.find_element(By.XPATH,f"//*[@id='inventory_container']/div/div[{index+1}]/div[2]/div[2]/button").click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.shopping_cart).click()
    
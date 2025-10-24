import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        # self.wait = WebDriverWait(self.driver, 10)
        
    def enter_checkout_info(self,FirstName, LastName, PostalCode):
        
        self.driver.find_element(*self.first_name).send_keys(FirstName)
        self.driver.find_element(*self.last_name).send_keys(LastName)
        self.driver.find_element(*self.postal_code).send_keys(PostalCode)
    
    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()
    
    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()

    def get_confirmation_message(self):
        return (
            self.driver.find_element(By.CLASS_NAME, "complete-header").text 
            + " " + 
            self.driver.find_element(By.CLASS_NAME, "complete-text").text
        )
    
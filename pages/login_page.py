from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.loginbutton = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
        
    def click_login(self):
        self.driver.find_element(*self.loginbutton).click()
    
    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
        
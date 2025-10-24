import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Create Chrome Service
    service = Service(ChromeDriverManager().install())
    
    # Initialize WebDriver with service
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    time.sleep(10)
    driver.quit()
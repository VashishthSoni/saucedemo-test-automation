import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Create Chrome Service
    service = Service(ChromeDriverManager().install())

    # Disabled all Alerts
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-blink-features=BlockCredentialedSubresources")

    # Initialize WebDriver with servic
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # driver.maximize_window()
    yield driver
    time.sleep(10)
    driver.quit()
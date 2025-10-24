import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()

    # Disable popups, notifications, and password alerts
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-blink-features=BlockCredentialedSubresources")
    chrome_options.add_argument("--disable-password-manager-reauthentication")
    chrome_options.add_argument("--disable-blink-features=CredentialLeakDetection")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")  # Optional: clean session

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    yield driver
    time.sleep(2)
    driver.quit()
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver']
        driver.save_screenshot(f"screenshots/{item.name}.png")
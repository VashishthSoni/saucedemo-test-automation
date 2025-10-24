# Saucedemo Automation Framework (Pytest + Selenium)

## Overview
This is a **Selenium-based end-to-end automation framework** using **Python and Pytest**, designed for the [Saucedemo](https://www.saucedemo.com) website.  
It demonstrates **best practices in automation**, including:

- Page Object Model (POM) structure  
- Explicit waits (WebDriverWait)  
- Logging  
- Screenshots on failure  
- Pytest HTML reports  
- Configurable test data and browser options  

This project is suitable for **QA internships, fresher roles**, and as a **GitHub showcase**.

---

## Prerequisites

- Python 3.10+ installed on your system  
- Google Chrome browser installed  
- `pip` package manager  

---

## Installation Steps

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd saucedemo-test-automation
```
### 2. Create and activate virtual environment 
### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Optional: Verify installation
```bash
pytest --version
python -m pip show selenium
```


## Running the Tests

### 1. Run all tests
```bash
pytest -v
```
### 2. Generate an HTML report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

Reports will be saved in reports/report.html
Screenshots of failed tests will be saved in screenshots/ folder

### 3. Run a specific test file
```bash
pytest tests/test_login.py -v
```

### 4. Run tests with markers
```bash
pytest -m smoke -v
```

Example markers: @pytest.mark.smoke, @pytest.mark.regression

## Framework Features
- Page Object Model (POM): Organized page classes for login, inventory, cart, and checkout.
- Pytest Fixtures: Handles setup and teardown for WebDriver.
- Explicit Waits: Ensures elements are loaded before interaction.
- Logging: Logs test actions and failures.
- Screenshots on Failure: Automatic capture for debugging.
- HTML Reports: Detailed test execution reports.
- Configurable: Base URL, credentials, and browser can be set in config.json.

## Test Workflow
1. Login Tests
    - Valid and invalid credentials
    - Error message validation
2. Inventory Tests
    - Verify product list
    - Add/remove items from cart
    - Navigate to cart page
3. Cart Tests
    - Verify items in cart
    - Remove items
    - Checkout navigation
4. Checkout Tests
    - Fill user information
    - Complete purchase
    - Validate confirmation message

## Folder for Artifacts
- Screenshots: screenshots/
- Reports: reports/


### Author

Vashi – QA & Test Automation Enthusiast
LinkedIn: https://www.linkedin.com/in/vashishthsoni/
GitHub: https://github.com/VashishthSoni
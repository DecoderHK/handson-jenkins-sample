"""
Comprehensive Selenium test suite for login and form submission functionality.
Uses pytest framework for better test organization and reporting.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
from datetime import datetime


class TestLogin:
    """Test suite for login functionality."""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver for all tests in this class."""
        options = webdriver.ChromeOptions()
        # Add headless option for CI/CD environments
        if os.getenv('HEADLESS', 'false').lower() == 'true':
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        yield driver
        driver.quit()
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Navigate to login page before each test."""
        driver.get("http://localhost:8000/login.html")
        yield
        # Cleanup: navigate back to login page after each test
        try:
            driver.get("http://localhost:8000/login.html")
        except:
            pass
    
    def test_successful_login(self, driver):
        """Test successful login with valid credentials."""
        username_input = driver.find_element(By.ID, "username")
        username_input.clear()
        username_input.send_keys("user")
        
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys("pass")
        
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("form.html"))
        assert "form.html" in driver.current_url, "Should navigate to form page after successful login"
    
    def test_login_with_invalid_username(self, driver):
        """Test login with invalid username."""
        username_input = driver.find_element(By.ID, "username")
        username_input.clear()
        username_input.send_keys("wronguser")
        
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys("pass")
        
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()
        
        # Wait for error message to appear
        wait = WebDriverWait(driver, 5)
        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        assert "error-message" in error_message.get_attribute("class"), "Error message should be displayed"
        assert "show" in error_message.get_attribute("class"), "Error message should be visible"
        assert "login.html" in driver.current_url, "Should remain on login page"
    
    def test_login_with_invalid_password(self, driver):
        """Test login with invalid password."""
        username_input = driver.find_element(By.ID, "username")
        username_input.clear()
        username_input.send_keys("user")
        
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys("wrongpass")
        
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()
        
        wait = WebDriverWait(driver, 5)
        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        assert "error-message" in error_message.get_attribute("class"), "Error message should be displayed"
        assert "show" in error_message.get_attribute("class"), "Error message should be visible"
    
    def test_login_with_empty_fields(self, driver):
        """Test login with empty username and password."""
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()
        
        wait = WebDriverWait(driver, 5)
        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        assert "error-message" in error_message.get_attribute("class"), "Error message should be displayed for empty fields"
        assert "show" in error_message.get_attribute("class"), "Error message should be visible"
    
    def test_login_with_whitespace_only(self, driver):
        """Test login with whitespace-only credentials."""
        username_input = driver.find_element(By.ID, "username")
        username_input.clear()
        username_input.send_keys("   ")
        
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys("   ")
        
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()
        
        wait = WebDriverWait(driver, 5)
        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        assert "error-message" in error_message.get_attribute("class"), "Error message should be displayed for whitespace-only input"
        assert "show" in error_message.get_attribute("class"), "Error message should be visible"


class TestFormSubmission:
    """Test suite for form submission functionality."""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver for all tests in this class."""
        options = webdriver.ChromeOptions()
        if os.getenv('HEADLESS', 'false').lower() == 'true':
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        yield driver
        driver.quit()
    
    @pytest.fixture(autouse=True)
    def login(self, driver):
        """Login before each form test."""
        driver.get("http://localhost:8000/login.html")
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("pass")
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("form.html"))
        yield
    
    def test_successful_form_submission(self, driver):
        """Test successful form submission with valid data."""
        name_input = driver.find_element(By.ID, "name")
        name_input.clear()
        name_input.send_keys("John Doe")
        
        email_input = driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys("john@example.com")
        
        message_input = driver.find_element(By.ID, "message")
        message_input.clear()
        message_input.send_keys("This is a test message")
        
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        
        # Wait for alert
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Form submitted successfully!" in alert.text
        alert.accept()
        
        # Verify success message is displayed
        success_message = driver.find_element(By.ID, "successMessage")
        assert "success-message" in success_message.get_attribute("class"), "Success message should be displayed"
        assert "show" in success_message.get_attribute("class"), "Success message should be visible"
    
    def test_form_submission_without_name(self, driver):
        """Test form submission without name field."""
        email_input = driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys("john@example.com")
        
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        
        wait = WebDriverWait(driver, 5)
        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        assert "error-message" in error_message.get_attribute("class"), "Error message should be displayed"
        assert "show" in error_message.get_attribute("class"), "Error message should be visible"
    
    def test_form_submission_without_email(self, driver):
        """Test form submission without email field."""
        name_input = driver.find_element(By.ID, "name")
        name_input.clear()
        name_input.send_keys("John Doe")
        
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        
        wait = WebDriverWait(driver, 5)
        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        assert "error-message" in error_message.get_attribute("class"), "Error message should be displayed"
        assert "show" in error_message.get_attribute("class"), "Error message should be visible"
    
    def test_form_submission_with_invalid_email(self, driver):
        """Test form submission with invalid email format."""
        name_input = driver.find_element(By.ID, "name")
        name_input.clear()
        name_input.send_keys("John Doe")
        
        email_input = driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys("invalid-email")
        
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        
        wait = WebDriverWait(driver, 5)
        error_message = wait.until(
            EC.presence_of_element_located((By.ID, "errorMessage"))
        )
        assert "error-message" in error_message.get_attribute("class"), "Error message should be displayed for invalid email"
        assert "show" in error_message.get_attribute("class"), "Error message should be visible"
    
    def test_form_submission_with_optional_message(self, driver):
        """Test form submission with only required fields (message is optional)."""
        name_input = driver.find_element(By.ID, "name")
        name_input.clear()
        name_input.send_keys("Jane Smith")
        
        email_input = driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys("jane@example.com")
        
        # Don't fill message field
        
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Form submitted successfully!" in alert.text
        alert.accept()


class TestEndToEnd:
    """End-to-end test scenarios."""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver for all tests in this class."""
        options = webdriver.ChromeOptions()
        if os.getenv('HEADLESS', 'false').lower() == 'true':
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        yield driver
        driver.quit()
    
    def test_complete_user_flow(self, driver):
        """Test complete user flow: login -> fill form -> submit."""
        # Step 1: Login
        driver.get("http://localhost:8000/login.html")
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("pass")
        login_button = driver.find_element(By.TAG_NAME, "button")
        login_button.click()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("form.html"))
        
        # Step 2: Fill form
        name_input = driver.find_element(By.ID, "name")
        name_input.send_keys("Test User")
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("test@example.com")
        message_input = driver.find_element(By.ID, "message")
        message_input.send_keys("End-to-end test message")
        
        # Step 3: Submit
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        
        # Step 4: Verify success
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Form submitted successfully!" in alert.text
        alert.accept()
        
        # Verify we're still on form page
        assert "form.html" in driver.current_url


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        # Get the driver from the test item
        for fixture_name in item.fixturenames:
            if 'driver' in fixture_name:
                driver = item.funcargs.get(fixture_name)
                if driver:
                    # Create screenshots directory if it doesn't exist
                    screenshots_dir = "screenshots"
                    os.makedirs(screenshots_dir, exist_ok=True)
                    
                    # Take screenshot
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_path = os.path.join(
                        screenshots_dir,
                        f"{item.name}_{timestamp}.png"
                    )
                    driver.save_screenshot(screenshot_path)
                    print(f"\nScreenshot saved: {screenshot_path}")


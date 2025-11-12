from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # For optional delays during debugging

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page
    driver.get("http://localhost:8000/login.html")

    # Step 2: Find and fill login form elements
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("pass")

    # Step 3: Click the login button
    login_button = driver.find_element(By.TAG_NAME, "button")  # The only button on the page
    login_button.click()

    # Step 4: Wait for navigation to form page (verify URL change)
    wait = WebDriverWait(driver, 10)  # 10-second timeout
    wait.until(EC.url_contains("form.html"))
    assert "form.html" in driver.current_url
    print("Login successful: Navigated to form page.")

    # Step 5: Fill the submission form
    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys("John Doe")

    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("john@example.com")

    # Step 6: Click the submit button
    submit_button = driver.find_element(By.TAG_NAME, "button")  # The button on the form page
    submit_button.click()

    # Step 7: Handle and verify the alert (submission success)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "Form submitted successfully!" in alert.text
    alert.accept()  # Close the alert
    print("Form submission successful.")

except AssertionError as ae:
    print(f"Assertion failed: {ae}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Clean up: Close the browser
    driver.quit()

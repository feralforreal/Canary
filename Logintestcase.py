#!/usr/bin/python

import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def parse_arguments():
    parser = argparse.ArgumentParser(description="Test login functionality")
    parser.add_argument("--username", required=True, help="The username to test")
    parser.add_argument("--password", required=True, help="The password to test")
    return parser.parse_args()

def validate_login_page(driver):
    # Step 1: Navigate to the login page
    driver.get("http://18.60.154.27:8080/login")

    # Step 2: Validate Login Page
    try:
        # Check for the presence of the <h1> element with the correct text
        header = driver.find_element(By.XPATH, "//h1/b[contains(text(), 'MATERIAL MANAGEMENT')]")
        assert header, "Login page title is incorrect or not found"
        print("Testcase - Passed : Login page appeared successfully.")
    except AssertionError as e:
        print(f"Tescase - Validation Failed: {e}")

def validate_elements_on_login_page(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='username']"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Forgot Password ?']"))
        )
        print("Testcase - Passed : All required elements are present on the Login Page.")
    except Exception as e:
        print(f"Testcase - Failed : Element Validation Failed: {e}")

def check_login_successful(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/mm/dashboard']"))
        )
        print("Testcase - passed : Login Successful!")
    except Exception as e:
        print(f"Testcase - Failed Login Success Check Failed: {e}")

def validate_login_credentials(driver, username, password):
    try:
        username_field = driver.find_element(By.XPATH, "//input[@formcontrolname='username']")
        password_field = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.clear()
        password_field.clear()

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        check_login_successful(driver)
    except Exception as e:
        print(f"Login Credential Validation Failed: {e}")

'''def validate_negative_cases(driver):
    # Validate when no credentials are entered
    validate_login_credentials(driver, "", "")
    # Check for error messages
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'User Name is required')]"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Password is required')]"))
        )
        print("Validation for empty credentials passed.")
    except Exception as e:
        print(f"Validation for empty credentials failed: {e}")

    # Validate when only username is entered
    validate_login_credentials(driver, "valid_username", "")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'User Name is required')]"))
        )
        print("Validation for missing password passed.")
    except Exception as e:
        print(f"Validation for missing password failed: {e}")

    # Validate when only password is entered
    validate_login_credentials(driver, "", "valid_password")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Password is required')]"))
        )
        print("Validation for missing username passed.")
    except Exception as e:
        print(f"Validation for missing username failed: {e}")

    # Validate with invalid username
    validate_login_credentials(driver, "invalid_username", "valid_password")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid Username')]"))
        )
        print("Validation for invalid username passed.")
    except Exception as e:
        print(f"Validation for invalid username failed: {e}")

    # Validate with invalid password
    validate_login_credentials(driver, "valid_username", "invalid_password")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid Password')]"))
        )
        print("Validation for invalid password passed.")
    except Exception as e:
        print(f"Validation for invalid password failed: {e}")'''


'''def validate_user_list(driver):
    try:
        # Click on User Management
        user_management_link = driver.find_element(By.XPATH, "//a[text()='User Management']")
        user_management_link.click()
    
        # Check User List screen
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='pn_id_122_header' and text()='User List']"))
        )
        print("User List screen is displayed.")'''

        # Validate columns in the User List
        '''for column in columns:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//th[text()='{column}']"))
                )
                print(f"Column '{column}' is present in the User List.")
            except Exception as e:
                print(f"Column '{column}' not found: {e}")

        # Validate Action buttons
        actions_buttons = ["pi-eye", "pi-file-edit", "pi-stop-circle"]
        for icon_class in actions_buttons:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//span[contains(@class, '{icon_class}')]"))
                )
                print(f"Action button with icon class '{icon_class}' is present.")
            except Exception as e:
                print(f"Action button with icon class '{icon_class}' not found: {e}")

        # Validate Create User button
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Create User']"))
            )
            print("Create User button is present.")
        except Exception as e:
            print(f"Create User button not found: {e}")

    except Exception as e:
        print(f"User List Validation Failed: {e}")'''


def main():
    args = parse_arguments()

    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        #launch_application(driver)
        validate_login_page(driver)
        validate_elements_on_login_page(driver)
        
        # Perform positive and negative test cases
        validate_login_credentials(driver, args.username, args.password)
        #validate_user_list(driver)
        #validate_negative_cases(driver)

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()

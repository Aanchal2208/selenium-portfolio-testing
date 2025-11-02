"""
Authentication Testing Project using Selenium WebDriver
Author: Student Portfolio Project
Description: Automated testing suite for login/authentication functionality
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import unittest


class AuthenticationTests(unittest.TestCase):
    """Test suite for authentication functionality"""
    
    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver before running tests"""
        print("\n=== Setting up Test Environment ===")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        
        cls.base_url = "https://practicetestautomation.com/practice-test-login/"
        
    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests"""
        print("\n=== Cleaning up Test Environment ===")
        time.sleep(2)
        cls.driver.quit()
        
    def setUp(self):
        """Navigate to login page before each test"""
        self.driver.get(self.base_url)
        print(f"\nNavigated to: {self.base_url}")
        
    def test_01_successful_login(self):
        """Test Case 1: Verify successful login with valid credentials"""
        print("\n--- Test 1: Valid Login ---")
        
        
        username_field = self.driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys("student")
        
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("Password123")
        
        
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("practicetestautomation.com/logged-in-successfully/")
            )
            success_message = self.driver.find_element(By.TAG_NAME, "h1").text
            print(f"Login successful! Message: {success_message}")
            self.assertIn("Logged In Successfully", success_message)
            
        except TimeoutException:
            self.fail("Login did not redirect to success page")
            
    def test_02_invalid_username(self):
        """Test Case 2: Verify error message with invalid username"""
        print("\n--- Test 2: Invalid Username ---")
        
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys("invalidUser")
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")
        
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        
        
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "error"))
            )
            print(f"Error displayed: {error_message.text}")
            self.assertIn("Your username is invalid", error_message.text)
            
        except TimeoutException:
            self.fail("Error message not displayed for invalid username")
            
    def test_03_invalid_password(self):
        """Test Case 3: Verify error message with invalid password"""
        print("\n--- Test 3: Invalid Password ---")
        
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys("student")
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("wrongPassword")
        
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        
        
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "error"))
            )
            print(f"Error displayed: {error_message.text}")
            self.assertIn("Your password is invalid", error_message.text)
            
        except TimeoutException:
            self.fail("Error message not displayed for invalid password")
            
    def test_04_empty_fields(self):
        """Test Case 4: Verify behavior with empty fields"""
        print("\n--- Test 4: Empty Fields ---")
        
        
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        
        time.sleep(2)
        
        e
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        self.assertIn("practice-test-login", current_url)
        
    def test_05_logout_functionality(self):
        """Test Case 5: Verify logout functionality after successful login"""
        print("\n--- Test 5: Logout Functionality ---")
        
        
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys("student")
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")
        
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        
        
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("logged-in-successfully")
        )
        
        logout_button = self.driver.find_element(By.LINK_TEXT, "Log out")
        logout_button.click()
        
        
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("practice-test-login")
        )
        print("Logout successful! Redirected to login page")
        self.assertIn("practice-test-login", self.driver.current_url)
        
    def test_06_ui_elements_present(self):
        """Test Case 6: Verify all UI elements are present on login page"""
        print("\n--- Test 6: UI Elements Verification ---")
        
        elements = {
            "Username field": (By.ID, "username"),
            "Password field": (By.ID, "password"),
            "Submit button": (By.ID, "submit")
        }
        
        for element_name, locator in elements.items():
            try:
                element = self.driver.find_element(*locator)
                self.assertTrue(element.is_displayed())
                print(f"✓ {element_name} is present and visible")
            except NoSuchElementException:
                self.fail(f"{element_name} not found on page")


def run_tests():
    """Main function to run the test suite"""
    print("\n" + "="*50)
    print("AUTHENTICATION TESTING SUITE")
    print("="*50)
    
    
    suite = unittest.TestLoader().loadTestsFromTestCase(AuthenticationTests)
    
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
     
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*50)
    

if __name__ == "__main__":
    run_tests()

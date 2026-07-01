from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize web driver
driver = webdriver.Chrome()

# Navigate to the target web page
driver.get('http://www.example.com')

# Locate username field
username = driver.find_element_by_name('username')

# Enter username
username.send_keys('username')

# Locate password field
password = driver.find_element_by_name('password')

# Enter password
password.send_keys('password')

# Locate submit button
submit_button = driver.find_element_by_name('submit')

# Click submit button
submit_button.click()

# Wait for login process to complete
time.sleep(5)

# Login successful
print('Login successful!')

driver.close()
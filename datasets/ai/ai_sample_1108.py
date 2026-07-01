from selenium import webdriver

# Create a webdriver
driver = webdriver.Chrome()

# Open the web page
driver.get('https://www.example.com/form')

# Enter the phone number
phone_number_field = driver.find_element_by_name('phone')
phone_number_field.send_keys('1234567890')

# Submit the form
submit_button = driver.find_element_by_id('submit')
submit_button.click()

# Check for any error messages
error_message = driver.find_element_by_class_name('error')
if error_message:
 print(error_message.text)

# Close the browser
driver.close()
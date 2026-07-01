from selenium import webdriver

# open web browser
driver = webdriver.Chrome()
driver.get("https://example.com/form")

# fill out form
name_field = driver.find_element_by_id("name")
name_field.send_keys("Joseph Smith")

address_field = driver.find_element_by_id("address")
address_field.send_keys("123 Main Street")

city_field = driver.find_element_by_id("city")
city_field.send_keys("New York")

state_field = driver.find_element_by_id("state")
state_field.send_keys("NY")

zip_field = driver.find_element_by_id("zip")
zip_field.send_keys("12345")

country_field = driver.find_element_by_id("country")
country_field.send_keys("United States")

# submit form
submit_button = driver.find_element_by_id("submit")
submit_button.click()
from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("https://www.example.com/")

# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("shoes")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name
product_list = driver.find_elements_by_class_name("product")

# iterate through each element and print the text that is
# name of the product
for product in product_list:
    print(product.text)

# close the browser window
driver.quit()
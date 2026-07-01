# Define the web scraper
from selenium import webdriver

# Define the URL
url = 'https://www.example.com/index.html'

# Initialize the web driver
driver = webdriver.Chrome()

# Load the URL
driver.get(url)

# Scrape the data
dataList = driver.find_elements_by_css_selector('div.data')

for data in dataList:
    print(data.text)

# Close the driver instance 
driver.close()
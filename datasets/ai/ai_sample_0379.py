from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://example.com')

# Check the title of the page
assert driver.title == 'Example Domain'

# Check the text on the page
text = driver.find_element_by_xpath('//p').text
assert text == 'This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.'

# Check for a hyperlink
link = driver.find_element_by_xpath('//a')
assert link.text == 'More information...'

time.sleep(2)
driver.quit()
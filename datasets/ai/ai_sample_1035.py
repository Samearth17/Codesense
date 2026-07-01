from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Initialize Webdriver
driver = webdriver.Firefox()

# Open the IMDB website
driver.get('https://www.imdb.com/chart/top?ref_=ft_250')

# Wait until the elements on the web page are loaded
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "chart")))

# Parse and store the information to a pandas dataframe
titles = driver.find_elements_by_class_name('titleColumn')
ratings = driver.find_elements_by_class_name('ratingColumn')
df = pd.DataFrame(columns = ['title', 'rating'])

for title, rating in zip(titles, ratings):
    df = df.append({'title': title.text, 'rating':rating.text}, ignore_index=True)

# Close the browser
driver.close()
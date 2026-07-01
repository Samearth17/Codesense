import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.nytimes.com/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# News Section
news_Section = soup.find("div", class_="css-1qwxefa esl82me1")
# print(news_Section)

# News Articles
articles = news_Section.find_all("h2", class_="e1xfvim30")
# print(articles)

# Empty list to store all news articles
news_list = []

# Loop over each article
for article in articles:
    # Extract the title of the article
    title = article.find("a").text

    # Extract the author of the article
    author = article.find("span", class_="css-1n7hynb").text
    
    # Extract the date the article was published
    date = article.find("time").text
    
    # Extract the URL of the article
    link = article.find("a")["href"]
    
    # Store all the information in one dictionary
    news_dict = {
        "title": title,
        "author": author,
        "date": date,
        "link": link
    }
    
    # Append the dictionary to the list
    news_list.append(news_dict)

# Print the list
print(news_list)
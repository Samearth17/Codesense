# define category variable
category = "Computer Science"
# import JSON library for retrieving the data
import json
# import HTTP library for fetching the data
import urllib.request

# create the target url
url = "https://www.example.com/books/category/" + category

# fetch the data
response = urllib.request.urlopen(url)
# read the data
data = json.loads(response.read())

# print the books
for book in data:
 print(book['title'])
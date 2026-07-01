import re
import requests 
from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Example Title</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
"""

# parse the html 
soup = BeautifulSoup(html_doc, 'html.parser')

# remove all script and style elements 
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# separate the text
text = soup.get_text()
text_list = re.split('[\r\n]', text)

# print the final text
for text in text_list:
    if len(text) > 0:
        print(text)
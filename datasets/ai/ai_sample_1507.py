import requests
import bs4

# set the url
url = "Sample URL"

# send a request
response = requests.get(url)

# get the response
html = response.text

# parse the response
soup = bs4.BeautifulSoup(html, "html.parser")


# extract the title
title = soup.title.text

# extract the meta description
meta = soup.find('meta', attrs={'name': 'description'})
description = meta.get('content')

# extract all h1-h6 tags
heading_tags = ""
for tag in soup.find_all(re.compile("^h[1-6]")):
 heading_tags += tag.text
 
print("Title:", title)
print("Meta Description:", description)
print("Heading Tags:", heading_tags)
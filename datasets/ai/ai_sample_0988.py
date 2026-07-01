import requests

# Specify your website URL
url = 'https://www.example.com'

# Send a request to the website
response = requests.get(url)

# Check the status of the response
if response.status_code == 200:
 # Parse the HTML of the response
 response_html = response.content

 # Do something with the HTML
 print(response_html)
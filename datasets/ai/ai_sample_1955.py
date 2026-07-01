import requests
from bs4 import BeautifulSoup

url = "https://www.example.com/"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

phone_numbers = []
for tag in soup.find_all('a'):
 text = tag.text.replace(" ", "").replace("-","")
 if (text.isdigit() and len(text) == 10):
 phone_numbers.append(text)

print("Phone Numbers: ", phone_numbers)
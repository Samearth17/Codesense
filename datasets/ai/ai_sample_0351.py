import requests
from bs4 import BeautifulSoup

def get_discography(artist):
  base_url = "https://en.wikipedia.org/wiki/"  # Wikipedia base URL
  artist_name = artist.replace(" ", "_")  # Format URL parameter
  url = base_url + artist_name
  response = requests.get(url)
  if response.status_code == 200:
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    discography = soup.find("span",{"id":"Discography"}).find_next_sibling().text.strip().replace("\n", ",").replace(")","").replace("(","")
    return discography.split(",")
  else:
    print("Error in response.")
    return None
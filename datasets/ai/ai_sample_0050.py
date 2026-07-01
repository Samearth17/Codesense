import requests
from bs4 import BeautifulSoup

# make a request to get the page content
page = requests.get("https://www.youtube.com/feed/trending")

# parse the page content
soup = BeautifulSoup(page.content, 'html.parser')

# extract the list of trending videos
trending_videos = soup.find_all(class_='expanded-shelf-content-item-wrapper')

# print the top ten trending videos
for video in trending_videos[:10]:
    print(video.find(class_='yt-uix-tile-link').get('title'))
#import library
import bs4

#store HTML data
html_data = '<p>This is some text</p><a href='www.example.com/'>Click Here</a>'

#parse HTML data
soup = bs4.BeautifulSoup(html_data, 'html.parser')

#get all tags
all_tags = soup.find_all()

#print result
for tag in all_tags:
 print(tag)
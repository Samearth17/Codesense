import scrapy
from bs4 import BeautifulSoup

class MySpider(scrapy.Spider):
    name = 'MySpider'
    # Create a start_requests() method to set the requests
    def start_requests(self):
        urls = [BASE_URL]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Create a parse() method to process the requests
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('div', attrs={'class':'some-class-name'})
        for div in data:
            # Extract the data from the div
            item = {
             'name': div.find('h3').text,
             'link': div.find('a')['href'],
             'price': div.find('span').text
            }
            # Return the item
            yield item
import scrapy

class ArticleSpider(scrapy.Spider):
 name = 'articles'
 start_urls = ['https://www.some-website.com/latest']
 
 def parse(self, response):
 for article in response.css('article'):
 yield {
 'title': article.css('h2 ::text').extract_first(),
 'url': article.css('a ::attr(href)').extract_first(),
 }

next_page = response.css('li.next a ::attr(href)').extract_first()
if next_page is not None:
 yield response.follow(next_page, callback=self.parse)
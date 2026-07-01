import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
 name = 'crawler'
 allowed_domains = ['example.com']
 start_urls = ['http://example.com/']
 
 rules = [
 Rule(LinkExtractor(allow=()), follow=True, callback='parse_item', process_links='filter_links', max_depth=2)
 ]

def filter_links(self, links):
 # Filter the links to follow
 filtered_links = []
 for link in links:
 if link.url not in self.visited_urls and link.url.startswith(self.domain):
 filtered_links.append(link)
 return filtered_links

def parse_item(self, response):
 # Parse the page
 pass
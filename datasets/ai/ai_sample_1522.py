import requests
import re

target_url = 'www.example.com'

def scrape_emails(url):
    # get the HTML source code from the given url
    response = requests.get(url)
    html = response.text
    # extract all emails from html with the help of regular expression
    emails = re.findall('\S+@\S+', html)
    # print all scraped emails
    print('Emails found:')
    print('\n'.join(emails))

if __name__ == '__main__':
    scrape_emails(target_url)
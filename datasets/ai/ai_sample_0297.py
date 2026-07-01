import bs4
from urllib.request import urlopen

def make_webpage_mobile_friendly(url):
    html = urlopen(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    head_html = soup.find('head')
    meta_attribute = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
    meta_tag = soup.new_tag('meta', attrs=meta_attribute)
    head_html.append(meta_tag)
    html_body = soup.find('body')
    for element in html_body.find_all('div', {'class': 'large-wrapper'}):
        element['style'] = 'max-width:100% !important'
        element['width'] = '100% !important'
    for element in html_body.find_all('img'):
        element['style'] = 'max-width:100% !important'
        element['width'] = '100% !important'

    return soup.prettify()
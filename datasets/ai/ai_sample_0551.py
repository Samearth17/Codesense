import requests

def check_for_broken_links(url):
    # Request webpage
    response = requests.get(url)

    # Parse webpage for all links
    links = response.html.find_all('a')
    
    # Check response code of each link
    for link in links:
        link_url = link['href']
        response = requests.get(link_url)
        if not response.ok:
            # Link is broken
            print('Broken link found:', link_url)

check_for_broken_links('http://example.com')
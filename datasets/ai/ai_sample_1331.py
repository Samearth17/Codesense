"""
Write a Python program to parse a given string and extract the domain name
"""

import re

def extract_domain_name(string):
    domain_name = ''
    matches = re.findall(r"://([^/]+)/?", string)
    if len(matches) > 0:
        domain_name = matches[0]
    return domain_name

string = 'https://www.google.com/search?q=google+search'
domain_name = extract_domain_name(string)

print("The domain name extracted is:", domain_name)
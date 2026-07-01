"""
Create a search engine using Python
"""

import re

def search(query):
    with open('data.txt', 'r') as f:
        data = f.read()
    results = []
    for word in re.findall(r'\w+', query):
        matches = re.findall(rf'\b{word}\b', data)
        for match in matches:
            if match not in results:
                results.append(match)
    return results

if __name__ == '__main__':
    query = input('Enter a query: ')
    print(search(query))
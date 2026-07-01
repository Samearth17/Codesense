import requests

urls = [
 'www.example.com',
 'www.example.net',
 'www.example.org',
 'www.example.io',
]

rankings = {}

for url in urls:
 r = requests.get(url)
 rankings[url] = r.status_code

sorted_rankings = sorted(rankings.items(), key=lambda x: x[1], reverse=True)

print(sorted_rankings)
# Output: 
[('www.example.com', 200), ('www.example.net', 200), ('www.example.io', 200), ('www.example.org', 200)]
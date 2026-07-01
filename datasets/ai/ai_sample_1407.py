from datetime import timedelta, date
import requests

def get_pageview_data(date, page):
  api_key = '<YOUR_API_KEY>'
  base_url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/{page}/daily/{date}/{date}'
 
  response = requests.get(base_url.format(page=page, date=date), headers={
      'User-Agent': 'My Personal Analytics App',
      'Accept': 'application/json',
      'X-WMF-User-Agent': api_key
      })
  
  response.raise_for_status()
  return response.json()

# Get the date from 30 days ago
date_before_30_days = date.today() - timedelta(days=30)

most_visited_sites = {}

for d in range(30):
  date = date_before_30_days + timedelta(days=d)
  date_string = date.strftime('%Y%m%d')
  
  # Get page view data for the current date
  pageview_data = get_pageview_data(date_string, 'Main_Page')
  
  # Store page view data in a dictionary
  most_visited_sites[date_string] = pageview_data["items"][0]["views"]

# Print log
print('Date\t\tViews')
for date, views in most_visited_sites.items():
  print('{}\t\t{}'.format(date, views))
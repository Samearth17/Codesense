"""
Access the Yelp API and build a program that takes a zip code and returns 
the average ratings for all restaurants in that zip code.
"""

import requests

def get_restaurant_ratings(zip_code):
    api_url = 'https://api.yelp.com/v3/businesses/search?location=' + zip_code
    headers = {'Authorization': 'Bearer [API KEY]'}
    r = requests.get(api_url, headers=headers)
    data = r.json()
    business_ids = [b['id'] for b in data['businesses']]
    total_rating = 0
    num_ratings = 0
    for business_id in business_ids:
        business_url = 'https://api.yelp.com/v3/businesses/' + business_id
        business_data = requests.get(business_url, headers=headers).json()
        total_rating += business_data['rating']
        num_ratings += 1
        
    return total_rating / num_ratings

if __name__ == '__main__':
    zip_code = '94115'
    print(get_restaurant_ratings(zip_code))
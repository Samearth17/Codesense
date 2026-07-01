"""
Python script to generate a load testing report for a given website
"""

import requests
import json

def generate_report(url):
    # Send a request to the given URL
    response = requests.get(url)

    # Get the request duration
    duration = response.elapsed.total_seconds()

    # Generate the report as a dictionary
    report = {
        'URL': url,
        'StatusCode': response.status_code,
        'Duration': duration
    }

    return report

if __name__ == '__main__':
    url = 'http://example.com'
    report = generate_report(url)
    print(json.dumps(report, indent=4))
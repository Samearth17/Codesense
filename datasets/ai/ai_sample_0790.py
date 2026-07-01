"""
Write a function in Python to gather data from a web page and save it in CSV format.
"""

import requests
import csv

def get_data_and_save_as_csv(url):
    response = requests.get(url)
    data = response.json()
    with open('output.csv', 'w', newline = '') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows([data[key] for key in data.keys()])

if __name__ == '__main__':
    url = input("Enter URL:")
    get_data_and_save_as_csv(url)
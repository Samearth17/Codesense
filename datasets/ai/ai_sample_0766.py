"""
Generate a Python API wrapper for an existing API
"""
import requests

class APIWrapper():
    # API URL
    API_URL = 'https://api.example.com'

    # API Endpoints
    API_ENDPOINTS = {
        'get': '/v1/get',
        'create': '/v1/create'
    }

    def __init__(self):
        pass

    def get(self, endpoint, data):
        url = self.API_URL + self.API_ENDPOINTS.get(endpoint)
        response = requests.get(url, params=data)
        return response.json()

    def create(self, endpoint, data):
        url = self.API_URL + self.API_ENDPOINTS.get(endpoint)
        response = requests.post(url, data=data)
        return response.json()
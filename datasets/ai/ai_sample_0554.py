from tldextract import extract
import requests

query_string = input("Enter a query string: ")

# Get the top-level domain from the query string
tld = extract(query_string).suffix

# Construct the API request URL
url = "https://api." + tld + "/v1/domains"

# Send the request and store the response
response = requests.get(url, params={
 "q": query_string,
 "fields": "domain_name",
})

# Extract all the domain names from the response data
data = response.json()
domain_names = [d["domain_name"] for d in data["domains"]]

# Print the list of domain names
print(domain_names)
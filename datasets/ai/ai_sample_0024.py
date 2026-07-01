import urllib.parse

url = 'https://www.example.com/path/to/file'
parsed_url = urllib.parse.urlparse(url)

# Get the protocol
protocol = parsed_url.scheme

# Get the domain name
domain_name = parsed_url.netloc

# Get the path
path = parsed_url.path

# Print the results
print('Protocol:', protocol)
print('Domain name:', domain_name)
print('Path:', path)

# Output:
# Protocol: https
# Domain name: www.example.com
# Path: /path/to/file
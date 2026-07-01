# Define a list of routes
routes = [
    ('/', 'homepage'), 
    ('/about', 'aboutpage'), 
    ('/contact', 'contactpage')
]

# Define a function to match the route and 
# get the name of the page
def match_route(route):
    for url, page in routes:
        if url == route:
            return page

# Test the function
result = match_route('/')
print(result)
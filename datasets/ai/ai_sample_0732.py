import requests

# Create a form
form_data = {
 'name': 'John Doe',
 'email': 'john@example.com'
 }

# Send request
r = requests.post('http://example.com/form-submit', data=form_data)

# Check status code
if r.status_code == 200:
 print('Form submitted successfully!')
else:
 print('Failed to submit form!')
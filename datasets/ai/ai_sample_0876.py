import xml.etree.ElementTree as ET

data = '''<?xml version="1.0"?>
<data>
 <customer>
 <name>John Smith</name>
 <email>john@example.com</email>
 </customer>
 <customer>
 <name>Jane Doe</name>
 <email>jane@example.com</email>
 </customer>
</data>'''

root = ET.fromstring(data)

for customer in root.findall('customer'):
 name = customer.find('name').text
 email = customer.find('email').text
 print(f'Name: {name}, Email: {email}')

# Output
# Name: John Smith, Email: john@example.com
# Name: Jane Doe, Email: jane@example.com
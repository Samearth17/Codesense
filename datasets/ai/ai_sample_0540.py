import xml.etree.ElementTree as ET
 
# Read the XML file
tree = ET.parse('items.xml')
 
# Get the root element
root = tree.getroot()
 
# Iterate over each item
for item in root.findall('item'):
 # Get the title
 title = item.find('title').text
 # Get the description
 description = item.find('description').text
 
 print('Title: ', title)
 print('Description: ', description)
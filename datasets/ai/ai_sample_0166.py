import xml.etree.ElementTree as ET

# creating the root element
data = ET.Element('data')

items = ['Item1', 'Item2', 'Item3']

# loop over items
for item in items:
    # creating sub elements
    item_element = ET.SubElement(data, 'item')

    # assign the value for the sub elements
    item_element.text = item

# write the XML Tree
tree = ET.ElementTree(data)
tree.write('data.xml')
import sqlite3
import xml.etree.ElementTree

xml_str = '''
<root> 
  <person> 
    <name>John Doe</name> 
    <age>32</age> 
  </person> 
  <person> 
    <name>Jane Doe</name> 
    <age>30</age> 
  </person> 
</root>
'''

conn = sqlite3.connect('test.db')
cur = conn.cursor()

sql_command = '''
CREATE TABLE IF NOT EXISTS people ( 
name VARCHAR(20), 
age INTEGER
);'''
cur.execute(sql_command)

root = xml.etree.ElementTree.fromstring(xml_str)
people = root.findall('person')
for person in people:
 name = person.find('name').text
 age = person.find('age').text
 cur.execute("INSERT INTO people VALUES (?, ?)", (name, age))

conn.commit()
conn.close()
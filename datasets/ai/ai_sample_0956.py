import xml.etree.ElementTree as et
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
 host="localhost",
 user="yourusername",
 passwd="yourpassword",
 database="mydatabase"
)

# Parse the XML
tree = et.parse('mytest.xml')
root = tree.getroot()

# Iterate over each element and add to database
for element in root:
 sql = "INSERT INTO mytable ("
 columns = []
 values = []
 for child in element:
 columns.append(child.tag)
 values.append("'"+child.text+"'")
 sql += ", ".join(columns)
 sql += ") VALUES ("
 sql += ", ".join(values)
 sql += ")"
 cursor = db.cursor()
 cursor.execute(sql)

# Commit changes
db.commit()
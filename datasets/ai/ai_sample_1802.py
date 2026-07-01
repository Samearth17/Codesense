import csv

data = [
 {'Name': 'John', 'Age': 30},
 {'Name': 'Alice', 'Age': 20},
 {'Name': 'Bob', 'Age': 25},
]

# Generate the table
table_html = "<table><tr><th>Name</th><th>Age</th></tr>"
for item in data:
 table_html += "<tr><td>{}</td><td>{}</td></tr>".format(item['Name'], item['Age'])
table_html += "</table>"

print(table_html)
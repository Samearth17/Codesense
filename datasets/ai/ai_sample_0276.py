import pandas as pd
import pyodbc

# Connect to database
server = '<yourserver>'
database = '<yourdatabase>'
username = '<yourusername>'
password = '<yourpassword>'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

# Read Excel file
df = pd.read_excel('<yourfilename>')

# Insert values into database
for index, row in df.iterrows():
 item_id = row['item_id']
 item_name = row['item_name']
 price = row['price']
 cursor.execute(f"INSERT INTO table (item_id, item_name, price) VALUES ({item_id}, '{item_name}', {price})")
conn.commit()
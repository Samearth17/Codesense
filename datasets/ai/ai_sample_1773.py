FROM python:3.6

RUN pip install mysql-connector-python
RUN pip install pandas

COPY data.csv .

CMD ["python", "main.py"]

# File: main.py

import mysql.connector
import pandas as pd

# Connect to MySQL
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="YOUR_PASSWORD_HERE"
)

# Read CSV file
df = pd.read_csv('data.csv')

# Insert data to database
for index, row in df.iterrows():
 cursor = mydb.cursor()
 sql = "INSERT INTO table (column_1, column_2) VALUES (%s, %s)"
 val = (row['column_1'], row['column_2'])
 cursor.execute(sql, val)
 mydb.commit()
 cursor.close()

mydb.close()
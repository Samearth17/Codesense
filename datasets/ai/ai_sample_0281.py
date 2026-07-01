import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="password",
 database="dbname"
)

mycursor = db.cursor()

sql = "SELECT product_id, name, price FROM Products"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for row in myresult:
  print(row)
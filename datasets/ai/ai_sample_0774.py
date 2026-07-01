import mysql.connector
import pymongo
import json
import pandas as pd

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="yourdatabase"
)

# Connect to the MongoDB database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["yourdatabase"]

# Create a DataFrame to store the customer data
df = pd.read_sql("SELECT * FROM customers", con=mydb)

# Transform the DataFrame to the desired format
# and store it in a json file
df_transformed = pd.DataFrame({
 'id': df['customer_id'],
 'name': df['name'],
 'age': df['age']
})
data = df_transformed.to_json(orient='records')

# Load the json data into the MongoDB database
json_data = json.loads(data)
db.customers.insert_many(json_data)
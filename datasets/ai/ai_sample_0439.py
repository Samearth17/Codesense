# Import the needed libraries
from pymongo import MongoClient

# Connect to the MongoDB client
client = MongoClient('localhost:27017')

# Create an instance of a MongoDB database
db = client['customer_database']

# Create the customers collection
customers = db.create_collection('customers')

# Add the needed fields
customers.create_index([("Name", 1)], unique=True)
customers.create_index([("Phone Number", 1)], unique=True)
customers.create_index([("Email", 1)], unique=True)
customers.create_index([("Address", 1)], unique=True)
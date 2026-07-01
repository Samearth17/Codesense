import pymongo

# Connect to the MongoDB Atlas Cluster
uri = "mongodb+srv://<dbuser>:<dbpassword>@<cluster>.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

# Set up the database and collection
db = client.get_database("<dbname>")
collection = db["<collectionname>"]

# Insert a document
document = { "name": "John Doe" }
collection.insert_one(document)

# Retrieve documents
documents = collection.find({})
for document in documents:
  print(document)

# Disconnect
client.close()
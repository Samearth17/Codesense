# Import the required libraries 
import pymongo
import json

# Establish a connection to the database 
client = pymongo.MongoClient("mongodb://localhost:27017")
mydb = client["mydb"]

# Define the API endpoints 
@app.route("/api/v1/getAll", methods=["GET"])
def api_get_all():
    # Get all the documents from the database and return as JSON
    documents = mydb.mycollection.find({})
    data = [json.loads(d) for d in documents]
    return json.dumps({"data": data})

@app.route("/api/v1/add", methods=["POST"])
def api_add():
    # Create a document from the `request.data` and insert it into the database
    doc = json.loads(request.data)
    mydb.mycollection.update(doc)
    return json.dumps({"message": "Document added successfully!"})
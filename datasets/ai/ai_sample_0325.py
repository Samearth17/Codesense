import json

# sample json object 
data = {
 "name": "John",
 "age": 24,
 "hobbies": ["Soccer", "Dance"]
}

# parse the json object 
parsed_data = json.loads(data)

# print the parsed values 
print("Name: ", parsed_data["name"])
print("Age: ", parsed_data["age"])
print("Hobbies: ", parsed_data["hobbies"])
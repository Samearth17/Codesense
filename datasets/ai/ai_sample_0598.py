import json

users = {
    "users": [
        {
            "name": "John",
            "age": 26
        },
        {
            "name": "Mark",
            "age": 32
        },
        {
            "name": "Alice",
            "age": 21
        }
    ]
}

search_term = "Alice"

for user in users["users"]:
    if user["name"] == search_term:
        print("Found user with name '{}' and age {}".format(user["name"], user["age"]))
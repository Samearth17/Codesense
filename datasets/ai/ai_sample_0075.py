import json

user_data = {"Name": "John", "Age": 25, "City": "New York"}

def store_user_data(data):
    with open('user_data.json', 'w') as f:
        json.dump(data, f)

def get_user_data():
    with open('user_data.json') as f:
        return json.load(f)

# store data in JSON file
store_user_data(user_data)

# get data
data = get_user_data()
print(data)
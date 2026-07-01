import json

# Load the JSON string
json_string = '{"name": "John Smith", "age": 33, "address": {"street": "123 Main Street", "city": "New York", "state": "NY", "zip": "10001"}, "phone_numbers": [{"type": "work", "number": "212 555-1234"}, {"type": "cell", "number": "646 555-4567"}]}'

# Parse the JSON string
data = json.loads(json_string)

# Extract data
name = data["name"]
age = data["age"]
street = data["address"]["street"]
city = data["address"]["city"]
state = data["address"]["state"]
zip_code = data["address"]["zip"]
work_phone_number = data["phone_numbers"][0]["number"]
cell_phone_number = data["phone_numbers"][1]["number"]

print(f'Name: {name}')
print(f'Age: {age}')
print(f'Street: {street}')
print(f'City: {city}')
print(f'State: {state}')
print(f'Zip Code: {zip_code}')
print(f'Work Phone Number: {work_phone_number}')
print(f'Cell Phone Number: {cell_phone_number}')
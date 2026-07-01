dictionary = {
 "data": {
  "user": {
   "id": "123",
   "name": "John Doe",
   "email": "john@example.com"
  }
 }
}

# extract values from dict
user_id = dictionary["data"]["user"]["id"]
user_name = dictionary["data"]["user"]["name"]
user_email = dictionary["data"]["user"]["email"]

print(user_id, user_name, user_email)
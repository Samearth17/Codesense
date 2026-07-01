class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return "Name: "+ self.name + ", Age: "+ str(self.age) +", Address: "+ self.address

class UsersDB:
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def get_users(self):
        return self.users

# Create a database
users_db = UsersDB()

# Add some users
user1 = User("John Doe", 25, "1600 Pennsylvania Avenue NW, Washington, DC")
users_db.add_user(user1)
user2 = User("Jane Doe", 20, "22 Jump Street, New York, NY")
users_db.add_user(user2)

# Print the users
print(users_db.get_users())
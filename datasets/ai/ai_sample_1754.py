# Create database to store user information 
db = sqlite3.connect('user_information.db')

# Create table in the database 
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS User_Info (Name TEXT, Age INTEGER, Gender TEXT, Phone_Number INTEGER)")

# Function to store user information in database 
def store_info(name, age, gender, number):
    cursor.execute("INSERT INTO User_Info (Name, Age, Gender, Phone_Number) VALUES(?, ?, ?, ?)", (name, age, gender, number))
    db.commit()

# Function to get user information from database
def get_info(name):
    cursor.execute("SELECT * FROM User_Info WHERE Name = ?", (name,))
    results = cursor.fetchall()
    return results

# Example 
store_info("John", 20, "Male", 8054839479)
john_info = get_info("John")
print(john_info)
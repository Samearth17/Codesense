import sqlite3

# Connect to the database
con = sqlite3.connect('customer_requests.db')
cursor = con.cursor()

# Create the customer table
cursor.execute("CREATE TABLE IF NOT EXISTS customer_requests(request_id INTEGER PRIMARY KEY, request TEXT NOT NULL)")

# Create and run the chatbot
def chatbot():
    print("Welcome to the chatbot! Enter 'exit' to quit.\n")
    while True:
        response = input("You: ")
        if response == 'exit':
            break
        else:
            print("Chatbot: Your request has been recorded.\n")
            # Store the request in the database
            con.execute(f"INSERT INTO customer_requests(request) VALUES ('{response}')")
            con.commit()

chatbot()
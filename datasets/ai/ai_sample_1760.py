class Customer:
 def __init__(self, name, address, phone_number):
 self.name = name
 self.address = address
 self.phone_number = phone_number
 
 #Create a class for storing the customers
class CustomersContainer:
 def __init__(self):
 self.customers = []
 
 def add_customer(self, customer):
 self.customers.append(customer)
 
 def search_customer(self, query):
 matches = []
 #Search for matches and append to list
 for customer in self.customers:
 if query.lower() in customer.name.lower():
 matches.append(customer)
 return matches

#Create instance of CustomersContainer
my_customers = CustomersContainer()
#Add customers
my_customers.add_customer(Customer('John Doe', '123 Main St', '555-5555'))
my_customers.add_customer(Customer('Jane Doe', '456 Elm St', '555-6666'))
#Search
customers = my_customers.search_customer('doe')
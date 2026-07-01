class Customer:
    '''
    A class used to store information about a Customer. 
    Attributes:
    name (str): the customer's name
    address (str): the customer's address
    phone_number (str): the customer's phone number
    email (str): the customer's email
    '''
    
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def display_info(self):
        print('Name: {}\nAddress: {}\nPhone Number: {}\nEmail: {}'.format(self.name, self.address, self.phone_number, self.email))
# Initialize a dictionary to store customer data
customers = {}

# Define a function to add customer information
def add_customer(customer_id, customer_name, customer_address):
    customers[customer_id] = {
        'name': customer_name,
        'address': customer_address
    }

# Define a function to update customer information
def update_customer_info(customer_id, customer_name=None, customer_address=None):
    # Return if customer does not exist
    if customer_id not in customers:
        print('Customer not found!')
        return
    
    # Update customer name if provided
    if customer_name: 
        customers[customer_id]['name'] = customer_name
    
    # Update customer address if provided
    if customer_address:
        customers[customer_id]['address'] = customer_address
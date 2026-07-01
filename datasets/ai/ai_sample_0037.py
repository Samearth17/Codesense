import sys 
  
def print_customer_data(name): 
    # Code for searching customer data by customer name and 
    # printing results 
    ...

# Main function for the customer search application
if __name__=="__main__": 
    # Get command line arguments 
    args = sys.argv 
    
    if len(args) == 2: 
        name = args[1]
        print_customer_data(name) 
    else: 
        print("Invalid arguments, please specify a customer name.")
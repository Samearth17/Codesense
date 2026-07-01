import collections 

def calculate_price(items): 
    items_dict = collections.Counter(items) 
    total_price = 0
    # Iterate through each item
    for item in items_dict: 
        price = items_dict[item] * prices[item] 
        total_price += price 
    # Return the total price
    return total_price 

# Mapping of item and its price 
prices = { 
    'apple': 2, 
    'banana': 4, 
    'orange': 6
    } 
# List of items to buy
items = ['apple', 'apple', 'orange', 'banana', 'apple'] 

# Calculate total price
price = calculate_price(items) 
print("Total Price is", price)
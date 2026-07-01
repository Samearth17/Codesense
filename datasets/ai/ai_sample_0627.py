# Initalize a shopping cart dictionary
shopping_cart = {}

# Function to add an item to the shopping cart
def add_item_to_cart(item, quantity):
    if item in shopping_cart:
        shopping_cart[item] += quantity
    else:
        shopping_cart[item] = quantity

# Function to remove an item from the shopping cart
def remove_item_from_cart(item):
    if item in shopping_cart:
        del shopping_cart[item]

# Function to calculate the total price
def calculate_total():
    total = 0
    for item, quantity in shopping_cart.items():
        total += item.price * quantity
        
    return total

# Function to clear the shopping cart
def clear_cart():
    shopping_cart.clear()
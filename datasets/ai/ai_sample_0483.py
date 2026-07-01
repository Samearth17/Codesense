class Inventory:
  def __init__(self):
    # Declare an empty dictionary to hold inventory information
    self.inventory = {}
 
  # Function for adding product
  def add_product(self, product_name, quantity):
    # If product_name exists in inventory, add quantity to existing product's quantity
    if product_name in self.inventory.keys():
      self.inventory[product_name] += quantity
    else:
      # If product_name is not in inventory, add it to inventory
      self.inventory[product_name] = quantity
 
  # Function for removing product
  def remove_product(self, product_name, quantity):
    # If product_name exists in inventory and there's insufficient quantity, print an error message
    if product_name in self.inventory.keys() and self.inventory[product_name] < quantity:
      print("Error: Insufficient Quantity!")
    else:
      # If product_name is in inventory and there's sufficient quantity, remove product from inventory
      self.inventory[product_name] -= quantity
      if self.inventory[product_name] == 0:
        del self.inventory[product_name]
 
  # Function for printing inventory
  def print_inventory(self):
    print("Inventory:")
    # Iterate through keys and values of inventory and print them
    for product_name, quantity in self.inventory.items():
      print(product_name + " : " + str(quantity))
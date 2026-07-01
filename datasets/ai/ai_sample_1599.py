"""
Create a basic point-of-sale system in Python
"""

# Define a class for a Point of Sale (POS) system
class PointOfSale:
 
  # Constructor to initialize the POS
  def __init__(self):
    self.total = 0 # Total amount
    self.products = [] # List of products purchased
 
  # Add a product to the list and calculate the total
  def addProduct(self, product):
    self.products.append(product)
    self.total += product.price
 
  # Print out the list of products purchased and the total amount
  def printReceipt(self):
    print("List of Products:")
    for product in self.products:
        print("{} - {:.2f}".format(product.name, product.price))
    print("Total Amount: {:.2f}".format(self.total))
 
# Define a class for products
class Product:
 
  # Constructor to initialize the product
  def __init__(self, name, price):
    self.name = name
    self.price = price
 
# Create some products
product1 = Product("Apple", 5.25)
product2 = Product("Banana", 3.00)
 
# Create a POS System
pos = PointOfSale()
 
# Add products to the POS
pos.addProduct(product1)
pos.addProduct(product2)
 
# Print out the receipt
pos.printReceipt()
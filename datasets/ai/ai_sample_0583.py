class ShoppingCart:
 def __init__(self, products):
 self.products = products
 self.total_price = 0

 def add_product(self, product):
 self.products.append(product)

 def calculate_total_price(self):
 self.total_price = 0
 for product in self.products:
 self.total_price += product['price']
 return self.total_price

 def make_purchase(self):
 self.total_price = self.calculate_total_price()
 print('You purchased {} items with a total price of {}'.format(len(self.products), self.total_price))
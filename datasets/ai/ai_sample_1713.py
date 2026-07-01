class ShoppingCart:
 def __init__(self, items):
 self.items = items
 
 def add_item(self, item):
 self.items.append(item)
 
 def remove_item(self, item):
 self.items.remove(item)
 
 def get_total_price(self):
 total_price = 0
 for item in self.items:
 total_price += item.price
 return total_price
 
# Usage
cart = ShoppingCart([item1, item2, item3])
cart.add_item(item4)
cart.remove_item(item3)
total_price = cart.get_total_price()
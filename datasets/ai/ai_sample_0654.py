class ShoppingCart:
    def __init__(self):
        self.cart = [] 
  
    def add_item(self, item):
        self.cart.append(item)
  
    def remove_item(self, item):
        self.cart.remove(item)
  
    def get_total(self):
        total = 0
        for item in self.cart:
            total += item.price
        return total
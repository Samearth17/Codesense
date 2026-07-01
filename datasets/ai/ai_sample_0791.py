class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Products:
    def __init__(self):
        self.products = []
 
    def add_product(self, product):
        self.products.append(product)
 
    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None
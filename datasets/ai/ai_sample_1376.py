class Bicycle:
 def __init__(self, type, size, price, speed):
 self.type = type
 self.size = size
 self.price = price
 self.speed = speed

 def get_type(self):
 return self.type

 def get_size(self):
 return self.size

 def get_price(self):
 return self.price

 def get_speed(self):
 return self.speed

# Creating an instance of the Bicycle class
bike = Bicycle("mountain", "medium", 500, 20)

# Accessing class attributes
print(bike.get_type())
print(bike.get_size())
print(bike.get_price())
print(bike.get_speed())

# Output: 
mountain
medium
 500 
 20
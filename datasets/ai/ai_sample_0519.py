# Python module for classes and objects


class MyClass:
    """A basic example to demonstrate classes and objects"""

    # Class attributes
    color = 'red'
    shape = 'circle'

    # Initializer
    def __init__(self, radius):
        self.radius = radius

    # Methods
    def area(self):
        return 3.14 * self.radius * self.radius


# Create an object
obj = MyClass(radius = 15)

# Access object attributes
print("The color of the object is:", obj.color)
print("The shape of the object is:", obj.shape)

# Access object methods
print("The area of the object is:", obj.area())
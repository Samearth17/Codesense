# Python program to display introduction of 
# Object Oriented Programming

# Creating a class
class Person:

    # Constructor 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def introduce_self(self):
        print("I'm {0} aged {1}.".format(self.name, self.age))

# Instantiating an object
p1 = Person("John", 25)

# Calling a method
p1.introduce_self()
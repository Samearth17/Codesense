class Employee:
 name = ""
 age = 0

def __init__(self):
 pass

def set_name(self, n):
 self.name = n

def set_age(self, a):
 self.age = a

def display_age(self):
 print(self.age)

# Call display_age directly
Employee().display_age()
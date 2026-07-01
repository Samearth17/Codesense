class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender

# Test person
person = Person("John", 30, "Male")

# Print person information
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Gender:", person.get_gender())
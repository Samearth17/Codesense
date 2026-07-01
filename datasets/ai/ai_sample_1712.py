class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age 
    
    def get_major(self):
        return self.major
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_age(self, new_age):
        self.age = new_age
    
    def set_major(self, new_major):
        self.major = new_major
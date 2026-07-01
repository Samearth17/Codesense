class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_salary(self,salary):
        self.salary = salary

employee1 = Employee("John", 30, 5000)
class Employee:
    def __init__(self, name, age, salary, designation):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation
 
    def show_details(self):
        print("Employee Details")
        print("-------------------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Designation:", self.designation)

emp1 = Employee("John", 25, 10000, "Developer")
emp1.show_details()
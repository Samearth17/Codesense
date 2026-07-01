class Employee:

    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary
    
    def displayEmployeeDetails(self):
        # This method prints employee details

        print("Employee Details -")
        print("Name: {}".format(self.name))
        print("Address: {}".format(self.address))
        print("Salary: {}".format(self.salary))

employee = Employee("John Doe", "NYC", "10000")
employee.displayEmployeeDetails()
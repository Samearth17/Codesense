# Object-Oriented Programming Implementation

class Python:
    # Basic data types
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean" 

    def __init__(self):
        self.__data_types = [self.INTEGER, self.FLOAT, self.STRING, self.BOOLEAN]

    # Function to get the data types
    def get_data_types(self):
        return self.__data_types

    # Loops

    # Function to loop through a list
    def loop_list(self, collection):
        for item in collection:
            print(item)

    # Function to loop through a range
    def loop_range(self, start, end):
        for i in range(start,end):
            print(i)
    
    # Functions

    # Function to calculate the sum
    def sum_nums(self, num1, num2):
        return num1+num2

    # Function to calculate the product
    def multiply_nums(self, num1, num2):
        return num1*num2

# Main code
python = Python()
data_types = python.get_data_types()

print("Data Types: ", data_types)

numbers = [1,2,3,4]
python.loop_list(numbers)

python.loop_range(1, 10)

print("Sum: ", python.sum_nums(4,5))
print("Product: ", python.multiply_nums(4,5))
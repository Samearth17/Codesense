class InputValidator:
    def __init__(self, userInput):
        self.userInput = userInput
 
    def is_valid_quantity(self):
        try:
            int(self.userInput) # Check if user input is an integer.
            return True
        except ValueError:
            return False

# Create a class instance
inputValidator = InputValidator("10") 
result = inputValidator.is_valid_quantity()
print(result) # Displays True
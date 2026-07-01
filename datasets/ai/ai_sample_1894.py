class Number:
    """Class to detect if a given number is a prime number."""

    def __init__(self, number):
        self.number = number
    
    def is_prime(self):
        """
        Method to detect if a given number is a prime number
        """

        for i in range(2, self.number):
            if self.number % i == 0:
                return False
        
        return True
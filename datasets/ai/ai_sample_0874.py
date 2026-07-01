"""
Generate a Python class for a race car that has the attributes of engine, transmission, and color
"""

class RaceCar:
    """
    A class to represent a race car with engine, transmission, and color attributes
    """
    
    def __init__(self, engine, transmission, color):
        """
        Initialize the race car with engine, transmission, and color attributes
        
        Parameters:
        engine (string): The type of engine
        transmission (string): The type of transmission
        color (string): The color of the car
        """
        self.engine = engine
        self.transmission = transmission
        self.color = color
    
    def __str__(self):
        """
        Return a string representation of the race car
        """
        return f"Race car with {self.engine} engine and {self.transmission} transmission; color is {self.color}"
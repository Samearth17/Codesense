class Circle:
    "This class represents a circle"
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def get_radius(self):
        return self.radius
    
    def get_color(self):
        return self.color
    
    def set_radius(self, radius):
        self.radius = radius
        
    def set_color(self, color):
        self.color = color
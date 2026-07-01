class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # method to get x-position
    def get_x(self):
        return self.x
    
    # method to get y-position
    def get_y(self):
        return self.y
            
    # method to move point
    def move_point(self, dx, dy):
        self.x += dx
        self.y += dy
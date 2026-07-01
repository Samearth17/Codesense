class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_color(self):
        return self.color
    
    def get_mileage(self):
        return self.mileage
    
    def set_mileage(self, new_mileage):
        self.mileage = new_mileage
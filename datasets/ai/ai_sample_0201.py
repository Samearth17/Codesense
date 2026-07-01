# Defining a class for 3-dimensional vectors 
 
class Vector: 
  
    # defining constructor 
    def __init__(self, x, y, z): 
        self.x = x 
        self.y = y 
        self.z = z 
  
    # Defining function to print vector
    def printVec(self):
        print(self.x, self.y, self.z) 
  
    # Defining function to add two vectors 
    def addVec(self, V):
        return Vector(self.x+V.x, self.y+V.y, self.z+V.z) 
  
    # Defining function to subtract two vectors 
    def subVec(self, V): 
        return Vector(self.x-V.x, self.y-V.y, self.z-V.z) 

# Driver code 
v1= Vector(1, 2, 3)
v2= Vector(5, 3, 2) 

print("Vector 1: ")
v1.printVec() 
print("Vector 2: ")
v2.printVec()

v3 = v1.addVec(v2)
print("sum of vector 1 and vector 2: ")
v3.printVec()

v4 = v1.subVec(v2) 
print("difference of vector 1 and vector 2: ")
v4.printVec()
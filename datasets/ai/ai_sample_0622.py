"""
Create a Python program that can identify a triangle using 3 provided side lengths.
"""

def is_valid_triangle(side1, side2, side3): 
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2): 
        return True 
    else: 
        return False

if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    print(is_valid_triangle(side1, side2, side3))
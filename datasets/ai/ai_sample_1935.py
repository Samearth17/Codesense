def double(value): 
    return value * 2

def triple(value): 
    return value * 3

def quad(value):
    return value * 4

def calculate_value(n): 
    if n > 10: 
        return double(n) 
    elif n > 5: 
        return triple(n) 
    else: 
        return quad(n) 
    
print(calculate_value(-2))
print(calculate_value(8)) 
print(calculate_value(13))
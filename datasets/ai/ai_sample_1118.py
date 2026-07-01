def is_in_rectangle(x,y,bottom_left,top_right):
    """
    Check if a given data point is inside a given 
    rectangle shaped area.
    """
    # Unpack bottom left and top right coordinates
    bx, by = bottom_left
    tx, ty = top_right
    
    # Check if (x,y) is inside the rectangle
    if bx <= x <= tx and by <= y <= ty:
        return True
    else:
        return False

# Data point (x,y)
x, y = (21,3.3)

# Area with bottom left corner at (2.8, -7.1) 
# and top right corner at (16.2, 13.7)
bottom_left = (2.8,-7.1) 
top_right = (16.2,13.7)

print(is_in_rectangle(x,y,bottom_left,top_right))
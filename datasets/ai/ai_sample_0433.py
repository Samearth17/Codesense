# define a function 
def getIntersectionPoint(line1, line2): 
    # line1 (slope and intercept) 
    l1_m = line1[0]
    l1_c = line1[1]
  
    # line2 (slope and intercept) 
    l2_m = line2[0]
    l2_c = line2[1]
    
    x = (l2_c - l1_c) / (l1_m - l2_m)
    y = l1_m * x + l1_c
    return (x, y) 
  
# given two lines
line1 = (3, 5) 
line2 = (7, 9)
  
# calculate intersection point
intersection_point = getIntersectionPoint(line1, line2)
  
# print the point
print("Intersection point of lines is:", intersection_point)
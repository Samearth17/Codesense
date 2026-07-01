# Find Maximum and Minimum using python 
def maxMin(list):
    max = list[0]
    min = list[0]
    for i in range(len(list)): 
        if list[i] > max: 
            max = list[i] 
        if list[i] < min: 
            min = list[i] 
    return max, min 
  
# Main Program 
list = [5, 2, 8, 9, 3, 6, 1] 
maximum, minimum = maxMin(list) 
  
print("Maximum number is: {}".format(maximum)) 
print("Minimum number is: {}".format(minimum))
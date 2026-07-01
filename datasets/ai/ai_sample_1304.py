# Function to return average
def average(lst):
    
    # Calculate sum of list
    sum_num = 0
    for x in lst:
        sum_num += x
        
    # Return average 
    return sum_num / len(lst)

# Sample List
lst = [1, 2, 3, 4, 5, 6, 7]

# Calling average function
print(average(lst))
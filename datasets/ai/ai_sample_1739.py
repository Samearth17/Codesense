def calculate_mean(data): 
    # Initialize the sum and length of data 
    sum = 0 
    length = len(data) 
  
    # Calculating the sum  
    for x in data: 
        sum += x   
    # Calculating the mean  
    mean = sum / length 
  
    return mean 
  
# Test the function 
data = [1, 2, 3, 4, 5, 6] 
print('Mean of data is:', calculate_mean(data))
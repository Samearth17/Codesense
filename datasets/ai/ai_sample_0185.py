# Function to calculate the maximum, minimum, and average values
def calculate_metrics(list):
    # Calculate the maximum value
    maximum = max(list)
    
    # Calculate the minimum value
    minimum = min(list)
   
    # Calculate the average
    n = len(list)
    total = 0
    for num in list:
        total += num
    average = total/n
    
    return maximum, minimum, average

# Main Program 
list = [3, 4, 5, 6, 21, 8]

maximum, minimum, average = calculate_metrics(list)

print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Average value:", average)
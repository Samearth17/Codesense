my_list = [1,2,3,4]

# function to find the sum of all possible combinations 
def sum_combinations(arr): 
    total = 0 
    for i in range(len(arr)): 
        partial_sum = 0
        for j in range(i,len(arr)): 
            partial_sum += arr[j] 
            total += partial_sum 
    return total 

# find the sum of all possible combinations  
total_sum = sum_combinations(my_list)

print("The sum of all possible combinations of numbers in the list is", total_sum)
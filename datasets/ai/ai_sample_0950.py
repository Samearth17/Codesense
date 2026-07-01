import random 
  
# function to generate a random 
# permutation of a list  
def randomize(data_list): 
    # Start from the last  
    # element and swap one by one.  
    for i in range(len(data_list) - 1, 0, -1):  
  
        # Pick a random index  
        # from 0 to i  
        j = random.randint(0, i + 1)  
  
        # Swap the randomly picked  
        # element with the current  
        data_list[i], data_list[j] = data_list[j], data_list[i]  
  
# Driver code  
data_list = [1, 2, 3, 4, 5] 
randomize(data_list) 

print(data_list)
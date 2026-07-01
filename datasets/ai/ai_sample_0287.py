"""
Write a Python program to complete the implementing of a searching algorithm
"""

# Function to implement searching algorithm 
def search(list, item): 
    # traverse through all list elements
    for i in range(len(list)): 
        if list[i] == item: 
            return i 
      
    # item not found
    return -1
  
# main 
if __name__ == "__main__": 
    # Given list 
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    item = 7
  
    # Calling Function 
    index = search(list, item) 
  
    if index != -1: 
        print("Item found at index", index) 
    else:
        print("Item is not found in list")
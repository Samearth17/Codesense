def linear_search(list, n): 
  
    for i in range(len(list)): 
  
        if list[i] == n: 
            return i 

list = [1, 2, 3, 4, 5, 6] 
n = 5

x = linear_search(list, n) 

if x == None: 
    print("Element is not present in the list") 
else: 
    print("Element is present at index", x)
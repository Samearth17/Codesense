def Powerset(arr): 
  
    # variable to store the power sets 
    powerset = [[]] 
      
    # generte the power sets 
    for ele in arr: 
          
        # give token which stores the length  
        # of the present power set 
        n = len(powerset) 
          
        # loop to give powerset of all element 
        for i in range(0, n): 
            newset = powerset[i].copy() 
            newset.append(ele) 
            powerset.append(newset) 
  
    return powerset 
  
# Driver Code 
arr = ['A', 'B', 'C'] 
print(Powerset(arr))
def compare_list(list1, list2): 
 
    # store comparison in results  
    results = [] 
  
    # iterate through lists 
    for x in list1: 
        for y in list2: 
            if x == y:  
                results.append(x) 
  
    # return result 
    return results 

# Driver code  
list1 = [1, 2, 3, 4, 5] 
list2 = [2, 3, 8, 9, 10] 

print(compare_list(list1, list2))
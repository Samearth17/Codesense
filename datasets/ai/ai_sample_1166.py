def count_unique_elements(list): 
 
    # initialize a set 
    unique_set = set() 
  
    # traverse for all elements 
    for x in list: 
        # check if exists in set or not 
        if x not in unique_set: 
            unique_set.add(x) 
  
    # print length of set 
    print("The number of unique elements is:" + str(len(unique_set))) 

count_unique_elements(list)
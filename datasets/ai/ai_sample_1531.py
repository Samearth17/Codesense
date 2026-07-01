def third_largest(arr): 
    first = arr[0] 
    second = -float("inf") 
    third = -float("inf") 
  
    for num in arr[1:]: 
        if (num > first): 
            third = second 
            second = first 
            first = num
  
        elif (num > second):              
            third = second 
            second = num 
  
        elif (num > third):               
            third = num 
                               
    return third
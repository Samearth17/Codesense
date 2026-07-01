def minOperations(n): 
  
    if n==0: 
        return 0
    elif n==1: 
        return 1
  
    x = n 
  
    for i in range(2, n): 
        if i>x: 
            break
  
        if n%i == 0: 
            x = minOperations(int(n/i)) +  i 
  
    return x 
  
result = minOperations(18)
print(result)
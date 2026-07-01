def fibonacci_sequence(num): 
    result = [0, 1] 
    if num < 0: 
        return None
    elif num == 0 or num == 1: 
        return 0
    elif num == 2: 
        return result 
    else: 
        for i in range(2,num): 
            next_num = result[i-1] + result[i-2] 
            result.append(next_num) 
        return result 

print(fibonacci_sequence(num))
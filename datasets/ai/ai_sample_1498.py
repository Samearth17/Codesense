def calculate(expression): 
    stack = [] 
    for i in expression: 
        if i.isdigit(): 
            stack.append(int(i)) 
        else: 
            val1 = stack.pop() 
            val2 = stack.pop() 
            if i == '+': 
                result = val2 + val1 
            elif i == '-': 
                result = val2 - val1 
            elif i == '*': 
                result = val2 * val1 
            else: 
                result = val2/val1 
            stack.append(result) 

    return stack.pop()  

print(calculate("10 + 2 * 5 - 3")) # 19
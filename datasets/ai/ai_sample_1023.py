def evaluate_expression(expression):
    stack = [] 
    expression_list = expression.split(" ")
    operators = ['+', '-', '*', '/'] 
    
    for i in expression_list: 
        if i not in operators: 
            stack.append(int(i))
        else: 
            val1 = stack.pop()  
            val2 = stack.pop() 
 
            if i == "+": 
                stack.append(val2 + val1) 
            elif i == "-": 
                stack.append(val2 - val1) 
            elif i == "*": 
                stack.append(val2 * val1) 
            else: 
                stack.append(int(val2 / val1)) 
                
    return stack.pop()

print(evaluate_expression("3*(2+7)"))  # prints 27
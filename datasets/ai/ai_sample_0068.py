def evaluate(expression): 
  
    # split expression into list  
    expression = expression.split() 
  
    # stack to store integer values. 
    stack = []  
  
    # do for every element of expression. 
    for element in expression: 
  
        # If element is an operand push 
        # into stack it's a number only 
        if element.isdigit(): 
            stack.append(element) 
  
        # if element is an operator, 
        # pop two elements from stack 
        # perform respective operations 
        else:  
            val1 = stack.pop() 
            val2 = stack.pop() 
            stack.append(str(eval(val2 + element + val1))) 
  
    # return the value  
    return (int(stack[0])) 
  
# Driver Code  
expression = "2 3 + 4 5 * *"
  
print(evaluate(expression)) 

Output: 46
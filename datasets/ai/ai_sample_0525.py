def infix_to_postfix(expression):
    # Separate the expression by tokens
    tokens = expression.split(' ')
    
    # Create an operator stack
    op_stack = []
    
    # Create a list for the postfix output
    postfix_output = []
    
    # Iterate through the tokens
    for token in tokens:
        # If token is an operator
        if token == '+' or token == '-' or token == '*':
            # Append it to the operator stack
            op_stack.append(token)
        # If token is an operand
        else:
            # Append it to the postfix output
            postfix_output.append(token)
            # Pop operands from the stack while not empty
            while op_stack:
                # Append it to the postfix output
                postfix_output.append(op_stack.pop())
                
    # Return the postfix output as a string
    return ' '.join(postfix_output)
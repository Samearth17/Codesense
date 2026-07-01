def calculator(expression):
    # create a stack for storing values
    stack = []
    # iterate through the expression
    for char in expression:
        # check if the character is a number
        if char.isdigit():
            # if so, push it to the stack
            stack.append(int(char))
        # check if the character is an operator
        if char == '+' or char == '*':
            # pop two values from the stack
            val_one = stack.pop()
            val_two = stack.pop()
            # determine which operator was used and
            # perform the corresponding operation
            if char == '+':
                stack.append(val_one + val_two)
            elif char == '*':
                stack.append(val_one * val_two)
    # return the calculated result
    return stack.pop()
def convert_to_boolean(expression):
    expression = expression.replace(" ", "")
    expression = expression.replace("(", "")
    expression = expression.replace(")", "")
    
    tokens = expression.split("+")
    for i in range(len(tokens)):
        tokens[i] = tokens[i].replace("-","+-")
    
    expression = "".join(tokens)
    expression = expression.replace(" > 0", "")
    expression = expression.split("+")
    
    boolean_expression = " ".join(expression)
    boolean_expression = boolean_expression.replace(" x", "True")
    boolean_expression = boolean_expression.replace("y", "True")
    boolean_expression = boolean_expression.replace("z", "False")
    
    return boolean_expression
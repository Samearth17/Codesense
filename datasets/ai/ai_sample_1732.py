def evaluate_tree(preorder):
 # base case
 if len(preorder) == 1:
 return preorder[0]
 else:
 # identify the lowest level operator and its operands
 operator = preorder[0]
 leftoperand = preorder[1]
 rightoperand = preorder[2]

# evaluate the operands
 leftoperand = evaluate_tree(leftoperand) if isinstance(leftoperand, list) else leftoperand
 rightoperand = evaluate_tree(rightoperand) if isinstance(rightoperand, list) else rightoperand

# compute the result of the operation
 if operator == '+':
 return leftoperand + rightoperand
 elif operator == '-':
 return leftoperand - rightoperand
 elif operator == '*':
 return leftoperand * rightoperand
 elif operator == '/':
 return leftoperand / rightoperand

print(evaluate_tree(['*', '+', 9, 10, 11]))
# prints 99
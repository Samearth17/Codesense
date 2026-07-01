"""
Python program to convert a given string of mathematical expression from infix notation to postfix notation.
"""

# Import Stack
from stack import Stack

# Function to convert Infix expression to Postfix
def infixToPostfix(exp):

	# Create a stack to store operators. 
	s = Stack()

	# Create a string to store postfix expression
	postfix = ""
	
	# Scan through the expression one character at a time.
	for c in exp:
		
		# If character is an operand, append it in postfix
		if (c.isalpha()):
			postfix += c
			
		# If character is an operator ( +, - or * )
		elif (c == "+" or c == "-" or c == "*"):
			
			# If the stack is empty, push the operator
			if s.isempty():
				s.push(c)
			
			# If the stack is not empty
			else:
				# pop all operators from stack
				# until an operator with lower precedence 
				# is found
				while s.isempty() == False and precedence(c) <= precedence(s.top()):
					postfix = postfix + s.pop()
				
				# Push the operator onto stack
				s.push(c)
		
		# If character is ( or ), push it to stack
		elif c == "(":
			s.push(c)
		elif c == ")":
			
			# pop all operators from stack
			# until an opening bracket is found
			while s.top() != "(":
				postfix = postfix + s.pop()
			
			# Remove the opening bracket
			s.pop()
			
	# append all operators to postfix
	while s.isempty() == False:
		postfix = postfix + s.pop()
	
	return postfix

# Function to return precedence of operators 
def precedence(operator): 
	if operator == '+' or operator == '-': 
		return 1 
	if operator == '*': 
		return 2 
	return 0 

# Driver program to test above function
exp = "A+B*C"
print(infixToPostfix(exp))
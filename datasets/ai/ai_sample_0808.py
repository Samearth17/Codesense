"""
Create a function in Python to parse a string representing an expression into a tree
"""

import re

# Node to store the information of each node in the expression Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Function to parse the expression string and
# build the expression Tree
def parse(expression):
 
    # split the expression string using space delimiter
    tokens = re.split('([+-/*])', expression)
    # create the root node
    root = Node(tokens[0])
    # store the current node
    current_node = root
 
    for i in range(1, len(tokens) - 1, 2):
        # create a new node
        node = Node(tokens[i + 1])
        if tokens[i] == '+' or tokens[i] == '-':
            # set the left child of current node
            current_node.left = node
            # make the newly created node as current node
            current_node = node
        elif tokens[i] == '*' or tokens[i] == '/':
            # set the right child of current node
            current_node.right = node
            current_node = node
 
    return root

if __name__ == "__main__":
    expression = "2 + 3*4 + 5"
    root = parse(expression)
    print("Expression Tree")
    print("     " + root.data)
    print("  /  \ ")
    print(root.left.data, root.right.data)
    print(" /\   /")
    print(root.left.right.data, root.right.left.data)
"""
Design an algorithm in Python to detect if a given tree is a binary search tree
"""

#Define the Node class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Define the isBST function 
def isBST(root): 
    # Base condition
    if root is None: 
        return True
  
    # Check if the value is within range
    if root.val < getMaxValue(root.left) or root.val > getMinValue(root.right): 
        return False
  
    # Check the subtrees
    if (not isBST(root.left)) or (not isBST(root.right)): 
        return False
  
    # Pass all test cases
    return True
  
# Find the minimum value in a tree
def getMinValue(root): 
    if root is None: 
        return float("inf") 
    minv = root.val 
    minv = min(minv, getMinValue(root.left)) 
    minv = min(minv, getMinValue(root.right)) 
    return minv
  
  
# Find the maximum value in a tree
def getMaxValue(root): 
    if root is None: 
        return -float("inf") 
    maxv = root.val 
    maxv = max(maxv, getMaxValue(root.left)) 
    maxv = max(maxv, getMaxValue(root.right)) 
    return maxv
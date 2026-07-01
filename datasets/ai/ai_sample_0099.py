# Python program to check if 
# a binary tree is subtree of another binary tree 
  
# A binary tree node 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def isSubTree(T, S): 
    
    if S is None: 
        return True
  
    if T is None: 
        return False
  
    if areIdentical(T, S): 
        return True
  
    return isSubTree(T.left, S) or isSubTree(T.right, S) 
  
  
def areIdentical(T, S): 
      
    if T is None and S is None: 
        return True
  
    if T is None or S is None: 
        return False
  
    return (T.data == S.data and areIdentical(T.left, S.left)and
        areIdentical(T.right, S.right))
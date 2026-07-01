class Node:
 def __init__(self, val):
 self.val = val
 self.left = None
 self.right = None
 
class BinarySearchTree:
 def __init__(self):
 self.root = None
 
 def insert(self, val):
 newNode = Node(val)
 if self.root == None:
 self.root = newNode
 else:
 curr = self.root
 while curr:
 if val < curr.val:
 if curr.left == None:
 curr.left = newNode
 break
 else:
 curr = curr.left
 else:
 if curr.right == None:
 curr.right = newNode
 break
 else:
 curr = curr.right
 
 def delete(self, val):
 curr = self.root
 parent = None
 isLeftChild = True
 
 while curr.val != val:
 parent = curr
 if val < curr.val:
 curr = curr.left
 isLeftChild = True
 else:
 curr = curr.right
 isLeftChild = False
 
 if curr == None:
 return
 
 # if node has no children
 if curr.left == None and curr.right == None:
 if isLeftChild:
 parent.left = None
 else:
 parent.right = None
 
 # if node has one child
 elif curr.left == None:
 if isLeftChild:
 parent.left = curr.right
 else:
 parent.right = curr.right
 
elif curr.right == None:
 if isLeftChild:
 parent.left = curr.left
 else:
 parent.right = curr.left
 
 # if node has two children
 else:
 succParent = curr
 succ = curr.right
 
 while succ.left != None:
 succParent = succ
 succ = succ.left
 
 # if successor is a direct right child
 if succParent == curr:
 succParent.right = succ.right
 else:
 succParent.left = succ.right
 
 curr.val = succ.val
 
 def traverse(self):
 if self.root is None:
 return
 curr = self.root
 self.traverseInOrder(curr)
 
 def traverseInOrder(self, curr):
 if curr.left != None:
 self.traverseInOrder(curr.left)
 print(curr.val)
 if curr.right != None:
 self.traverseInOrder(curr.right)
class Node:
 def __init__(self, data):
 self.data = data
 self.left = None
 self.right = None

def construct_tree(preorder, inorder):
 if not preorder or not inorder:
 return None

 # first element of preorder is the root
 root = Node(preorder[0])

 # get index of root in inorder
 idx = inorder.index(root.data)

 # left and right subtrees are constructed recursively
 root.left = construct_tree(preorder[1: idx + 1], inorder[0:idx])
 root.right = construct_tree(preorder[idx + 1:], inorder[idx + 1:])

 return root

if __name__ == "__main__":
 preorder = ["A", "B", "E", "K", "C", "F", "G", "D"]
 inorder = ["E", "B", "K", "A", "F", "C", "D", "G"]

 root = construct_tree(preorder, inorder)
# A recursive function to clear a binary tree 
def clearBinaryTree(root): 
	
	# Base case 
	if root is None: 
		return

	# First clear the left nodes 
	clearBinaryTree(root.left) 
	
	# Then clear the right nodes 
	clearBinaryTree(root.right) 
	
	# Clear the data of this node 
	root.data = None
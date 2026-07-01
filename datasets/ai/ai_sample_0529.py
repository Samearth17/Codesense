def rotateNodes(root): 
    # if node has a left child 
    if root.left is not None: 
        # we rotate clockwise 
        newRoot = root.left 
        root.left = newRoot.right 
        newRoot.right = root 
        root = newRoot 
  
    # if node has a right child 
    if root.right is not None: 
        # we rotate counter clockwise 
        newRoot = root.right 
        root.right = newRoot.left  
        newRoot.left = root 
        root = newRoot 

    return root
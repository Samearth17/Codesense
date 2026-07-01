def dropLeafNodes(head): 
    
    # If node is not None and doesn't have any children 
    if head and not head.left and not head.right: 
        return None
  
    # Don't change anything if head is None 
    if not head: 
        return None
  
    # Recursively call dropLeafNodes on left and right subtrees
    head.left = dropLeafNodes(head.left) 
    head.right = dropLeafNodes(head.right) 
  
    # Return head of the modified tree
    return head
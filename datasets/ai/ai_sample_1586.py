def deleteNode(head, key): 
  
    # Store head node 
    temp = head 
  
    # If head node itself holds the key to be deleted 
    if (temp is not None): 
        if (temp.data == key): 
            head = temp.next
            temp = None
            return head 
  
    # Search for the key to be deleted, keep track of the 
    # previous node as we need to change 'prev.next' 
    while(temp is not None): 
        if temp.data == key: 
            break 
        prev = temp 
        temp = temp.next
  
    # if key was not present in linked list 
    if (temp == None): 
        return head 
  
    # Unlink the node from linked list 
    prev.next = temp.next
  
    temp = None
  
    return head
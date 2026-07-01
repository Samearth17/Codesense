def deleteNode(head, position):
  # If linked list is empty 
  if head == None: 
    return

  # Store head node  
  temp = head 
 
  # If head needs to be removed  
  if position == 0: 
    head = temp.next
    temp = None
    return head 

  # Find previous node of the node to be deleted  
  for i in range(position-1): 
    temp = temp.next
    if temp is None: 
        break

  # if position is more than number of nodes  
  if temp is None: 
    return

  # Node temp.next is the node to be deleted  
  # store pointer to the next of node to be deleted  
  next = temp.next.next

  # Unlink the node from linked list  
  temp.next = None

  temp.next = next

  return head
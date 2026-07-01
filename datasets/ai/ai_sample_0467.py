# Python function to delete a node 
# in a Linked List. 
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None

# Function to delete node from Linked List 
def deleteNode(head, position): 
    # If linked list is empty 
    if head == None: 
        return 

    temp = head 
 
    # If head needs to be removed 
    if position == 0: 
        head = temp.next
        temp = None
        return head 

    # Find previous node of the node to be deleted 
    for i in range(position -1 ): 
        temp = temp.next
        if temp is None: 
            break
 
    # If position is more than number of nodes 
    if temp is None: 
        return 
 
    if temp.next is None: 
        return 

    # Node temp.next is the node to be deleted 
    # store pointer to the next of node to be deleted 
    next = temp.next.next

    # Unlink the node from linked list 
    temp.next = None
 
    temp.next = next 

    return head
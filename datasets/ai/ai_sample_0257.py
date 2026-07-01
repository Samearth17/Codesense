# Node class
class Node: 
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
  
  
# Linked List class
class LinkedList: 
  
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
  
    # Deletes the node at position n
    def deleteNode(self, position): 
  
        # If linked list is empty 
        if self.head == None: 
            return 
  
        # Store headnode 
        temp = self.head 
  
        # If head needs to be removed 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted 
        for i in range(position-1): 
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
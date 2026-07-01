class Node: 
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    def remove_duplicates(self, list_nodes):
        curr_node= self.head 
        new_list=[]
        while curr_node != None: 
            if curr_node.data not in new_list: 
                new_list.append(curr_node.data) 
            curr_node = curr_node.next
                
        # creating a linked list from the unique elements of list_nodes  
        self.head=None
        for i in new_list:
            self.insert_node(i)
    
    def insert_node(self, data): 
    # Create a new node 
        new_node = Node(data) 
        # Check if list is empty
        if self.head is None: 
            self.head = new_node 
            return
        # Otherwise, traverse to the end of list before 
        # inserting the new Node 
        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  new_node